# Programmers: Bascetta / Hernandez
# Date: 3/21/18
# Lab 7

# Import os for path exists

import os

# create a function to verify the user inputs a valid filename


def verify():
    filename = input("Please enter the file name here > ")
    while not os.path.exists( filename ):
        filename = input("Please enter a valid file name here > ")

    print("Thank you", filename , "is a valid file name")
    return filename
# call the function


file_open = verify()

# create a function for the max profit


def maxprofit(file_open):
    movies_file = open(file_open, "r")
    maxiprofit = 0
    for line in movies_file:
        movieProf = line
        releaseDate, movieTitle, revenue, budget = movieProf.split(",")
        budget = float(budget)
        revenue = float(revenue)
        profit = revenue - budget
        if profit > maxiprofit:
            maxiprofit = profit
            titleMovie = movieTitle
    print("The movie with the most profit is", titleMovie, "with $",maxiprofit, "in profit")
    return maxprofit


mostprofit(file_open)

# create a function to process the file to read and write to


def process(file_open, data_file):
    movies_file = open(file_open, "r")
    data_file = open("data.txt", "w")
    print("The revenue for the movie is", file=data_file)


# create a function to verify the output
def verify_output():

    valid_output = input("Input a filename to output to > ")
    while not os.path.exists(valid_output):
        valid_output = input("Please enter a valid filename > ")

    return valid_output









def main():
    print("This program is designed to inform you of the movie with the highest profit")
    file_open = verify()

    mostprofit(file_open)

    output_file = process()

    output(file_open, output_file)

    








