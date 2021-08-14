# Maximum-weight-in-a-Tree
Team Members: Adeyemi Adedayo Tolulope, Hilal Saim

This project was initially written in Java.

PROBLEM DESCRIPTION 
The project is about finding a group of shareholders in a joint-stock company with the biggest sum of shares in which none of the shareholders spy each other. 
In this company each shareholder except one spy on exactly one other shareholder. 
The project group is to design and implement a dynamic programming algorithm that will solve the problem listed above. 
 
SOLUTION DESCRIPTION (PSEUDOCODE) 
Below is an example showing the way the result of our algorithm should look like. 
There are 5 shareholders in the company.  
  
SHAREHOLDER 	SHARES  	SPIES 
A 	20 	B 
B 	15 	A 
C 	10 	D 
D 	15 	C 
E 	30 	  
  
In the table above, each shareholder spies exactly one other shareholder. To get the right result, we must choose the highest sum of shareholders not spying on each other. 
To enable us to get the highest sum of shareholders we will be using Graph algorithm.  
For the example in the table above, the image below is what the solution using a directed graph looks like. 
 
 
In the directed graph above there are 3 connected components 
i)              AB      ii) CD         iii) E 
And 3 cycles: ABA, CDC, EE 
In the directed graph, the shareholders spying each other are connected. Then from each connected component of the graph the highest shareholder will be chosen. Then the sum of each highest shareholder in a component will give us the sum of the highest shareholders not spying each other. 
Now going by our solution of choosing the highest shareholder in each cycle we will choose A in the first components, then D in the second components and E in the third. 
Therefore, the sum will be 20+15+30 which gives the highest sum of shareholders not spying each other at 65. 
By dividing the problem into sub-problems, the solution falls under the dynamic programming structure.
We will use DFSUtil method to find components. 
Then a Solve method will be defined to calculate each component separately. 
Each sub problem has an isCycle value. 
Now, if we are using a tree algorithm, to enable us to get the independent set of maximum weight in a tree we will do a depth first search through the tree. Our search will compute two values for every subtree in the graph:
X(i): which is the size of the maximum independent set in the subtree
rooted at i in which node i must be included in the set.
Y(i): which is the size of the maximum independent set in the subtree
rooted at i in which node i must not be included in the set.
To compute X(i) which involves including the weight of node i to the total factor, we will not be able to include the children of i to the solution. We will however be able to include the weight of its subtree’s root at its grandchildren, making it an independent set. To make this program optimal for all subtrees, we have to include all we can get into the solution. Therefore, the maximum total number of shares we will get will include the weight of the node i and the sum of all the optimal solutions for the overall grandchildren w of i. On the other hand, to compute Y(i), if we do not add the root i to the solution of the problem, then we can compute the solution independently for all its children. That is solving it optimally for its children and we can take the sum of all the vertices which are independent subtrees, resulting in the union of all the vertices.
The maximum independent set in the whole tree will be the max between X(i) and Y(i)

Now, if the problem is a cycle, we will solve it by choosing any vertex of that cycle which is denoted by (v) and then computing two solutions: 
i) A solution with the condition that v is included in the solution 
ii) A solution with condition that v is excluded from the solution 
Then we will choose the optimal solution of the two. The graph becomes a forest after we decide to either include or exclude v, it can now be solved using the tree algorithm above for each tree in the forest. 
