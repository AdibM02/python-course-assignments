import random
r = random.randint(1,100)
counter = 0
while True:
   guess = int(input("Your guess is?"))
   counter += 1
   if guess == r:
       print("You found the number in", counter, "moves.")
       break
   elif guess < r:
       print("Larger")
   else:
       print("Smaller")
print("After game")
