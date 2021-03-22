  #Hello Admin 5-8
print("Hello Admin Task")
users = {"admin", "Kyle", "Jake", "Ronnie", "Ben"}
for user in users:
  if user == "admin":
   print("Good afternoon Admin, Would you like to see a status report?")
  else:
  	print("Good Afternoon " + user + ", Thanks for logging in!")
  #5-9 No Users
print("--------------------")
print("User List Empty Task")
print("Proof that the list has values: ")
for user in users:
	print(user)
print("Now to clear the list...")
users.clear()
if not users:
	print("We need users!")
#5-10 Checking Usernames
current_users = {"Matrix", "Neo", "Morpheus", "Mr.Smith", "GrayFox"}
new_users = {"MATRIX", "GrayFox", "Snake", "Liquid", "PsychoMantis"}
current_users_lower = [user.lower() for user in current_users]

for new_users in new_users:
	if new_users.lower() in current_users_lower:
		print(f"Sorry {new_users}, that username is taken!")
	else:
		print(f"{new_users} is still available!")\
#5-11 Ordinal Numbers
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

	

