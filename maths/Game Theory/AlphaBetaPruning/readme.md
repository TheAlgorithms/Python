# Alpha-Beta Pruning

An optimization technique for the minimax algorithm that reduces the number of nodes evaluated by eliminating branches that won't affect the final decision (basically an upgrade of minimax algorithm)

As we have seen in the minimax search algorithm that the number of game states it has to examine are exponential in depth of the tree. Since we cannot eliminate the exponent, but we can cut it to half. Hence there is a technique by which without checking each node of the game tree we can compute the correct minimax decision, and this technique is called pruning. This involves two threshold parameter Alpha and beta for future expansion, so it is called alpha-beta pruning. It is also called as Alpha-Beta Algorithm. Alpha-beta pruning can be applied at any depth of a tree, and sometimes it not only prunes the tree leaves but also entire sub-tree. The two-parameter can be defined as:

1. Alpha: The best (highest-value) choice we have found so far at any point along the path of Maximizer. The initial value of alpha is -∞.
2. Beta: The best (lowest-value) choice we have found so far at any point along the path of Minimizer. The initial value of beta is +∞. The Alpha-beta pruning to a standard minimax algorithm returns the same move as the standard algorithm does, but it removes all the nodes which are not really affecting the final decision but making algorithm slow. Hence by pruning these nodes, it makes the algorithm fast.
## Acknowledgements

 - [Original Author](https://github.com/anmolchandelCO180309)
 - [Wiki](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

#### /// The alphabetapruning.py file has a Tic-Tac-Toe game implemented with a good explanation ///
