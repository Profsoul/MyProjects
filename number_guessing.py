#import the Random module.
import random as rd

#define the function to start the game.
def play():
    print("Guess the number",end = "  ")
    print("||| For help enter '-1'")

    magic_number = rd.randint(1,100)
#define the function for option 2.
    def anal(val,a,b):
        if val<=a+4:
            print("Number range from {}-{}".format(a,a+4))
        else:
            print("Number range from {}-{}".format(b-4,b))
            
    user_number = int(input("Enter the number you Guess ")) #Get the value form user.
    count = 0 #Variable used to count the attempts.
    while(magic_number != user_number):
        count += 1
        if magic_number == user_number: #If the magic_number is equal to user input then it come out of loop.
            break

        if user_number == -1: # If the user input  is '-1' then related option will be shown.
            if magic_number >0 and magic_number <= 10:
                print("Number range from 1-10")
            if magic_number >=11 and magic_number <= 20:
                print("Number range from 11-20")
            if magic_number >=21 and magic_number <= 30:
                print("Number range from 21-30")
            if magic_number >=31 and magic_number <= 40:
                print("Number range from 31-40")
            if magic_number >=41 and magic_number <= 50:
                print("Number range from 41-50")
            if magic_number >=51 and magic_number <= 60:
                print("Number range from 51-60")
            if magic_number >=61 and magic_number <= 70:
                print("Number range from 61-70")
            if magic_number >=71 and magic_number <= 80:
                print("Number range from 71-80")
            if magic_number >=81 and magic_number <= 90:
                print("Number range from 81-90")
            if magic_number >=91 and magic_number <= 100:
                print("Number range from 91-100")
            print("\n For more help press'0'")


        if user_number == 0: #If the user input is equal to the '0' then the second option will be shown.
            if magic_number <= 10:
                anal(magic_number,1,10)
            elif magic_number > 10 and magic_number <=20:
                anal(magic_number,11,20)
            elif magic_number > 20 and magic_number <= 30:
                anal(magic_number,21,30)
            elif magic_number > 30 and magic_number <= 40:
                anal(magic_number,31,40)
            elif magic_number > 40 and magic_number <= 50:
                anal(magic_number,41,50)
            elif magic_number > 50 and magic_number <=60:
                anal(magic_number,51,60)
            elif magic_number > 60 and magic_number <=70:
                anal(magic_number,61,70)
            elif magic_number > 70 and magic_number <= 80:
                anal(magic_number,71,80)
            elif magic_number > 80 and magic_number <=90:
                anal(magic_number,81,90)
            else:
                anal(magic_number,91,100)
        user_number = int(input("Enter the number you Guess "))

    print("\nCongratulations!!!\n")

    print("No. of attempts",count)
    print("The Guessing number is ",magic_number)

play()
s = True
while(s): #the loop will be continuously run until the user stops.
    user_reply = input("\n Want to play again??? Yes/No  ")
    if  user_reply.lower() == "yes":
        play()
    elif user_reply.lower() == "no" :
        print("Thank You!!!")
        s = False

#Soul Corporation.
#For contact Gmail -> profsoul23@gmail.com
#the above code is the simple product from the Soul corporation and ltd.
