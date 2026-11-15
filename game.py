import time

location = 'Wasteland'
supplies = 0
game_running = True

time.sleep(2)
name = input("Enter your name: ")
print(f"Welcome {name}! You are stuck in a wasteland. Find 5 supplies and escape!")

while game_running:

    if location == 'Wasteland':
        print("\nYou see a crashed plane and a dark cave.")
        print("1. Go to the plane")
        print("2. Enter the cave")
        answer = input("Choose: ")

        if answer == '1':
            location = 'Plane'
        elif answer == '2':
            location = 'Cave'
        else:
            print("Invalid input!")

    elif location == 'Plane':
        print(f"\nYou have {supplies} supplies.")

        if supplies >= 5:
            print("You repaired the plane and escaped! Congratulations!")
            game_running = False
        else:
            print("You need 5 supplies to repair the plane.")
            location = 'Wasteland'

    elif location == 'Cave':
        print("\nYou find a GK question, a jumbled word and a crate.")
        print("1. GK Question")
        print("2. Jumbled Word")
        print("3. Leave cave")
        print("4. Open crate")
        answer = input("Choose: ")

        if answer == '1':
            location = 'GK Question'
        elif answer == '2':
            location = 'jumbled words'
        elif answer == '3':
            location = 'Wasteland'
        elif answer == '4':
            print("You found 3 supplies!")
            supplies += 3
        else:
            print("Invalid input!")

    elif location == 'GK Question':
        answer = input("\nHow many provinces are there in Nepal? ")

        if answer == '7':
            print("Correct! You got 1 supply.")
            supplies += 1
        else:
            print("Wrong! The answer is 7.")

        location = 'Cave'

    elif location == 'jumbled words':
        answer = input("\nUnscramble this word: O C I N ")

        if answer.lower() == 'coin':
            print("Correct! You got 1 supply.")
            supplies += 1
        else:
            print("Wrong! The answer is coin.")

        location = 'Cave'