I don't play word games, they don't interest me. However, novel solutions to problems do interest me. After the
wordle craze started I looked into how others were solving the problem. Most of the solutions were based on attempting
to solve the problem for almost every possible 5-letter english word. Since the game itself is constrained to only 2315 words, 
I decided to see if I could simply brute force a solution instead of taking a novel approach.

I started this effort because I was boasting on slack and I was called out for it. Per that conversation I had to solve the problem with the following constraints. 

1. It should only take a few hours (it didn't)
2. The average guess count should be 3.4 or better, matching a specific novel solution (still working on it, but unlikely)
3. I would not copy any algorithms found online or use any word scoring systems published by others (I didn't)

In the end it turned into an fun exercise. I was able to write a solver that brute forced a solution for 98% of the words in the answer list in about 6 hours. Through some bug fixes and optimizations I was able to get the percentage above 99% with an average number of guesses in the range of 3.55. 

This is the inital commit based on those numbers. The goal here is to share what I started with those I boasted to and then try to further optimize to solve for 100% of the words in the answer list with fewer guesses than right now. At some point I might clean up the readme and repository.