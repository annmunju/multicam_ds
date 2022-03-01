# 각 학생별 점수 리스트 생성

kim = [90, 85, 70]
choi = [88, 92, 72]
kang = [100, 95, 100]
lee = [90, 60, 70]

students = [kim, choi, kang, lee]
print(students)

# 학생별 총점과 평균 점수 출력
sum = 0
sum_ls = []
avg_ls = []

for i in range(len(students)):
    for j in range(len(students[i])):
        sum += students[i][j]
    sum_ls.append(sum)
    avg_ls.append(round(sum/3,2))
    sum = 0

print(f"학생별 총점 : {sum_ls}")
print(f"학생별 평균 : {avg_ls}")

# 과목별 총점과 평균 점수 출력

sum = 0
sum_ls = []
avg_ls = []

for i in range(len(students[0])):
    for j in range(len(students)):
        sum += students[j][i]
    sum_ls.append(sum)
    avg_ls.append(round(sum/4,2))
    sum = 0

print(f"과목별 총점 : {sum_ls}")
print(f"과목별 평균 : {avg_ls}")
