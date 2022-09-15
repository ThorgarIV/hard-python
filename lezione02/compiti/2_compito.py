users_number = 5
users = []
current_user = 1

while len(users) < users_number:
    nickname = input(f"Insert nickname for user #{current_user}: ")
    age = input(f"Insert age for user #{current_user}: ")
    gender = input(f"Insert gender for user #{current_user}: ")

    user = { "nickname" : nickname, "age" : age, "gender" : gender}

    if user not in users:
        print(f"Added user #{current_user}")
        current_user += 1
        users.append(user)
    else:
        print("User already defined! Exiting program...")
        break

genders_in_users = {}
total_ages_in_users = 0
total_names_length_in_users = 0

age_min = 10000000000
age_max = 0

for user in users:

    if user["gender"] == "M":
        if "M" in genders_in_users.keys():
            genders_in_users["M"] += 1
        else:
            genders_in_users["M"] = 1
    else:
        if "F" in genders_in_users.keys():
            genders_in_users["F"] += 1
        else:
            genders_in_users["F"] = 1

    user_age = int(user['age'])

    if user_age < age_min:
        age_min = user_age

    if user_age > age_max:
        age_max = user_age

    total_ages_in_users += user_age

    total_names_length_in_users += int(len(user["nickname"]))

print(f"Males: {genders_in_users['M']}")
print(f"Females: {genders_in_users['F']}")
print(f"Min age: {age_min}")
print(f"Max age: {age_max}")
print(f"Average age: {total_ages_in_users / len(users)} ")
print(f"Average nickname length: {total_names_length_in_users / len(users)}")