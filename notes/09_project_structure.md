## Project strucutre

When starting a new project, we must identify which files we will require and organize them logically between folders. This is critical because, depending on the scope of the project, a real-world project might have anything from a few hundred to several thousand files. Although many frameworks provide a predefined structure, these are mainly simply suggestions rather than hard and fast rules. Furthermore, because many projects use many frameworks at the same time or even none at all, the question of project structure is almost always relevant.

## Choosing the right technologies

This is highly subjective topic. I tend to follow the following rules of thumb:

1. HTML and CSS over JavaScript.
2. Vanilla Javascript (or TypeScript) over any framework.
3. Frameworks only for complex web apps.
4. The best framework are the ones that are already in use. Never chase the hype.
5. Don't mix frameworks.

## Example structure

You may use any structure you choose, but here's one suggestion:

    project
    ├── css
    │   ├── reset.css
    │   ├── typography.css
    │   ├── layout.css
    │   ├── navigation.css
    │   ├── ui_elements.css
    │   ├── forms.css
    │   └── media_queries.css
    ├── js
    |   └── script.js
    ├── views
    │   ├── view_a.html
    │   ├── view_b.html
    │   └── ...
    ├── media
    │   ├── image_a.jpg
    │   ├── image_b.jpg
    │   └── ...
    └── index.html

For CSS, you may put everything into a single file or divide the code into several smaller ones. The files should then be bundled together before being deployed to the production server.

Similarly, many components in HTML will be duplicated on practically every page. You may break them into distinct files, each of which is responsible for elements like the header, navigation, sidebar, and footer. Then, before deployment, insert into each page file.

## Boilerplates

You don't want to say it again. Each project is unique, however some code will be shared across them. To have a starting point for constructing a new project, you can prepare yourself or utilize templates created by others.

CSS code can even be entirely copied across projects as long as HTML components are given suitable class names and ids. You may save a lot of time by doing this and simply modifying the portions that are particular to the project.

## Links

* https://github.com/MWins/rapid-site-development
* http://www.sitepoint.com/a-minimal-html-document-html5-edition/
* http://meyerweb.com/eric/thoughts/2011/01/03/reset-revisited/
* http://www.cssreset.com/
* https://html5boilerplate.com/
