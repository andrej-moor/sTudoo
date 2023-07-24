---
title: Design Decisions
parent: Technical Docs
nav_order: 5
---

Andy
{: .label }

# Design decisions
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## 01: Vanilla CSS vs. CSS-Framework/Library

### Meta

Status
: **Decided**

Updated
: 24-Jul-2023

### Problem statement

One of the main design decisions for the UI is whether a CSS-Framework should be used or if plain vanilla CSS is a sufficient solution.

### Decision

The decision that has been taken is: Plain Vanila CSS. The main arguments for plain CSS are, that a framework like Bootstrap or Tailwind has to be learned which is time consuming. Since sTudoo is a small app and there are no requirements for responsive design, the plain CSS code is more flexible, can be quickly customized and faster to implement than learning all the necessary classes to achive the same goal with a CSS framework.

The decision was made by:

Andy
{: .label }

### Regarded options

Further bolow you can find the pros & cons for the taken decision.

|Plain CSS|CSS-Framework/Library|
|---------|---------------------|
|+ inhouse competence|- learning curve |
|+ cleaner html code|- bloated code with a lot of classes|
|+ custom coloring & layout |- bloated code with a lot of classes|
| responsive design is not a requirement |+ responsive design|

---