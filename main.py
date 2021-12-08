#import your controller
import pygame
from src import controller
def main():
    #Create an instance on your controller object
	pygame.init()
	team = {"lead": "Deepanshi Gaur", "backend": "Kweku Antwi-Obeng", "frontend": "Joey Zhang"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:" , team["frontend"])
	main_window = controller.Controller()
	main_window.mainLoop()
main()
