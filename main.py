import sys, time
from PyGM.master import *

pygame.display.init()
screen = pygame.display.set_mode((320, 240))

FPS = 60
clock = pygame.time.Clock()

running = True
pygame.display.set_caption("PY-GM")

class GameTimer(Entity):
    def __init__(self, **kw):
        super(GameTimer, self).__init__(**kw)
        self.alarm = {"print_complete": 200, "end_game": 20000}

    def print_complete(self):
        print "Completed!"

    def end_game(self):
        global running
        running = False
        print "game ended"

    def event_step(self):
        super(GameTimer, self).event_step()
        #print self.alarm

class Character(Entity):
    def __init__(self, **kw):
        super(Character, self).__init__(**kw)
        self.last = pygame.time.get_ticks()
        self.cooldown = 500
        self.alarm = {'stand': 11}

    def stand(self):
        if self.alarm['stand'] == 0:
            self.alarm = {'stand': 10}
            group_draw(group, screen)
        elif self.alarm['stand'] == 11:
            self.alarm = {'stand': 10}
            group_draw(group, screen)

    def event_step(self):
        super(Character, self).event_step()
        # print self.alarm['stand']
        
    

class Tree(Entity):
    def __init__(self, **kw):
        super(Tree, self).__init__(**kw)
        self.alarm = {"sayhi" : 500}

    def sayhi(self):
        print "hi"

    def event_step(self):
        super(Tree, self).event_step()


NewGameRoom()
NewGameRoom.add_object(0, 0, GameTimer)
NewGameRoom.add_object(0, 0, Tree)
NewGameRoom.add_object(100, 100, Character)

obj = NewGameRoom.object_index(1)
obj_maple = NewGameRoom.object_index(2)

spr_maple = Create_Sprite('assets/stand1_0.png', obj_maple)
spr_maple.images.append(load_image('assets/stand1_1.png'))
spr_maple.images.append(load_image('assets/stand1_2.png'))
spr_maple.images.append(load_image('assets/stand1_3.png'))

group = pygame.sprite.Group(spr_maple)

#NewGameRoom.instance_destroy(NewGameRoom.type_nearest(100, 0, Tree))

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE]):
            running = False
        if keys[pygame.K_UP]:
            obj.sayhi()

    obj_maple.stand()

    #make all objects in world preform step event
    NewGameRoom.room_step()

    clock.tick(FPS)

    pygame.display.flip()

