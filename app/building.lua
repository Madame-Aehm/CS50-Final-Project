function drawBuilding(label, left, topOffset)
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