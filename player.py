import random
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.bonus = 0
        self.all_frames = []

    def got_strike(self):
        self.bonus = 2
        self.score = self.score + 10
        print(self.name, "got a strike, nice!")

    def got_spare(self):
        self.bonus = 1
        self.score = self.score + 10
        print(self.name, "got a spare, nice!")

    def roll(self, total_pins, roll_num):
        done_flag = False
        player_pins = random.randint(0,10)
        total_pins = total_pins - player_pins
        if(total_pins <= 0 and roll_num == 1): #strike
            self.got_strike()
            done_flag = True
        elif(total_pins <= 0 and roll_num == 2): #spare
            self.got_spare()
            done_flag = True
        else:
            self.score = self.score + (10 - total_pins)
            print(self.name, "knocked down", 10 - total_pins, "nice!")
        if(roll_num == 2 and total_pins > 0):
            self.bonus -= 1
        return (total_pins, done_flag)

    def bonus_from_spare_or_strike(self):
        if(self.bonus == 1):
            self.score = self.score + self.all_frames[-1]
            self.bonus -= 1
        elif(self.bonus >= 2):
            self.score = self.score + self.all_frames[-1] + self.all_frames[-2]
            self.bonus -= 2

    def finish_frame(self):
        self.all_frames.append(self.score)
        print(self.name, "has a score currently of", self.score)

    def frame_ten(self):
        total_pins = 10
        one_more = False
        total_pins,end_round = self.roll(total_pins, 1)
        if(end_round):
            one_more = True
        if(one_more):
            total_pins,end_round = self.roll(total_pins, 1)
        else:
            total_pins,end_round = self.roll(total_pins, 2)
            if(end_round):
                total_pins,end_round = self.roll(total_pins, 1)

        self.bonus_from_spare_or_strike()
        print(self.name, "has a final score of", self.score)


    def play_frame(self, frame_num):
        total_pins = 10
        for i in range(1, 3):
            total_pins,end_round = self.roll(total_pins, i)
            if(end_round):
                self.finish_frame()
                return
        self.bonus_from_spare_or_strike()
        self.all_frames.append(self.score)
        print(self.name, "has a score currently of", self.score)
