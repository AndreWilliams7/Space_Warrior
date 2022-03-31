# This example shows how a class can have attributes that are also classes.
# We are also passing functions through the classes, in particular the look_at values.
# Start with a breakpoint on andre.look_at(100, 200) and step into the code to see how it executes and how the parts fit.


class Eye:
    def __init__(self, name, color):
        self.name = name
        self.look_position = {"x": 0, "y": 0}
        self.color = color

    def look_at(self, x, y):
        self.look_position["x"] = x
        self.look_position["y"] = y
        print(self.name, "is looking at:", self.look_position)


class Ear:
    def listen(self):
        return

class Head:
    def __init__(self, eye_color):
        self.left_eye = Eye("left eye", eye_color)
        self.right_eye = Eye("right eye", eye_color)
        self.left_ear = Ear()
        self.right_ear = Ear()

    def look_at(self, x, y):
        self.left_eye.look_at(x, y)
        self.right_eye.look_at(x, y)

    def listen(self):
        self.left_ear.listen()
        self.right_ear.listen()

# a person has a head and
# a head has two eyes and two ears
# each eye and each ear has its own attributes and function on its own
class Person:
    def __init__(self):
        self.head = Head("blue")

    def look_at(self, x, y):
        # calling this function will chain it all the way until it gets to the eye who does the work.
        # debug to see how this works.
        self.head.look_at(x, y)


andre = Person()
andre.look_at(100, 200)
