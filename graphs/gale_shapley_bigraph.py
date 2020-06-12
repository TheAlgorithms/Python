def stable_matching(n: int, men_preferences: list, women_preferences: list) -> list:
    '''
    Finds the stable match in any bipartite graph, i.e a pairing where no 2 objects prefer each other over their partner.
    Here marriage is used to make the variable names easier and so the algorithm can be intuitively understood.
    The function accepts the preferences of the men and women (where both are named from 0 to n-1) and returns a list where index
    position corresponds to the man and value at the index is the woman he is marrying.
    E.g:
    n = 4
    men_preferences = [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]]
    women_preferences = [[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]
    >>>print(stable_matching(n,men_preferences,women_preferences))
    [1,2,3,0]
    P.S: Marriages are heterosexual since it is a bipartite graph where there must be 2 distinct sets of objects to be matched - i.e
    patients and organ donors.
    To better understand the algorithm, see also:
    https://github.com/akashvshroff/Gale_Shapley_Stable_Matching (Detailed README).
    https://www.youtube.com/watch?v=Qcv1IqHWAzg&t=13s (Numberphile YouTube Video).
    '''
    unmarried_men = [i for i in range(n)]
    man_spouse = [None for i in range(n)]
    woman_spouse = [None for i in range(n)]
    num_proposals = [0 for i in range(n)]
    while unmarried_men:
        man = unmarried_men[0]
        his_preferences = men_preferences[man]
        woman = his_preferences[num_proposals[man]]
        num_proposals[man] += 1
        her_preferences = women_preferences[woman]
        husb = woman_spouse[woman]
        if husb != None:
            if her_preferences.index(husb) > her_preferences.index(man):
                woman_spouse[woman], man_spouse[man] = man, woman
                unmarried_men.append(husb)
                unmarried_men.remove(man)
        else:
            woman_spouse[woman], man_spouse[man] = man, woman
            unmarried_men.remove(man)
    return man_spouse
