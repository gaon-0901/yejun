# random 모듈을 r로 import
import random as r

# 승리와 패배 횟수를 기록하는 변수 초기화
win = 0
lose = 0

# 게임 결과를 판단하는 함수
def judge(a, input_lose):
    # 만약 잘못된 입력으로 패배한 경우 "패배" 반환
    if input_lose == 1:
        return "패배"

    # 승리와 패배를 체크하기 위해 전역변수를 사용
    global win, lose
    for x in range(len(a) - 2):
        # 리스트 'a'에서 연속된 세 개의 1인지 확인하여 승리를 체크
        if a[x] == 1 and a[x + 1] == 1 and a[x + 2] == 1:
            win = 1
        # 리스트 'a'에서 연속된 세 개의 2인지 확인하여 패배를 체크
        if a[x] == 2 and a[x + 1] == 2 and a[x + 2] == 2:
            lose = 1

    # 'win'과 'lose' 플래그를 기준으로 최종 게임 결과 반환
    if win == 1 and lose == 0:
        return "승리"  # 승리
    elif win == 0 and lose == 1:
        return "패배"  # 패배
    else:
        return "무승부"  # 무승부

# 리스트 'a'의 요소 개수 입력 받기
n = int(input())

# 빈 리스트 'a'와 패배 여부를 저장하는 변수 초기화
a = []
input_lose = 0

# 리스트 'a'를 0으로 초기화
for x in range(n):
    a.append(0)

# 플레이어와 컴퓨터가 번갈아가며 차례를 진행하는 게임 루프 시작
for x in range(n):
    if x % 2 == 0:
        # 플레이어의 차례
        p = int(input("사용자 : "))  # 플레이어 입력 받기
        if p < 0 or p >= n:
            input_lose = 1  # 잘못된 입력이면 패배 플래그 설정
            break
        if a[p] != 0:
            input_lose = 1  # 이미 선택된 위치면 패배 플래그 설정
            break
        a[p] = 1  # 플레이어가 선택한 위치에 1로 표시
    else:
        # 컴퓨터의 차례
        while True:
            p = r.randint(0, n - 1)  # 랜덤으로 컴퓨터가 위치 선택
            if a[p] == 0:
                break  # 선택한 위치가 비어있으면 루프 종료
        print("컴퓨터 :", p)  # 컴퓨터가 선택한 위치 출력
        a[p] = 2  # 컴퓨터가 선택한 위치에 2로 표시
    print(a)  # 각 턴이 끝난 후 리스트 'a'의 현재 상태 출력

# judge 함수를 호출하여 최종 게임 결과를 판단하고 출력
print(judge(a, input_lose))
