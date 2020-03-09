import pygame ##pygame module is designed for writing video games. It includes computer graphics and sound libraries
# designed to be used with the Python programming language
import time ## Initializes timing in our game. For example we use this module to set the amount of seconds that the
# game over message appears when the green box hits the jet.
import random ## random allows the objects in our game to randomly fall anywhere in the canvas.
import pygame.mixer #Allows sound to be incorporated

pygame.init()
pygame.mixer.init() #Initializes pygame mixer
display_width = 600 #display_width and display_height initializes the size of our game canvas.
display_height = 500

#Initiates the color variables used throught space dodger
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (65, 228, 52)
blue = (10, 10, 188)
Light_blue = (0, 255, 255)
purple= (145,34,255)
purple2 = (197,138,255)
gold = (224,186,186)
gold2 = (235,210,146)
yellow = (252,250,0)

car_width = 65
car_height = 65

##*****GAME INSTRUCTIONS.****** WELCOME TO SPACE DODGER 3. TO START PLAYING PRESS THE BEGIN BUTTON OTHERWISE PRESS QUIT.
##*****GAME INSTRUCTIONS.****** THE GOAL IS TO DODGE THE FALLING GREEN SQUARES, BUT BEWARE THE SPEED OF THE GREEN SQUARE INCREASE SO TAKE CAUTION.
##*****GAME INSTRUCTIONS.******  WHEN FINISHED PLAYING CLICK THE X AT THE TOP RIGHT HAND OF THE CANVAS AND REMEMBER TO RECALL THE TOTAL # OF DODGED SQUARES YOU HAD BEFORE QUITING.
##*****GAME INSTRUCTIONS.****** USE THE [a and d keys to control the blue jet otherwise use the left and right arrow keys on your keyboard]
##*****GAME INSTRUCTIONS.****** ENJOY. :)


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Dodger Game') ## Sets the caption on the game the canvas
clock = pygame.time.Clock()

#carImg Sets and gets the directory for the spacejet/vehicle image
carImg = pygame.image.load('spacejet.png')

Track = pygame.mixer.Sound('guitar.wav') #Assigns the gameplay song to a variable, also loads the soundfile
collision = pygame.mixer.Sound('Crash.aiff')#Assigns the crashing noise to a variable, also loads the soundfile
Track.play(-1) #Makes the guitar song play on start up, the '-1' allows for infinite playback
##mouseclick = pygame.mixer.Sound('click.wav')
#want to make a clicking sound once "begin" is pressed but it repeatedly playsback the sound until 'begin' is pressed

##It shows how many squares you have dodged so far
## the function def for things_dodged keeps track of the number of objects that fell on the canvas using count. this function call also writes the (text) statements and assigns the text color

def things_dodged(count):
 font = pygame.font.SysFont(None, 30)
 text = font.render("DODGED SQUARES: " + str(count), True, green)
 gameDisplay.blit(text,(2,19)) ## MOVING THE LOCATION OF DODGED SQUARES TEXT

##count2 manages how many red circles have fallen on the canvas so far, location of the text and color
def things_dodged2(count2):
 font = pygame.font.SysFont(None, 30)
 text = font.render("FALLEN DECOY CIRCLE: " + str(count2), True, red)
 gameDisplay.blit(text,(2,50)) ## MOVING THE LOCATION OF THE RED CIRCLE

##It shows how many blue circles have fallen  on the canvas so far
def things_dodged3(count3):
 font = pygame.font.SysFont(None, 30)
 text = font.render("FALLEN DECOY CIRCLE: " + str(count3), True, blue)
 gameDisplay.blit(text,(2,80)) ## MOVING THE LOCATION OF DODGED SQUARES

##draw a shape with any number of sides
#sets the blue circle coordinates like the x coordinate(xcor1), y coordinate, the width, height of the green square and color of the square. This function also manages the location of the object.
def objects(xcor1, ycor1, cirw1, cirh1, color):
 pygame.draw.polygon(gameDisplay, color, [xcor1, ycor1, cirw1, cirh1])

##defines a circle. the x coordinates and y coordinates along with the color. it then draws the circle in the game
def circle(xcor, ycor, cirw, cirh, color):
 pygame.draw.ellipse(gameDisplay, color, [xcor, ycor, cirw, cirh])
 #pygame.draw.e

##Draws a rectangle
#sets the green square coordinates like the x coordinate, y coordinate, the width, height of the green square and color of the square. This function also manages the location of the square.
def things(thingx, thingy, thingw, thingh, color):
 pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 #pygame.draw.ellipse()

