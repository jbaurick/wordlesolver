import re

class WordleData:

    def __init__(self):
        self.regex_cnt = 0
        self.regex = [None, None, None, None, None]

        self.regex_exclude_cnt = 0
        self.regex_exclude = [None, None, None, None, None]
        self.guess_set = set()
        self.found_set = set()
        self.exclude_set = set()

    def add_exclusion(self, idx, char):
        self.regex_exclude_cnt += 1
        
        if self.regex_exclude[idx] == None:
            self.regex_exclude[idx] = char
        else:
            self.regex_exclude[idx] = self.regex_exclude[idx] + char
    
    def append(self, guess, match):
        self.guess_set.add(guess)

        for idx in range(0, len(match)):
            if match[idx] == 2:
                self.found_set.add(guess[idx])
                self.regex[idx] = guess[idx]
                self.regex_cnt += 1
            elif match[idx] == 1:
                self.found_set.add(guess[idx])
                self.add_exclusion(idx, guess[idx])                    
            else:
                self.exclude_set.add(guess[idx])

    def check_regex(self, word):
        regex = ""

        for idx in range(len(word)):
            if self.regex[idx] != None:
                regex = regex + self.regex[idx]
            elif self.regex_exclude[idx] != None:
                regex = regex + "[^" + ''.join(self.regex_exclude[idx]) + "]"
            else:
                regex = regex + "[a-z]"

        return re.fullmatch(regex, word) != None

    def intersect_word_count(self, test_set, word):
        return len(test_set.intersection(set(word)))

    def check_found(self, word):
        return len(self.found_set) == self.intersect_word_count(self.found_set, word)

    def check_exclude(self, word):
        return self.intersect_word_count(self.exclude_set, word) == 0

    def possible_match(self, word):
        if word in self.guess_set:
            return False

        regex = self.check_regex(word)
        found = self.check_found(word)
        exclude = self.check_exclude(word)

        return regex and found and exclude
    
    def unmatched_characters(self, word):
        return set(word).difference(self.found_set.union(self.exclude_set))

    def __repr__(self):
        return "WordleData"

    def __str__(self):
        return "g: " + str(self.guess_set) + ", r: " + str(self.regex) + ", f: " + str(self.found_set) + ", e: " + str(self.exclude_set)