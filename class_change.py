import random as r

class Game:
    def __init__(self, n):
        self.n = n
        self.a = [0] * n
        self.input_lose = 0

    def judge(self):
        if self.input_lose == 1:
            return "패배"

        win = 0
        lose = 0
        for x in range(len(self.a) - 2):
            if self.a[x] == 1 and self.a[x + 1] == 1 and self.a[x + 2] == 1:
                win = 1
            if self.a[x] == 2 and self.a[x + 1] == 2 and self.a[x + 2] == 2:
                lose = 1

        if win == 1 and lose == 0:
            return "승리"
        elif win == 0 and lose == 1:
            return "패배"
        else:
            return "무승부"

    def player_turn(self):
        p = int(input("사용자 : "))
        if p < 0 or p >= self.n:
            self.input_lose = 1
        elif self.a[p] != 0:
            self.input_lose = 1
        else:
            self.a[p] = 1

    def computer_turn(self):
        while True:
            p = r.randint(0, self.n - 1)
            if self.a[p] == 0:
                break
        print("컴퓨터 :", p)
        self.a[p] = 2

    def play(self):
        for x in range(self.n):
            if x % 2 == 0:
                self.player_turn()
            else:
                self.computer_turn()
            print(self.a)
            if self.input_lose == 1:
                break

        result = self.judge()
        print(result)

# 리스트 'a'의 요소 개수 입력 받기
n = int(input("숫자 범위를 입력하세요: "))
game = Game(n)
game.play()
