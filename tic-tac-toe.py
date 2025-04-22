import pygame
from pygame.locals import *

pygame.init()

screen_height = 300
screen_width = 300
line_width = 20
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('game')


r = (255,155,255)
g = (2,231,200)
b = (200,0,135)


font = pygame.font.SysFont(None, 40)


clicked = False
player = 1
pos = (0,0)
markers = []
game_over = False
winner = 0


again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)


for x in range (3):
	row = [0] * 3
	markers.append(row)



def draw_board():
	bg = (28,10,6)
	grid = (50, 50, 50)
	screen.fill(bg)
	for x in range(1,3):
		pygame.draw.line(screen, grid, (0, 100 * x), (screen_width,100 * x), line_width)
		pygame.draw.line(screen, grid, (100 * x, 0), (100 * x, screen_height), line_width)

def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, r, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
				pygame.draw.line(screen, r, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
			if y == -1:
				pygame.draw.circle(screen, g, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
			y_pos += 1
		x_pos += 1	


def check_game_over():
	global game_over
	global winner

	x_pos = 0
	for x in markers:
		
		if sum(x) == 3:
			winner = 1
			game_over = True
		if sum(x) == -3:
			winner = 2
			game_over = True
		
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == 3:
			winner = 1
			game_over = True
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == -3:
			winner = 2
			game_over = True
		x_pos += 1

	
	if markers[0][0] + markers[1][1] + markers [2][2] == 3 or markers[2][0] + markers[1][1] + markers [0][2] == 3:
		winner = 1
		game_over = True
	if markers[0][0] + markers[1][1] + markers [2][2] == -3 or markers[2][0] + markers[1][1] + markers [0][2] == -3:
		winner = 2
		game_over = True

	
	if game_over == False:
		tie = True
		for row in markers:
			for i in row:
				if i == 0:
					tie = False
		
		if tie == True:
			game_over = True
			winner = 0



def draw_game_over(winner):

	if winner != 0:
		end_text = "Player " + str(winner) + " wins"
	elif winner == 0:
		end_text = "!you both tied!"

	end_img = font.render(end_text, True, b)
	pygame.draw.rect(screen, g, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
	screen.blit(end_img, (screen_width // 2 - 100, screen_height // 2 - 50))

	again_text = ' play again'
	again_img = font.render(again_text, True, b)
	pygame.draw.rect(screen, g, again_rect)
	screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))



run = True
while run:

	
	draw_board()
	draw_markers()

	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			run = False
		
		if game_over == False:
			
			if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
				clicked = True
			if event.type == pygame.MOUSEBUTTONUP and clicked == True:
				clicked = False
				pos = pygame.mouse.get_pos()
				cell_x = pos[0] // 100
				cell_y = pos[1] // 100
				if markers[cell_x][cell_y] == 0:
					markers[cell_x][cell_y] = player
					player *= -1
					check_game_over()

	
	if game_over == True:
		draw_game_over(winner)
		
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
		if event.type == pygame.MOUSEBUTTONUP and clicked == True:
			clicked = False
			pos = pygame.mouse.get_pos()
			if again_rect.collidepoint(pos):
				
				game_over = False
				player = 1
				pos = (0,0)
				markers = []
				winner = 0
				
				for x in range (3):
					row = [0] * 3
					markers.append(row)

	
	pygame.display.update()

pygame.quit()
