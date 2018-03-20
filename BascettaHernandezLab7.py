import os


def verify():
    filename = input("Please enter the file name here > ")
    while not os.path.exists( filename ):
        filename = input("Please enter a valid file name here > ")

    print("Thank you", filename , "is a valid file name")
    return filename

file_open = verify()


def maxiprofit(file_open):
    movies_file = open(file_open, "r")
    maxProfit = 0
    for line in movies_file:
        movieProf = line
        releaseDate, movieTitle, revenue, budget = movieProf.split(",")
        budget = float(budget)
        revenue = float(revenue)
        profit = revenue - budget
        if profit > maxProfit:
            maxProfit = profit
            titleMovie = movieTitle
    print("The movie with the most profit is", titleMovie, "with $",maxProfit, "in profit")
    return maxProfit
maxiprofit(file_open)


def main():
    print("This program is designed to inform you of the movie with the highest profit")
    








