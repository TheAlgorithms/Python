from typing import List


def stable_matching(donor_pref: List[int], recipient_pref: List[int]) -> List[int]:
    """
    Finds the stable match in any bipartite graph, i.e a pairing where no 2 objects
    prefer each other over their partner.  The function accepts the preferences of
    oegan donors and recipients (where both are assigned numbers from 0 to n-1) and
    returns a list where the index position corresponds to the donor and value at the
    index is the organ recipient.

    To better understand the algorithm, see also:
    https://github.com/akashvshroff/Gale_Shapley_Stable_Matching (README).
    https://www.youtube.com/watch?v=Qcv1IqHWAzg&t=13s (Numberphile YouTube).

    >>> donor_pref = [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]]
    >>> recipient_pref = [[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]
    >>> print(stable_matching(donor_pref, recipient_pref))
    [1, 2, 3, 0]
    """
    assert len(donor_pref) == len(recipient_pref)
    n = len(donor_pref)
    unmatched_donors = list(range(n))
    donor_record = [-1] * n  # who the donor has donated to
    rec_record = [-1] * n  # who the recipient has received from
    num_donations = [0] * n
    while unmatched_donors:
        donor = unmatched_donors[0]
        donor_preference = donor_pref[donor]
        recipient = donor_preference[num_donations[donor]]
        num_donations[donor] += 1
        rec_preference = recipient_pref[recipient]
        prev_donor = rec_record[recipient]
        if prev_donor != -1:
            if rec_preference.index(prev_donor) > rec_preference.index(donor):
                rec_record[recipient] = donor
                donor_record[donor] = recipient
                unmatched_donors.append(prev_donor)
                unmatched_donors.remove(donor)
        else:
            rec_record[recipient] = donor
            donor_record[donor] = recipient
            unmatched_donors.remove(donor)
    return donor_record