##drawing background on the surface, blit the jet image
##coordinates of the jet(x,y)
def car(x,y):
 gameDisplay.blit(carImg,(x,y))

##declaring variable for font color
def text_objects(text, font):
 textSurface = font.render(text, True, black)
 return textSurface, textSurface.get_rect()

##manages the text messages displayed in the game
def messsage_display(text):
     largeText = pygame.font.Font("freesansbold.ttf", 40)
     TextSurf, TextRect = text_objects(text, largeText)
     TextRect.center = ((display_width/2), (display_height/3))
     gameDisplay.blit(TextSurf, TextRect)

     pygame.display.update()
     time.sleep(.3)
     game_loop()


##display the message when the user crashed
def crash():
     messsage_display("YOU CRASHED")

##declaring button function for the start menu
def button(msg,x,y,w,h,ic,ac, action = None):
 mouse = pygame.mouse.get_pos()
 click = pygame.mouse.get_pressed()
 #print(click)

 # print(mouse)
 ##below is the code that changes the box colors when you hover the mouse over it
 #also code below manages the quit button on the right
 if x + w > mouse[0] > x and y + h > mouse[1] > y:
     pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
     if click[0] == 1 and action != None:
         action()

 smallText = pygame.font.Font("freesansbold.ttf", 20)
 textSurf, textRect = text_objects(msg, smallText)
 textRect.center = ((x + (w / 2)), (y + (h / 2)))
 gameDisplay.blit(textSurf, textRect)

 pygame.draw.rect(gameDisplay, gold, (170, 440, 280, 50))
 # pygame.draw.circle(gameDisplay, gold,(440,300), 21)
 pygame.draw.polygon(gameDisplay, black, ((23, 41), (32, 92), (96, 89), (45, 78))) ## this is the polygon that is ontop of the S on the start screen
##polygon that is on top of the S on the start screen
def quitgame():
 pygame.quit()
 quit()


def game_intro():
 intro = True
 while intro:
     for event in pygame.event.get():
         #print(event)
         if event.type == pygame.QUIT:
             pygame.quit()
             quit()
     gameDisplay.fill(white)
     largeText = pygame.font.Font("freesansbold.ttf", 75)
     TextSurf, TextRect = text_objects("Space Dodger 3", largeText)
     TextRect.center = ((display_width/2), (display_height/4))
     gameDisplay.blit(TextSurf, TextRect)

     button("BEGIN", 35, 338, 100, 50, gold2, gold, game_loop)
     button("Quit", 470, 338, 100, 50, purple2, purple, quitgame)

     #button(msg, x, y, w, h, ic, ac)
     mouse = pygame.mouse.get_pos()
     print(mouse)

     #below is the code that chabges the box colors when you hover the mouse over it
     if 35 + 100 > mouse[0] > 35 and 338 + 50 > mouse[1] > 338:
         pygame.draw.rect(gameDisplay, gold2, (35, 338, 100, 50))
     else:
         pygame.draw.rect(gameDisplay, gold, (35, 338, 100, 50))

     if 470 + 100 > mouse[0] > 470 and 338 + 50 > mouse[1] > 338:
         pygame.draw.rect(gameDisplay, purple2, (470, 338, 100, 50))  # right_rectr
     else:
         pygame.draw.rect(gameDisplay, purple, (470, 338, 100, 50))  # right_rectr

     #pygame.draw.rect(gameDisplay, gold, (170, 440, 280, 50))
     if 170 + 280 > mouse[0] > 170 and 440 + 50 > mouse[1] > 440:
         pygame.draw.rect(gameDisplay, green, (125,440,350,50))
     else:
          pygame.draw.rect(gameDisplay, red, (125,440,350,50))
#Creates labels within the rectangles
     smallText = pygame.font.Font("freesansbold.ttf", 20)
     textSurf, textRect = text_objects('ONLY DODGE THE GREEN SQUARE', smallText)
 #x-cord + how tall the object is, then divide by two to center the X
 # y - cord + # of pixels tall then center by two
     textRect.center = ((250 + (100 / 2)), (440 + (50 / 2)))
#center the words over the button
     gameDisplay.blit(textSurf, textRect)

     smallText = pygame.font.Font("freesansbold.ttf", 20)
     textSurf, textRect = text_objects('BEGIN', smallText)
     textRect.center = ((35 +(100/2)), (338 + (50/2)))
     gameDisplay.blit(textSurf, textRect)

     smallText = pygame.font.Font("freesansbold.ttf", 20)
     textSurf, textRect = text_objects('Quit', smallText)
     textRect.center = ((470 + (100 / 2)), (338 + (50 / 2)))
     gameDisplay.blit(textSurf, textRect)

     pygame.display.update()
     clock.tick(15)

