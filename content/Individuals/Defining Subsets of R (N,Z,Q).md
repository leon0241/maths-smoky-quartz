---
---

**Tags:** #Definition #Analysis/Reals  #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Defining Subsets of R (N,Z,Q)](Defining%20Subsets%20of%20R%20%28N,Z,Q%29.md)
 > 
 > * We will define a positive real number as any $a\in\R$ where $a>0$. We define a non-negative real number as any $a\in\R$ where $a\ge0$.
 > * We define the set of natural numbers $\N$:
 >   $$\N = {1,2,3,\dots},$$
 > * The set of natural numbers with zero $\N_0$:
 >   $$\N_0={0,1,2,3,\dots},$$
 > * The set of integers $\Z$:
 >   $$\Z={\dots,-2,-1,0,1,2,3,\dots}$$
 > * The set of rationals $\Q$:
 >   $$\Q=\Big{\frac{m}{n} : m,n\in\Z \text{ and }n\ne0\Big}$$


 > 
 > \[!Definition\]+ Def: [Peano Axioms to define N and Z](Peano%20Axioms%20to%20define%20N%20and%20Z.md)
 > From just stating $N = {1,2,3,\dots}$, it is not clear what $2$ or $3$ actually is, so we will need to define $2$ as $1 + 1$, and $3$ as $2 + 1$ or $1 + 1+1$, and so forth. Define functions $s(n)$(successor of $n$) and $p(n)$(predecessor of $n$) where $s(n)=n+1$, and $p(n) = n - 1$. We can first construct a list of axioms to define every number in $\N_0$ called the Peano Axioms.
 > 
 > * **N1:** $0\in\N_0$
 > * **N2:** For any $n\in\N_0$, there exists $s(n)\in\N_0$
 > * **N3:** If $s(n) = s(m)$ then $n = m$
 > * **N4:** There does not exist $n\in\N_0$ with $s(n) = 0$
 > * **N5:** If $0\in A\subset\N$ and if $n\in A$ implies $s(n)\in A$ then $A = \N_0$

We can then define $\Z$ as a set that contains $\N_0$ and has the following properties:

 > 
 > * **Z1:** Given $n\in\Z$ then there exists $p(n)\in\Z$ such that $s(p(n))=n$
 > * **Z2:** If $A\subset\Z$ and $s(n)\in A$ iff $n\in A$, then $A = Z$

