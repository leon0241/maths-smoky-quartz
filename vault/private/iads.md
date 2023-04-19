D question i
For any $v\in V$, if $v$ is a leaf node, the maximal independent set that includes $v$ is $v$. Conversely, the maximal independent set that doesn't include $v$ is the empty set, or a set with a weight of $0$.
In other words, for a leaf node $v$ with weight $w(v)$,
$$k_{v,0}=0,\qquad k_{v,1}=w(v)$$
For any non-leaf node $v$, the value $k_{v,1}$ of $v$ can be defined as the weight of $v$ added to the maximal independent set of the child nodes. Since you cannot have two adjacent nodes, the only valid value is $k_{v,0}$ of the child nodes of $v$.
In other words, for a node $v$ with a set of child nodes $X$ and weight $w(v)$,
$$k_{v,1} = w(v) +\sum k_{x,0},\quad \forall x\in X$$
Similarly, $k_{v,0}$ of $v$ can be defined as the sum of the maximumal independent set of the child nodes. However, there is nothing preventing you from having two adjacent non-IS nodes in a valid independent set. Therefore, the value to take from a child node can either be $k_{v,1}$ of the node or $k_{v,0}$, depending on which is larger. 
In other words, for a node $v$ with a set of child nodes $X$,
$$k_{v,0} = \sum \max{(k_{x,0},\,k_{x,1})},\quad\forall x\in X$$
An algorithm to find the maximal independent set can be found using a bottom up approach. By first getting $k_{v,0}$ and $k_{v,1}$ of every node in the bottom-most layer (i.e. all the bottom-most leaf nodes), $k_{v,1}$ and $k_{v,0}$ of the next layer up can be obtained without needing to go more than one layer deep. This is since $v$ is either a leaf in which case $k_{v,0}$ and $k_{v,1}$ is trivial, or $v$ is a parent to nodes you have already accounted for, in which case you can sum the previously calculated values using the recurrances shown above. This can be repeated along each layer until you get to the top, i.e. the root node.
At the root node, after you calculate $k_{v,0}$ and $k_{v,1}$, you can then find the maximal independent set by taking the maximum of the two.

#### algorithm to find the maximal independent set
```

(1) starting from the root node, for each node:
(2)		traverse down and record the layer of each node
(3)	take the highest level as the starting position

(4)	for each level, going from max -> 0:
(5)		for each node on that level:
(6)			if the node is a leaf:
(7)				kv0 is 0, and kv1 is w(node)
(8)			if the node is not a leaf:
(9)				kv1 is the sum of all (max of kv0 and kv1) child nodes
(10)			kv0 is the sum of all kv1 child nodes
(11)return the max of (kv0 and kv1) of the root node
```
- Line $1$ is $O(n)$ because it goes through every single node once
- Line 2 and 3 is $O(1)$ because it is only one action
- Line $4$ and $5$ are both $O(n)$, but together they are only $O(n)$ because similarly to line $1$, you will only visit each node once, no matter the configuration of the tree.
- Line $6-11$ is $O(1)$ since they are all one action
Therefore, the algorithm runs on $O(n)$ time complexity



