import time
time.sleep(2)
location = 'Wasteland'
supplies = 0
game_running = True
name = input("Enter your name: ")
time.sleep(1)
print(f"Welcome {name}. You wake up abandoned in a war-torn wasteland, with no memory of how you got here. Your goal is to survive and escape by repairing the old plane. You can gather supplies by exploring the Cave. Good luck!")
while game_running:
    if location == 'Wasteland':
        time.sleep(1)
        print("You find yourself in a desolate, smoke-covered wasteland. To your left, an old crashed plane with supplies of food scattered around it. To your right, a dark, mysterious cave.")
        print("")
        time.sleep(1)
        print("If you want to try to repair and board the plane, enter '1'. To enter the cave, enter '2'")
        print('')
        answer = input("1-2:  ")
        if answer == '1':
            location = 'Plane'
        elif answer == '2':
            location = 'Cave'
        else:
            time.sleep(1)
            print("Invalid input. Please enter '1' or '2'.")
            continue
    if location == 'Plane':
        time.sleep(2)
        print("You approach the old crashed plane. Its engine is damaged, and it needs 5 supplies worth of scrap and fuel to get it running again.")
        print('')
        time.sleep(1)
        print(f"You currently have {supplies} supplies.")
        if supplies >= 5:
            time.sleep(1)
            print("You use your supplies to patch up the engine. The old plane sputters to life, and you climb aboard, finally escaping the wasteland. Congratulations, you've escaped!")
            game_running = False
        else:
            print("You don't have enough supplies to repair the plane. You need 5 supplies.")
            location = 'Wasteland'
    elif location == 'Cave':
        time.sleep(1)
        print("You step into the dark cave and look around. there, to your left, you see a GK Question carved into the wall. To your right, you see a Jumbled word scratched into the stone.")
        print('')
        time.sleep(1)
        print("for the GK question, enter '1'. For the Jumbled word, enter '2'. to go back to the Wasteland, enter '3'. But you also see a small crate in the middle of the cave. You can open it to see if there are any supplies inside. To open the crate, enter '4'.")
        print('')
        answer = input("1-4:  ")

        if answer == '1':
            location = 'GK Question'
        elif answer == '2':
            location = 'jumbled words'
        elif answer == '3':
            location = 'Wasteland'
        elif answer == '4':
            time.sleep(1)
            print("You pry open the crate and find 3 supplies inside!")
            supplies += 3
            print(f"You now have {supplies} supplies.")
        else:
            print("Invalid input. Please enter '1', '2', '3', or '4'.")
            continue
    if location == 'GK Question':
        time.sleep(1)
        print("You approach the general knowledge question. It reads: 'How many provinces are there in Nepal?'")
        print('')
        answer = input("Your answer: ")
        if answer == '7':
            print("Correct! You have solved the question and earned 1 supply.")
            supplies += 1
            print(f"You now have {supplies} supplies.")
            location = 'Cave'
        else:
            print("Incorrect. The correct answer was 7. You return to the cave.")
            location = 'Cave'
    elif location == 'jumbled words':
        time.sleep(1)
        print("You approach the Jumbled word. It reads: 'Unscramble the letters: 'O C I N '. What is the word?'")
        print('')
        answer = input("Your answer: ")
        if answer.lower() == 'coin':
            print("Correct! You have solved the Jumbled word and earned 1 supply.")
            supplies += 1
            print(f"You now have {supplies} supplies.")
            location = 'Cave'
        else:
            print("Incorrect. The correct answer was 'coin'. You return to the cave.")
            location = 'Cave'
    elif location == 'Wasteland':
        time.sleep(1)
        print("You are back in the Wasteland. To your left, the old crashed plane with its scattered supplies. To your right, the dark cave.")
        print("If you want to try to repair and board the plane, enter '1'. To enter the cave, enter '2'")
        print('')
        answer = input("1-2:  ")
        if answer == '1':
            location = 'Plane'
        elif answer == '2':
            location = 'Cave'
        else:
            print("Invalid input. Please enter '1' or '2'.")
            continue