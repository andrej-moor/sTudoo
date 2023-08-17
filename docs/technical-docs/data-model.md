---
title: Data Model
parent: Technical Docs
nav_order: 3
---

Jana
{: .label }

Andy
{: .label }

# Data Model

To understand how data and the database  is structured in sTudoo, let's have a look at sTudoo's data model in the entity-relationship diagram.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Entity-Relationship Diagram

```mermaid

erDiagram

STUDENT ||--o{ CLASS : attends
STUDENT {
    string studentId PK, FK
    string firstName
    string lastName
    string email
    string password
}

CLASS ||--o{ PROJECT: consists
CLASS {
    string classId PK, FK
    string className
    boolean classChecked
}

PROJECT ||--o{ TODO: contains
PROJECT {
    string projectId PK, FK
    int submissionDate
    string projectName
    boolean projectChecked
}

TODO {
    string todoId PK, FK
    string todoName
    boolean todoChecked
}
```

## User to Classes

What you can see is a 1-n cardinality between each entity. This means that a user has to be created to before university classes can be added, but each user can have many classes as entries.

## Classes to Projects

Projecs follows a similiar rule. To a project to exist in sTudoo it has to be matched to a class. Like in real life a project in university belongs a class that is taken. But again, a uni class can have several project assigned to it.

## Projects to Todos

Each todo in university context belongs to a project. A project can have one or many todos assigned to it.