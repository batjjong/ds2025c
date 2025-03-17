import random

ran = random.randint(1, 100)
win = False

for i in range(7):
    print(f"{7-i}번 남았습니다")
    n = int(input("정수 입력:"))
    if n < ran:
        print("그 수보다 큽니다")
    elif n > ran:
        print("그 수보다 작습니다")
    elif n == ran:
        print("정답입니다")
        win = True
        break
if win:
    print("win")
else:
    print(f"lose answer is {ran}")
