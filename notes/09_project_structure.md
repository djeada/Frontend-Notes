## Project Structure

A well-organized project structure ensures that code remains maintainable, scalable, and understandable, especially as the project grows. As there's no one-size-fits-all answer, adapting based on the project's needs is vital.

### Key Considerations

- **Scalability**: As your project grows, it should be easy to add new components or modules without disrupting existing functionality.
- **Maintainability**: Any developer, whether they're familiar with the project or not, should be able to understand the structure and make changes.
- **Reusability**: Common components and utilities should be easily identifiable and reusable across the project.

## Choosing the Right Technologies

While technology choices heavily depend on the project's needs, here are some timeless guidelines:

1. **HTML and CSS First**: Always start with the basics. Structure with HTML and beautify with CSS.
2. **Vanilla Over Framework**: If possible, use Vanilla Javascript (or TypeScript) before considering frameworks. It ensures better performance and greater control.
3. **Frameworks for Complexity**: Reserve frameworks like React, Angular, or Vue for projects that truly benefit from their features.
4. **Stay Consistent**: If your project or team already uses a particular technology stack, stick to it unless there's a compelling reason to switch.
5. **Avoid Mixing Frameworks**: Mixing can lead to conflicts and unexpected behavior, decreasing maintainability.

### Example Structure

You can use any structure you prefer, but here's a suggested organization:

```
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
```

For CSS, you can use a single file or divide the code into several smaller ones. Before deploying to the production server, bundle the files together.

In HTML, many components will be duplicated on nearly every page. You can separate them into distinct files responsible for elements like the header, navigation, sidebar, and footer. Then, insert these components into each page file before deployment.

## Boilerplates

Boilerplates are essentially templates or sets of standardized files used as a starting point for various projects. They offer a foundation upon which you can build, streamlining the setup process and ensuring best practices from the get-go.

### Why Use Boilerplates?

1. **Speed Up Development**: With boilerplates, you can hit the ground running, eliminating the need to rewrite the basic structure each time you start a new project.
2. **Consistency**: They ensure consistent coding practices across different projects, making the codebase easier to understand for anyone who works on multiple projects.
3. **Best Practices**: Often, boilerplates are designed by experienced developers who've incorporated best practices, ensuring efficient and robust code.
4. **Customizability**: While boilerplates provide a foundation, they are designed to be flexible, allowing developers to easily modify or extend the structure to fit specific project needs.

### Using CSS in Boilerplates

CSS is a common inclusion in many boilerplates, and here's why:

- **Reusable Components**: Many web elements, like buttons, navigation bars, or modals, tend to have similar styling across different websites. By including these styles in a boilerplate, you ensure a consistent look and feel while minimizing repetitive work.
  
- **Consistent Theming**: A boilerplate can include a base theme (colors, fonts, etc.), ensuring a consistent brand identity across projects. This theme can be easily customized for individual projects.

- **Efficient Overrides**: With a well-structured CSS in your boilerplate, it becomes easier to override or extend styles for specific components or sections in your project.

### Finding and Using Boilerplates

1. **Create Your Own**: If you find yourself often reusing certain code patterns or structures, consider creating your own boilerplate. This ensures it's tailored to your specific needs and preferences.

2. **Community Boilerplates**: Platforms like GitHub host a myriad of open-source boilerplates designed for various purposes – from simple HTML-CSS-JS templates to more complex setups with frameworks like React or Vue.

3. **Maintainability**: Keep your boilerplates updated. As you learn and as technology evolves, it's essential to revisit and refine your templates.

4. **Documentation**: Whether you're using someone else's boilerplate or creating your own, always ensure there's clear documentation. This aids in understanding the structure, components, and any specific configurations or dependencies.

## Links

* https://github.com/MWins/rapid-site-development
* http://www.sitepoint.com/a-minimal-html-document-html5-edition/
* http://meyerweb.com/eric/thoughts/2011/01/03/reset-revisited/
* http://www.cssreset.com/
* https://html5boilerplate.com/
