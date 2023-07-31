import random as r

class Game:
    def __init__(self, n):
        # 게임 초기화: 인스턴스 변수 설정
        self.n = n  # 숫자 범위를 저장하는 변수
        self.a = [0] * n  # 게임 보드를 나타내는 리스트, 0으로 초기화된 길이 n의 리스트
        self.input_lose = 0  # 잘못된 입력으로 인한 패배 여부를 저장하는 변수

    def judge(self):
        # 게임 결과 판단 함수: 승리, 패배, 무승부를 반환
        if self.input_lose == 1:
            return "패배"

        win = 0  # 승리를 체크하기 위한 플래그
        lose = 0  # 패배를 체크하기 위한 플래그
        for x in range(len(self.a) - 2):
            # 리스트 'a'에서 연속된 세 개의 1인지 확인하여 승리 플래그 설정
            if self.a[x] == 1 and self.a[x + 1] == 1 and self.a[x + 2] == 1:
                win = 1
            # 리스트 'a'에서 연속된 세 개의 2인지 확인하여 패배 플래그 설정
            if self.a[x] == 2 and self.a[x + 1] == 2 and self.a[x + 2] == 2:
                lose = 1

        # 'win'과 'lose' 플래그를 기준으로 최종 게임 결과 반환
        if win == 1 and lose == 0:
            return "승리"  # 승리
        elif win == 0 and lose == 1:
            return "패배"  # 패배
        else:
            return "무승부"  # 무승부

    def player_turn(self):
        # 플레이어의 차례: 사용자로부터 입력을 받아 게임 보드를 업데이트
        p = int(input("사용자 : "))  # 사용자로부터 위치 입력 받기
        if p < 0 or p >= self.n:
            self.input_lose = 1  # 잘못된 입력이면 패배 플래그 설정
        elif self.a[p] != 0:
            self.input_lose = 1  # 이미 선택된 위치면 패배 플래그 설정
        else:
            self.a[p] = 1  # 플레이어가 선택한 위치에 1로 표시

    def computer_turn(self):
        # 컴퓨터의 차례: 랜덤하게 위치를 선택하여 게임 보드를 업데이트
        while True:
            p = r.randint(0, self.n - 1)  # 랜덤으로 컴퓨터가 위치 선택
            if self.a[p] == 0:
                break  # 선택한 위치가 비어있으면 루프 종료
        print("컴퓨터 :", p)  # 컴퓨터가 선택한 위치 출력
        self.a[p] = 2  # 컴퓨터가 선택한 위치에 2로 표시

    def play(self):
        # 게임 진행 함수: 플레이어와 컴퓨터가 번갈아가며 게임을 진행하고 결과 출력
        for x in range(self.n):
            if x % 2 == 0:
                self.player_turn()  # 플레이어의 차례
            else:
                self.computer_turn()  # 컴퓨터의 차례
            print(self.a)  # 각 턴이 끝난 후 게임 보드의 현재 상태 출력
            if self.input_lose == 1:
                break  # 잘못된 입력으로 인해 게임 종료

        result = self.judge()  # 최종 게임 결과 판단
        print(result)  # 결과 출력

# 리스트 'a'의 요소 개수 입력 받기
n = int(input("숫자 범위를 입력하세요: "))
game = Game(n)  # 게임 인스턴스 생성
game.play()  # 게임 시작
