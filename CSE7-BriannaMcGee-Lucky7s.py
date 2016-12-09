###
#Lucky Sevens
###

# Start with $10, every game costs $1 to play
# Roll two dice
# If the result is seven, win $5 (+$4 overall after the $1 cost)

import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
money = 10
rounds_played = 0
while money > 0:    
    dice_roll = random.randint(1, 6), random.randint(1, 6)  
    rounds_played +=1
    print dice_roll[0], dice_roll[1]
    myrole = sum(dice_roll)
    if myrole == 7:
        money += 4  
        print "Your roll was a 7 you earned. Press enter to roll again:", money
    else:
        money -= 1
        print "Sorry you did not roll a 7. Press enter to roll again:", money
    raw_input()
    
print "Sorry, there's no more money in your pot.", "Rounds you played:", rounds_played
