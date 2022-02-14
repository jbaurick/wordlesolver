# Introduction
I don't play word games, they don't interest me. However, novel solutions to problems do interest me. After the
wordle craze started I looked into how others were solving the problem. Most of the solutions were based on attempting
to solve the problem for almost every possible 5-letter english word. Since the game itself is constrained to only 2315 words, 
I decided to see if I could simply brute force a solution instead of taking a novel approach.

I started this effort because I was boasting on slack and I was called out for it. Per that conversation I had to solve the problem with the following constraints. 

1. It should only take a few hours (it didn't)
2. The average guess count should be 3.4 or better, matching a specific novel solution (still working on it, but unlikely)
3. I would not copy any algorithms found online or use any word scoring systems published by others (I didn't)

In the end it turned into an fun exercise. I was able to write a solver that brute forced a solution for 98% of the words in the answer list in about 6 hours. Through some bug fixes and optimizations I was able to get the percentage above 99% with an average number of guesses in the range of 3.55. 

This is the inital commit based on those numbers. The goal here is to share what I started with those I boasted to and then try to further optimize to solve for 100% of the words in the answer list with fewer guesses than right now.

# Setup
None so far, unsing only standard python.

# Description
A brute force algorithm that attempts to solve wordle by reducing the possible solution set then attempting to pick the next guess from that set. The reduce method exludes words that cannot be a valid solution. The next guess method attempts to pick the next word which provides the most possible data to further improve the reduce. 

## main.py
The main entry point to run the solution. It loads the list of answers from word_list.txt, iterates over the list picking each word as the first guess and then testing the algorithm against it. The output is printed into a result.csv, the first column is the starting word, second column is solve rate, and third column is average number of guesses.

## test.py
Some basis tests used while writing the classes, primitative test based development. It can also be used to test modifications to the algorithm as it prints more data.

## wordlesolver.py
The solver. This file contains the reduce and next guess methods. 

## wordlegame.py
Simple implementation of the game. It only has one method which is make_guess, this method takes the guess and returns one of two results, either -1 for game over or the count of fully matched characters.

## wordledata.py
Contains the history of guesses made along with the data about green, yellow and grey letters. This class is used by both the game and solver.

# TODO
- [] Implement new next_guess method in wordlesolver which includes more possible guesses. The method is currently implemented to favor words based on the frequency of unidentified in the solution set. The method will stop when it finds all the words with the five most frequent indentified letters. This is not an ideal solution as it doesn't allow the guess picker to also consider the frequency per position. 
- [] Update the best_guess method in wordlesolver to not include green letters in the word score.
- [] Implement a better progress bar for main.py, it's really bad.
- [] Add command line arguments to main.py to allow it to solve for one word, not the complete set of words. 
- [] Cleanup wordledata, some of the functionality in that class does not belong there, it was just done for convience. 