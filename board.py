from includes import *

from snake import snake
from apple import apple


class board:

	def __init__(self):
		self.player = snake(screen_width/2, screen_height/2)

		self.apples = []
		for i in range(number_of_apples):
			self.apples.append(apple())

	def randomize_all(self):
		for i in self.apples:
			self.apples[i] = random.randrange(0, 800)

	def draw_apples(self, collision=False):
		if collision:
			for i in range(len(self.apples)):
				if self.apples[i] == collision:
					self.apples[i].randomize()
					self.player.grow()
		else:
			for i in range(len(self.apples)):
				self.apples[i].draw()

	# bounding box collision inspired by
	# https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection
	
	def check_collision(self, new_location, locations):
		signal = -1
		for i in range(len(locations)):
			if new_location[0] < locations[i].x + pixel and \
				new_location[1] < locations[i].y + pixel and \
				new_location[0] + pixel > locations[i].x and \
				new_location[1] + pixel > locations[i].y:
				signal = i

		return signal

	def check_wall(self, new_location):
		if new_location[0] < 0 or new_location[1] < 0 or new_location[0] > screen_width or new_location[1] > screen_height:
			return 1
		return 0

	def game_over(self):
		message = font.render('Game Over!', False, BLACK)
		center = message.get_rect(center=(screen_width/2, screen_height/2))
		screen.blit(message, center)

		message = font.render('Press \'r\' to continue!', False, BLACK)
		center = message.get_rect(center=(screen_width/2, screen_height/2 + font_size))
		screen.blit(message, center)

		return 0

	def update(self):
		self.draw_apples()

		new_location = self.player.move()

		# Check if an apple was hit
		hit = self.check_collision(new_location, self.apples)

		if hit > -1:
			pygame.draw.rect(screen, WHITE, (self.apples[hit].x, self.apples[hit].y, pixel, pixel), 0)
			self.apples[hit].randomize()

			self.player.grow()

		# Check if the snake body was hit
		self.check_collision(new_location, self.player.body)

		if self.check_collision(new_location, self.player.body) > 0 or self.check_wall(new_location) > 0:
			return self.game_over()

		return 1
