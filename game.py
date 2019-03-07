from player import Player
class Game:
    def __init__(self, p1, p2):
        self.player_one = p1
        self.player_two = p2
        self.frames = 10
        self.currentFrame = 0

    def play_game(self):
        num_frames = 0
        while(num_frames < 9):
            self.player_one.play_frame(num_frames)
            self.player_two.play_frame(num_frames)
            num_frames = num_frames + 1
        self.player_one.frame_ten()
        self.player_two.frame_ten()
        print(self.who_won(self.player_one,self.player_two))

    def who_won(self,p1, p2):
        if(p1.score > p2.score):
            return(p1.name + " is the winner")
        elif(p2.score > p1.score):
            return(p2.name + " is the winner")
        else:
            return("You really managed to tie in fake bowling?")

def main():
    p1_name = input("Who is the name of Player One? ")
    p2_name = input("Who is the name of Player Two? ")
    p1 = Player(p1_name)
    p2 = Player(p2_name)
    game = Game(p1,p2)
    game.play_game()

#main()
