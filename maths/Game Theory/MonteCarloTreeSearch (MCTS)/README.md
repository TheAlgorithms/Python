
# Monte Carlo Tree Search (MCTS)

A heuristic search algorithm used for decision-making processes, particularly in games like Go.

The focus of MCTS is on the analysis of the most promising moves, expanding the search tree based on random sampling of the search space. The application of Monte Carlo tree search in games is based on many playouts, also called roll-outs. In each playout, the game is played out to the very end by selecting moves at random. The final game result of each playout is then used to weight the nodes in the game tree so that better nodes are more likely to be chosen in future playouts.

#### In the monte_carlo_tree_search.py file there is a minimal implementation of Monte Carlo tree search (MCTS) in Python 3

#### In the tictactoe.py file tere is an example implementation of the abstract Node class for use in MCTS


## Acknowledgements

 - [Original Author](https://gist.github.com/qpwo/c538c6f73727e254fdc7fab81024f6e1)
 - [Wiki](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)
