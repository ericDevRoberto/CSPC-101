with open("life-expectancy.csv") as data:

    date = int(input("Enter the year of interest: "))

    overall_max_whole = 0.00
    country_max_whole = ""
    overall_min_whole = 999.00
    country_min_whole = ""
    sum_expectation_whole_time = 0.0

    overall_max_especific = 0.00
    overall_min_especific = 999.00
    country_max_especific = ""
    country_min_especific = ""
    overall_max_date = ""
    overall_min_date = ""
    sum_expectation = 0.0

    count = 0
    especific_count = 0

    for country in data:        

        if count != 0:
        
            country_data = country.split(",")
            country_name = country_data[0]
            country_date = int(country_data[2])
            country_expectation = float(country_data[3])
            sum_expectation_whole_time += country_expectation

            if country_expectation > overall_max_whole:
                overall_max_whole = country_expectation
                country_max_whole = country_name
                overall_max_date = country_date

            if country_expectation < overall_min_whole:
                overall_min_whole = country_expectation
                country_min_whole = country_name
                overall_min_date = country_date

            if country_date == date:
                
                especific_count += 1
                sum_expectation += country_expectation

                if country_expectation > overall_max_especific:
                    overall_max_especific = country_expectation
                    country_max_especific = country_name
                
                if country_expectation < overall_min_especific:
                    overall_min_especific = country_expectation
                    country_min_especific = country_name

        count += 1


    print()
    print(f"The overall max life expectancy is: {overall_max_whole} from {country_max_whole} in {overall_max_date}")
    print(f"The overall min life expectancy is: {overall_min_whole} from {country_min_whole} in {overall_min_date}")   
    print(f"The average life expectancy in all the World in whole time is {sum_expectation_whole_time / (count - 1):.2f} ")    
    print()
    print(f"For the year {date}:")
    print(f"The average life expectancy across all countries was {sum_expectation / especific_count:.2f}")
    print(f"The max life expectancy was in {country_max_especific} with {overall_max_especific}")
    print(f"The min life expectancy was in {country_min_especific} with {overall_min_especific}")         