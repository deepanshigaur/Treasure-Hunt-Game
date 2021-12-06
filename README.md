:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
### << Semester, Year >>
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

<< [https://github.com/<repo>](#) >>

<< [link to demo presentation slides](#) >>

### Team: Amigos de frijoles
#### Team Members:
	Deepanshi Gaur
	Joey Zhang
	Kweku Antwi-Obeng

***

## Project Description *(Software Lead)*
A typical treasure hunt game where the player has to find the treasure that could be hidden randomly in the 1 of the 6 rooms. The game starts with the 'start screen' and  providing instructions to the user. The player gets 3 attempts to guess where the treasure is hidden. If the player guesses correctly, they win, but after 3 failed attempts the game will automatically end and the game over screen will appear. The player can be moved by the user by pressing the buttons 'F', 'B', 'L', 'R' that indicates moving forward, backward, left and right respectively.

***    

## User Interface Design *(Front End Specialist)*

1. Start Screen/Instructions Screen-
This opening screen is the first thing the player sees upon playing, there is a big "start" button to begin the game and the title "Steven Moore's Treasure Adventure" is displayed at the top of the screen. The instructions are displayed below the "Start" button and it tells the user how to play the game by pressing certain buttons to navigate around the map.
	![IMG_1789](https://user-images.githubusercontent.com/89817993/144934577-fd920f94-c24c-40b6-87aa-6bf7b53a9a42.png)

2. The Game Menu-
This screen is where the treasure hunt actually begins. A player icon is set in the middle of a map and the treasure is in one of the six rooms. The user is able to move the character around by pressing certain buttons mentioned in the instructions. The player gets three chances to try and successfully find the treasure within the six rooms in order to win. 
	![IMG_1786](https://user-images.githubusercontent.com/89817993/144914801-8dbe0733-6afa-4aa5-a67e-30a4f3a466d0.png)
	
3. The "You Win" Screen-
If the player is able to successfully find the treasure within the three tries that they are given then the "You Win" screen will pop up indicating their victory.
	![IMG_1787](https://user-images.githubusercontent.com/89817993/144914963-3e8544b5-040c-48e8-adb4-c640f2679b2d.png)

4. The "Game Over" Screen-
If the player still can't reach the treasure within three tries then the game will be over. The "game over" sign will pop up along with the "play again" button for them to restart the game. 
	![IMG_1788](https://user-images.githubusercontent.com/89817993/144914885-0df72fdb-3f88-4258-8811-232cef40681e.png)

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. >>
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
        * ![class diagram](assets/class_diagram_v110241024_1.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * << You should have a list of each of your classes with a description. >>
	-Dickinson Building: creates the background/setting for the model to move around in
	-Steven_ moore: object controller by user input that moves within the setting
## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* bin
    * <all of your python files should go here>
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Deepanshi Gaur

* Worked as integration specialist by underlining our responsibilities and contacting other team mates, making deadlines and making sure everyone meets them. Regularly met on Tuesdays and Thursdays to ensure progress and discussed new ideas that can make the game more interesting. She also helped in creating the User Interface Images with the front-end specialist and designed the overall layout of the game screen. She tested the overall code, debugged it and made sure it can't be broken by the user. the development environment was also set up by the software lead.

### Front End Specialist - Joey Zhang

* Specifically analysed the structure of the Johnson's building in Dickinson Community for reference to map out the background of the game, Created the player icon and the hidden treasure. She created the game start/ instructure screen, game screen, winning screen and the game over screen. She went through the pygame documentation and tutorials to find the relevant pygame feature that helps in making the code drier and concise. She also collaborated with the software lead to find a testing strategy and worked on design outline.
	
### Back End Specialist - Kweku Antwi-Obeng

* The back end specialist helped with the “Model” portion of Treasure hunt by writing the major classes that would be used in the main game, as well as implementing major pygame functionality into each of them. He created the basic class and controller flowchart to get the initial idea of the code layout. He collaborated with Software lead to create the project structure. He also collaborated with Front-End in the implementation of the classes and functions. 

## Testing *(Software Lead)*
* << Describe your testing strategy for your project. >>
    * << Example >>

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Open terminal, navigate to folder/directory, run main.py | Game is initialized                         |                 |
|  2  | Player receives hint/message with possible hiding spots  | The console is updated to display a message |                 |
|  3. | Player chooses to move forward, left, or right, back     | The user is inputting the correct option and is interacting with the main game when the message pops up in the console |           |
|  4. | In three room check attempts, the treasure should be found. If three incorrect rooms are checked, or if the player chooses to backward more than three times the game over screen appears | If the treasure is found the screen will be updated to congratulate the player, If the treasure isn’t found or three moves were used up then the screen is updated to game over |
    
  


