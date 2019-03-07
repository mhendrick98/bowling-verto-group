from game import Game
from player import Player
import unittest


class TestBowlingGame(unittest.TestCase):
    def test_setUp(self):
        self.game = Game(Player("Test 1"), Player("Test 2"))
        assert self.game is not None
        assert self.game.player_one.name == "Test 1"
        assert self.game.player_two.name == "Test 2"

    def test_strike(self):
        self.player = Player("Test")
        self.player.got_strike()
        assert self.player.score == 10
        assert self.player.bonus == 2

    def test_spare(self):
        self.player = Player("Test")
        self.player.got_spare()
        assert self.player.score == 10
        assert self.player.bonus == 1

    def test_first_roll(self):
        self.player = Player("Test")
        results = self.player.roll(10, 1)
        assert results[0] > -1
        assert results[0] <= 10
        if(self.player.score == 10):
            assert results[1] == True

    def test_second_roll(self):
        self.player = Player("Test")
        results = self.player.roll(10, 2)
        assert results[0] > -1
        assert results[0] <= 10
        if(self.player.score == 10):
            assert results[1] == True

    def test_bonus_from_spare_or_strike(self):
        self.player = Player("Test")
        self.player.all_frames = [5,8]
        self.player.bonus = 1
        self.player.bonus_from_spare_or_strike()
        assert self.player.bonus == 0
        assert self.player.score == 8
        self.player.score = 0
        self.player.bonus = 2
        self.player.bonus_from_spare_or_strike()
        assert self.player.bonus == 0
        assert self.player.score == 13

    def test_finish_frame(self):
        self.player = Player("Test")
        self.player.finish_frame()
        assert self.player.all_frames == [0]

    def test_who_won(self):
        self.game = Game(Player("Test 1"), Player("Test 2"))
        self.game.player_one.score = 5
        self.game.player_two.score = 9
        assert (self.game.player_two.name + " is the winner") == self.game.who_won(self.game.player_one, self.game.player_two)
        self.game.player_one.score = 10
        self.game.player_two.score = 9
        assert (self.game.player_one.name + " is the winner") == self.game.who_won(self.game.player_one, self.game.player_two)
        self.game.player_one.score = 10
        self.game.player_two.score = 10
        assert ("You really managed to tie in fake bowling?") == self.game.who_won(self.game.player_one, self.game.player_two)



if __name__ == '__main__':
    unittest.main()
