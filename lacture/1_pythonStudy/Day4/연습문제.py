# 학생 n명의 점수를 입력받아서 리스트로 생성하고 총점과 평균을 계산하여 출력하시오

scores = []

stu_cnt = int(input("학생의 수 입력 : "))
sum = 0
hightscore = 0

for i in range(1,stu_cnt+1):
    score = int(input(f'학생{i} 점수 입력 : '))
    if score >= 80:
        hightscore += 1
    scores.append(score)
    sum += score

avg = sum/10

print(f"총점 : {sum}")
print(f"평균 : {avg:.2f}")

print(f"80점 이상인 학생의 수 : {hightscore}")