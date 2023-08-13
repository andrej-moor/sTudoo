---
title: Data Model
parent: Technical Docs
nav_order: 3
---

Jana
{: .label }

Andy
{: .label }

# [Data model]
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Entity-Relationship Diagram of sTudoo

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