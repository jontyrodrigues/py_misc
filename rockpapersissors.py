# a game of rock paper scissors, against the computer

import random
import sys
import os
import time

def clear():
    if os.name == "nt":
        os.system("cls")

arr = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

def main():
    clear()
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.")
    print("The rules are as follows:")
    for i in range(1, len(arr) + 1):
        print(str(i) + ". " + arr[i - 1] + " beats " + arr[i % len(arr)] + " and loses to " + arr[(i + 1) % len(arr)] + ".")
    print("Please enter your choice below.")
    print("Choices are: ")
    for i in range(1, len(arr) + 1):
        print(str(i) + ". " + arr[i - 1])
    print("Enter 'q' to quit.")
    choice = input("Enter your choice: ")
    while choice != "q":
        if int(choice) > len(arr):
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")
            continue
        else:
            choice = arr[int(choice) - 1]
        print("You chose: " + choice)
        print("The computer is choosing...")
        time.sleep(0.5)
        computer_choice = random.randint(1, len(arr))
        computer_choice = arr[computer_choice - 1]
        print("The computer chose: " + computer_choice)
        if choice == computer_choice:
            print("It's a tie!")
        # get the size of the array
        elif arr.index(choice) == len(arr) - 1 and arr.index(computer_choice) == 0:
            print("You lose!")
        elif arr.index(choice) == 0 and arr.index(computer_choice) == len(arr) - 1:
            print("You win!")
        elif arr.index(choice) - arr.index(computer_choice) == 1:
            print("You win!")
        elif arr.index(choice) - arr.index(computer_choice) == -1:
            print("You lose!")
        else:
            print("It's a tie!")
        choice = input("Enter your choice: ")
    print("Thanks for playing!")
    sys.exit()

if __name__ == "__main__":
    main()
