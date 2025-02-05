student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

high_score = 0
for i in student_scores:
    if i > high_score:
        high_score = i
print(high_score)
