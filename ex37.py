def test():
    index = 0
    while index < 100:
        print "Now index = %d" % index
        if index % 27 == 26:
            break
        index += 1

test()
