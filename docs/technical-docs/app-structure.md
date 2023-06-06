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

## Overview of sTudoo's structure (Use Case Diagram)

To get a big picture of the functions lets take a look at the use case diagram of sTudoo.

![Use Case Diagram of sTudoo](/diagrams/Studoo_Features.png)

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

To become

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
