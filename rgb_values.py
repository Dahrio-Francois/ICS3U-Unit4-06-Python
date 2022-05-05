#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: April 2022
# This program uses nested loops to print out RGB values


def main():
    # this starts the nested loop program

    counter1 = 0
    counter2 = 0
    counter3 = 0

    # process & output
    for counter1 in range(255):
        for counter2 in range(255):
            for counter3 in range(255):
                print("RGB values {0} {1} {2}".format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()
