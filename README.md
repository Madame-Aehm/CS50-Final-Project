# LÖVE

The first version of my project was attempted with LÖVE, a game engine framework on Lua, as this framework is recommended on the CS50 suggestions for projects. 

I enjoyed learning about coding with a game engine, using the frame refresh to draw and redraw based on updates. I got as far as creating a sprite, and when it goes into a building, the screen will redraw based on the location. In the police station, the first step is to look through the crime scene reports, and so I created inputs so the user can type the day, month, year, and location, and those filters will apply to the SQL query. I connected the SQL database, constructed a query from the input values, and could print the output in the console. 

Ultimately, I found myself wanting HTML elements. Building the inputs from scratch was very challenging, and then trying to decide how I was going to display the output in a scrollable table was overwhelming, since I know I could use HTML to display this so easily in a browser. So I reconsidered my options, and decided to use Flask instead. This would mean rethinking how the user navigates the map, relying on point and click rather than a sprite. 


resources:

## lua

## sql
- https://lua.sqlite.org/home/doc/tip/doc/lsqlite3.wiki
- https://github.com/CentauriSoldier/SQLite3-for-Lua
- https://github.com/togfoxy/TacticalGridIron/blob/main/main.lua

## clues
- All you know is that the theft took place on July 28, 2023 and that it took place on Humphrey Street.