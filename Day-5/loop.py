# fruits=["Apple","peach","peer"]
# for fruit in fruits:
#     print(fruit)

student_score=[120,234,234,454,565,453]
# total_exam_score=sum(student_score)
# print(total_exam_score)

max=0
for score in student_score:
    if(score>max):
        max=score

print(max)