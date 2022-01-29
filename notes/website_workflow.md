## Basic Workflow for building HTML-CSS sites

A github repo exists. [Github Repo](https://github.com/MWins/rapid-site-development) Clone it to your account and modify to match your preference. 

Do you have a standard starting point HTML 5 page? 

Which CSS reset do you use? 

Got a default site structure you prefer (like css/js goes in resources/, a media/ folder for content images) ?

Are you using LESS or SASS ?

If it's multi page, don't copy the layout manually into new pages use a server side language like php to provide templating.


### Structure 
Use what you prefer, here's an option :

- public/css
- public/css/style.css
- public/js
- public/js/script.js
- public/fonts
- media/
- views/
- _data/
- index.html
- index.php
- robots.txt
- .htaccess


Structure's good. Just have to populate it with some defaults. Here's one of the simplest HTML5 page

    <!DOCTYPE html>
    <html lang="en">
     <head>
     <meta charset="utf-8">
     <title>title</title>
     <link rel="stylesheet" href="style.css">
     <script src="script.js"></script>
      </head>
      <body>
        <!-- page content -->
      </body>
    </html>

Source : http://www.sitepoint.com/a-minimal-html-document-html5-edition/

Not having to type that out has a benefit beyond the obvious 'oh that's easy'. It's about not having to repeat yourself.

Problem is it isn't good enough. Sites require more than the basics so you have to add those. 


(You could use HTML5 Boilerplate which is good but has lots to work through.)



Another part is how you approach the CSS. The idea should be to work from general to specific. You can cheat a bit and have a default css file which has commented sections for the various parts of the site. If you don't have a problem with using default elements, putting standard selectors will save some time and prevents forgetting details. This means defining H1,H2,H3 elements, having empty rulesets for the various A link states. 
    
    /* Reset */
    
    /* Typography */
    
    /* Layout */
    
    /* Navigation */
    
    /* UI-elements */
    
    /* Forms */
    
    /* Media Queries */ 

You can put that into a single file or break each section into it's own file and use concatenation to join the files. Here's what ZURBS Foundation used in one of their earlier versions: 

* app.css
* forms.css
* globals.css
* grid.css
* ie.css
* mobile.css
* orbit.css
* reveal.css
* typography.css
* ui.css


That's much more complex than what we need for a quick page IMO. But the idea is the same, organize the approach.

Moving to HTML/CSS. Look over the PSD and site layout. Do you need any page types beyond the standard frontpage and article layout? What UI elements will be included ? For the most common page type create a template which you copy over, I usually make a page.php and it becomes the site's boilerplate. 

When doing a multi page site it's best to realize the header,navigation,sidebar(if present) and footer are making up the bulk of the pages. If the layout for the site isn't standard then you need to determine the most common sections and focus on those first. 

### Resets

A CSS reset forces all browsers/devices to the same level. It resets them so you work from a known state. It's about how like IE and Firefox render elements with slight differences. Get them to agree and things get much easier.

Look for the meyer reset , it was the most popular for some time. There's others and it's another thing you have to decide for yourself which suits how you work.




### Links : 

[Minimal HTML5 Doc](http://www.sitepoint.com/a-minimal-html-document-html5-edition/)

[Meyer's Reset](http://meyerweb.com/eric/thoughts/2011/01/03/reset-revisited/)

[CSS Resets - popular list](http://www.cssreset.com/)


[HTML5 Boilerplate](https://html5boilerplate.com/)

[Snippets from Boilerplate to use](http://www.1stwebdesigner.com/snippets-html5-boilerplate/)
\* Article is 5 years old - might be dated suggestions. Use as a reference but check H5B's docs for current information.


[Using PHP for templating using includes](http://buildinternet.com/2009/12/using-the-php-include-function-to-template-faster/)




