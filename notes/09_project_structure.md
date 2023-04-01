## Project Structure

Organizing files and folders logically is crucial when starting a new project. A real-world project might have anything from a few hundred to several thousand files, depending on its scope. Many frameworks provide a predefined structure, but these are mainly suggestions rather than strict rules. Since many projects use multiple frameworks or none at all, the question of project structure is almost always relevant.

## Choosing the Right Technologies

Selecting the right technologies for your project is highly subjective. Here are some general guidelines:

1. Prefer HTML and CSS over JavaScript.
2. Favor Vanilla Javascript (or TypeScript) over any framework.
3. Use frameworks only for complex web apps.
4. The best frameworks are the ones already in use. Avoid chasing hype.
5. Don't mix frameworks.

### Example Structure

You can use any structure you prefer, but here's a suggested organization:

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


For CSS, you can use a single file or divide the code into several smaller ones. Before deploying to the production server, bundle the files together.

In HTML, many components will be duplicated on nearly every page. You can separate them into distinct files responsible for elements like the header, navigation, sidebar, and footer. Then, insert these components into each page file before deployment.

## Boilerplates

Each project is unique, but some code will be shared across them. To create a starting point for building a new project, you can prepare your own templates or use ones created by others.

You can save a lot of time by copying CSS code across projects, as long as HTML components have appropriate class names and ids. Modify only the parts that are specific to the project.

## Links

* https://github.com/MWins/rapid-site-development
* http://www.sitepoint.com/a-minimal-html-document-html5-edition/
* http://meyerweb.com/eric/thoughts/2011/01/03/reset-revisited/
* http://www.cssreset.com/
* https://html5boilerplate.com/
