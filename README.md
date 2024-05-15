# Harvard CS50 AI
Inspired by Jeff Hawkins's resounding book on neuroscience and future of AI, I have decided to devote myself to this booming field in pursuit of an answer that has haunted me since I watched Terminator 1 as a kid -- will robots, equipped with a steel exterior that could withstand far more severa conditions than human bodies and powered by micro-processors that's more potent and precise than human brains, ever advance to such level of intelligence that they decide to eliminate humans so that they could be their own masters?

This course marks my first step towards that goal.

## Week 0 Search
**Prerequisites**
- Search algorithms can be categorized based on different criterias. For the purpose of this conversation, we will organize them according to the kind of data structures they can operate on.
- Conventional search algorithms, like selection sort, merge sort, quick sort etc. is suitable for none-hierachical data, while breadth-first search (BFS), depth-first search, greedy best-first search are designed to run on hierachical data.
- Greedy best-first search and A* search are also called informed search because they use problem-solving strategy or domain-specific knowledge to guide its search process, delivering a better  performance than uninformed search.
- Informed search employ a heuristic function to aid its decision when confronted with branching situation.
- Greedy best-first search differs from A* search in that it only considers estimated cost from current state to end state, which means the solution it finds may not always be optimal.
- While greedy best-first search makes its decision solely on the approximated cost from current node to end node, dijkstra's algorithm focuses instead of minimizing the cost incurred so far from starting node. 
- A* search combines the best of both worlds from greedy best-first search and dijkstra's search, ensuring an optimal solution while keeping the cost low.


**Assignment: Tic Tac Toe** [Project Directory](/tictactoe/)
- We're asked to implement a minimax search algorithm in a Tic Tac Toe game where a player is pitted against the computer on a 3x3 board.
- The computer is playing optimally by assuming the most likely move that the opponent would take at each turn out of all possible moves. 
- It could be challenging to code function minimax as it involves calling another function that in turn invokes the caller until a terminal state is reached.
- Driver file resides in `runner.py`, while all functions are inside `tictactoe.py`. Play the game by issuing `python runner.py` from the command line.
- Check the demo ![tic tac toe demo](/demos/tictactoe.gif)
