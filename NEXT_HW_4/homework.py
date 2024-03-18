#session4 과제
number = int(input("숫자 게임의 최댓값을 입력해주세요:"))
print("1부터", number, "까지의 숫자를 하나 생각하세요.")
input("준비가 되었다면 Enter를 누르세요.")

min= 1
max = number
cycle_count = 1

while True:
      guess = (min + max) // 2
      print("당신이 생각한 숫자는", guess, "입니까?")

      user= input("제가 맞췄다면 '맞음', 제가 제시한 숫자보다 크다면 '큼', 작다면 '작음'을 입력해주세요: ")

      if user == "맞음":
            print(cycle_count, "번 만에 맞췄다")
            break
      elif user == "큼":
            min = guess + 1
            cycle_count += 1
      elif user == "작음":
            max = guess - 1
            cycle_count += 1
      else:
            print("오류")
