def activitySelection(activities):

    result = []
    n=len(activities)
    activities.sort(key=lambda x: x[1])
    i = 0
    result.append(activities[i])


    for j in range(1,n):

        if activities[j][0] >= activities[i][0]:
            i = j
            result.append(activities[j])
    print("The selected activities are as follows")
    for activity in result:
        print(activity,end=" ")
    print()

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

activities = []
for i in range(len(start)):
    activities.append([start[i],finish[i]])

activitySelection(activities=activities)