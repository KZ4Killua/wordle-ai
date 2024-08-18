# wordle-ai
A game playing agent for playing Wordle

The AI can be started by running wordle.py.
When started, the AI will suggest a guess eg.

`Guess: crane`

`pattern: `

It is the job of the user to test that guess and
tell the AI what pattern of colours that guess gives.

For example, say I try the word "crane" and get the following colour pattern:
⬜🟨🟩🟨⬜

I will then enter the following:

`pattern: aygya`

ie 'g' for GREEN, 'a' for GRAY, and 'y' for YELLOW

The AI also works in hard mode and will in fact always use all the information gotten from 
a guess to make the next guesses.
The AI has a success rate of 93.08% and, when successful, takes an average of 4.27 guesses
to reach a solution.
