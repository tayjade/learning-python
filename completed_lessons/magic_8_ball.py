#Using import random and the random python library, call the method random.randint(a,b) to write an 8 ball script
import random

question = input("Ask the magic 8 Ball a question.")

answer = random.randint(1,8)

print(answer)

if  answer == 1:
    print("For sure, my dude.")
elif answer == 2:
    print ("Who the fuck knows?")   
elif answer == 3:
    print ("Don't be a dumbass.")
elif answer == 4: 
    print ("One Hundred Percent.")  
elif answer == 5:
    print ("Hell yeah.")
elif answer == 6:
    print ("Ew, no.")
elif answer == 7:
    print ("Probs.")
elif answer == 8:
    print ("That's the stupidest question I've ever heard.")


