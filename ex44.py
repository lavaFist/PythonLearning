class Parent(object):
    def implicit(self):
        print "parent implicit()"

    def overwrite(self):
        print "parent overwrite()"

    def altered(self):
        print "parent altered()"

class Child(Parent):

    def overwrite(self):
        print "child overwrite()"

    def altered(self):
        print "child before altered()"
        super(Child, self).altered()
        print "child after altered()"

class Other(object):
    def implicit(self):
        print "Other implicit()"

    def overwrite(self):
        print "Other overwrite()"

    def altered(self):
        print "Other altered()"

class Child2(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        other.implicit()

    def overwrite(self):
        print "Child2 overwrite()"

    def altered(self):
        print "child2 before altered()"
        other.altered()
        print "child2 after altered()"

dad = Parent()
son = Child()
other = Other()
girl = Child2()

print "\n"
print "*"* 10 , " implicit ", "*"* 10

dad.implicit()
son.implicit()
other.implicit()
girl.implicit()
print "*"* 10 , " overwrite ", "*"* 10
dad.overwrite()
son.overwrite()
other.overwrite()
girl.overwrite()
print "*"* 10 , " altered ", "*"* 10
dad.altered()
son.altered()
other.altered()
girl.altered()
print "\n"
