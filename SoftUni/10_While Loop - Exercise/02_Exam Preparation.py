
bad_scores = int(input())

last_problem = ""
problem_name = ""

score = 0
problem_count = 0
average_score = 0
total_score = 0
bad_count = 0


while bad_count != bad_scores:
    problem_name = input()
    if problem_name == "Enough":
        break
    score = int(input())
    problem_count += 1
    total_score += score
    last_problem = problem_name
    if score <= 4:
        bad_count += 1
    if score <= 4 and bad_count >= bad_scores:
        break


average_score = total_score / problem_count

if problem_name == "Enough":
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problem_count}")
    print(f"Last problem: {last_problem}")
elif bad_count == bad_scores:
    print(f"You need a break, {bad_count} poor grades.")
