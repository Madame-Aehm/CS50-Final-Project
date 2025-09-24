local utils = require("utils")

local PoliceStation = {}

local activeinput = ""
local inputs = {
    -- {label = "Date (DDMMYYYY):", value = "", activeKey = "date"},
	{label = "Day (1-31):", value = "", activeKey = "day"},
	{label = "Month (1-12):", value = "", activeKey = "month"},
	{label = "Year (YYYY):", value = "", activeKey = "year"},
    {label = "Location:", value = "", activeKey = "location"}
}

local function handleSubmit()
	print("Submitting with values:")
	for i, v in ipairs(inputs) do
		print(v["label"], v["value"])
	end

	local day = tonumber(inputs[1].value)
	local month = tonumber(inputs[2].value)
	local year = tonumber(inputs[3].value)
	local street = inputs[4].value

	local query = [=[
		SELECT * FROM crime_scene_reports
		WHERE ]=]
			..  [=[ street = ']=] .. street .. [=[']=]
			..  [=[ AND year = ]=] .. year
			..  [=[ AND month = ]=] .. month
			..  [=[ AND day = ]=] .. day
			.. [=[;]=]

	print("Executing query:", query)

	local results = utils.queryDB(query)
	if #results > 0 then
		print("Found", #results, "matching reports:")
		for i, row in ipairs(results) do
			for key, value in pairs(row) do
				print(key, value)
			end
			print("---")
		end
	else
		print("No matching reports found.")
	end
end


function PoliceStation.inPoliceStation()
	local utf8 = require("utf8")
	love.keyboard.setKeyRepeat(true)

	-- focus input with click
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

	-- track user input into active input value
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

	-- handle backspace
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

	local inputYStart = 10
    for i, v in ipairs(inputs) do
		inputs[i]["yStart"] = inputYStart
        utils.makeInput(inputs[i], activeinput == v["activeKey"])
		inputYStart = inputYStart + 90
    end

	utils.makeSubmitButton(
		"Submit", 
		inputs,
		handleSubmit
	)
end

return PoliceStation