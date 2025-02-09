person_pace = [1, 2, 5, 10, 12, 16]
person_pace.sort()  # Sort the array for optimal pairing
people = len(person_pace)

# Base cases
if people == 1:
    print("Min Time to Cross is:", person_pace[0])
elif people == 2:
    print("Min Time to Cross is:", person_pace[1])
else:
    total_time = 0
    while people > 3:
        # Strategy 1: Send the two fastest first, then the fastest returns
        option1 = person_pace[1] + person_pace[0] + person_pace[-1] + person_pace[1]
        # Strategy 2: Send the two slowest, then the fastest returns
        option2 = person_pace[-1] + person_pace[0] + person_pace[-2] + person_pace[0]

        # Choose the minimum of the two strategies
        total_time += min(option1, option2)

        # Remove the two slowest people who have crossed
        person_pace = person_pace[:-2]

    # Handle the last 2 or 3 people
    if len(person_pace) == 3:
        total_time += person_pace[2] + person_pace[0] + person_pace[1]
    elif len(person_pace) == 2:
        total_time += person_pace[1]

    print("Min Time to Cross is:", total_time)
