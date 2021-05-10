#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program tells you if you can date her grandchild.
#    with numbers inputted from the user


def main():
    # This function tells you if you can date her grandchild.

    # input
    first_string = input("Please enter your age: ")
    print("")

    # process/output
    try:
        first_numbers = int(first_string)

        if first_numbers >= 25 and first_numbers <= 40:
            print("You are accepted to date my grandchild.")
        elif first_numbers < 25:
            print("You are too young, come back when your older.")
        elif first_numbers > 40:
            print("You are too old.")
    except Exception:
        print("{} is not an number".format(first_string))
    finally:
        print("Thanks for trying")
    print("\nDone")


if __name__ == "__main__":
    main()
