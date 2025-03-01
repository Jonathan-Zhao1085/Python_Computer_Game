"""
Program Name: Stickman Battle
Programmer Name: Jonathan Zhao
Program Date: June 13th, 2023
Program Description: a two player fighting game which tracks scores and records match history into a text file while keeping individual players’ scores recorded. Border control and cooldown mechanics are also incorporated
Program Input: multiple strings
Program Outputs: strings written into a text file
"""

#import tkinter module and random module
import tkinter as tk
import random

#create a class called Menu, for the menu screen
"""
Program Name: Stickman Battle
Programmer Name: Jonathan Zhao
Program Date: June 13th, 2023
Class Description: sets up the menu screen
Class Input: multiple strings
Class Outputs: strings extracted from a file
"""
class Menu:
    #initialize all the variables and text
    #create a class called Menu, for the menu screen
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: initializes the menu screen
    Function Inputs: none
    Function Outputs: strings and images
    """
    def __init__(self, root):

    #create the tips mechanism
        #create a list called tips containing a series of tips for the game
        tips = ["Patience Is Key", "Timing, Timing, Timing", "Remeber The Cooldown!", "Try Moving Diagonal", "When all else fails, BRUTE FORCE", "Strategy. You Must Have A Plan", "Predicting: Beneficial, Detrimental", "Risks are risky :D", "Minceraft"]
        #make the random module assign a random integer within the index of the tips list to a variable called random_index
        random_index = random.randint(0, 8)
        #assign a variable called random_tip as the random_index of the tips list
        random_tip = tips[random_index]

    #set up the canvas for the menu        
        self.root = root
        #set the width and height as 990x990
        self.canvas = tk.Canvas(self.root, width=990, height=990)
        self.canvas.pack()

    #display text on screen allinged in the center: "WELCOME TO" and "STICKMAN BATTLE"
        #"WELCOME TO": x=495, y=50, font is (Arial,50) and color is black
        self.canvas.create_text(495, 50, text="WELCOME TO", font=("Arial", 50))
        #"WELCOME TO": x=495, y=120, font is (Arial,50) and color is black
        self.canvas.create_text(495, 120, text="STICKMAN BATTLE", font=("Arial", 50))

    #display the text for the random tip on screen
        #"TIP!": x=495, y=600, font is (Arial,30) and color is black
        self.canvas.create_text(120, 600, text = "TIP!", font=("Arial", 30))
        #random_tip: x=495, y=640, font is (Arial,20) and color is black
        self.canvas.create_text(230, 640, text = str(random_tip), font=("Arial", 15))

    #create the buttons for starting the game and entering player names
        #create a button labeled "PLAY", assigning to it the function start_game
        self.play_button = tk.Button(self.canvas, text="PLAY", command=self.start_game, width=50, height = 7, bg = "white")
        #make the play button located at x=495, y=250
        self.canvas.create_window(495, 250, window=self.play_button)
        #create a button labeled "PLAYERS", assigning to it the function start_player_entry
        self.player_entry_button = tk.Button(self.canvas, text="PLAYERS", command=self.start_player_entry, width=40, height = 6)
        #make the players button located at x=495, y=400
        self.canvas.create_window(495, 400, window=self.player_entry_button)

    #render the character images on the sides of the screen
        #assign the file path of the red image to the varaible character_red_image
        self.character_red_image = tk.PhotoImage(file="C:\\stickmanrs.png").subsample(2)
        #make character_red_image located at x=900, y=400
        self.canvas.create_image(900, 400, image=self.character_red_image)
        #assign the file path of the blue image to the varaible character_blue_image
        self.character_blue_image = tk.PhotoImage(file="C:\\stickmanbs.png").subsample(2)
        #make character_blue_image located at x=90, y=400
        self.canvas.create_image(90, 400, image=self.character_blue_image)

        #create a dictionary for players names and their scores
        file = open("C:\\Score Keeper.txt", "r")
        sentence = file.readline()
        self.dictionary = {}
        List = sentence.split()
        for i in range(len(List)):
            temp = List[i].split(":")
            self.dictionary[temp[0]] = int(temp[1])

        #create a player search box
        self.canvas.create_text(660, 632, text="Search Player Name", font=("Arial", 15), fill="Black")
        #create an entry box for player search
        self.search = tk.Entry(self.canvas, width=17, font = ("Arial", 15))
        #display player search entry box
        self.canvas.create_window(660, 660, anchor=tk.CENTER, window=self.search)
        #create a button labeled "submit"
        self.submit_button = tk.Button(self.canvas, text="search", command=self.submit, width=5, height=1)
        #make the submit button
        self.canvas.create_window(772, 660, window=self.submit_button)

    #create a function to submit the player name to find their score
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: searches for a string from a file
    Function Inputs: strings
    Function Outputs: strings
    """
    def submit(self):
        try:
            self.canvas.delete(self.score)
            self.search_name = self.search.get()
            try:
                self.number = str(self.dictionary[self.search_name])
                self.score = self.canvas.create_text(663, 690, text="score is: " + self.number, font=("Arial", 12), fill="Black")
            except:
                pass

        except:
            self.score = self.canvas.create_text(663, 690, text="", font=("Arial", 12), fill="Black")
            self.canvas.delete(self.score)
            self.search_name = self.search.get()
            try:
                self.number = str(self.dictionary[self.search_name])
                self.score = self.canvas.create_text(663, 690, text="score is: " + self.number, font=("Arial", 12), fill="Black")

            except:
                pass


    #create the function to start the game aspect
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: starts the game class
    Function Inputs: none
    Function Outputs: none
    """
    def start_game(self):
    #close the menu and open the game
        #close the menu canvas
        self.canvas.destroy()
        #create an instance of the game class
        game = Game(self.dictionary)
        #use the run_game function to run the game aspect
        game.run_game()

    #create a game to start the Player_Entry class
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: starts the player entry class
    Function Inputs: none
    Function Outputs: none
    """
    def start_player_entry(self):
    #close the menu and open the player entry window
        #close the menu canvas
        self.canvas.destroy()
        #create an instance of the player entry class
        player_entry = Player_Entry(self.root, self.dictionary)
        #run the player entry class
        player_entry.run_player_entry()

    #make a function to run the menu screen
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: runs the menu screen
    Function Inputs: none
    Function Outputs: none
    """
    def run_menu(self):
        #run the menu
        self.root.mainloop()


        
#create a class for the player name entry window
"""
Program Name: Stickman Battle
Programmer Name: Jonathan Zhao
Program Date: June 13th, 2023
Class Description: sets up the player entry screen
Class Input: multiple strings
Class Outputs: strings extracted from a file
"""
class Player_Entry:
    #initialize all the varaibles and display text on screen
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: initializes the player entry screen
    Function Inputs: none
    Function Outputs: strings write into file
    """
    def __init__(self, root, dictionary):

    #pass the dictionary from the menu class into the player entry class
        self.dictionary = dictionary
        self.dictionary_string = ""

    #set up the canvas
        self.root = root
        #make the width and height 990 by 990
        self.canvas = tk.Canvas(self.root, width=990, height=990)
        self.canvas.pack()

    #create a button to go back to the menu
        #create a button labeled "DONE", assigning to it the function back_to_menu
        self.menu_button = tk.Button(self.canvas, text="DONE", command=self.back_to_menu, width=35, height=5)
        #make the DONE button located at x=495, y=250
        self.canvas.create_window(495, 700, window=self.menu_button)

    #create player name entries
        #create text "PLAYER 1 NAME" with the color blue and have it at x=210, y=150
        self.canvas.create_text(210, 150, text="PLAYER 1 NAME", font=("Arial", 15), fill="blue")
        #create an entry box for player 1
        self.player_one = tk.Entry(self.canvas, width=15, font = ("Arial", 20))
        #display player 1's entry box at x=210, y=200
        self.canvas.create_window(210, 200, anchor=tk.CENTER, window=self.player_one)

        #create text "PLAYER 2 NAME" with the color red and have it at x=780, y=150
        self.canvas.create_text(780, 150, text="PLAYER 2 NAME", font=("Arial", 15), fill="red")
        #create an entry box for player 2
        self.player_two = tk.Entry(self.canvas, width=15, font = ("Arial", 20))
        #display player 2's entry box at x=210, y=200
        self.canvas.create_window(780, 200, anchor=tk.CENTER, window=self.player_two)

        #create text to show player 1's controls, located underneath player 1's name entry 
        self.canvas.create_text(210, 300, text="PLAYER 1 Controls", font=("Arial", 15), fill="black")
        self.canvas.create_text(210, 330, text="Movement: W,S,A,D", font=("Arial", 13), fill="black")
        self.canvas.create_text(210, 360, text="Attack: Q", font=("Arial", 13), fill="black")
        
        #create text to show player 2's controls, located underneath player 2's name entry box
        self.canvas.create_text(780, 300, text="PLAYER 2 Controls", font=("Arial", 15), fill="black")
        self.canvas.create_text(780, 330, text="Movement: I,K,J,L", font=("Arial", 13), fill="black")
        self.canvas.create_text(780, 360, text="Attack: P", font=("Arial", 13), fill="black")

    #create the function that goes back to the menu
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: brings program back to menu class and saves player name entries
    Function Inputs: none
    Function Outputs: writes into file
    """
    def back_to_menu(self):
        #global is used to make game class have access to player names
        global blue_name
        global red_name

        #retrieve the names entered and assign them as variables
        blue_name = self.player_one.get()
        red_name = self.player_two.get()

        #check if the entered names are already in the dictionary
        #if the names are not already in the dictionary, add them in
        if red_name not in self.dictionary and red_name != "":
            self.dictionary[str(red_name)] = 0
        if blue_name not in self.dictionary and blue_name != "":
            self.dictionary[str(blue_name)] = 0

        #format the dictionary to write back into the file without curly brackets, etc.
        for key, value in self.dictionary.items():
            self.dictionary_string += key + ":" + str(value) + " "
            self.dictionary_string.strip()

        #write the modified dictionary string into the score keeper text file
        file = open("C:\\Score Keeper.txt", "w")
        file.write(self.dictionary_string)
        file.close()

        #close the player entry window
        self.canvas.destroy()
        #create an instance of the menu class
        menu = Menu(self.root)
        #run the menu
        menu.run_menu()

    #create a function to run the player entry window
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: runs the player entry window
    Function Inputs: none
    Function Outputs: none
    """
    def run_player_entry(self):
        #run the player entry window
        self.root.mainloop()

