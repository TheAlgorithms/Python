def stable_matching(n: int, donor_pref: list, recipient_pref: list) -> list:
    '''
    Finds the stable match in any bipartite graph, i.e a pairing where no 2
    objects prefer each other over their partner.
    The function accepts the preferences of the donors and recipients (where
    both are assigned numbers from 0 to n-1) and returns a list where the index
    position corresponds to the donor and value at the index is the organ
    recipient.
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
    unmatched_donors = [i for i in range(n)]
    donor_record = [None for i in range(n)]  # who the donor has donated to
    rec_record = [None for i in range(n)]  # donor received from
    num_donations = [0 for i in range(n)]
    while unmatched_donors:
        donor = unmatched_donors[0]
        donor_preference = donor_pref[donor]
        recipient = donor_preference[num_donations[donor]]
        num_donations[donor] += 1
        rec_preference = recipient_pref[recipient]
        prev_donor = rec_record[recipient]
        if prev_donor is not None:
            if rec_preference.index(prev_donor) > rec_preference.index(donor):
                rec_record[recipient], donor_record[donor] = donor, recipient
                unmatched_donors.append(prev_donor)
                unmatched_donors.remove(donor)
        else:
            rec_record[recipient], donor_record[donor] = donor, recipient
            unmatched_donors.remove(donor)
    return donor_record
