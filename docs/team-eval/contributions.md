---
title: Contributions
parent: Team Evaluation
nav_order: 2
---

Jana
{: .label }

Andy
{: .label }

# Summary of individual contributions
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Jana's Contributions
- Setting Up the Database with the implementation of the Data model
  - `databyse.py`
- Coding the Routes (Backend Logic)
  - `routes.py`
    - Index
    - Sign Up
    - Signed Up
    - Login
    - Loged in
    - User Account
    - User Account Delete
    - User Account Deleted
    - Classes
    - Projects
    - Todos
- **Docs**
  - App Behavior
  - Api Reference

## Andy's Contributions
- Setting Up Github repo & Github pages
- Planing the routes based on Requirements Analysis
- Creating routes related structure of the Jinja Templates
- Coding the Frontend (HTML & CSS)
- Presentation Structure & Design
- Creating of the UML grafics (Data Model & Requirements Analysis )
- Restructure App (`/app`, `.flaskenv`, `config.py`, `.gitignore`)
- Create `requirements.txtf`
- **Docs**
  - Readme
  - Installation Instructions (with Ngnix server)

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



## Database (SQLite) @Jana
- [>] Create Class Diagrams (Class, Attributes, Methods)
  
  &rarr; User ,Class, Projects, Todos
- [x] Create ER Diagram (Attributes, IDs, Primary Keys, Foreign Key, Relations) @Andy
  
  &rarr; User ,Class, Projects, Todos
- [x] Create database
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

## Documentation
- [x] Home (Index) @Jana @Andy
- [-] Tecnical Docs
  - [x] [Tech Docs Index](/docs/technical-docs/)
  - [>] [App Structure](/docs/technical-docs/app-structure)
    - [-] 8 Routes @Andy
    - HTML & CSS Templates Overview @Andy
    - Structure Diagram of CSS Files @Andy
  - [-] [App Behavior](/docs/technical-docs/app-behavior)
    - [x] Use-case diagram of the App (user Uni classes, projects & todos) @Andy
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



=============


# Documentation Outline

[Link to Documentation](https://www.andreas-moor.de/sTudoo/)

---
## Index

### 1. Value Proposition

- The Problem We Want To Solve @Jana @Andy
- The Solution We Want to offer @Jana @Andy

### 2. App Structure

- Class diagram @Jana
- HTML & CSS Templates Overview @Andy
- Structure Diagram of CSS Files @Andy

### 3. App Behavior

- Use-case diagram of the App (user Uni classes, projects & todos)@Andy
- Class diagram @Jana
- App routes and functionality @Jana

### 4. Data Model

- ERM diagram @Andy
- Database implementation @Jana

### 5. API Reference

- API for Export of Todos as a JSON file @Andy @Jana

### 6. Design Decisions

- UI Design Decisions @Andy
- CSS Structure Decisions @Andy
- SQLite3 for practical reasons @Jana
- Blueprint for better overview structure @Jana

### 7. User Evaluation 
- @Andy @Jana

### 8. Goals

- Our Goals @Jana @Andy
- Goals achieved @Jana @Andy
- Goals missed @Jana @Andy

### 9. Individual Contribution

- Jana's Contributions @Jana
- Andy's contributions @Andy