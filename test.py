from wordlegame import WordleGame
from wordlesolver import WordleSolver

def make_test_guess(game, word):
    test_words = ["abbot", "about", "chalk", "reedy"]

    print("Guessing " + word)    
    result = game.make_guess(word)
    print(game)

    if result == -1:
        print("Game over")
        return
    elif result == 5:
        print("Winner winner, chicken dinner!")
        return

    test_output = ""

    for word in test_words:
        test_output = test_output + word + ": " + str(game.get_data().possible_match(word)) + ", "

    print(test_output)

def create_game(word):
    print("Creating game with a solution of " + word)
    return WordleGame(word)

def get_answer_list():
    input_file = open("word_list.txt", "r")
    inputs = input_file.readlines()

    answers = []
    for item in inputs:
        answers.append(item.strip())

    return answers

def run_game_test(word, list):
    game = create_game(word)

    for guess in list:
        make_test_guess(game, guess)

def run_unmatched_test(word, list):
    game = create_game(word)

    for guess in list:
        make_test_guess(game, guess)

        for second in list:
            unmatched = game.get_data().unmatched_characters(second)
            print("Unmatched characters in " + second + ": " + str(unmatched))


def run_reduce_test(word, guess_list):
    game = create_game(word)
    solver = WordleSolver(guess_list[0], game, get_answer_list())

    for guess in guess_list:
        print("Guess " + guess)
        game.make_guess(guess)
        solver.reduce()
        print("Search set size: " + str(len(solver.get_search_list())))


def run_unmatched_test(word, guess_list):
    game = create_game(word)
    solver = WordleSolver(guess_list[0], game, get_answer_list())

    for guess in guess_list:
        game.make_guess(guess)
        solver.reduce()
        letters = solver.get_unmatched_list()
        print("Answer: " + word + ", Guess: " + guess + ", Unmatched: " + str(letters))

def run_next_guess_test(word, guess_list):
    game = create_game(word)
    solver = WordleSolver(guess_list[0], game, get_answer_list())

    for guess in guess_list:
        game.make_guess(guess)
        solver.reduce()
        solver.generate_next_guess()
        print("Answer: " + word + ", Guess: " + guess + ", Next: " + str(solver.get_guess()))

def run_solver_test(word, guess):
    game = create_game(word)
    solver = WordleSolver(guess, game, get_answer_list())

    result = game.make_guess(guess)

    while result != -1 and result != 5:
        last_guess = solver.get_guess()
        solver.reduce()
        print(str(solver.get_search_list()))
        solver.generate_next_guess()
        print("Answer: " + word + ", Guess: " + last_guess + ", Next: " + str(solver.get_guess()) + ", Size: " + str(len(solver.get_search_list())))
        print(str(game))
        result = game.make_guess(solver.get_guess())

    if result == -1:
        print("Game over!")
    else:
        print("Winner!")

guess_list = ["crate", "briar", "reedy", "scare", "teary", "until", "abbot"]
guess_word = "union"

#run_unmatched_test(guess_word, guess_list)
#run_game_test(guess_word, guess_list)

#print("\n")

#guess_list = ["crate", "teary", "reedy"]
#guess_word = "reedy"

#run_game_test(guess_word, guess_list)
#run_reduce_test(guess_word, guess_list)
#run_unmatched_test(guess_word, guess_list)
#run_next_guess_test(guess_word, guess_list)
run_solver_test(guess_word, "bluff")