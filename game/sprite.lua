sprite = {
	speed = 400,
	size = 20,
	posX = 100,
	posY = 100,

	moveRight = function (self, dt)
		if self.posX < windowWidth - self.size then
			self.posX = self.posX + self.speed * dt
		end
	end,

	moveLeft = function (self, dt)
		if self.posX > self.size then
			self.posX = self.posX - self.speed * dt
		end
	end,

	moveUp = function (self, dt)
		if self.posY > self.size then
			self.posY = self.posY - self.speed * dt
		end
	end,

	moveDown = function (self, dt)
		if self.posY < windowHeight - self.size then
			self.posY = self.posY + self.speed * dt
		end
	end
}

function spriteControl(dt) 
	if love.keyboard.isDown("right") then
		sprite.moveRight(sprite, dt)
	end
	if love.keyboard.isDown("left") then
		sprite.moveLeft(sprite, dt)
	end
	if love.keyboard.isDown("down") then
		sprite.moveDown(sprite, dt)
	end
	if love.keyboard.isDown("up") then
		sprite.moveUp(sprite, dt)
	end
end
