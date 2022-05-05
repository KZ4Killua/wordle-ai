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
        

def make_guess(possible_solutions, counts):
    """Guesses a word from the set of words given the possible solutions
    we have left."""
    # Pick the word that uses up the most letters
    return max(possible_solutions, key=lambda word: sum(counts[c] for c in set(word)))

def filter_words(words, guess, pattern, counts):
    """Filter out any words that do not match a pattern from an earlier guess."""
    for word in words.copy():
        if not matches_pattern(word, guess, pattern):
            # Remove the word from the set
            words.remove(word)
            # Update counts
            counts -= collections.Counter(set(word))
    return words, counts

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
            # Look ahead and count the number of greens of that letter 
            n = 0
            for j in range(i + 1, WORD_LENGTH):
                if (solution[j] == guess[i]) and (solution[j] == guess[j]):
                    n += 1
            # Count the number of occurences of that letter so far
            n += guess[:i + 1].count(guess[i])
            # If the solution has less than n of that letter, add a gray
            if n > solution.count(guess[i]):
                pattern += GRAY
            else:
                pattern += YELLOW

    return pattern

        
def simulate():

    correct = 0
    total = 0
    guesses = 0

    words = load_words(VALID_GUESSES)
    # Count how many words have each letter
    letter_counts = sum((collections.Counter(set(word)) for word in words), start=collections.Counter())

    for solution in load_words(SOLUTIONS):
        
        possible_solutions = words.copy()
        counts = letter_counts.copy()

        for i in range(ALLOWED_GUESSES):
            # Make a guess
            guess = make_guess(possible_solutions, counts)
            # Get a pattern
            pattern = get_pattern(guess, solution)
            # Check to see if we have won
            if pattern == "ggggg":
                correct += 1
                guesses += (i + 1)
                break
            # Remove all words that do not match the pattern
            possible_solutions, counts = filter_words(possible_solutions, guess, pattern, counts)

        total += 1

    print(f"Success rate: {correct / total * 100}")
    print(f"Average guesses: {guesses / correct}")


def play():

    # Load all words
    words = load_words(VALID_GUESSES)
    # At first, every word is a possible solution
    possible_solutions = words.copy()
    # Count how many words have each letter
    counts = sum((collections.Counter(set(word)) for word in possible_solutions), start=collections.Counter())

    for i in range(ALLOWED_GUESSES):
        # Make a guess
        guess = make_guess(possible_solutions, counts)
        print(f"Guess: {guess}")
        # Get a pattern
        pattern = input("pattern: ")
        # Check if we have won (pattern is all greens)
        if pattern == "ggggg":
            break
        # Remove all words that do not match the pattern
        possible_solutions, counts = filter_words(possible_solutions, guess, pattern, counts)


def main():
    play()
    # simulate()


if __name__ == "__main__":
    main()