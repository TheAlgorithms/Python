
# Minimax Algorithm

A decision-making algorithm for two-player games to minimize the maximum possible loss (This is a simple, recursive, implementation of the MiniMax algorithm in Python)

MiniMax is used in decision, game theory, statistics and philosophy. It can be implemented on a two player's game given full information of the states like the one offered by games like Tic Tac Toe. That means MM cannot be used in games that feature randomness like dices. The reason is that it has to be fully aware of all possible moves/states during gameplay before it makes its mind on the best move to play.

The following implementation is made for the cube/sticks game: User sets an initial number of cubes available on a table. Both players (the user & the PC implementing MM) can pick up a number of cubes off the table in groups of 1, 2 or K. K is also set by the user. The player who picks up the last remaining cubes from the table on a single take wins the game.

The MiniMax algorithm is being implemented for the PC player and it always assume that the opponent (user) is also playing optimum. MM is fully aware of the remaining cubes and its valid moves at all states. So technically it will recursively expand the whole game tree and given the fact that the amount of possible moves are three (1,2,K), all tree nodes will end up with 3 leaves, one for each option.

Game over is the case where there are no available cubes on the table or in the case of a negative amount of cubes. The reason for the negative scenario is due to the fact that MM will expand the whole tree without checking if all three options are allowed during a state. In a better implementation we could take care of that scenario as we also did on the user side. No matter what, if MM’s move lead to negative cubes he will lose the game.

Evaluation starts on the leaves of the tree. Both players alternate during game play so each layer of the tree marks the current player (MAX or MIN). That way the evaluation function can set a higher/positive value if player MAX wins and a lower/negative value if he loses (remember evaluation happens from the MiniMax’s perspective so he will be the MAX player). When all leaves get their evaluation and thanks to the recursive implementation of the algorithm, their values climb up on each layer till the root of the tree also gets evaluated. That way MAX player will try to lead the root to get the highest possible value, assuming that MIN player (user) will try its best to lead to the lowest value possible. When the root gets its value, MAX player (who will be the first one to play) knows what move would lead to victory or at least lead to a less painful loss.

So the goal of MiniMax is to minimize the possible loss for a worst case scenario, from the algorithm's perspective.



/// There is an example code implemented with deatailed explanation in the minimax.py file ///




## Acknowledgements

 - [Original Author](https://github.com/savvasio)
 - [Wiki](https://en.wikipedia.org/wiki/Minimax)
 - [Video Explanation](https://www.youtube.com/watch?v=l-hh51ncgDI)

