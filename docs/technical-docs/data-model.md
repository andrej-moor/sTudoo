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
    string projectName
    int submissionDate
    boolean projectChecked
}

TODO {
    string todoId PK, FK
    string todoName
    boolean todoChecked
}
```

## Student (User) to Classes

What you can see is a 1-n cardinality between each entity. This means that a user has to be created before university classes can be added, but each user can have many classes as entries.

The _Student_ entity holds the attributes `studentId`, `firstName`, `lastName`, `email`, `email` & `password` which are all string data types. `studentId` has the primary and foreign key assigned to it.

## Classes to Projects

The projecs follow a similiar rule. For a project to exist in sTudoo it has to be matched to a class. Like in real life a project in university belongs to a class that is taken. But again, a uni class can have several project assigned to it.

The _Class_ entity holds the attributes `classId`, `className` & `classChecked`. The first two are string data types the last one a boolean. `classId` has the primary and foreign key assigned to it.

## Projects to Todos

Each todo in university context belongs to a project. A project can have one or many todos assigned to it.

The _Project_ entity holds the attributes `projectId`, `projectName`, `submissionDate` & `projectChecked`. The first two are string data types, the third an integer and the last one is a boolean. `projectId` has the primary and foreign key assigned to it.

The _Todos_ entity hold the attributes `todoId`, `todoName` & `todoChecked`. The first two are string data types the last one is a boolean.