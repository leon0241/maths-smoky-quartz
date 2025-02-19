---
---

**Tags:** #Analysis/Proofs #Main #Course/FPM 

 > 
 > \[!Definition\]+ Thm: [Proving a Sequence is Convergent](Proving%20a%20Sequence%20is%20Convergent.md)
 > A sequence of real numbers $(x\_{n})$ is said to converge to a real number $L$ if for every $\epsilon>0$ there is $N\in\N$ (where $N$ usually depends on $\epsilon$) such that
 > $$\text{for all } n\ge N\quad\text{we have that } \lvert x\_{n}-L \rvert \<\\epsilon $$


 > 
 > \[!Notation\]+ Ntn: [Convergent Series Notation](../Individuals/Convergent%20Series%20Notation.md)
 > The following phrases will be used interchangeably:
 > 
 > * $(x\_{n})$ converges to $a$
 > * $x\_{n}$ converges to $a$ as $n$ goes to infinity
 > * $x\_{n}\to a$ as $n\to\infty$
 > * $\displaystyle\lim\_{ n \to \infty } x\_{n} = a$
 > * the *limit* of $(x\_{n})$ exists and is equal to $a$


###### Idea

The main method to show convergence is to start with an arbitrary $\epsilon$ and find a sufficiently large $N\in\N$. Furthermore, the constraint that $N$ is a natural number is unneccessary. From the [Archimedean Principle](../Individuals/Archimedean%20Principle.md#7feff5), we know that for each real number $r$ we can find a natural number $N$ such that $N>r$. With this we can easily swap between the two definitions.

###### [Examples of an Epsilon N Proof](../Individuals/Examples%20of%20an%20Epsilon%20N%20Proof.md)

