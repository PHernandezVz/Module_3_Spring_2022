 #change numbers to see how it works
score_one = 90
score_two = 81

#You can build simple expressions with one condition using relational operators
if score_one > 90:
    print("A")
else:
    print("Not an A")

#Or compound expressions
if score_one > 90 and score_two > 90:
    print("A")
else:
    print("Not an A")

#There can even be compound statements, for multiple choices
if score_one > 90:
    print("A")
elif score_one > 80:
    print("B")
else:
    print("Not A or B")
