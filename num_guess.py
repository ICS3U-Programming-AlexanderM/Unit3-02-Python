#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Dec, 7, 2021
# This program gets the user to guess a number
# between 0 and 9 and tell them if it is correct.
import constants


def main():
    # this function checks the user's number

    # input
    user_number = float(input("Enter your number: "))
    print("")

    # check number size
    if user_number >= 10:
        print("Number must be between 0 and 9.")

    elif user_number <= -1:
        print("Number must be between 0 and 9.")

    # process & output
    elif user_number == constants.CORRECT:
        print("Correct!")

    else:
        print("Wrong. :-(")


if __name__ == "__main__":
    main()
