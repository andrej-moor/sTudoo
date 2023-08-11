---
title: App Structure
parent: Technical Docs
nav_order: 1
---

[Andy]
{: .label }

# [sTudoos app structure]
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

```bash
sTudoo
├── app
│   ├── database.py
│   ├── entries.py
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   └── images
│   └── templates
├── classes.db
├── config.py
├── .flaskenv
├── README.md
└── studoo.py
```
```bash
├── app
│   ├── database.py
│   ├── entries.py
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── images
│   │       ├── account_delete.png
│   │       ├── account_functions.png
│   │       ├── add_classes_form_and_overview.png
│   │       ├── add_projects_form_and_overview.png
│   │       ├── add_todos_form_and_overview.png
│   │       ├── classes_function.png
│   │       ├── create_tables_functions.png
│   │       ├── css_structure.png
│   │       ├── data_model.png
│   │       ├── delete_entry.png
│   │       ├── erm_project_todos.png
│   │       ├── erm_student_classes.png
│   │       ├── get_projects_function.png
│   │       ├── login_form.png
│   │       ├── login_function.png
│   │       ├── main_layout.png
│   │       ├── projects_function.png
│   │       ├── sign_up_form.png
│   │       ├── sign_up_function.png
│   │       ├── students.jpg
│   │       ├── studoo_features.svg
│   │       ├── templates_overview.png
│   │       ├── textureConrete.jpg
│   │       ├── todos_functions.png
│   │       └── whiteBricks.jpg
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
├── classes.db
├── config.py
├── .flaskenv
├── README.md
└── studoo.py
```

## Overview of sTudoo's structure (Use Case Diagram)

To get a big picture of the functions lets take a look at the use case diagram of sTudoo.

![Use case diagram](../assets/diagrams/Studoo_Features.png)

To use the full functionality it is necessary for a user to register an login. After the registration an the login the user is able to:
-  add,
-  edit,
-  delete,
-  mark as completed and
-  view

the **classes, projects and todos**.

To stay focused the user can choose between different views:

- Classes:
  - see all classes
  - see class relevant projects
  - see class relevant todos
- Projects:
  - see all projects
  - see project relevant todos
- Todos:
  - see all todos

## The necessary routes

sTudoo as a web app is build with the Flask framework which uses routes to present the content to the user. The following routes should acts as a more precise navigation through the app functionality.

### User Account Registration (Route 1)

To use sTudoo the user needs a registration.

**Functions**:
- Clicking the Register Link at *Home* page
- Receive user data
  - First name
  - Last name
  - Email
  - Password (min. 6 characters)
  - Link "Reset Password" (OPTIONAL, NEEDS A SEPERATE ROUTE)

### User Login (Route 2)

After the registration the user is able to login into the account and add classes, projects and todos.

Additionaly the user is able to change its personal data i.e. email & password.

**Functions**:

- Loging user
  - Email
  - Password
- Change *Login Link* to *Logout Link*
- Open All-Classes-View
- Edit user data
  - First Name
  - Last Name
  - Email
  - Password 

### User Logout (Route 3 )

The User is also able to logout.

**Functions**:
- Logout user when clicking the logout sign
- Open *Home* page

### All-Classes-View (Route 4)

During the time in university every student has to visit classes that can be seen as sub goals that lead to the main goal of finishing university and getting a degree.

Thats why sTudoo has an overview for uni classes, in which the user cann add, edit and remove classes to keep an eye on the big picture.

**Functions**:

- Add classes to a list
  - Name of class
- List the classes as an overview
- Edit classes from the list
- Remove classes from the list
- Hyperlink each of the classes to their class related project view 

### Class-Related-Projects-View (Route 5)

Many courses at the university have combined exams. This means that several examination performances must be completed.

Each of the performances can be seen as a project that leads to the goals of passing a specific class.

**Functions**:

- Add projects to a list that is connected to a specific class
  - Date of submission
  - Project name
- List the projects in overview
- Edit project name and date of submission
- Delete project
- Link each project to Project-Todos-View

### All-Projects-View (Route 6)

One of the overwhelming things in university is to work on more than one project at a time.

When the date of submission in a project is set, the *All-Projects-View* helps the student to see which of the projects to tacle first, because is sorted by date.

**Functions**:

- List all projects by the date of submition
  - Name of project
  - Tag with link to belonging class
- Link each project to Project-Todos-View
- Edit project name and date of submission
- Delete project
- Mark projects red that are due in less than a month

### Project-Todos-View (Route 7)

Each project can be broken down into specific tasks which lead to the completion of it. The Project-Todos-View helps the user to see all the project related todos in one list.

**Functions**:

- Adding todos to a list
  - Name of todo
  - Priority (A,B,C - OPTIONAL)
  - Tag with link of belonging class
  - Tag with link of belonging project
- List the todos in an overview
- Edit the todo name
- Delete a todo
- Marking a todo as done (strike through)

### All-Todos-View (Route 8)

Finishing the organizational work, it's up to the user to get thing done. 

The All-Todos-View is the sum of all todos from all classes and their projects.

**Functions**:
- List the todos in an overview
  -> Name
  -> Project
  -> Class 
- Edit the todo name & (priority)
- Delete a todo
- Marking a todo as done (strike through)
