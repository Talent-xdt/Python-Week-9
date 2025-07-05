#Lesson 2 (exp)
try:
    print(x)
except NameError:
    print("Variable is not deined")
else:
    ("Everything went wrong")
    
x = -1
if x < 0:
    raise Exception("Sorry no numbers below zero")

# TRY, EXCEPT, FINALLY, ELSE AND RAISE