#

n = input("please enter a number:")
n = int(n)

if n % 2 == 1:
    print("Weird")

elif n in range (2,5):
     print("not weird")

elif n in range (6,21):
    print("Weird")

elif n > 20:
    print("not weird")
    


