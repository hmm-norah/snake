from includes import *
from board import board


def main():
	game = board()
	screen.fill(WHITE)

	finished = False
	while not finished:
		clock.tick(fps)

		game.draw_apples()

		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished = True


	# while True:
	# 	events = pygame.event.get()
	# 	for event in events:
	# 		if event.type == pygame.KEYDOWN:
	# 			if event.key == pygame.K_LEFT:
	# 				print("Left Key")
	# 			elif event.key == pygame.K_RIGHT:
	# 				print("Right Key")


	# pygame.event.pump()
	# keys = pygame.key.get_pressed()
	#
	# if keys[pygame.K_RIGHT]:
	# 	print("Right arrow pressed")
	#
	# keys[pygame.K_RIGHT]


main()
