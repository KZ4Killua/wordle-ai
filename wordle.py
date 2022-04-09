import random
import collections

WORD_LENGTH = 5
ALLOWED_GUESSES = 6

GREEN = 'g'
YELLOW = 'y'
GRAY = 'a'

VALID_GUESSES = "guesses.txt"
SOLUTIONS = "solutions.txt"


def load_words(path):
    """Takes a txt file and returns a set of words."""
    with open(path) as file:
        words = file.read().splitlines()
    return set(words)
        

def make_guess(words, possible_solutions):
    """Guesses a word from the set of words given the possible solutions
    we have left."""
    return random.choice(list(possible_solutions))


def filter_words(words, guess, pattern):
    """Filter out any words that do not match a pattern from an earlier guess."""
    for word in words.copy():
        if not matches_pattern(word, guess, pattern):
            words.remove(word)
    return words


def matches_pattern(word, guess, pattern):
    """Check whether a word matches a pattern gotten from an earlier guess."""
    return (get_pattern(guess, word) == pattern)


def get_pattern(guess, solution):
    """Returns a wordle pattern for a guess given a target solution."""
    pattern = ""
    for i in range(WORD_LENGTH):
        # Letter is at the right spot
        if guess[i] == solution[i]:
            pattern += GREEN
        # Letter is not in the word
        elif guess[i] not in solution:
            pattern += GRAY
        else:
            # Count the number of occurences of that letter so far
            n = collections.Counter(guess[:i])[guess[i]] + 1
            # If the solution has more than n of that letter, add a gray
            if n > collections.Counter(solution)[guess[i]]:
                pattern += GRAY
            else:
                pattern += YELLOW

    return pattern

        
def simulate():

    correct = 0
    total = 0
    guesses = 0

    words = load_words(VALID_GUESSES)

    for solution in load_words(SOLUTIONS):
        
        possible_solutions = words.copy()
        # print(f"Solution: {solution}")
        for i in range(ALLOWED_GUESSES):
            # Make a guess
            guess = make_guess(words, possible_solutions)
            # print(f"Guess: {guess}")
            # Compare and get a pattern
            pattern = get_pattern(guess, solution)
            # print(f"Pattern: {pattern}")
            # Check to see if we have won
            if pattern == "ggggg":
                correct += 1
                guesses += (i + 1)
                break
            # Remove all words that do not match the pattern
            possible_solutions = filter_words(possible_solutions, guess, pattern)
        # print()

        total += 1

    print(f"Success rate: {correct / total * 100}")
    print(f"Average guesses: {guesses / correct}")


def play():

    # Load all words into a hash table
    words = load_words(VALID_GUESSES)
    possible_solutions = words.copy()

    for i in range(ALLOWED_GUESSES):
        # Make a guess
        guess = make_guess(words, possible_solutions)
        print(f"Guess: {guess}")
        # Get a pattern
        pattern = input("pattern: ")
        # Check if we have won (pattern is all greens)
        if pattern == "ggggg":
            break
        # Remove all words that do not match the pattern
        possible_solutions = filter_words(possible_solutions, guess, pattern)   


def main():
    play()
    # simulate()


if __name__ == "__main__":
    main()