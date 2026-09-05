from main import app, db, Posts
from datetime import datetime


# ============================================================
# PROFESSIONAL BLOG POSTS
# ============================================================

posts_data = [

    # ========================================================
    # POST 1
    # ========================================================
    {
        "title": "Python for Beginners: A Practical Introduction",
        "slug": "python-for-beginners",
        "content": """
Python has become one of the most popular programming languages in the world.
Its simple syntax, large ecosystem, and wide range of applications make it an
excellent choice for beginners as well as experienced developers.

Whether you want to build websites, automate repetitive tasks, work with data,
create APIs, or explore artificial intelligence, Python provides a practical
starting point.

## What Is Python?

Python is a high-level, general-purpose programming language created with
readability and simplicity in mind. Unlike some programming languages that
require a lot of code to perform a simple task, Python allows developers to
express ideas with relatively few lines of code.

For example, displaying a message in Python is as simple as:

print("Hello, World!")

This simplicity is one of the main reasons Python is widely used for learning
programming.

## Why Is Python So Popular?

Python is popular because it is relatively easy to read and write. Its syntax
is clean, and developers can focus more on solving problems rather than
dealing with complicated language rules.

Another major advantage is its huge collection of libraries and frameworks.
Developers can use existing tools instead of building everything from scratch.

Python is commonly used for:

- Web development
- Data analysis
- Automation
- Web scraping
- REST APIs
- Machine learning
- Artificial intelligence
- Testing and scripting
- Desktop applications

## Where Is Python Used?

Python is used in many different areas of software development.

For web development, frameworks such as Flask and Django allow developers
to build websites and APIs.

For data-related work, libraries such as Pandas and NumPy provide powerful
tools for processing and analysing information.

Python is also commonly used for automation. A developer can write a Python
program to perform repetitive tasks, process documents, collect information
from websites, generate reports, or perform repetitive data automatically.

## Installing Python

To start learning Python, you first need to install Python on your computer.

After installation, you can verify that Python is available by opening a
terminal or command prompt and running:

python --version

Once Python is installed successfully, you are ready to write your first
Python programs.
""",
        "img_file": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=1600&q=80"
    },


    # ========================================================
    # POST 2
    # ========================================================
    {
        "title": "Python Variables and Data Types Explained",
        "slug": "python-variables-data-types",
        "content": """
Variables are one of the first concepts you should understand when learning
Python. A variable allows us to store a value and use that value later in
our program.

## What Is a Variable?

A variable is a name that refers to a value.

For example:

name = "Drashti"
age = 25

Here, name stores text and age stores a number.

Python automatically determines the type of value stored in a variable, so
you do not normally need to declare the type separately.

## Strings

Strings are used to store text.

For example:

name = "The Magic Coder"

You can also combine strings using different techniques.

## Integers

Integers are whole numbers.

For example:

age = 25
year = 2026

You can perform mathematical operations using integers.

## Floating-Point Numbers

Floating-point numbers contain decimal values.

For example:

price = 99.50
temperature = 36.5

## Boolean Values

Boolean values represent either True or False.

For example:

is_logged_in = True
is_admin = False

Boolean values are commonly used in conditions.

## Lists

Lists allow you to store multiple values in a single variable.

For example:

languages = ["Python", "JavaScript", "Java"]

You can access individual values using their index.

## Dictionaries

Dictionaries store information using key-value pairs.

For example:

user = {
    "name": "Drashti",
    "role": "Python Developer"
}

Dictionaries are extremely useful when working with structured information.

## Why Data Types Matter

Understanding data types is important because different types support
different operations.

For example, numbers can be added together while strings are normally
combined using string operations.

Once you understand variables and data types, many other Python concepts
become much easier to learn.
""",
        "img_file": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1600&q=80"
    },


    # ========================================================
    # POST 3
    # ========================================================
    {
        "title": "Python Conditional Statements: if, elif and else",
        "slug": "python-conditional-statements",
        "content": """
Programs often need to make decisions. Python provides conditional
statements that allow a program to execute different code depending on
whether a condition is true or false.

## The if Statement

The simplest conditional statement is if.

For example:

age = 20

if age >= 18:
    print("You are an adult.")

The code inside the if block runs only when the condition is true.

## The else Statement

The else statement provides an alternative when the condition is false.

For example:

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

## The elif Statement

Sometimes a program needs to check multiple conditions.

Python provides elif for this purpose.

For example:

marks = 75

if marks >= 90:
    print("Excellent")
elif marks >= 60:
    print("Good")
else:
    print("Keep practising")

Python checks the conditions from top to bottom.

## Comparison Operators

Some commonly used comparison operators are:

- == equal to
- != not equal to
- > greater than
- < less than
- >= greater than or equal to
- <= less than or equal to

These operators are frequently used in conditional statements.

## Logical Operators

Python also provides logical operators such as:

- and
- or
- not

For example:

age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive.")

Conditional statements are essential because they allow programs to respond
differently to different situations.
""",
        "img_file": "https://images.unsplash.com/photo-1516116216624-53e697fedbea?auto=format&fit=crop&w=1600&q=80"
    },


    # ========================================================
    # POST 4
    # ========================================================
    {
        "title": "Python Loops: Understanding for and while Loops",
        "slug": "python-loops-for-while",
        "content": """
Loops are used when we need to execute the same block of code multiple
times. They are one of the most useful features of Python.

Instead of writing the same code repeatedly, we can use a loop.

## The for Loop

The for loop is commonly used when we want to iterate over a sequence.

For example:

languages = ["Python", "JavaScript", "Java"]

for language in languages:
    print(language)

The loop processes each item in the list one by one.

## Using range()

The range() function is frequently used with for loops.

For example:

for number in range(5):
    print(number)

This produces numbers from 0 through 4.

## The while Loop

A while loop continues running as long as a condition remains true.

For example:

count = 1

while count <= 5:
    print(count)
    count += 1

The loop stops when the condition becomes false.

## break

The break statement can be used to stop a loop early.

For example:

for number in range(10):
    if number == 5:
        break
    print(number)

## continue

The continue statement skips the current iteration and moves to the next
one.

For example:

for number in range(5):
    if number == 2:
        continue
    print(number)

## Why Loops Are Important

Loops are used everywhere in software development.

They are useful when processing lists, reading files, handling database
records, processing API responses, scraping websites, and automating tasks.

Once you understand loops, you can write much more powerful Python programs.
""",
        "img_file": "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=1600&q=80"
    },


    # ========================================================
    # POST 5
    # ========================================================
    {
        "title": "Python Functions: Write Cleaner and Reusable Code",
        "slug": "python-functions",
        "content": """
As Python programs become larger, writing all the code in one place can
quickly become difficult to manage.

Functions help us organise code into small, reusable pieces.

## What Is a Function?

A function is a block of code designed to perform a specific task.

For example:

def greet():
    print("Hello, welcome to The Magic Coder!")

We can call the function whenever we need it:

greet()

## Function Parameters

Functions can receive information through parameters.

For example:

def greet(name):
    print("Hello", name)

We can then call:

greet("Drashti")

The function receives the value and uses it inside the function.

## Returning Values

A function can also return a result.

For example:

def add(a, b):
    return a + b

result = add(10, 20)

The result variable will contain 30.

## Why Functions Are Useful

Functions provide several important benefits:

- Code reuse
- Better organisation
- Easier testing
- Easier debugging
- Improved readability
- Smaller and more manageable programs

For example, instead of writing the same calculation several times, we
can create one function and call it whenever necessary.

## Functions in Real Projects

Functions are used heavily in real-world Python applications.

A Flask application may contain functions for handling requests, accessing
a database, processing forms, and rendering templates.

A web scraping application may use separate functions for downloading
pages, extracting information, validating data, and saving results.

Learning how to design useful functions is an important step toward writing
professional Python applications.
""",
        "img_file": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1600&q=80"
    },


    # ========================================================
    # POST 6
    # ========================================================
    {
        "title": "Python Lists and Tuples: What Is the Difference?",
        "slug": "python-lists-and-tuples",
        "content": """
Lists and tuples are two important Python data structures used to store
multiple values.

Although they look similar, they have an important difference.

## Python Lists

A list is an ordered collection of values.

For example:

languages = ["Python", "Java", "JavaScript"]

Lists are mutable, which means their contents can be changed.

For example:

languages.append("C++")

The new item is added to the list.

## Python Tuples

A tuple is also an ordered collection, but tuples are immutable.

For example:

coordinates = (10, 20)

Once a tuple is created, its values cannot normally be changed.

## When Should You Use a List?

Lists are useful when your collection of data needs to change.

For example:

- Shopping items
- User records
- API results
- Scraped data
- Tasks

## When Should You Use a Tuple?

Tuples are useful when the data should remain fixed.

For example:

coordinates = (10, 20)

## Lists vs Tuples

The main difference is mutability.

Lists can be modified after creation, while tuples are designed to remain
unchanged.

Understanding this difference helps you choose the right data structure
for your program.
""",
        "img_file": "https://images.unsplash.com/photo-1521737711867-e3b97375f902?auto=format&fit=crop&w=1600&q=80"
    },


    # ========================================================
    # POST 7
    # ========================================================
    {
        "title": "Python Dictionaries: Store Data Using Key-Value Pairs",
        "slug": "python-dictionaries",
        "content": """
Dictionaries are one of the most useful data structures in Python.

They allow us to store information using key-value pairs.

## Creating a Dictionary

For example:

user = {
    "name": "Drashti",
    "role": "Python Developer",
    "experience": 3
}

Each key identifies a value.

## Accessing Values

You can access a value using its key.

For example:

print(user["name"])

This returns the value associated with the name key.

## Adding Values

New values can be added easily.

For example:

user["city"] = "Ahmedabad"

## Updating Values

Existing values can also be changed.

For example:

user["role"] = "Senior Python Developer"

## Why Dictionaries Are Important

Dictionaries are extremely common in Python applications.

They are especially useful when working with:

- JSON data
- REST APIs
- Configuration files
- Database records
- User information
- Application settings

If you work with web development or APIs, you will use dictionaries very
frequently.
""",
        "img_file": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1600&q=80"
    },


    # ========================================================
    # POST 8
    # ========================================================
    {
        "title": "Python Exception Handling with try and except",
        "slug": "python-exception-handling",
        "content": """
Programs sometimes encounter unexpected situations.

A file may not exist, a user may enter invalid information, or a database
operation may fail.

Python provides exception handling to deal with these situations safely.

## The try Statement

Code that might produce an error can be placed inside a try block.

For example:

try:
    number = int(input("Enter a number: "))
except:
    print("Please enter a valid number.")

If the conversion fails, the except block handles the error.

## Why Exception Handling Matters

Without exception handling, an unexpected error can stop a program.

With proper exception handling, the program can respond gracefully.

## Handling Specific Exceptions

It is often better to handle specific exceptions.

For example:

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

This makes the program easier to understand and debug.

## finally

Python also provides finally.

The finally block runs whether an exception occurs or not.

This is useful for cleanup operations such as closing files or releasing
resources.

Exception handling is an important skill for building reliable Python
applications.
""",
        "img_file": "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&w=1600&q=80"
    },


    # ========================================================
    # POST 9
    # ========================================================
    {
        "title": "How Python Modules and Packages Organize a Project",
        "slug": "python-modules-and-packages",
        "content": """
As a Python project grows, keeping everything inside one file becomes
difficult.

Modules and packages help developers organise large applications into
smaller and more manageable parts.

## What Is a Module?

A Python module is usually a Python file containing code that can be
imported into another file.

For example, suppose we have a file called calculator.py:

def add(a, b):
    return a + b

Another Python file can import it:

import calculator

result = calculator.add(10, 20)

## Why Modules Are Useful

Modules help separate responsibilities.

For example, a project might contain:

database.py
utils.py
api.py
scraper.py

Each file can handle a specific responsibility.

## What Is a Package?

A package is a collection of related Python modules organised inside a
directory.

Packages become especially useful when applications become larger.

## Real-World Projects

Professional Python applications commonly use multiple modules and
packages.

Flask applications, Django applications, automation tools, APIs, and
data-processing systems all use this approach.

Good project organisation makes code easier to maintain, test, and extend.
""",
        "img_file": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80"
    },


    # ========================================================
    # POST 10
    # ========================================================
    {
        "title": "How Python Is Used for Web Development",
        "slug": "python-web-development",
        "content": """
Python is widely used for web development.

Developers can use Python frameworks to build websites, APIs, dashboards,
and complete web applications.

## Flask

Flask is a lightweight Python web framework.

It provides the basic tools required to create web applications while
allowing developers to choose additional libraries when needed.

A simple Flask application can look like this:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

## Django

Django is another popular Python web framework.

It provides many features out of the box, including URL routing,
database integration, authentication, forms, and an administration panel.

## APIs

Python can also be used to create REST APIs.

APIs allow different applications to communicate with each other.

For example, a web application can request information from a Python API
and receive the response as JSON.

## Databases

Python web applications frequently work with databases such as MySQL,
PostgreSQL, and SQLite.

A typical web application may receive a request, process the data, interact
with a database, and return an HTML page or API response.

## Why Python Is Good for Web Development

Python provides a large ecosystem of frameworks and libraries.

This allows developers to focus on solving application problems instead of
building every feature from scratch.

If you already know Python, learning Flask or Django is a natural next
step toward becoming a Python web developer.
""",
        "img_file": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1600&q=80"
    }

]


