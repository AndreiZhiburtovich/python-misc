# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.
# Examples(Input1, Input2 --> Output):
# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"


def rps(p1, p2):
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if p1 not in beats and p2 not in beats:
        return "Error! Unacceptable arguments!"
    elif p1 == p2:
        return "Draw!"
    elif p1 in beats and beats[p1] == p2:
        return "Player 1 won!"
    elif p2 in beats and beats[p2] == p1:
        return "Player 2 won!"


def assert_equals(a, b):
    print(a == b)


assert_equals(rps('something', '!!!'), 'Error! Unacceptable arguments!')
assert_equals(rps('scissors', 'scissors'), 'Draw!')
assert_equals(rps('rock', 'scissors'), 'Player 1 won!')
assert_equals(rps('scissors', 'rock'), 'Player 2 won!')
assert_equals(rps('paper', 'rock'), 'Player 1 won!')
assert_equals(rps('rock', 'paper'), 'Player 2 won!')
assert_equals(rps('scissors', 'paper'), 'Player 1 won!')
assert_equals(rps('paper', 'scissors'), 'Player 2 won!')
