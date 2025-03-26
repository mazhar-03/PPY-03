correct_password = "secure123"
max_attempts = 3
attempts = 0

username = input("Enter your username: ")
while attempts < max_attempts:
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print(f"Access granted for user {username}")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Wrong password! {remaining_attempts} attempts left.")
        else:
            print(f"Account locked for user {username}")
