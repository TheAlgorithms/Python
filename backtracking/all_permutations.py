'''
	In this problem, we want to determine all possible permutations
	of the given sequence. We use backtracking to solve this problem.

	Time complexity: O(n! * n),
	where n denotes the length of the given sequence.
'''


def generate_all_permutations(sequence):
	create_state_space_tree(sequence, [], 0, [0 for i in range(len(sequence))])


def create_state_space_tree(sequence, current_sequence, index, index_used):
	'''
	Creates a state space tree to iterate through each branch using DFS.
	We know that each state has exactly len(sequence) - index children.
	It terminates when it reaches the end of the given sequence.
	'''

	if index == len(sequence):
		print(current_sequence)
		return

	for i in range(len(sequence)):
		if not index_used[i]:
			current_sequence.append(sequence[i])
			index_used[i] = True
			create_state_space_tree(sequence, current_sequence, index + 1, index_used)
			current_sequence.pop()
			index_used[i] = False


'''
remove the comment to take an input from the user 

print("Enter the elements")
sequence = list(map(int, input().split()))
'''

sequence = [3, 1, 2, 4]
generate_all_permutations(sequence)

sequence = ["A", "B", "C"]
generate_all_permutations(sequence)
