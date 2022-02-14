from wordledata import WordleData

class WordleGame:

    def __init__(self, answer):
        self.guess_cnt = 0
        self.answer = answer
        self.data = WordleData()

    def make_guess(self, word):
        if self.guess_cnt == 6:
            return -1
            
        match_cnt = 0

        self.guess_cnt += 1

        match = [0, 0, 0, 0, 0]

        for idx in range(0, len(word)):
            #print("Testing " + word[idx] + " against " +  self.answer[idx])
            if word[idx] == self.answer[idx]:
                match[idx] = 2
                match_cnt += 1
            elif word[idx] in self.answer:
                match[idx] = 1
        
        #print(str(match_cnt) + " " + str(match))

        self.data.append(word, match)

        if match_cnt != 5 and self.guess_cnt == 6:
            return -1
        
        return match_cnt

    def get_data(self):
        return self.data

    def __str__(self):
        return "c: " + str(self.guess_cnt) + " " + str(self.data)