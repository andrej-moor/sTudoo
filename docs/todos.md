---
title: Todos
nav_order: 0
---
[Andy]
{: .label }

# [Project Todos Structure]

The project structure should help us to navigate through the project and stay on track.

The main milstones in the *sTudoo* project are the following:

- [8 Routes (Python & Flask)](#8-routes-python--flask)
- [Database (SQLite)](#database-sqlite)
- [HTML & CSS Templates (Jinja)](#html--css-templates-jinja)
- [Headless API (JSON delivery)](#headless-api-json-delivery)
- [Documentation](#documentation)
- [Presentation](#presentation)
- [Bonus: Deploy on dedicated Web server (NGINX/Waitress)](#deploy-on-dedicated-web-server-nginxwaitress)

## Description of labels & states

@Name = assignment to responsible contributer

- [-] = Task not started


- [>] = Task in progess

- [x] = Task finished

Below you can find the detailed tasks to each of the milestones.

---

## 8 Routes (Python & Flask)

- [x] Define the 8 Routes @Andy
- [>] Programm the app
  - [>] Programm User Account Registration (Route 1) @Jana
  - [-] Programm User Login (Route 2)
  - [-] Programm User Logout (Route 3 )
  - [-] Programm All-Classes-View (Route 4)
  - [-] Programm Class-Related-Projects-View (Route 5)
  - [-] Programm All-Projects-View (Route 6)
  - [-] Programm Project-Todos-View (Route 7)
  - [-] Programm All-Todos-View (Route 8)

Resources: 
  - [Harvard CS50’s Introduction to Programming with Python](https://youtu.be/nLRL_NcnK-4)
  - [Harvard CS50's Web Programming with Flask](https://youtu.be/zdgYw-3tzfI)

## Database (SQLite) @Jana
- [>] Create Class Diagrams (Class, Attributes, Methods)
  
  &rarr; User ,Class, Projects, Todos
- [x] Create ER Diagram (Attributes, IDs, Primary Keys, Foreign Key, Relations) @Andy
  
  &rarr; User ,Class, Projects, Todos
- [>] Create database
- [>] Connect database to app

Ressources:
- [Entity-Relationship Diagrams 1](https://youtu.be/QpdhBUYk7Kk)
- [Entity-Relationship Diagrams 2](https://youtu.be/QpdhBUYk7Kk)
- [Primary & Foreign Keys](https://youtu.be/QpdhBUYk7Kk)
- [UML Tutorial](https://youtu.be/WnMQ8HlmeXc)
- [SQLite in python/flask](https://youtu.be/tPxUSWTvZAs)
- [Mermaid.js Docs for Diagrams](https://mermaid.js.org/intro/)

## HTML & CSS Templates (Jinja) 
- [x] Template User Account Registration -> @Andy
  - [x] Registered Message -> @Andy
- [x] Template User Login -> @Andy
  - [x] Overview LogedIn -> @Andy
  - [x] User Account -> @Andy
- [x] Template User Logout ->@Andy
- [x] Template All-Classes-View -> @Andy
- [x] Template All-Projects-View -> @Andy
- [x] Template All-Todos-View -> @Andy

## Headless API (JSON delivery)
- [-] Talk to Mr. Eck reg. API (Export of Projects & Todos)

## Documentation
- [x] Home (Index) @Jana @Andy
- [-] Tecnical Docs
  - [x] [Tech Docs Index](/docs/technical-docs/)
  - [>] [App Structure](/docs/technical-docs/app-structure)
    - [-] 8 Routes @Andy
    - HTML & CSS Templates Overview @Andy
    - Structure Diagram of CSS Files @Andy
  - [-] [App Behavior](/docs/technical-docs/app-behavior)
    - [>] Use-case diagram of the App (user Uni classes, projects & todos) @Andy
    - [-] Class Diagram @Jana
  - [-] [App Data Model](/docs/technical-docs/data-model)
    - [x] Entity-Relationship Model @And
  - [-] [API Reference](/docs/technical-docs/api-reference)
  - [-] [Design Decisions](/docs/technical-docs/design-decisions)
- [-] User Evaluation
- [-] Team Evaluation
  - [-] [Team Evaluation Index](/docs/team-eval/index)
  - [-] [Goals](/docs/team-eval/goals)
  - [-] [Contributions](/docs/team-eval/contributions)@Jana @Andy
  - [-] [Improvement](/docs/team-eval/improvements) @Jana @Andy
  - [-] [Peer Review](/docs/team-eval/peer-review)

## Presentation

- [x] Structure Presentation (see pdf from 1st session) @Andy
  - [x] What is **_sTudoo_** @Andy
  - [-] The Team 
  - [-] Our Value Proposition
  - [-] Key Design Decisions We Took
  - [-] Why We Won't Implement These Useful Features
- [x] Install Reveal.js @Andy
- [-] Plan and devide Todos between @Andy & @Jana
- [x] [Watch "Markdown Presentation Tools" & choose a Tool](https://youtu.be/owx5KoiqFBs) @Andy

Resources:
- **[Reveal.js]**(https://revealjs.com/)

## Deploy on dedicated Web server (NGINX/Waitress)

- [-] Research: flask app deployment with NGNIX/Waitress
- [-] Plan Todos

---

[Link Documentation Page](https://www.andreas-moor.de/sTudoo/)