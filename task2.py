def adjust_salaries():
    employees = []

    print("Enter employee datas (type 'done' when finished):")
    while True:
        name = input("Employee Name: ")
        if name == 'done':
            break

        salary_input = input("Salary: ")
        if not salary_input.replace('.', '').isdigit():
            print(f"Invalid salary {salary_input}")
            continue
        salary = float(salary_input)

        score_input = input("Performance Score [0,5]: ")
        if not score_input.replace('.', '').isdigit():
            print(f"Invalid score {score_input}")
            continue
        score = float(score_input)

        if score >= 4.5:
            print("Salary updated")
            new_salary = salary * 1.10
        elif 3.0 <= score < 4.5:
            new_salary = salary * 1.05
            print("Salary updated")
        else:
            new_salary = salary
            print("Salary did not change")

        employees.append({'Name': name, 'Old Salary': salary, 'New Salary': new_salary, 'Score': score})

    print("\nUpdated Salary Report:")
    for emp in employees:
        print(f"{emp['Name']}: Score = {emp['Score']}, Old Salary = ${emp['Old Salary']:.2f}, "
              f", New Salary = ${emp['New Salary']:.2f}")


adjust_salaries()
