local utils = {}


function utils.queryDB(query)
	require("/lib/sqlite3")
	local db = sqlite3.open("fiftyville.db")

	local result = {}
	if db then
		local function showRow(_, colCount, values, names)
			local row = {}
			for i = 1, colCount do
				-- print(names[i], values[i])
				row[names[i]] = values[i]
			end
			
			table.insert(result, row)
			return 0
		end
		db:exec(query, showRow)
	else
		print("Database connection failed")
	end
	db:close()
	-- for i, row in ipairs(result) do
	-- 	for key, value in pairs(row) do
	-- 		print(key, value)
	-- 	end
	-- 	print("---")
	-- end
	return result
end


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
	love.graphics.setColor(1, 1, 1)
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


function utils.makeSubmitButton(label, inputs, submitFunction)
	local lastInputY = inputs[#inputs]["yStart"]
	love.graphics.rectangle("line", 10, lastInputY + 90, 100, 30)
	love.graphics.printf(label, 25, lastInputY + 92, 105)

	local mouseX, mouseY = love.mouse.getPosition()
	if mouseX >= 10 and mouseX <= 110 and mouseY >= lastInputY + 90 and mouseY <= lastInputY + 120 then
		love.graphics.setColor(255,165,0)
		love.graphics.rectangle("line", 5, lastInputY + 85, 110, 40)
		love.graphics.setColor(255,255,255)
	end

	if love.mouse.isDown(1) and mouseX >= 10 and mouseX <= 110 and mouseY >= lastInputY + 90 and mouseY <= lastInputY + 120 then
		love.graphics.setColor(255,165,0)
		love.graphics.rectangle("fill", 5, lastInputY + 85, 110, 40)
		love.graphics.setColor(0,0,0)
		love.graphics.printf(label, 25, lastInputY + 92, 105)
		love.graphics.setColor(255,255,255)
		if submitFunction then
			submitFunction()
		end
	end
end

return utils