from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
import json,os,math,markdown,uuid
from werkzeug.utils import secure_filename

load_dotenv()

required_env_vars = [
    "FLASK_SECRET_KEY",
    "LOCAL_DATABASE_URI",
    "PROD_DATABASE_URI",
    "GMAIL_USERNAME",
    "GMAIL_PASSWORD",
    "ADMIN_USERNAME",
    "ADMIN_PASSWORD"
]

missing_vars = [
    var for var in required_env_vars
    if not os.getenv(var)
]

if missing_vars:
    raise RuntimeError(
        "Missing required environment variables: "
        + ", ".join(missing_vars)
    )


with open('config.json') as json_file:
    params = json.load(json_file)['params']

local_server = os.getenv("LOCAL_SERVER", "True").lower() == "true"
app = Flask(__name__)
csrf = CSRFProtect(app)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
def allowed_file(filename):
    return (
        '.' in filename
        and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    )
def convert_markdown_posts(posts):
    for post in posts:
        post.content_html = markdown.markdown(
            post.content,
            extensions=['fenced_code']
        )
    return posts


app.secret_key = os.getenv("FLASK_SECRET_KEY")


UPLOAD_FOLDER = os.path.join(app.static_folder, "assets", "img")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=os.getenv("GMAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("GMAIL_PASSWORD"),
)
mail = Mail(app)

if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("LOCAL_DATABASE_URI")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("PROD_DATABASE_URI")

db = SQLAlchemy(app)

class Contacts(db.Model):
    '''sno, name, email, phone_no, msg, date'''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone_no = db.Column(db.String(20), nullable=False)
    msg = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=True)

