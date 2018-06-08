import random
i = 0

while i < 10:
    random_number = random.randint(1,10)
    i = i + 1
    guessed_number = int(raw_input("Guess an integer (between 1 and 10): "))
    print 'random_number is ', random_number
if guessed_number > random_number:
    print "Your guess is too high."
if guessed_number < random_number:
    print "Your guess is too low"
if guessed_number == random_number: 
    print "you are correct!"
    'break'
