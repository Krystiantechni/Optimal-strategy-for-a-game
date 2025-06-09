# Optimal strategy for a game

This project implements an algorithm to solve the classic Optimal Strategy for a Game problem,

Two players take turns picking coins from either end of a row. The goal is to maximize the total value of the coins collected, assuming both players play optimally.

# The algorithm uses dynamic programming to find the best move for each subarray, storing the current player's max value, the opponent's value, and the optimal coin index (left or right).

The Game class includes:

- find_moves(pots): Builds the DP table with optimal decisions.

- print_sequence(pots, moves): Reconstructs the move sequence and prints results for both players.
