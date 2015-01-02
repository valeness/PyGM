PyGM
====

GM logic for Python

The goal of this project is to create a game engine in Python that is as easy to work with as GML.

PyGM is based heavily around PyGame, but only for drawing and GUI rendering. A fully capable text game could be built using just PyGM classes and functions.

## QuickStart
To start a basic PyGame window, do:
```python
from PyGM.master import *

# Initialize PyGame Window and set screen dimensions
pygame.display.init()
# Must set dimensions as a tuple
screen = pygame.display.set_mode((320, 240))

# Make sure the loop runs
running = True
# Set Window Caption
pygame.display.set_caption("PY-GM")

# Initialize Main Game Loop
while running:
	# Add keys pressed to a dict for access
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT or(keys[pygame.K_ESCAPE]):
			running = False
```

This will show you a black screen 320px by 240px. Keep note that the console is still running behind the window, keep track of this, we'll be using it to test and show realtime data on alarms.

Now we'll add all the PyGM stuff to it, I'll try my damnedest to comment them well.

```python
from PyGM.master import *

# Initialize PyGame Window and set screen dimensions
pygame.display.init()
# Must set dimensions as a tuple
screen = pygame.display.set_mode((320, 240))

# Set clock FPS
FPS = 60
# Initialize Clock (Keeps time between screen draws consistent)
clock = pygame.time.Clock()

# Make sure the loop runs
running = True
# Set Window Caption
pygame.display.set_caption("PY-GM")

# Create the Game Timer Class
class GameTimer(Entity):
    def __init__(self, **kw):
        super(GameTimer, self).__init__(**kw)
        # Define Alarms
        # alarm_example needs to be the name of the function
        # you want to call after a certain number of steps
        # 200 is the number of steps, or "Frames" before 
        # the function is called
        self.alarm = {"alarm_example": 200}

    def alarm_example(self):
    	print("Alarm Ended")
    	print("Function Executed!")

	# Define the event step
	# Determines what this 'object' does every step
    def event_step(self):
    	super(GameTimer, self).event_step()
    	# Print each step of the alarm
    	# (Printing the alarm step can slow the game at high FPS)

# Create another Game Object
# Example could be an RPG character
class Character(Entity):
	def __init__(self, **kw):
		super(Character, self).__init__(**kw)
		self.hitpoints = 50
		self.alarm = {"take_damage": 200}

	def take_damage(self):
		print("RPG Character takes 20 hitpoints!")
		self.hitpoints - 20
		print("Hitpoints: %s") % self.hitpoints

	def event_step(self):
		super(Character, self).event_step()
		if self.alarm:
			print self.alarm
		else:
			pass

# Initialize the Game Room
NewGameRoom()
# Add the GameTimer as a game object
NewGameRoom.add_object(0, 0, GameTimer)
# Add your RPG character
# 10, 10 are the x/y coordinates
# Even though not visible, the coordinates
# are important and link directly to
# graphics when implemented
NewGameRoom.add_object(10, 10, Character)

# In order to access your objects, you 
# must assign them to variables

# The object index is the order in which the object 
# was loaded into the room. You can also select
# an object by coordinates
timer = NewGameRoom.object_index(1)
char = NewGameRoom.object_index(NewGameRoom.type_nearest(10, 10, Character))

# Initialize Main Game Loop
while running:
	# Add keys pressed to a dict for access
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT or(keys[pygame.K_ESCAPE]):
			running = False

	# Make all objects perform their "event_step"
	# Essentially one world step
	NewGameRoom.room_step()

	# Tick the Pygame Clock
	# This just standardizes the room_step
	clock.tick(FPS)

	# Flip Surface to screen
	pygame.display.flip()
```

That was a lot to take in so we'll go through it later when I feel like fleshing out the rest of the readme... lol