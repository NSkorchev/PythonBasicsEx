# Read user input
n_count = int(input())
salary = int(input())
# Logic

for i in range(0, n_count):
    website = (input())

    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

else:
    print(f"{salary}")


# Output
