from random import randint

player = raw_input('rock (r), paper (p), or scissors (s)? ')

while player != 'r' and player != 'p' and player != 's':
    player = raw_input('Must choose rock (r), paper (p), or scissors (s) ')

# end='' tells print to print an extra space instead of a line in python 3 and above

computer = randint(1, 3)
if computer == 1:
    computer = 'r'
elif computer == 2:
    computer = 'p'
else:
    computer = 's'
print(player, 'vs', computer)

if(player == computer):
    print('TIE!')
elif(player == 'r' and computer == 's' or player == 's' and computer == 'p' or player == 'p' and computer == 'r'):
    print('PLAYER WINS!')
else:
    print('COMPUTER WINS!')
