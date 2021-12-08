import pygame
import turtle
import random
import time

class SteveMoore(pygame.sprite.Sprite):
	def __init__(self, x, y, image):
		pygame.sprite.Sprite._init(self)
		self.image = pygame.image.load(img_file).convert_alpha()
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

	
	def search(self):
		self.state == "GAME"
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
	def guess(self, room):
		ingusnum == 0
		if right == True
			print("You guessed right!!!!!!!")
		else:
		 
		igusnum += 1


			













