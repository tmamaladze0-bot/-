correct_password = "python2024"
for number in range(1,4):
    password = input("შეიყვანეთ პაროლი:")
    if password == "":
        continue
    if password == correct_password:
        print("წვდომა დაშვებულია")
        break
    else:
        remaining = 3 - number
        print("დარჩენილი მცდელობა", remaining)
else:
    print("ანგარიში დაბლოკილია")