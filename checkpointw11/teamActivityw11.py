with open("hr_system.txt") as employers:

    for employer in employers:

        employer_data = employer.split()

        employer_name = employer_data[0]

        employer_id = employer_data[1]

        employer_title = employer_data[2]

        employer_salary = float(employer_data[3]) / 24

        if employer_title == "Engineer":

            employer_salary += 1000

        print(f"{employer_name} (ID: {employer_id}), {employer_title} - {employer_salary:.2f}")