#### Question aiv something like that
The graph construction is designed so that each $u$ in $\{u_{1},u_{2},\dots,u_{\lceil n/3 \rceil}\}$ has exactly $3$ edges connected to it, those being $(u_{i},v_{i}), (u_{i},v_{i + \lceil n/3 \rceil}), (u_{i},v_{i + \lceil 2n/3 \rceil})$. On the other hand, every $v$ in $\{v_{1},v_{2},\dots,v_{n}\}$ has exactly $5$ edges connected to it, those being one edge connected to a $u$ node, and also connected to all $w\in \{w_{1},w_{2},w_{3},w_{4}\}$. Every $w$ node is connected to $n$ edges, since each one is connected to all $v\in\{v_{1},v_{2},\dots,v_{n}\}$.
From this, the total node counts are that all $u$ nodes have degree $3$, all $w$ nodes have degree $n$, and all $v$ nodes have degree $5$. Therefore, in the GreedyIS() algorithm, it will choose the independent set in the following order:
- Choose some $v\in V$, delete all $3$ edges that are connected to a $v$ node. This also removes all $12$ edges connecting said $v$ nodes to the four $w$ nodes.
- Repeat this until there are no $v$ nodes left.
- Now every single $v$ node should be excluded from the independent set, and every single $w$ node has $0$ degree. Therefore, in any order pick all $w$ nodes.
- Now every node in $E_{1}$ is in the independent set, and every node in $E_{2}$ is excluded from the independent set.
- However, the maximal independent set is the set of every node in $E_{2}$ i.e. all nodes $v\in V$. If $n=30$, the maximal IS is $30$, but greedyIS would return $14$.
- Since there are $\frac{n}{3} + 4$ elements in $E_{1}$ compared to $n$ elements in $E_{2}$, this means that as $n$ grows large, the $4$ will become insignificant, and the approximate size of the GreedyIS independent set will approach $\frac{1}{3}$ the size of the maximal independent set. For example, if $n=300$,
- $$\lvert \text{GreedyIS(v)} \rvert =100 + 4=104,\qquad \lvert \text{MaximalIS(v)} \rvert =300$$
Therefore,
$$\lvert \text{GreedyIS(v)} \rvert =\frac{104}{300} \approx \frac{1}{3} \text{ of the maximal IS}$$

#### Part A final question
To make a graph where GreedyIS will give progressively worse results, we can change the graph construction in the previous question, but edit the set of $u$ from being length $\frac{n}{3}$, to a larger denominator $m$, resulting in a smaller set of $U$ but the same size set $V$. As it gets larger, the difference in size from $E_{1}$ to $E_{2}$ will cause GreedyIS to give a worse and worse approximation of the maximal independent set.

#### Part Dii
For any tree, the graph can be reduced to an initial construction and a list of additional nodes. The starting state is $1$ node and $0$ edges. From there a tree is constructed from a list of additional operations that are made from $1$ node that connects to exactly $1$ edge on the existing graph. From this, we can say that
$$\lvert \text{Nodes} \rvert = \lvert \text{Edges} \rvert + 1 \iff \text{Graph is a Tree}$$
And therefore it follows that,
$$\lvert \text{Nodes} \rvert \ne \lvert \text{Edges} \rvert + 1\quad \iff \text{Graph is not a Tree}$$
Therefore, if we wanted to construct a function that would tell if a graph is a tree, then we can iterate through each node, and iterate through the edges that are connected to each node. If by the end of it, the statement above does not hold true, then it shows the graph is not a tree.


#### $O(n^{2}+m)$
- Line 1 is $O(1)$
- Line 3 is $O(n)$ (n iterations through the whole list)
- Line 5 is $O(n)$ (worst case is $n$ iterations, and drops off from there)
- Line 6 is $O(n)$ (best/worst case is $n$ iterations, all vertices need to be checked each time since nodes are not being deleted)
- Lines 8 - 10 are in total $O(m)$. This is because each edge only gets checked once and then deleted, so eventually there will be $m$ iteratations in total
- Line 11 is $O(n)$ (n iterations through the whole list)
Since Line 5 and 6 are nested, this means that Lines 5 - 10 are $O(n^{2})$. Since there is nothing larger than that, the $n^{2}$ term overpowers every other term in the algorithm
Therefore, the algorithm runs in $O(n^{2}+m)$






```
empty parent array size n
empty discovery array size n

chosen_node = start at a random node

while there is empty entries in parent array
	register chosen_node in parent array
	check every edge connected to the chosen_node
		if edge is connected to a node without an entry in discovery
			register in discovery array
		else if edge is connected to a node with an entry in parent array
			do nothing, it's part of the tree
		else if edge is connected to a node without an entry in parent
			remove edge, it's already been discovered and is in the tree
		
	chosen_node = a discovered entry that is not in parent array
```