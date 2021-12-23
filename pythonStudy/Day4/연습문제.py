# 학생 10명의 점수를 입력받아서 리스트로 생성하고 총점과 평균을 계산하여 출력하시오

scores = []

sum = 0

for i in range(1,11):
    score = int(input(f'학생{i} 점수 입력 : '))
    scores.append(score)
    sum += score

avg = sum/10

print(f"총점 : {sum}")
print(f"평균 : {avg:.2f}")