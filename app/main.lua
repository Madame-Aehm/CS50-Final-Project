gamestate = "map"

function love.load()
	require("sprite")
	require("policestation")

	font = love.graphics.newFont(20)
    love.graphics.setFont(font)
end

function love.draw()
	love.graphics.circle("fill", sprite.posX, sprite.posY, sprite.size)
	if sprite.posY < 210 and sprite.posX > love.graphics.getWidth() - 210 then
		drawBuilding("Police Station", false)
	elseif sprite.posY < 210 and sprite.posX < 210 then
		drawBuilding("Bank", true)
	else
		drawBuilding("Police Station", false)
		drawBuilding("Bank", true)
	end
end

function love.update(dt)
	spriteControl(dt)
end
