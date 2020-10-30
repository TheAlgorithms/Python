import sys
import copy

def dpChangeMoney(total, units, stored):

    if (total == 0): # terminating conditions
        return [{}]
    elif (total < 0 ) : 
        return []
    else:
        length_n = len(units) # length of the money the user enters (the denominations)
        
        if total in stored.keys() : # if the amount(total) in keys
            if length_n in stored[total] :
                return stored[total][length_n] 
            else :
                stored[total][length_n] = []
                for i in range(0,length_n):
                    sols = copy.deepcopy(dpChangeMoney(total-units[i],  # we are using copy.deepcopy
                                                       units[i:length_n], stored)) 
                    for sol in sols: # updating if units in sol
                        if (units[i] in sol):
                            sol[units[i]] = sol[units[i]] + 1 # increment by 1 if in sol
                        else:
                            sol[units[i]] = 1 # assign a new one / it wasnt there before
                        stored[total][length_n].append(sol) # save the solutions at stored!
                return stored[total][length_n] # return our primary dictionary
        else: # if total not in stored.keys()
            stored[total],stored[total][length_n] = {} , []
            for i in range(0,length_n):
                sols = copy.deepcopy(dpChangeMoney(total-units[i], 
                                                   units[i:length_n], stored)) # again we are using copy.deepcopy
                for sol in sols: 
                    if (units[i] in sol):
                        sol[units[i]] = sol[units[i]] + 1 
                    else:
                        sol[units[i]] = 1
                    stored[total][length_n].append(sol) 
            return stored[total][length_n] 

dollars = int(sys.argv[1])
bills = [int(x) for x in sys.argv[2:len(sys.argv)]]
ways = dpChangeMoney(dollars, bills, {})
print("There are " + str(len(ways)) + " possible ways to make "+str(dollars))
for way in ways:
    print(sorted(way.items()))
