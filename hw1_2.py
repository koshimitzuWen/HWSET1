while True:
    score = input("Please input your score:")
    new_score = int(score)
    if 90 <= new_score <= 100:
        print("A")
        break
    elif 80 <= new_score < 90:
        print("B")
        break
    elif 60 <= new_score < 80:
        print("C")
        break
    elif 0 <= new_score < 60:
        print("D")
        break
    else:
        print("Invalid score!")