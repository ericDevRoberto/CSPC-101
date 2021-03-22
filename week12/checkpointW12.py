people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_name = ""
youngest_age = 99

for line in people:

    line_split = line.split()
    
    name = line_split[0]

    age = int(line_split[1])

    if age < youngest_age:

        youngest_name = name
        youngest_age = age


print(f"{youngest_name} is youngest and his age is {youngest_age}")