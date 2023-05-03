---
title: UI Components
nav_order: 99
---

[to be deleted]
{: .label .label-red }

{: .attention}
> Once you are familiar with the available UI components of this template, exclude this page by changing `nav_order: 99` to `nav_exclude: true` on top of this page (line 3). Its *front matter* will then look like this:
> ```
> ---
> title: UI Components
> nav_exclude: true
> ---
> ```

# UI components

The [Just the Docs documentation](https://just-the-docs.github.io/just-the-docs/docs/ui-components) details more UI components.

For a quick reference of the markdown syntax, visit [this page](https://github.com/just-the-docs/just-the-docs/blob/main/docs/index-test.md?plain=1).

## Images

```markdown
![get_list_todos_sample](../assets/images/fswd-intro_02.png)
```

![get_list_todos_sample](../assets/images/fswd-intro_02.png)

## Callouts

{: .info }
> This is an info callout.

{: .tip }
> This is a tip callout.

{: .attention }
> This is an attention callout.

## Labels

[Default label]
{: .label }

[Green label]
{: .label .label-green }

[Red label]
{: .label .label-red }

## Mermaid.js

```mermaid
graph TD;
    A-->B;
    A-->C;
```
