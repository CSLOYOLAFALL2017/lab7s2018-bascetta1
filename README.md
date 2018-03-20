#CS151 Lab 7
50 points	 
Due: 03/20/2018
	
#Problem
You've been hired to study the movie industry and how much money various movies have made over the past few decades. To complete your study you have been provided with a file with over 4000 movies, their release dates, their budget, and their box office gross (how much money they made in theaters). You need to create a program to answer the specific questions of your client.

#Purpose
This lab gives you practice with: 
* Following problem-solving techniques
* Checking user input
* Doing file I/O
* Interacting with Strings.

#Details
You need to design, write, and test a program that calculates information about movies. You need to determine and output the following: 
* the movie with the highest profit (output to the console)
* info on all movies (saved to a new file)

Your program MUST ask for the following information from the user: the name of the input file, and the name of the output file.

###Error Checking
Unfortunately, you don't really trust your user to follow the directions in your program, so you need to protect your program
from bad user input.  You must do this in two ways: use a loop to continue asking for a file name until you are given one that
exists for the input file, and use try/except to ensure that your program does not crash if the file disappears while your program runs.
You do NOT need to check the name of the output file, because Python creates your output file for you if it doesn't exist.

###Output
For the file output, your program must output to a new file the release date, name, and profit of each movie. This information should be comma delimited (i.e. have a comma separating each value). There should be one movie per line. You can use sep="" in your print statement to control what is output between each value.

The console (screen) output should contain the name and profit for the movie with the highest profit.
Note that output to the console means using standard output that we've been using all semester.

###Input Files
The input file looks like this: Release date, movie title, budget, box office gross.
Each line of the file is a single movie with information in this order. You can open the file and look at it.

Note that profit is NOT one of the values in your file! You must calculate this for each movie.

Your repository has 2 input files: test.csv and movies.csv.
The test file is a small file that is easy to test on. 
The movies file is the one you actually want to run your program on in the end. 
Beware: Your computer may want to open these files in Excel, but that will lead you astray. Only view in PyCharm or in Notepad (or a similar text editor).

#Design
You should use iterative development for this problem. For example, to calculate the highest profit, I suggest using the following smaller problems to help you devise a solution: Reading from the file line by line, calculating the profit for each movie (line by line), updating the max while reading line by line.

#Steps:
1. Make sure you understand the problem
2. Make sure your PyCharm project is using Python 3! (File -> Settings -> Project -> Interpreter)
3. Write your algorithm in algorithm.txt using iterative development as described above. Get Professor Franceschi's approval. Use functions as shown in the starting algorithm.txt file.
4. Create a new python file and write your code to match your algorithm. Writing each piece and then testing it before moving on is a great way to do iterative development. To succeed on this lab it is crucial that you get each piece working before moving on to the next.
5. Test your code by determining what the answers should be from the test.csv file. Then ensure that it runs on movies.csv.
6. Write comments in your code to make it clear what it is doing. Don't forget function comments.
7. Include an updated version of the intro comments. YOU NOW need to put something in the "other files" section (there was one in the lab 1 skeleton file), as your program can't work without an input file of a specific format.

#Submit:
* To GitHub and Moodle
  * Your completed algorithm (algorithm.txt)
  * Your .py file 
* On paper in class
  * Your .py file 
  * A short individual reflection about what you did in lab, what it was like working with your partner, and what you had the most trouble with. (1 per person)
