# Minimal LESS Project

This is a minimal setup for using LESS (Leaner Style Sheets) in a web project. Follow the instructions below to get started.

## Prerequisites

Before you begin, ensure you have [Node.js](https://nodejs.org/) installed on your machine as it includes npm, which is necessary for managing the packages.

## Install Dependencies

Run the following command to install the necessary npm package for LESS:

```bash
npm install less
```

This will install LESS, which is required for compiling LESS files.

## Usage

To start using LESS in your project, follow these steps:

1. Write LESS: Edit your LESS files located in the less folder.

2. Compile LESS to CSS: Run the following command to compile your LESS files to CSS:

```bash
npx lessc less/styles.less css/styles.css
```

This command compiles the styles.less file into a styles.css file inside the css folder.

3. View Your Project: Open the index.html file in a web browser to see your changes.

