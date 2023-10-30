# •	Ако не открие търсената книгата да се отпечата на два реда:
# o	"The book you search is not here!"
# o	"You checked {брой} books."
# •	Ако открие книгата си се отпечатва един ред:
# o	"You checked {брой} books and found it."

book_target = input()
found_book = ""
checked = 0

while found_book != book_target:
    found_book = input()
    if found_book == "No More Books":
        break
    elif found_book == book_target:
        break
    else:
        checked += 1


if found_book == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {checked} books.")
else:

    print(f"You checked {checked} books and found it.")
