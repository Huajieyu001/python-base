scoreList = []

while True:
    score = input("please input your score: ")
    if score == 'q':
        break
    scoreList.append(int(score))

avgScore = sum(scoreList) / len(scoreList)

print("the average score is", avgScore)