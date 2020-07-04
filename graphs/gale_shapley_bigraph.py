def stable_matching(n: int, donor_pref: list, recipient_pref: list) -> list:
    '''
    Finds the stable match in any bipartite graph, i.e a pairing where no 2
    objects prefer each other over their partner.
    The function accepts the preferences of the donors and recipients (where
    both arecnamed from 0 to n-1) and returns a list where the index position
    corresponds to the donor and value at the index is the recipient (of the organ).
    E.g:
    n = 4
    donor_pref = [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]]
    recipient_pref = [[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]
    >>> print(stable_matching(n,donor_pref,recipient_pref))
    [1,2,3,0]
    To better understand the algorithm, see also:
    https://github.com/akashvshroff/Gale_Shapley_Stable_Matching (README).
    https://www.youtube.com/watch?v=Qcv1IqHWAzg&t=13s (Numberphile YouTube).
    '''
    undonated_donors = [i for i in range(n)]
    donor_record = [None for i in range(n)]  # who the donor has donated to
    recipient_record = [None for i in range(n)]  # donor received from
    num_donations = [0 for i in range(n)]
    while undonated_donors:
        donor = undonated_donors[0]
        donor_preference = donor_pref[donor]
        recipient = donor_preference[num_donations[donor]]
        num_donations[donor] += 1
        recipient_preference = recipient_pref[recipient]
        prev_donor = recipient_record[recipient]
        if prev_donor is not None:
            if recipient_preference.index(prev_donor) > recipient_preference.index(donor):
                recipient_record[recipient], donor_record[donor] = donor, recipient
                undonated_donors.append(prev_donor)
                undonated_donors.remove(donor)
        else:
            recipient_record[recipient], donor_record[donor] = donor, recipient
            undonated_donors.remove(donor)
    return donor_record
