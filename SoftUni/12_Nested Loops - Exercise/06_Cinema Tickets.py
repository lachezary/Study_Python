

movie_name = ""
total_places = 0
student = 0
standard = 0
kid = 0
ticket = ""
busy = 0
total_tickets = 0


while movie_name != "Finish":
    movie_name = input()
    total_places = int(input())
    while ticket != "End":
        free_spots = input()
        if ticket == "End":
            break
        elif ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1
        if (student + standard + kid) >= total_places:
            break
    movie_tickets = ((student + standard + kid) / total_places) * 100
    print(f"{movie_name} - {movie_tickets:.2f}% full.")


total_tickets += (student + standard + kid)
student = student / total_tickets * 100
standard = standard / total_tickets * 100
kid = kid / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student:.2f}% student tickets.")
print(f"{standard:.2f}% standard tickets.")
print(f"{kid:.2f}% kids tickets.")
