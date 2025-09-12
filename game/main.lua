function love.load()
	-- require("sprite")
	-- windowWidth = love.graphics.getWidth()
	-- windowHeight = love.graphics.getHeight()

	tick = require("lib/tick")
	drawRect = false
	tick.delay(function() drawRect = true end, 2)
end


function love.draw()
	-- love.graphics.circle("fill", sprite.posX, sprite.posY, sprite.size)
	-- if drawRect then
		love.graphics.rectangle("line", 100, 100, 100, 100)
	-- end
end


-- function love.update(dt)
-- 	spriteControl(dt)
-- end
