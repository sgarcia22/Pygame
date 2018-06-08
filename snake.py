import pygame
import random

def main():
	pygame.init()

	pygame.display.set_caption = "Pygame Snake Game"
	screen = pygame.display.set_mode((500,500))
	clock = pygame.time.Clock()
	x = 235
	y = 235
	running = True
	food_alive = False
	temp_x = 0
	temp_y = 0
	last_pressed = None
	while running:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False	
		#Movement
		button = pygame.key.get_pressed()
		prev_x = x
		prev_y = y
		if button[pygame.K_UP]: 
			last_pressed = pygame.K_UP
		elif button[pygame.K_DOWN]: 
			last_pressed = pygame.K_DOWN
		elif button[pygame.K_RIGHT]: 
			last_pressed = pygame.K_RIGHT
		elif button[pygame.K_LEFT]: 
			last_pressed = pygame.K_LEFT

		if last_pressed == pygame.K_DOWN:
			y += 3
		elif last_pressed == pygame.K_UP:
			y -= 3
		elif last_pressed == pygame.K_RIGHT:
			x += 3
		elif last_pressed == pygame.K_LEFT:
			x -= 3

		#Make sure player stays in bounds of screen
		if x < 0: x = prev_x
		if x > 500: x = prev_x - 15
		if y < 0: y = prev_y
		if y > 500: y = prev_y - 15

		screen.fill((0,0,0))
		pygame.draw.rect(screen, (0,255,0), pygame.Rect(x,y,15,15))

		#Food 
		curr = random_pos(food_alive, screen)
		#If not picked up, None
		if curr is not None:
			food_alive = True
			temp_x = curr[0]
			temp_y = curr[1]
			pygame.draw.rect(screen, (255,0,0), pygame.Rect(curr[0],curr[1],15,15))
		else:
			pygame.draw.rect(screen, (255,0,0), pygame.Rect(temp_x,temp_y,15,15))

		if abs(x - temp_x) <= 20 and abs(y - temp_y) <= 20:
			#Ate the food
			food_alive = False
			pygame.draw.rect(screen, (255,255,255), pygame.Rect(temp_x,temp_y,15,15))

		clock.tick(60)
		pygame.display.flip()

def random_pos(alive, screen):
	food = None
	if not alive:
		rand_num = random.randint(0, 500 * 500)
		rand_x = rand_num % 500
		rand_y = int (rand_num / 500)
		food = [rand_x, rand_y]
		print (food)
	if food: return food
	else: return None

if __name__=="__main__":
	main() 