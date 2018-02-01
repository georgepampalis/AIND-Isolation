"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

from importlib import reload

import isolation
import game_agent

#from game_agent import (MinimaxPlayer, AlphaBetaPlayer, custom_score,
#                        custom_score_2, custom_score_3)

from sample_players import (RandomPlayer, GreedyPlayer, open_move_score,
                            improved_score, center_score)
#from game_agent import (MinimaxPlayer, AlphaBetaPlayer, custom_score,
#                        custom_score_2, custom_score_3)


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer(search_depth=4) #"Player1"
        self.player2 = game_agent.AlphaBetaPlayer(search_depth=4) #GreedyPlayer() #"Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_example(self):
        # TODO: All methods must start with "test_"
        ## self.fail("Hello, World!")

        # place player 1 on the board at row 2, column 3, then place player 2 on
        # the board at row 0, column 5; display the resulting board state.  Note
        # that the .apply_move() method changes the calling object in-place.
        self.game.apply_move((2, 3))
        self.game.apply_move((0, 5))
        print(self.game.to_string())

        """
        # players take turns moving on the board, so player1 should be next to move
        assert(self.player1 == self.game.active_player)

        # get a list of the legal moves available to the active player
        print(self.game.get_legal_moves())

        # get a successor of the current state by making a copy of the board and
        # applying a move. Notice that this does NOT change the calling object
        # (unlike .apply_move()).
        self.new_game = self.game.forecast_move((1, 1))
        assert(self.new_game.to_string() != self.game.to_string())
        print("\nOld state:\n{}".format(self.game.to_string()))
        print("\nNew state:\n{}".format(self.new_game.to_string()))

        # play the remainder of the game automatically -- outcome can be "illegal
        # move", "timeout", or "forfeit"
        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))
        """

        print("\n ====================== \n")
        list_of_moves = [(move, game_agent.custom_score(self.game.forecast_move(move), self.game.active_player)) for move in self.game.get_legal_moves(self.game.active_player)]
        print(list_of_moves)
        print("\n ====================== \n")

        for move, score in list_of_moves:
            new_game = self.game.forecast_move(move)
            if score != len(new_game.get_legal_moves(self.game.active_player)):
                print(move, score, new_game.get_legal_moves())
                print(new_game.to_string())



if __name__ == '__main__':
    unittest.main()
