from wordlegame import WordleGame
from wordlesolver import WordleSolver

def get_answer_list():
    input_file = open("word_list.txt", "r")
    inputs = input_file.readlines()

    answers = []
    for item in inputs:
        answers.append(item.strip())

    return answers

answers = get_answer_list()
answer_cnt = len(answers)

output = open('results.csv', 'w')

for guess in answers:
    idx = 0
    total_guesses = 0
    total_solved = 0

    for answer in answers:
        game = WordleGame(answer)

        solver = WordleSolver(guess, game, answers)

        try:
            result = solver.solve()
        except:
            print("Failed with " + guess + " " + answer)

        if result != -1:
            total_guesses += result
            total_solved += 1

    avg_guesses = total_guesses / answer_cnt
    solve_perc = total_solved / answer_cnt
    print("{}, {:.2f}, {:.2f}".format(guess, solve_perc * 100, avg_guesses), file=output)
    output.flush()

    if idx > 0:
        print("{:.2f}% complete".format((idx / answer_cnt) * 100))

    idx += 1

output.close()