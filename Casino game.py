import random #must include cuz python doesnt include by def same with time
import time
Money = 500 
while True: # establish a while loop
    if Money <= 0:
        print ("You have depleted all your funds")
        
        Money = 500
        time.sleep(1)  #sets a cooldown for when user deplete funds
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("You have Replenished your funds\n")
    print ("Ready to be a winner?!")
    answer = input(" Yes  No \n")

    if answer.lower()=="Yes":
        print ("Let's hope you win!")

        print ("Okay. Here is your result:")

        randomarray = random.randint(1,10) # allow random odds to be generate

        result = ""

        if randomarray == 1:
            result = "winner!" 
            Money += 200   
        elif 2 <= randomarray <= 10:
            result = "You lose"
            Money -= 50
        print (result)
        print ("Your fund:", Money)
    elif answer.lower()=="No":
        print ("Come back again!")
        break