def game_loop():

     x = (display_width * 0.41)  ## move image L/R
     y = (display_height * 0.85) ## move image U/D
     x_change = 0
     y_change = 0

     thing_startx = random.randrange(0, display_width)
     thing_starty = (-50)
     thing_speed = 2 #change the speed of the falling object
     thing_width = 50 ## change the size of the object
     thing_height = 50 ## change the size of the object

     ## Blue decoy circle
     #circle(xcor, ycor, cirw, cirh, color):
     thing_xcor = random.randrange(3, display_width)
     thing_ycor = -100
     thing_cirspeed = 3 #change the speed of the falling object
     thing_cirw = 30  ## change the size of the object
     thing_cirh = 30  ## change the size of the object

     ##Red decoy circle
     # circle(xcor1, ycor1, cirw1, cirh1, color):
     thing_xcor1 = random.randrange(2, display_width)
     thing_ycor1 = 100
     thing_cirspeed1 = 5 #change the speed of the falling object
     thing_cirw1 = 30 ## change the size of the object
     thing_cirh1 = 30  ## change the size of the object

     ##initializing variables
     dodged = 0
     dodged2 = 0
     dodged3 = 0

     ##button for exiting
     gameExit = False
     while not gameExit:

         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
             ##this code sets the variables to enable us to control the jet with the (a left movement) and the (d key which makes the jet move right.
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_a:
                     x_change = -8.5 #change speed of jet
                 elif event.key == pygame.K_d:
                     x_change = 8.5

             if event.type == pygame.KEYUP:
                 if event.key == pygame.K_a or event.key == pygame.K_d:
                     x_change = 0

            ##for using right and left arrow keys
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RIGHT:
                     x_change = 6
                 elif event.key == pygame.K_LEFT:
                     x_change = -6
                     ## this code lets the jet stop once you release the left or right arrow keys because x_change is set to 0. if not the jet will continue moving even after you let go of the arrow keys.
             if event.type == pygame.KEYUP:
                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                     x_change = 0

         ##setting background color
         x += x_change
         y += y_change
         gameDisplay.fill(white)
         ## the syntax below manages the shortcut variable names that will enable us to set the x coordinates, y coordinates, height of the square width and color

         #things(thingx, thingy, thingw, thingh, color):
         things(thing_startx, thing_starty, thing_width, thing_height, green)
         thing_starty += thing_speed

         #circle(xcor, ycor, cirw, cirh, color):
         circle(thing_xcor, thing_ycor, thing_cirw, thing_cirh, blue)
         thing_ycor += thing_cirspeed

         # circle(xcor1, ycor1, cirw1, cirh1, color):
         circle(thing_xcor1, thing_ycor1, thing_cirw1, thing_cirh1, red)
         thing_ycor1 += thing_cirspeed1

         car(x,y)
         things_dodged(dodged)
         things_dodged2(dodged2)
         things_dodged3(dodged3)

         if x > display_width - car_width or x < 5:
             #x = (display_width * 0.30) ##reset jet in the middle of canvas
             collision.play()#Plays crash sound when object crashes to window
             crash()
        ## Green square
         if thing_starty > display_height:
             thing_starty = 0 - thing_height
             thing_startx = random.randrange(0, display_width)
             dodged += 1 ## increments one after dodging the object
             thing_speed += .3 ## increase the speed of the object while number of dodges goes up
        ##Blue circle
         if thing_ycor > display_height:
             thing_ycor = 0 - thing_cirh
             thing_xcor = random.randrange(3, display_width)
             thing_cirspeed += .01
             thing_cirw += 1 ## increase the size of the object
             thing_cirh += 1
             dodged3 += 1

        ## Red circle
         if thing_ycor1 > display_height:
             thing_ycor1 = 0 - thing_cirh1 ## makes the object fall at different locations
             thing_xcor1 = random.randrange(2, display_width)
         #if dodged2 % 10 == 0:
             dodged2 += 1  ## increments one everytime the red decoy circle falls over the canvas
             thing_cirw1 +=  (.10) ## increase the size of the object
             thing_cirh1 += (.10) ## increase the size of the object

     ## checking if the box hit our jet
         if y < thing_starty + thing_height:
             print('y cross_Over')

             if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                 print('x cross over')
                 collision.play() #plays crash sound if object collides with killbox
                 crash()


         pygame.display.update()
         clock.tick(60)
##calling most of the variables we defined earlier.
game_intro()
game_loop()
pygame.quit()
quit()