class Posts(db.Model):
    '''sno , name , email , phone_no , msg, date '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=True)
    img_file = db.Column(db.String(255),nullable=True)


@app.route('/')
def home():
    page = 1
    per_page = params['no_of_posts']

    total_posts = Posts.query.count()
    total_pages = math.ceil(total_posts / per_page)

    posts = Posts.query.order_by(
        Posts.sno.desc()
    ).offset(
        (page - 1) * per_page
    ).limit(
        per_page
    ).all()

    posts = convert_markdown_posts(posts)

    return render_template(
        'index.html',
        params=params,
        posts=posts,
        page=page,
        total_pages=total_pages
    )

@app.route('/page/<int:page>')
def page(page):

    per_page = 5

    total_posts = Posts.query.count()
    total_pages = math.ceil(total_posts / per_page)

    if page < 1 or page > total_pages:
        return render_template("404.html", params=params), 404

    posts = Posts.query.order_by(Posts.sno.desc()).offset((page - 1) * params['no_of_posts']).limit(params['no_of_posts']).all()

    posts = convert_markdown_posts(posts)

    return render_template(
        'index.html',
        params=params,
        posts=posts,
        page=page,
        total_pages=total_pages
    )


@app.route('/post/<string:post_slug>')
def post_route(post_slug):

    post = Posts.query.filter_by(slug=post_slug).first()

    if post is None:
        return render_template("404.html", params=params), 404

    content_html = markdown.markdown(
        post.content,
        extensions=['fenced_code']
    )

    return render_template(
        "post.html",
        params=params,
        post=post,
        content_html=content_html
    )


@app.route('/search')
def search():

    query = request.args.get('q', '').strip()

    if not query:
        return redirect(url_for('home'))

    posts = Posts.query.filter(
        db.or_(
            Posts.title.ilike(f"%{query}%"),
            Posts.content.ilike(f"%{query}%")
        )
    ).all()

    posts = convert_markdown_posts(posts)

    return render_template(
        'search.html',
        params=params,
        posts=posts,
        query=query
    )


@app.route('/about')
def about():
    return render_template('about.html',params=params)

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        message = request.form.get('msg', '').strip()

        # Required field validation
        if not name or not email or not phone or not message:
            flash("All fields are required.", "danger")
            return redirect(url_for('contact'))

        # Save contact message
        entry = Contacts(
            name=name,
            email=email,
            phone_no=phone,
            msg=message,
            date=datetime.now()
        )

        db.session.add(entry)
        db.session.commit()

        # Send email notification
        mail.send_message(
            'New message from ' + name,
            sender=email,
            recipients=[os.getenv("GMAIL_USERNAME")],
            body=message + "\n" + phone
        )

        flash("Your message has been sent successfully!", "success")

        return redirect(url_for('contact'))

    return render_template(
        'contact.html',
        params=params
    )

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/admin")

@app.route("/dashboard")
def dashboard_home():

    if 'user' not in session:
        return redirect("/admin")

    # ================= POSTS PAGINATION =================

    post_page = request.args.get("post_page", 1, type=int)
    post_per_page = 5

    total_posts = Posts.query.count()

    total_post_pages = math.ceil(total_posts / post_per_page)

    if total_post_pages == 0:
        total_post_pages = 1

    if post_page < 1:
        post_page = 1

    if post_page > total_post_pages:
        post_page = total_post_pages

    posts = Posts.query.order_by(
        Posts.sno.desc()
    ).offset(
        (post_page - 1) * post_per_page
    ).limit(
        post_per_page
    ).all()


    # ================= CONTACT PAGINATION =================

    contact_page = request.args.get("contact_page", 1, type=int)
    contact_per_page = 5

    total_contacts = Contacts.query.count()

    total_contact_pages = math.ceil(
        total_contacts / contact_per_page
    )

    if total_contact_pages == 0:
        total_contact_pages = 1

    if contact_page < 1:
        contact_page = 1

    if contact_page > total_contact_pages:
        contact_page = total_contact_pages

    contacts = Contacts.query.order_by(
        Contacts.sno.desc()
    ).offset(
        (contact_page - 1) * contact_per_page
    ).limit(
        contact_per_page
    ).all()


    return render_template(
        "dashboard.html",
        params=params,
        posts=posts,
        contacts=contacts,

        post_page=post_page,
        total_post_pages=total_post_pages,

        contact_page=contact_page,
        total_contact_pages=total_contact_pages
    )

@app.route('/admin', methods=['GET', 'POST'])
def dashboard():

    if request.method == "POST":

        username = request.form.get("uname", "").strip()
        password = request.form.get("pass", "")

        admin_username = os.getenv("ADMIN_USERNAME", "").strip()
        admin_password = os.getenv("ADMIN_PASSWORD", "")

        if username == admin_username and password == admin_password:
            session['user'] = username
            return redirect("/dashboard")

    return render_template(
        "login.html",
        params=params
    )

@app.route("/edit/<string:sno>", methods=["GET", "POST"])
def edit(sno):

    if 'user' not in session:
        return redirect("/admin")

    post = None

    if sno != "0":
        post = Posts.query.filter_by(sno=sno).first()

        if post is None:
            return "Post Not Found", 404

    if request.method == "POST":

        title = request.form.get("title")
        slug = request.form.get("slug")
        content = request.form.get("content")

        # Required field validation
        if not title or not slug or not content:
            return render_template(
                "edit.html",
                params=params,
                post=post,
                error="Title, slug and content are required."
            )

        # Duplicate slug validation
        existing_post = Posts.query.filter_by(slug=slug).first()

        if existing_post:
            if sno == "0" or existing_post.sno != int(sno):
                return render_template(
                    "edit.html",
                    params=params,
                    post=post,
                    error="This slug already exists. Please use a different slug."
                )

        image = request.files.get("image")

        img_file = None

        if image and image.filename:

            if not allowed_file(image.filename):
                return render_template(
                    "edit.html",
                    params=params,
                    post=post,
                    error="Only PNG, JPG, JPEG, GIF and WEBP images are allowed."
                )

            original_filename = secure_filename(image.filename)
            extension = original_filename.rsplit(".", 1)[1].lower()

            filename = f"{uuid.uuid4().hex}.{extension}"

            image.save(
                os.path.join(app.config["UPLOAD_FOLDER"], filename)
            )

            img_file = filename

        # Add new post
        if sno == "0":

            post = Posts(
                title=title,
                slug=slug,
                content=content,
                img_file=img_file,
                date=datetime.now()
            )

            db.session.add(post)

        # Edit existing post
        else:

            post.title = title
            post.slug = slug
            post.content = content

            if img_file:
                # Delete old image from folder
                if post.img_file:
                    old_image_path = os.path.join(
                        app.config["UPLOAD_FOLDER"],
                        post.img_file
                    )

                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)

                # Save new image filename in database
                post.img_file = img_file

        db.session.commit()

        return redirect("/dashboard")

    return render_template(
        "edit.html",
        params=params,
        post=post
    )

@app.route("/delete/<string:sno>", methods=["POST"])
def delete(sno):

    if 'user' not in session:
        return redirect("/admin")

    post = Posts.query.filter_by(sno=sno).first()

    if post is None:
        return "Post Not Found", 404

    # Delete image from folder
    if post.img_file:

        image_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            post.img_file
        )

        if os.path.exists(image_path):
            os.remove(image_path)

    # Delete post from database
    db.session.delete(post)
    db.session.commit()

    return redirect("/dashboard")

@app.route("/delete_contact/<string:sno>", methods=["POST"])
def delete_contact(sno):

    if 'user' not in session:
        return redirect("/admin")

    contact = Contacts.query.filter_by(sno=sno).first()

    if contact is None:
        return "Contact message not found", 404

    db.session.delete(contact)
    db.session.commit()

    return redirect("/dashboard")


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode)

