local utils = {}

function utils.drawBuilding(label, left, topOffset)
    local size = 200
    local x, y
    if left == true then
        x, y = 10, topOffset or 10
    else
        x, y = love.graphics.getWidth() - (size + 10), topOffset or 10
    end
    love.graphics.rectangle("line", x, y, size, size)

	local text_width = font:getWidth(label)
	local text_height = font:getHeight()
	local text_x = x + (size - text_width) / 2
    local text_y = y + (size - text_height) / 2
	love.graphics.setColor(1, 1, 1) -- Set text color to white (RGB: 1, 1, 1)
    love.graphics.print(label, text_x, text_y)
end

function utils.makeInput(input, active) 
	love.graphics.printf(input["label"], 
		10, input["yStart"], love.graphics.getWidth() - 220)
	love.graphics.rectangle("line", 10, input["yStart"] + 35, 300, 30)
	love.graphics.printf(input["value"], 12, input["yStart"] + 37, love.graphics.getWidth())

	if active then
		love.graphics.setColor(255,165,0)
		love.graphics.rectangle("line", 5, input["yStart"] + 30, 310, 40)
		love.graphics.setColor(255,255,255)
	end
end

return utils