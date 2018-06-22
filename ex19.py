def party_time(countA, countB):
    print "There are %d A!" %countA
    print "There are %d B!" %countB
    print "Time for a party!"
    print "Go ahead!"

print "Just assign number to the parameters"
party_time(10,8)

print "Use variables from script"
amount_A = 16
amount_B = 23
party_time(amount_A, amount_B)

print "Use math to calculate"
party_time(15+8, 77-69)

print "Variables with math"
party_time(amount_A * 3, amount_B % 5)