"""
Program Name: Stickman Battle
Programmer Name: Jonathan Zhao
Program Date: June 13th, 2023
Class Description: sets up the game window
Class Input: keyboard control keys
Class Outputs: writes into a file
"""
#create the class for the game
class Game:
    #initialize the variables
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: initializes the game window
    Function Inputs: none
    Function Outputs: strings and images
    """
    def __init__(self, dictionary):

        #pass the player scores dictionary into the game
        self.dictionary = dictionary
        self.dictionary_string = ""

        #set the x and y coordinates of the characters
        self.redx = 930
        self.redy = 690
        self.bluex = 60
        self.bluey = 690

        #set up the window for the game
        self.root = root
        self.canvas = tk.Canvas(self.root, width=990, height=780)
        self.canvas.pack()

        #import the character normal and attack images from computer files
        self.character_red_normal = tk.PhotoImage(file="C:\\stickmanrs.png").subsample(3)
        self.character_red_attack = tk.PhotoImage(file="C:\stickmanra.png").subsample(3)

        self.character_blue_normal = tk.PhotoImage(file="C:\\stickmanbs.png").subsample(3)
        self.character_blue_attack = tk.PhotoImage(file="C:\\stickmanba.png").subsample(3)

        #load the images on screen
        self.red = self.canvas.create_image(self.redx, self.redy, image=self.character_red_normal)
        self.blue = self.canvas.create_image(self.bluex, self.bluey, image=self.character_blue_normal)

        #set the cooldown statuses of the characters as false
        self.reddown = False
        self.bluedown = False

        #set the scores of the players as 0
        self.redscore = 0
        self.bluescore = 0

        #create the hitbox of the red character
        self.red_left_hitbox = self.redx - 50
        self.red_right_hitbox = self.redx + 50
        self.red_top_hitbox = self.redy - 110
        self.red_bottom_hitbox = self.redy + 110

        #create the hitbox of the blue character
        self.blue_left_hitbox = self.bluex - 50
        self.blue_right_hitbox = self.bluex + 50
        self.blue_top_hitbox = self.bluey - 110
        self.blue_bottom_hitbox = self.bluey + 110

        #create text onscreen that shows red's score
        self.redtext = self.canvas.create_text(930, 50, text=str(self.redscore), font=("Arial", 24), fill="red")

        #create text onscreen that shows blue's score
        self.bluetext = self.canvas.create_text(60, 50, text=str(self.bluescore), font=("Arial", 24), fill="blue")

        #make the program able to receive keyboard commands
        self.canvas.focus_set()
        #make a command happen once the key is released
        self.canvas.bind("<KeyRelease>", self.move_players)

    #create a function to update the score of red
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: updates a score
    Function Inputs: none
    Function Outputs: creates text on screen
    """
    def updatered(self):
        self.canvas.delete(self.redtext)
        self.redtext = self.canvas.create_text(930, 50, text= str(self.redscore), font=("Arial", 24), fill="red")

    #create a fucntion to update the score of blue
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: updates a score
    Function Inputs: none
    Function Outputs: creates text on screen
    """
    def updateblue(self):
        self.canvas.delete(self.bluetext)
        self.bluetext = self.canvas.create_text(60, 50, text= str(self.bluescore), font=("Arial", 24), fill="blue")

    #create a function for red's attack mechanism
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: changes the image to the attack image
    Process: checks for a cooldown
    Function Inputs: none
    Function Outputs: an image
    """
    def redfight(self):
        if not self.reddown:
            self.redcheck()
            self.updatered()
            self.canvas.delete(self.red)
            self.red = self.canvas.create_image(self.redx, self.redy, image=self.character_red_attack)
            self.root.after(300, self.redback)
            self.redcooldown()
            
    #create a function to make red character go back to normal
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: changes the image to the normal image
    Function Inputs: none
    Function Outputs: an image
    """
    def redback(self):
        self.canvas.delete(self.red)
        self.red = self.canvas.create_image(self.redx, self.redy, image=self.character_red_normal)

    #create a function for blue's attack mechanism
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: changes the image to the attack image
    Process: checks for a cooldown
    Function Inputs: none
    Function Outputs: an image
    """
    def bluefight(self):
        if not self.bluedown:
            self.bluecheck()
            self.updateblue()
            self.canvas.delete(self.blue)
            self.blue = self.canvas.create_image(self.bluex, self.bluey, image=self.character_blue_attack)
            self.root.after(300, self.blueback)
            self.bluecooldown()

    #create a function to make blue character go back to normal
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: changes the image to the normal image
    Function Inputs: none
    Function Outputs: an image
    """
    def blueback(self):
        self.canvas.delete(self.blue)
        self.blue = self.canvas.create_image(self.bluex, self.bluey, image=self.character_blue_normal)

    #create a function that initiates red's cooldown
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: starts the cooldown
    Function Inputs: none
    Function Outputs: none
    """
    def redcooldown(self):
        self.reddown = True
        self.root.after(3000, self.reddone)

    #create a funcion that ends red's cooldown
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: stops the cooldown
    Function Inputs: none
    Function Outputs: none
    """
    def reddone(self):
        self.reddown = False

    #create a function that initiates blue's cooldown
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: starts the cooldown
    Function Inputs: none
    Function Outputs: none
    """
    def bluecooldown(self):
        self.bluedown = True
        self.root.after(3000, self.bluedone)
    
    #create a funcion that ends blue's cooldown
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: stops the cooldown
    Function Inputs: none
    Function Outputs: none
    """
    def bluedone(self):
        self.bluedown = False

    #make function to check if red got hit
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: checks to see if a point should be added
    Process: Checks to see if the hitboxes are overlapped
    Function Inputs: none
    Function Outputs: updates the player score variables
    """
    def redcheck(self):
        if (
            self.red_left_hitbox >= self.blue_left_hitbox and self.red_left_hitbox <= self.blue_right_hitbox
        ) or (
            self.red_right_hitbox >= self.blue_left_hitbox and self.red_right_hitbox <= self.blue_right_hitbox
        ):
            if (
                self.red_top_hitbox >= self.blue_top_hitbox and self.red_top_hitbox <= self.blue_bottom_hitbox
            ) or (
                self.red_bottom_hitbox >= self.blue_top_hitbox and self.red_bottom_hitbox <= self.blue_bottom_hitbox
            ):
                self.redscore += 1

    #make function to check if blue got hit
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: checks to see if a point should be added
    Process: Checks to see if the hitboxes are overlapped
    Function Inputs: none
    Function Outputs: updates the player score variables
    """
    def bluecheck(self):
        if (
            self.blue_left_hitbox >= self.red_left_hitbox and self.blue_left_hitbox <= self.red_right_hitbox
        ) or (
            self.blue_right_hitbox >= self.red_left_hitbox and self.blue_right_hitbox <= self.red_right_hitbox
        ):
            if (
                self.blue_top_hitbox >= self.red_top_hitbox and self.blue_top_hitbox <= self.red_bottom_hitbox
            ) or (
                self.blue_bottom_hitbox >= self.red_top_hitbox and self.blue_bottom_hitbox <= self.red_bottom_hitbox
            ):
                self.bluescore += 1

    #create movement and attack keys for the players
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: moves the players on screen
    Function Inputs: keyboard movement inputs
    Function Outputs: moves images
    """
    def move_players(self, event):
        #attack keys
        if event.keysym == "p" and self.bluescore < 5 and self.redscore < 5:
            self.redfight()
            if self.redscore == 5:
                self.canvas.create_text(495, 50, text="RED WINS!", font=("Arial", 50), fill="black")
                try:
                    self.dictionary[red_name] += 1
                    for key, value in self.dictionary.items():
                        self.dictionary_string += key + ":" + str(value) + " "
                        self.dictionary_string.strip()
                    file = open("C:\\Score Keeper.txt", "w")
                    file.write(self.dictionary_string)
                    file.close()
                    quit()

                except:
                    pass

        elif event.keysym == "q" and self.redscore < 5 and self.bluescore < 5:
            self.bluefight()
            if self.bluescore == 5:
                self.canvas.create_text(495, 50, text="BLUE WINS!", font=("Arial", 50), fill="black")
                try:
                    self.dictionary[blue_name] += 1
                    for key, value in self.dictionary.items():
                        self.dictionary_string += key + ":" + str(value) + " "
                        self.dictionary_string.strip()
                    file = open("C:\\Score Keeper.txt", "w")
                    file.write(self.dictionary_string)
                    file.close()
                    quit()
                    
                except:
                    pass
                
                
                    
        #movement keys
        if event.keysym == "i":
            self.canvas.move(self.red, 0, -30)
            self.redy -= 30
            if self.redy < 90:
                self.canvas.coords(self.red, self.redx, 90)
                self.redy += 30
            self.red_top_hitbox = self.redy - 110
            self.red_bottom_hitbox = self.redy + 110
        elif event.keysym == "k":
            self.canvas.move(self.red, 0, 30)
            self.redy += 30
            if self.redy > 690:
                self.canvas.coords(self.red, self.redx, 690)
                self.redy -= 30
            self.red_top_hitbox = self.redy - 110
            self.red_bottom_hitbox = self.redy + 110
        elif event.keysym == "j":
            self.canvas.move(self.red, -30, 0)
            self.redx -= 30
            if self.redx < 30:
                self.canvas.coords(self.red, 30, self.redy)
                self.redx += 30
            self.red_left_hitbox = self.redx - 50
            self.red_right_hitbox = self.redx + 50
        elif event.keysym == "l":
            self.canvas.move(self.red, 30, 0)
            self.redx += 30
            if self.redx > 960:
                self.canvas.coords(self.red, 960, self.redy)
                self.redx -= 30
            self.red_left_hitbox = self.redx - 50
            self.red_right_hitbox = self.redx + 50
        elif event.keysym == "w":
            self.canvas.move(self.blue, 0, -30)
            self.bluey -= 30
            if self.bluey < 90:
                self.canvas.coords(self.blue, self.bluex, 90)
                self.bluey += 30
            self.blue_top_hitbox = self.bluey - 110
            self.blue_bottom_hitbox = self.bluey + 110
        elif event.keysym == "s":
            self.canvas.move(self.blue, 0, 30)
            self.bluey += 30
            if self.bluey > 690:
                self.canvas.coords(self.blue, self.bluex, 690)
                self.bluey -= 30
            self.blue_top_hitbox = self.bluey - 110
            self.blue_bottom_hitbox = self.bluey + 110
        elif event.keysym == "a":
            self.canvas.move(self.blue, -30, 0)
            self.bluex -= 30
            if self.bluex < 30:
                self.canvas.coords(self.blue, 30, self.bluey)
                self.bluex += 30
            self.blue_left_hitbox = self.bluex - 50
            self.blue_right_hitbox = self.bluex + 50
        elif event.keysym == "d":
            self.canvas.move(self.blue, 30, 0)
            self.bluex += 30
            if self.bluex > 960:
                self.canvas.coords(self.blue, 960, self.bluey)
                self.bluex -= 30
            self.blue_left_hitbox = self.bluex - 50
            self.blue_right_hitbox = self.bluex + 50

    #create a function to run the game
    """
    Program Name: Stickman Battle
    Programmer Name: Jonathan Zhao
    Program Date: June 13th, 2023
    Function Description: runs the game class
    Function Inputs: none
    Function Outputs: none
    """
    def run_game(self):
        self.root.mainloop()


#set root as an instance of the tkinter module
root = tk.Tk()
#create an instance of the menu class
menu = Menu(root)
#run the menu
menu.run_menu()


