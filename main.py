#import your controller
import pygame

def main():
    #Create an instance on your controller object
	pygame.init()
	team = {"lead": "Deepanshi Gaur", "backend": "Kweku Antwi-Obeng", "frontend": "Joey Zhang"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:" , team["frontend"])
main()
