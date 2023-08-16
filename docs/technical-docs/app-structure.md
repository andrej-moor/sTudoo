---
title: App Structure
parent: Technical Docs
nav_order: 1
---

Andy
{: .label }

# sTudoos Application Structure

To get a glimpse of the application structure and it's compoments, let's dive into the directory tree.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

```
sTudoo
├── app
│   ├── database.py
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   └── images
│   └── templates
├── classes.db
├── .flaskenv
├── README.md
├── requirements.txt
└── studoo.py
```

## README.md (Application Description)

The `README.md` file contains the description of sTudoo's value proposition and the links to the documentation and the installation instructions.

## The app package (The Main code)

The main code of sTudoo is located in the `app` directory and contains a `__init__.py` file which makes it a package that can be imported. Via the `__init__.py` file the `routes.py` and the `database.py` are imported.

### routes.py & database.py
The `routes` modul contains all routes (view functions) that are used in the application. The `datatbase` modul includes all database related functions that are responsible to create the database with the necessary tables and those functions which are responsible to get and write data into the database.

### The 'static' directory (CSS, Images & Templates)

The `static` sub-directory contains the `css` and the `images`.

```
├── app
:
│   ├── static
│   │   ├── css
│   │   └── images
:
```
The `templates` directory contains the Jinja templates which are used to render the HTML which is requested by the browser. The `includes` directory contains templates which are imported in other templates to avoid redundant code.
```
:   :
│   └── templates
│       ├── classes.html
│       ├── includes
│       │   ├── _footer.html
│       │   ├── _logo.html
│       │   ├── _logo_loged_in.html
│       │   ├── _navbar.html
│       │   ├── _navbar_loged_in.html
│       │   └── _social.html
│       ├── index.html
│       ├── layout.html
│       ├── logedin.html
│       ├── login.html
│       ├── logout.html
│       ├── projects.html
│       ├── signed_up.html
│       ├── sign_up.html
│       ├── todos.html
│       ├── user_account_deleted.html
│       ├── user_account_delete.html
│       └── user_account.html
:
```
## classes.db (The Database)
The `classes.db` file is the database that save the application relevant data.

## studoo.py & .flaskenv (Run The App)
The `studoo.py` file is a python script that defines the Flask application instance. It imports the `app` varible from the `app` package (see above).

To run the application `FLASK_APP` environment variable is set to `studoo.py` in the `.flaskenv` file.

## requirements.txt (Dependencies)
The `requirements.txt` file contains the relevant dependencies which are installed via pip during the installation of sTudoo.