#Lesson 1 exception_handling(TRY, EXCEPT,FINALLY)

try:
    print(x)
except:
    print("An exception occured") # Answer = An exception occured

 #2
try:
    print(x)
except NameError:
    print("Varriable x is not defined")
except:
    print("An exception occured") #Answer = Varriable x is not defined

#3  
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is fineshed ") #Answer = Something went wrong The 'try except' is fineshed 