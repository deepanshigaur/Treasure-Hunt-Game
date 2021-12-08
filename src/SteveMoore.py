import pygame
import turtle
import random

class SteveMoore(pygame.sprite.Sprite):
	def __init__(self, x, y, image):
		"""
	creates the background of the game
	args: self(class), x, y , image
	return: None
		"""
		pygame.sprite.Sprite._init(self)
		self.image = pygame.image.load(img_file).convert_alpha()
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect = rect
	def forward(self):
		"""
	moves the player icon forward
	args: self(class)
	return: None
		"""
		self.rect.y += y
	def backward(self):
		"""
	moves the player icon backward
	args: self(class)
	return: None
		"""
		self.rect.y -= y
	def left(self):
		"""
	moves the player icon forward
	args: self(class)
	return: None
		"""
		self.rect.x -= x
	def right(self):
		"""
	moves the player icon forward
	args: self(class)
	return: None
		"""
		self.rect.x += x

	
	def search(self):
		"""
	asks user which direction they wanna go to
	args: self(class)
	return: None
		"""
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
		"""
	prints you guessed right if the player succesafully finds the treasure
	args: self(class)
	return: None
		"""
		ingusnum == 0
		if right == True
			print("You guessed right!!!!!!!")
		else:
		 
		igusnum += 1


			













