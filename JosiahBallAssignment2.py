# INF360B - Programming in Python
# Josiah Ball
# Assignment 2
#(1 point) - Initial comments*
#(1 points) - Use at least 2 different comparison operators.
#(1 points) - Use at least 1 boolean operator (and, or, not).
#(2 points) - Write at least 1 if statement that MUST contain 2 elif statements and 1 else statement.
#(2 points) - Write at least 1 while statement that contains a break and continue.
#(2 points) - Write at least 1 for loop using the range() method.
#(1 point) - Use the import keyword to import the random module. Use the random.randint() function somewhere in your script.
v = str('a')              #input for if a
x = str('b') 
z = str('c') 
y = str('d')
vV = str('A')
xX = str('B')
zZ = str('C')
yY = str('D')
numBer = int('6')
import random
l = random.randint(1,10)
 
print("You are roaming around in africa against mothers approval")
print("press enter to continue")
kkey = input(">>")
print("But you know that there is a cool cliff you can cliff jump from")
print("press enter to continue")
kkKey = input(">>")
print("you are walking towards the cliff when you get a..")
print("funny feeling there is a predator near by.")
print("press enter to continue")
kKkey = input(">>")
print("if you come up on a lion should you... Use A,B,C, or D for your answer")
print(" ")
print("A. ----- Hide, the Lion can't see me")
print(" ")
print("B. ---- Run, you think the lion will not beable to catch you before reaching the cliff")
print(" ")
print("C. --- Scream, the Lion is scared of loud noise")
print(" ")
print("D. -- Do Nothing, the Lion ain't bothering anyone")
print(" ")
print("press enter to start")

ais = input ('>>')


while True:  # trying to loop everything 
    ais = input ('>>')
    if ais == v or ais == vV:  # Hide
        print('The lion found you before you could hide.')
        print('Try again')
        continue
    elif ais == x or ais == xX:  # Run
        print('Run, you had to jump off of the cliff.')
        break
    elif ais == z or ais == zZ:  # Scream
        print('The lion is not scared of loud noise; you were attacked.')
        print('Try again')
        continue
    elif ais == y or ais == yY:  # Do Nothing
        print('The lion had not eaten in 2 weeks; you were his lunch.')
        print('Try again')
        continue
    else:
        ais != x or ais != xX
        print('Choose again')
        print('Try again')
        continue
    
print('the lion jumped when you were jumping')
print('guess the right number to break your fall with the lion. Pick between 1-10')

number = int(input('>>'))
    
###trying to loop everything  BREAK CODE AFTER PUTTING IN B FOR ANSWER
for numbers in range(1,10):
    print ('')
    if (number == int(l)):
        print('critical grab')
        break
    else:
        print ('the number is')
        print (l)
        print ('choose another number')
        l = random.randint(1, 10)  # generating new random number next time you input
        number = int(input('>>'))
        continue
print ('you survived... well done!')
print (exit)

   
        

