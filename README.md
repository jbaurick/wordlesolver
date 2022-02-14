I don't play word games, they don't interest me. However, novel solutions to problems do interest me. After the
wordle craze started I looked into how others were solving the problem. Most of the solutions were based on attempting
to solve the problem for almost every possible 5-letter english word. Since the game itself is constrained to only 2315 words, 
I decided to see if I could simply brute force a solution instead of taking a novel approach.

This effort started for the following reasons.

1. I was boasting on slack that I could solve Wordle for 2315 words in a few hours (I didn't)
2. That my solution would match some of the more novel approaches in terms of average guesses, 3.4 to be exact (still working on it, but unlikely)

In the end it turned into an fun exercise. I was able to write a solver that brute forced a solution for 98% of the words in the answer list in about 6 hours. Through some bug fixes and optimizations I was able to get the percentage above 99% with an average number of guesses in the range of 3.55. 

This is the inital commit based on those numbers. The goal here is to share what I started with those I boasted to and then try to further optimize to solve for 100% of the words in the answer list with fewer guesses than right now. At some point I might clean up the readme and repository.