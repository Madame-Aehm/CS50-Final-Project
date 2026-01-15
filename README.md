# CS50 Final Project

My idea was to create a gamified UI for the CS50 SQL Challenge. I really enjoyed learning SQL with this challenge, and wanted to attempt to implement those queries into a project of some kind. 

## Version 0: LÖVE 

The first version of my project was attempted with LÖVE, a game engine framework on Lua, as this framework is recommended on the CS50 suggestions for projects. 

I enjoyed learning about coding with a game engine, using the frame refresh to draw and redraw based on updates. I got as far as creating a sprite, and when it goes into a building, the screen will redraw based on the location. In the police station, the first step is to look through the crime scene reports, and so I created inputs so the user can type the day, month, year, and location, and those filters will apply to the SQL query. I connected the SQLite database, constructed a query from the input values, and could print the output in the console. 

Ultimately, I found myself wanting HTML elements. Building the inputs from scratch was very challenging, and then trying to decide how I was going to display the output in a scrollable table was overwhelming, since I know I could use HTML to display this so easily in a browser. So I reconsidered my options, and decided to use Flask instead. This would mean rethinking how the user navigates the map, relying on point and click rather than a sprite. 

## Version 1: Flask

I already have some experience in web development, but CS50 was my first time using Flask. After using JavaScript frameworks like React and Next.js, I found the different approach of handling all rendering server-side to be challenging, but I've always found the surest way to learn a new framework is to create a little project, so I've used this as an opportunity to kill 2 birds! 

It is a very bare-bones design in terms of style, using font and basic CSS to create something of an old-school 8-bit look. The available pages include:
  - Landing page
  - Map 
  - Police station
  - Bakery

### Landing page

The landing page gives the user a summary of what they are expected to achieve for the game.

### Map

The map is how the user will navigate the game. 

### Clue Modal

There is a button on the bottom right side of the page that will open a modal with clues. The first clue is the initial clue provided by the game, all other clues must be added by the user as they uncover information. The clues are rows from tables in the database that the user might want to see again, this is simply a reference point and can be used or ignored. I did not want to have to build authentication, so the clues are saved in the local storage of the browser to maintain persistence across multiple sessions. 

### Police Station

The police station is the first stop for the user, as the first clue suggests they start their investigation here to learn more information about the crime. There is a single form that has been customized to make queries to two separate tables, based on the user's selections. I used JavaScript to change the visual cues on the form to represent the appropriate labels. The trickiest part was syntax related, when I discovered some of the strings in the interviews table had apostrophes that would break the string in the Jinja template. In the end my solution was to write a function to replace all of those symbols. 

### Bakery




resources:
## sql
- https://lua.sqlite.org/home/doc/tip/doc/lsqlite3.wiki
- https://github.com/CentauriSoldier/SQLite3-for-Lua
- https://github.com/togfoxy/TacticalGridIron/blob/main/main.lua
