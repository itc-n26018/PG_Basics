numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:
    answer = input("数字を当ててみて or qで終了: ")
    
    if answer == "q":
        break
    
    try:
        answer = int(answer)
    except ValueError:
        print("もう一度入力して or qで終了。")
        continue
        
    if answer in numbers:
        print("大正解！")
    else:
        print("不正解！")
