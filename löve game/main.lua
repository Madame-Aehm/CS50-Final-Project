io.stdout:setvbuf("no")

local utils = require("utils")
local PoliceStation = require("policestation")
local SpriteUtils = require("sprite")
-- require("/lib/sqlite3");

function love.load()
	font = love.graphics.newFont(20)
    love.graphics.setFont(font)
end


function love.draw()
	SpriteUtils.drawSprite()
	if SpriteUtils.sprite.posY < 210 and SpriteUtils.sprite.posX > love.graphics.getWidth() - 210 then
		PoliceStation.inPoliceStation()
	-- 
	elseif SpriteUtils.sprite.posY < 210 and SpriteUtils.sprite.posX < 210 then
		utils.drawBuilding("Bakery", true)
	else
		utils.drawBuilding("Police Station", false)
		utils.drawBuilding("Bakery", true)
		utils.drawBuilding("Gym", false, 220)
		utils.drawBuilding("University", true, 220)
	end
	
end


function love.update(dt)
	SpriteUtils.spriteControl(dt)
end