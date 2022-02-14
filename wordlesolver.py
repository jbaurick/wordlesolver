from operator import truediv
from turtle import pos
from wordlegame import WordleGame
from wordledata import WordleData

class WordleSolver:
    def __init__(self, guess, game, answers):
        self.guess = guess
        self.game = game
        self.answers = answers
        self.search_list = answers
        self.idx_hist = [dict() for i in range(5)]

    def reduce(self):
        reduce_list = []

        for word in self.search_list:
            if self.game.get_data().possible_match(word):
                reduce_list.append(word)
        
        self.search_list = reduce_list

        histogram_list = [dict() for i in range(len(word))]

        for word in self.search_list:
            for idx in range(len(word)):
                cur = word[idx]
                idx_dict = histogram_list[idx]

                if cur in idx_dict:
                    cnt = idx_dict[cur]
                    idx_dict[cur] = cnt + 1
                else:
                    idx_dict[cur] = 1
        
        self.idx_hist = histogram_list
    
    def get_search_list(self):
        return self.search_list

    def get_unmatched_list(self):
        letter_cnt = {}

        # generate a histogram of unmatched characters in the search list
        for word in self.search_list:
            unmatched = self.game.get_data().unmatched_characters(word)

            for letter in unmatched:
                if letter in letter_cnt:
                    cnt = letter_cnt[letter]
                    letter_cnt[letter] = cnt + 1
                else:
                    letter_cnt[letter] = 1

        sort_list = sorted(letter_cnt.items(), key=lambda x:x[1], reverse=True)
        ordered_list = [item[0] for item in sort_list]

        return ordered_list

    def get_guess(self):
        return self.guess

    def best_word(self, words):
        # Find the best word in the list of provided words. The best word
        # answers as many questions as possible. 
        max_value = 0
        max_word = words[0]

        for word in words:
            sum = 0

            for idx in range(len(word)):
                idx_dict = self.idx_hist[idx]

                if word[idx] in idx_dict:
                    sum += idx_dict[word[idx]]

            if sum > max_value:
                max_value = sum
                max_word = word

        return max_word

    def generate_next_guess(self):
        if len(self.search_list) == 1:
            self.guess = self.search_list[0] # We solved it!
        else:
            self.guess = None
            unmatched_letters = self.get_unmatched_list()
            unmatched_cnt = len(unmatched_letters)
            found = False

            if unmatched_cnt == 0: 
                if len(self.search_list) == 1:
                    self.guess = self.search_list[0]
                else:
                    self.guess = self.best_word(self.search_list)
                return

            start_idx = 5 if unmatched_cnt > 4 else unmatched_cnt
            possible_words = set()
            for cnt in range(start_idx, -1, -1):
                unmatched_set = set()

                for idx in range(0, unmatched_cnt):
                    unmatched_set.add(unmatched_letters[idx])

                    if idx + 1 >= cnt:
                        possible_guesses = self.search_list if cnt < 5 else self.answers
                        for guess in possible_guesses:
                            temp = unmatched_set.intersection(set(guess))
                            if len(temp) == cnt: 
                                if cnt == start_idx:
                                    found = True

                                possible_words.add(guess)
                                
                    if found:
                        break
                
                if found:
                    break

            final_list = list(possible_words)
            if len(final_list) == 1:
                self.guess = final_list[0]
            else: # This cannot be random, it needs to be compared to the search set to find the best chance of uncovering more information
                self.guess = self.best_word(final_list)
            
    def solve(self):
        cnt = 1
        result = self.game.make_guess(self.guess)

        while result != -1 and result != 5:
            self.reduce()
            self.generate_next_guess()
            result = self.game.make_guess(self.guess)
            cnt += 1

        if result == -1:
            return -1
        else:
            return cnt