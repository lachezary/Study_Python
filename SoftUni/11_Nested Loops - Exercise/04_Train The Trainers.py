presentation_avg_score = 0
total_avg_score = 0
input_text = ""
exams = 0
all_scores = 0
exam_scores = 0
jury_ppl = int(input())

while input_text != "Finish":
    presentation_name = input()
    if presentation_name == "Finish":
        break
    for i in range(jury_ppl):
        scores = float(input())
        exam_scores += scores
    exams += 1
    presentation_avg_score = exam_scores / jury_ppl
    all_scores += presentation_avg_score
    print(f"{presentation_name} - {presentation_avg_score:.2f}.")
    exam_scores = 0


total_avg_score = all_scores / exams

print(f"Student's final assessment is {total_avg_score:.2f}.")
