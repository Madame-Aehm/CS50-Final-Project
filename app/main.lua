function love.load()
	require("sprite")
	require("building")

	font = love.graphics.newFont(20)
    love.graphics.setFont(font)
end

function mainMap()
	function love.draw()
		drawSprite()
		drawBuilding("Police Station", false)
		drawBuilding("Bakery", true)
		if sprite.posY < 210 and sprite.posX > love.graphics.getWidth() - 210 then
			inPoliceStation()
		-- elseif sprite.posY < 210 and sprite.posX < 210 then
		-- 	drawBuilding("Bakery", true)
		end
	end
end

mainMap()


function love.update(dt)
	spriteControl(dt)
end


function inPoliceStation()
	local utf8 = require("utf8")
	love.keyboard.setKeyRepeat(true)
	local datevalue = ""
	local locationvalue = ""

	local activeinput = ""

	function love.mousepressed(x,y,button)
		if button == 1 then
			if x >= 10 and x <= 120 and y >= 70 and y <= 100 then
				activeinput = "date"
			elseif x >= 10 and x <= 210 and y >= 170 and y <= 200 then
				activeinput = "location"
			else
				activeinput = ""
			end
		end
	end
	
	function love.textinput(t)
		if activeinput == "date" and t:match("%d") and string.len(datevalue) < 8 then
			datevalue = datevalue .. t
		elseif activeinput == "location" then
			locationvalue= locationvalue .. t
		end
	end

	function love.keypressed(key)
		if key == "backspace" then
			if activeinput == "date" then
				local byteoffset = utf8.offset(datevalue, -1)
				if byteoffset then
					datevalue = string.sub(datevalue, 1, byteoffset - 1)
				end
			elseif activeinput == "location" then
				local byteoffset = utf8.offset(locationvalue, -1)
				if byteoffset then
					locationvalue = string.sub(locationvalue, 1, byteoffset - 1)
				end
			end
		end
	end

	function love.draw()
		drawSprite()
		drawBuilding("Police Station", false)

		-- love.graphics.printf("Enter the date (DDMMYYY) for the police reports you would like to read:", 
		-- 	10, 10, love.graphics.getWidth() - 220)
		
		-- love.graphics.rectangle("line", 10, 70, 110, 30)
		-- love.graphics.printf(datevalue, 12, 72, love.graphics.getWidth())

		dateInput(datevalue, activeinput)

		locationInput(locationvalue, activeinput)





		if not (sprite.posY < 210 and sprite.posX > love.graphics.getWidth() - 210) then
			mainMap()
		end
	end
end

function dateInput(datevalue, active)
	love.graphics.printf("Enter the date (DDMMYYY) for the police reports you would like to read:", 
		10, 10, love.graphics.getWidth() - 220)
	love.graphics.rectangle("line", 10, 70, 110, 30)
	love.graphics.printf(datevalue, 12, 72, love.graphics.getWidth())

	if active == "date" then
		love.graphics.setColor(255,165,0)
		love.graphics.rectangle("line", 5, 65, 120, 40)
		love.graphics.setColor(255,255,255)
	end
end

function locationInput(locationvalue, active)
	love.graphics.printf("Enter the name of a street:", 
		10, 130, love.graphics.getWidth() - 220)
	love.graphics.rectangle("line", 10, 170, 200, 30)
	love.graphics.printf(locationvalue, 12, 172, love.graphics.getWidth())
	-- Humphrey Street

	if active == "location" then
		love.graphics.setColor(255,165,0)
		love.graphics.rectangle("line", 5, 165, 210, 40)
		love.graphics.setColor(255,255,255)
	end
end