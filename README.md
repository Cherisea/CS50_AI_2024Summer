# Harvard CS50 AI

Inspired by Jeff Hawkins's resounding book on neuroscience and future of AI, I have decided to devote myself to this booming field in pursuit of an answer that has haunted me since I watched Terminator 1 as a kid -- will robots, equipped with a steel exterior that could withstand far more severa conditions than human bodies and powered by micro-processors that's more potent and precise than human brains, ever advance to such level of intelligence that they decide to eliminate humans so that they could be their own masters?

This course marks my first step towards that goal.

## Week 0 Search

**Prerequisites**

- Search algorithms can be categorized based on different criterias. For the purpose of this conversation, we will organize them according to the kind of data structures they can operate on.
- Conventional search algorithms, like selection sort, merge sort, quick sort etc. is suitable for none-hierachical data, while breadth-first search (BFS), depth-first search, greedy best-first search are designed to run on hierachical data.
- Greedy best-first search and A\* search are also called informed search because they use problem-solving strategy or domain-specific knowledge to guide its search process, delivering a better performance than uninformed search.
- Informed search employ a heuristic function to aid its decision when confronted with branching situation.
- Greedy best-first search differs from A\* search in that it only considers estimated cost from current state to end state, which means the solution it finds may not always be optimal.
- While greedy best-first search makes its decision solely on the approximated cost from current node to end node, dijkstra's algorithm focuses instead of minimizing the cost incurred so far from starting node.
- A\* search combines the best of both worlds from greedy best-first search and dijkstra's search, ensuring an optimal solution while keeping the cost low.

**Assignment: Tic Tac Toe** [Project Directory](/week0/)

- We're asked to implement a minimax search algorithm in a Tic Tac Toe game where a player is pitted against the computer on a 3x3 board.
- The computer is playing optimally by assuming the most likely move that the opponent would take at each turn out of all possible moves.
- It could be challenging to code function minimax as it involves calling another function that in turn invokes the caller until a terminal state is reached.
- Driver file resides in `runner.py`, while all functions are inside `tictactoe.py`. Play the game by issuing `python runner.py` from the command line.
- Check the demo ![tic tac toe demo](/demos/tictactoe.gif)

**Extended Challenge**

- Integrate alpah-beta pruning with the minimax algorithm for better performance.
- Code a game that's more complex than tic tac toe in a 3x3 board.

## Week 1 Knowledge

**Prerequisites**

- While the term **knowledge** conveys different meanings in different domains, it can be defined as a fact or information internally represented in a machine that should be accepted as truth.
- The primary task related to knowledge we want our computer to perform involves drawing reasonable conclusions from a set of known facts encoded in computer language through the use of algorithms (or in human language's term, logic).
- To that end, the course introduces a formal system of propositional logic that deals with the relationship and interaction between different elements.
- The first algorithm is model checking, a somewhat brute force strategy that enumerates all possible combinations of propositions involved and cross checks known facts with the combinations to establish a truth.
- Another algorithm is called resolution, a process by which a set of known facts are reduced as much as possible by applying inference rules in an effort to achieve contradiction, thus drawing new conclusions from an entailment.
- Another inference logic we can utilize to represent knowledge is known as first order logic, a structure of predicates, constants, functions, variables and sentences.
- Compared to propositional logic, first order logic is better at dealing with individual entities and expressing generalization, such as quantifiers.

**Assignment 1: Knights** [Project Directory](/week1/knights)

- Based on a logical puzzle game Knights and Knaves, our task is to implement an AI model(a priliminary one) that, given a knowledge base(a set of information expressed with propositional logic), is capable of determining the identity of each character involved.
- The building blocks of this task, logical connectives and representation of knowledge are already implemented for us. All we are asked to do is specify a list of known facts grouped together by the defined connectives.
- It's worth our efforts examining the classes provided to us in `logic.py` as it helps us understand how elements necessary in building propositional logic are represented in code. The `Sentence` class acts as a parent class that all other classes inherit from, providing definition of the core funtionality that each derived class must implement. This is simiarly to an abstract class in Java.
- Each child class is required to implement at least three methods -- `evaluate`, which determines whether an expression is true or false; `formula`, which returns a string representation of a logical expression designed to provide meaningful information to humans; `symbols`, enumerating labels included in an expression.
- Function `model_check` is of particular interest as it's the processing engine that takes what's known to the program, ie knowledge base, to deduce the truthfulness of a query. This is the part that bestows "intelligence" to the entire script. If peering under the hood, however, we would discover this is actually nothing mysterious about it. This function draws a conclusion by exhasuting every possible combination of the value of symbols involved, evaluting a query to true if it's true in every possible models and false otherwise.
- This obversation raises interesting questions: what does intelligence really mean? Will computer ever achieve true intelligence if all it does is follow pre-defined process dictated by humans?
