# Reading these notes with perspective

A code example shows what an API does. Engineering judgment also asks **why it exists, what changed, and which cost we are willing to accept**. The chapters combine reference examples with historical context, competing approaches, and practical situations to reason through.

Keep three distinctions in mind:

- **Supported alternative:** React classes and Vue's Options API can still work even when another style is preferred for new code. A different style is not automatically a deprecation.
- **Superseded workflow:** Redux Toolkit improves how we write Redux; native CSS covers some former reasons to use Sass. The underlying idea or tool may remain useful.
- **Retired dependency:** Vue 2, Node Sass and the archived Recoil repository need explicit maintenance or migration decisions. Code that still runs does not establish ongoing support.

Those status examples were checked against the linked maintainer documentation on **23 October 2026**. Follow each chapter's sources for version-specific details; this is not a claim that every example or dependency in `projects/` has been upgraded.

| Chapter | Perspective to look for |
|---|---|
| [HTML](01_html.md) | Linked documents, the Living Standard, and progressive enhancement. |
| [CSS](02_css.md) | Why layout moved beyond float workarounds; viewport versus container decisions. |
| [CSS frameworks](03_css_frameworks.md) | Native CSS and Sass; component styles versus utilities; Bootstrap version boundaries. |
| [JavaScript](04_javascript.md) | Asynchronous syntax versus request ownership; static types versus runtime data. |
| [JavaScript frameworks](05_javascript_frameworks.md) | Rendering philosophies, supported older APIs, and state-management evolution. |
| [UX](06_ux.md) | Expert judgment, observed behavior, and the limits of heuristics. |
| [UI](07_ui.md) | Native controls, styled kits, and headless behavior primitives. |
| [Protocols](08_protocols.md) | Which newer protocols change transport, and which choices change the application contract. |
| [Project structure](09_project_structure.md) | Organizing for the next change and understanding why build tools evolved. |
| [Testing](10_testing.md) | Different distributions of tests and the maintenance cost of each. |
| [Hosting](11_hosting_websites.md) | Static, server, and managed execution models; operational ownership. |
| [Quizzes](12_quizes.md) | Explain a tradeoff or migration decision before revealing a suggested answer. |
| [Resources](13_additional_resources.md) | Learn a durable idea without inheriting an obsolete setup. |

The practical scenarios are teaching examples and recommendations, not reports of the author's production incidents. When applying one, write down the constraint, chosen approach, downside, and evidence that would make you revisit it. “We chose this because…” is more useful to the next developer than “this is best practice.”
