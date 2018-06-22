from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is yet configured. Subclass it and implement Enter()"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.open_scene()
        last_scene = self.scene_map.next_scene('finished')


        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    quips = [
        "You died, you kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "Such a looser.",
        "I have a small puppy that's better than this."
    ]

    def enter(self):
        print Death.quips[randint (0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "You are running down the central corriddor to the Weapons Armory"
        print "when a Gothon jumps out, red scarly skin, dark grimp teeth, and"
        print "evil clown costume following around his hate filled body. He is"
        print "blocking the door to the Armory and about to pull a weapon to"
        print "blast you."

        action = raw_input("\"shoot\" or \"dodge\" or\"tell a joke\":>")

        if action == "shoot":
            print "Quick on the draw you tank out your blaster and fire it at"
            print "Gothon, his clown costume is floowing and moving around his"
            print "body, which throws off your aim. Your laser hit his costume"
            print "but missed him entirely. This completed ruins his brand new"
            print "costume his monther bought him, which makes him fly into an"
            print "insane rage and blast you repeatly in the face until you are"
            print "dead. Then he eats you!"

            return 'death'

        elif action == "dodge":
            print "Like a world class boxer you dodge, weave, slip and slide"
            print "right as Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps"
            print "on your head and eats you!"

            return 'death'

        elif "joke" in action:
            print "Lucky for you they made you learn Gothon insults in the past"
            print "You tell the one Gothon joke you know:"
            print "Lrad vhg!d zyprt kkir!"
            print "The Gothon stops, tries not to laugh, then burst out laughing"
            print "and cannot move."
            print "While he's launghing you run up and shoot him square in the"
            print "head, putting him down, then jump through the weapon armory"
            print "door!"

            return "finished"

        else:
            print "CANNOT COMPUTE!"
            return 'central_corridor'

class Finished(Scene):
    def enter(self):
        print "Congrats, you won!"
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        #'laser_weapon_armory': LaserWeaponArmory(),
        #'the_bridge': TheBridge(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def open_scene(self):
        return self.next_scene(self.start_scene)


new_map = Map('central_corridor')
new_game = Engine(new_map)
new_game.play()
