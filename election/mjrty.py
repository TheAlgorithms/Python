"""

AKA: Boyer–Moore majority vote algorithm

Given a list of votes with a majority (n/2 + 1), declare the leader. 
As in, the most frequently occurring vote. It is possible to get the 
result in linear time O(n) AND constant space O(1).

"""


def find_leader(votes):
    # Assigning initial leader
    leader = votes[0]
    count = 1

    for i in range(1, len(votes)):

        if votes[i] == leader:
            # Current leader gets another vote
            count += 1
        else:
            # Someone else got a vote
            count -= 1

        if count == 0:
            # Assigning new leader
            leader = votes[i]
            count = 1

    return leader


if __name__ == "__main__":
    # Satisfies the majority condition -> correct answer.
    print(find_leader(['A', 'B', 'A', 'A', 'C']))   # A

    # Doesn't satisfy the majority condition -> wrong answer.
    print(find_leader(['A', 'B', 'A', 'B', 'C']))   # C