# ============================================================
# INSERT POSTS
# ============================================================

with app.app_context():

    inserted = 0
    deleted = 0

    print()
    print("=" * 60)
    print("STARTING POST IMPORT")
    print("=" * 60)
    print()

    # --------------------------------------------------------
    # STEP 1:
    # Delete all existing copies of these posts
    # based on their slug.
    #
    # This prevents duplicate posts when you run
    # add_posts.py multiple times.
    # --------------------------------------------------------

    for post_data in posts_data:

        slug = post_data["slug"]

        existing_posts = Posts.query.filter_by(
            slug=slug
        ).all()

        for existing_post in existing_posts:

            print(
                f"DELETING: "
                f"{existing_post.sno} - "
                f"{existing_post.title}"
            )

            db.session.delete(existing_post)

            deleted += 1

    # Save all deletions
    db.session.commit()

    print()
    print(f"Old/duplicate posts deleted: {deleted}")
    print()

    # --------------------------------------------------------
    # STEP 2:
    # Insert fresh posts
    # --------------------------------------------------------

    for post_data in posts_data:

        new_post = Posts(
            title=post_data["title"],
            slug=post_data["slug"],
            content=post_data["content"].strip(),
            img_file=post_data.get(
                "img_file",
                "home-bg.jpg"
            ),
            date=datetime.now()
        )

        db.session.add(new_post)

        inserted += 1

        print(
            f"ADDED: {post_data['title']}"
        )

    # Save all new posts
    db.session.commit()

    # --------------------------------------------------------
    # STEP 3:
    # Verify that every slug has exactly one post
    # --------------------------------------------------------

    print()
    print("=" * 60)
    print("VERIFYING POSTS")
    print("=" * 60)
    print()

    verified = 0

    for post_data in posts_data:

        slug = post_data["slug"]

        matching_posts = Posts.query.filter_by(
            slug=slug
        ).all()

        if len(matching_posts) == 1:

            print(
                f"OK: {post_data['title']}"
            )

            verified += 1

        elif len(matching_posts) == 0:

            print(
                f"ERROR: Not found - {post_data['title']}"
            )

        else:

            print(
                f"ERROR: Duplicate found - "
                f"{post_data['title']} "
                f"({len(matching_posts)} copies)"
            )

    # --------------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------------

    print()
    print("=" * 60)
    print("POST INSERTION COMPLETED")
    print("=" * 60)
    print()
    print(f"Old posts deleted : {deleted}")
    print(f"New posts inserted: {inserted}")
    print(f"Posts verified    : {verified}")
    print(f"Expected posts    : {len(posts_data)}")
    print()

    if verified == len(posts_data):

        print("SUCCESS!")
        print("All posts were inserted without duplicates.")

    else:

        print("WARNING!")
        print("Please check the messages above.")

    print()
    print("=" * 60)