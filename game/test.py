import unittest
from game import Game

class TestGierka(unittest.TestCase):

    def test_single_element(self):
        game = Game()
        pots = [10]
        moves = game.find_moves(pots)
        total, first_seq, second_seq = game.print_sequence(pots, moves)
        self.assertEqual(total, 10)
        self.assertEqual(first_seq, "10")
        self.assertEqual(second_seq, "")

    def test_equal_values(self):
        game = Game()
        pots = [5, 5, 5, 5]
        moves = game.find_moves(pots)
        total, first_seq, second_seq = game.print_sequence(pots, moves)
        self.assertEqual(total, 10)
        self.assertEqual(len(first_seq.split(", ")), 2)
        self.assertEqual(len(second_seq.split(", ")), 2)

if __name__ == "__main__":
    unittest.main()
