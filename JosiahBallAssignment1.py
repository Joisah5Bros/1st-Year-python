# INF360B - Programming in Python
# Josiah Ball
# Assignment 1
#(1 point) - Initial comments*
#(2 points) - Use of the print() function to display a welcome and prompt a question to the user.
#(2 points) - Use of the input() function and store in a variable called myInput.
#(1 point) - Use the print() function to print the contents of myInput.
#(2 points) - Use two different math operators from Table 1-1 in your script. This may be used to manipulate some input from the user.
#(2 points) - Use string concatenation.
print('welcome user.')
print('Lets start with math. What does 2 + 2 =')
myInput1 = input('>')
print('what is your first name')
myInput = input('>>>')
print('what is your last name')
myName = input('>>')
print('what is your age')
myAge = input('>')
print(myInput, 'I thought you would be older')
print('Whats greater 18% or 20%?')
greater = input('>>>')
if greater == ('1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27') :
    print('wrong try again')                 #need to fix not correct code
elif greater == ('20') :
    print('correct')
print ('press enter to continue')           # splitting up print code information
kkey = input('>')
print ('your first answer + your age =')
print (int(myInput1) + int(myAge))
print ('press enter to see full name')
kkkey = input('>')
print ('Your full name is')
print ((myInput) + '_' + (myName))
print ('press enter to continue')
key = input('>')
print ('you are going to be 100 Years Old in')
howClose = (100 - int(myAge))
print (str(howClose) + ('years'))


