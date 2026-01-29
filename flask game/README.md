# CS50 Final Project - Ducknapped!

For the video demo [click here](https://youtu.be/xNdaNFJcj0c).

My idea was to create a gamified UI for the CS50 SQL Challenge. I really enjoyed learning SQL with this challenge, and wanted to attempt to implement those queries into a project of some kind. 

## Version 0: LÖVE 

The first version of my project was attempted with LÖVE, a game engine framework on Lua, as this framework is recommended on the CS50 suggestions for projects. 

I enjoyed learning about coding with a game engine, using the frame refresh to draw and redraw based on updates. I got as far as creating a sprite, and when it goes into a building, the screen will redraw based on the location. In the police station, the first step is to look through the crime scene reports, and so I created inputs so the user can type the day, month, year, and location, and those filters will apply to the SQL query. I connected the SQLite database, constructed a query from the input values, and could print the output in the console. 

Ultimately, I found myself wanting HTML elements. Building the inputs from scratch was very challenging, and then trying to decide how I was going to display the output in a scrollable table was overwhelming, since I know I could use HTML to display this so easily in a browser. So I reconsidered my options, and decided to use Flask instead. This would mean rethinking how the user navigates the map, relying on point and click rather than a sprite. 

## Version 1: Flask

I already have some experience in web development, but CS50 was my first time using Flask.

Rather than continuing to use the SQLite database, I decided to move everything into an PostgreSQL database hosted on Supabase, with the eventual intention of being able to deploy the Flask app to be playable online.

I decided against an authentication strategy, and instead store all game progress in the browser's local storage. 

It is a very simple design in terms of style, using font and basic CSS to create something of an old-school 8-bit look. The available pages include:
  - Landing page
  - Map 
  - Police station
  - Bakery
  - Bank
  - Phone Company
  - Airport
  - Report

### Landing page

The landing page gives the user a summary of what they are expected to achieve for the game.

### Map

The map is how the user will navigate the game.

### Clue Modal

There is a button on the bottom right side of the page that will open a modal with clues. The first clue is the initial clue provided by the game, all other clues must be added by the user as they uncover information. The clues are rows from tables in the database that the user might want to see again, this is simply a reference point and can be used or ignored. This is the data saved to the local storage, in order to persist between sessions. 

### First page

The police station is the first stop for the user, as the first clue suggests they start their investigation here to learn more information about the crime. There is a single form that has been customized to make queries to three separate tables (crime_scene_reports, interviews, and people for license plate match), based on the user's selections. I used JavaScript to change the visual cues on the form to represent the appropriate labels. 

The trickiest part was syntax related, when I discovered one of the of the strings in the interviews table had apostrophes that would break the string in the Jinja template, but others used a curly apostrophe that didn't cause a problem. I started by writing a function that would replace all instances of "'" with "’", but after looking at how often this occurred, it was only one string that was clearly added by the CS50 team to be the clue, so I simply updated this manually in the Supabase database.

### Second page

Writing the filter query for the bakery is when I decided that it was also time to reformat the way dates and times are saved in the table. So consolidated the date and time columns into single timestamps. I've added this value to the police interviews and reports, however I've left that code to use as proof that this step was necessary.

### Third page and beyond...

The bank is where I realized I wouldn't be able to just customize the same form for different purposes, so I created another template where the different forms could be rendered, based on what the user is looking for. 

After completing these routes, my `app.py` was getting very long, and the code felt inefficient. I took some time to look at the documentation for Flask, then installed Cursor and asked my first agent to review my code and suggest improvements. It suggested using Blueprints to organize my routes, macros to reduce code repetition, and a library to make my validation more robust (I had been validating everything manually).

I worked with it to implement its suggestions and create the next few pages, which work very much the same as the previous pages, with custom forms. I also found a tutorial that suggested using `.html.j2` files, which would mean I could install extensions for syntax highlighting. 

#### resources:
- https://lua.sqlite.org/home/doc/tip/doc/lsqlite3.wiki
- https://github.com/CentauriSoldier/SQLite3-for-Lua
- https://github.com/togfoxy/TacticalGridIron/blob/main/main.lua
- https://nagasudhir.blogspot.com/2022/05/macros-in-python-flask-jinja-templates.html
- https://codepen.io/albpara/pen/JjRarO
- https://pixabay.com/
