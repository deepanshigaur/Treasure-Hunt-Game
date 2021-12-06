import pygame
import turtle
import time
import random


class SteveMoore(pygame.sprite.Sprite):
	def __init__(self, x, y, image):
		pygame.sprite.Sprite._init(self)
		self.image = pygame.image.load().convert_alpha()
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect = rect
	def forward(self):
		self.rect.y += y
	def backward(self):
		self.rect.y -= y
	def left(self):
		self.rect.x -= x
	def right(self):
		self.rect.x += x

	while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.steve.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.steve.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.steve.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.steve.move_right()
	
	def search(self):
		ques1 = input("Would you like to go forward(F) or backward(B) ?")
	        ques2 = input("Would you like to go right(R) or left(L) ?")

		if ques1 == 'F':
			 = self.rect.y -= self.speed
		elif ques1 == 'B':
			= self.rect.y += self.speed
		else:
			none### add kill switch
		if ques2 == 'R':
			= self.rect.x += self.speed
		elif ques2 == :
			= self.rect.x -= self.speed
		else:
			none ### add kill switch

	def guess():
		if right == True
			self.state == "GAME OVER"
		else:
		 
		igusnum = 

			













