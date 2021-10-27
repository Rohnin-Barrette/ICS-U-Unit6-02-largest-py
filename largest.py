#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: oct 2021
# this function generates 10 random numbers and finds the largest one
import random


def largest_finder(number_list):
    # This function finds the largest number of an array

    largest = number_list[0]

    for loop_counter in range(0, len(number_list)):
        if number_list[loop_counter] > largest:
            largest = number_list[loop_counter]
        else:
            largest = largest
    return largest


def main():
    # This function generates 10 random numbers

    number_list = []

    for loop_counter in range(0, 10):
        random_number = random.randint(0, 100)
        number_list.append(random_number)
        print("The random number is: {}".format(random_number))

    largest_number = largest_finder(number_list)

    print("\n\nThe largest number is {}".format(largest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
