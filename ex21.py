def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def devide(a, b):
    print "Deviding %d / %d" % (a, b)
    return a / b

print "Let's do some math with just fuctions"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)

print "Age: %d, Height: %d, Weight: %d, Iq: %d" %(
    age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, devide(iq, 2))))

print "That becomes:", what, "Can yo dou it by hand?"
# 35 + (74- (180 * (50/2))) = -4391
