local posX = love.graphics.getWidth() / 2 - 20
local posY = 100

local SpriteUtils = {}

SpriteUtils.sprite = {
	speed = 400,
	size = 20,
	posX = posX,
	posY = posY,

	moveRight = function (self, dt)
		if self.posX < love.graphics.getWidth() - self.size then
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
		if self.posY < love.graphics.getHeight() - self.size then
			self.posY = self.posY + self.speed * dt
		end
	end
}

function SpriteUtils.spriteControl(dt) 
	if love.keyboard.isDown("right") then
		SpriteUtils.sprite.moveRight(SpriteUtils.sprite, dt)
	end
	if love.keyboard.isDown("left") then
		SpriteUtils.sprite.moveLeft(SpriteUtils.sprite, dt)
	end
	if love.keyboard.isDown("down") then
		SpriteUtils.sprite.moveDown(SpriteUtils.sprite, dt)
	end
	if love.keyboard.isDown("up") then
		SpriteUtils.sprite.moveUp(SpriteUtils.sprite, dt)
	end
end

function SpriteUtils.drawSprite()
	love.graphics.circle("fill", SpriteUtils.sprite.posX, SpriteUtils.sprite.posY, SpriteUtils.sprite.size)
end

return SpriteUtils