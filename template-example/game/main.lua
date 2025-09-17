function love.load()
	-- require("sprite")
	-- windowWidth = love.graphics.getWidth()
	-- windowHeight = love.graphics.getHeight()
	x = 200
	y = 200
end



function love.draw()
	-- love.graphics.circle("fill", sprite.posX, sprite.posY, sprite.size)
	love.graphics.rectangle("line", x, y, 100, 100)
end

function love.keypressed(key)
	if key == "space" then
		x = math.random(100, 500)
		y = math.random(100, 500)
	end
end


-- function love.update(dt)
-- 	spriteControl(dt)
-- end


