local utils = require("utils")

local PoliceStation = {}

local activeinput = ""
local inputs = {
    {label = "Date (DDMMYYYY):", yStart = 10, value = "", activeKey = "date"},
    {label = "Location:", yStart = 100, value = "", activeKey = "location"}
}

function PoliceStation.inPoliceStation()
	local utf8 = require("utf8")
	love.keyboard.setKeyRepeat(true)

	function love.mousepressed(x,y,button)
		if button == 1 then
			for i, v in ipairs(inputs) do
				if x >= 10 and x <= 310 and y >= v["yStart"] + 35 and y <= v["yStart"] + 65 then
					activeinput = v["activeKey"]
					return
				end
			end
			activeinput = ""
		end
	end
	
	
	function love.textinput(t)
		if activeinput ~= "" then
			for i, v in ipairs(inputs) do
				if v["activeKey"] == activeinput then
					if activeinput == "date" then 
                        if t:match("%d") and string.len(inputs[i].value) < 8 then
				        	inputs[i].value = inputs[i].value .. t
                        end
                    else
                        inputs[i].value = inputs[i].value .. t
                    end
					return
				end
			end
		end
	end

	function love.keypressed(key)
		if key == "backspace" then
			if activeinput ~= "" then
				for i, v in ipairs(inputs) do
					if v["activeKey"] == activeinput then
						local byteoffset = utf8.offset(v["value"], -1)
						if byteoffset then
							inputs[i]["value"] = string.sub(v["value"], 1, byteoffset - 1)
						end
					end
				end
			end
		end
	end

    utils.drawBuilding("Police Station", false)

    for i, v in ipairs(inputs) do
        utils.makeInput(inputs[i], activeinput == v["activeKey"])
    end

end

return PoliceStation