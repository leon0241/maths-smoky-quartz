---
---

**Tags:** #Algebra/Groups #Main #Course/FPM 

**Tags:** #Algebra/Groups #Notation #Course/FPM 

 > 
 > \[!Notation\]+ Ntn: [Partition](..\Individuals\Partition.md)
 > Intuitively, we often think of sets schematically as blobs containing elements, drawn as dots:
 > ![Pasted image 20230213172002.png](..\Images\Pasted%20image%2020230213172002.png)
 > For various reasons, often we want to *partition* this set into *non-overlapping subsets*, which we draw as
 > ![Pasted image 20230213172045.png](..\Images\Pasted%20image%2020230213172045.png)

^239899

When we want to partition an set like shown above, we use an equivalence relation:

**Tags:** #Algebra/Groups #Notation #Course/FPM 

 > 
 > \[!Notation\]+ Ntn: [Relation](..\Individuals\Relation.md)
 > Let $X$ be a set, and $R$ a subset of $X\times X$; thus $R$ consists of some ordered pairs $(s,t)$ with $s,t\in X$. If $(s,t) \in R$ we write $s \sim t$ and say "$s$ is related to $t$". We call $\sim$ a *relation* on $X$.

^149542

^0b1489

###### Examples of Relations

 > 
 > \[!Example\]+ Ex: [Equivalence Modulo](..\Individuals\Relation.md)
 > Let $n\ge 2$ be an integer. We define a relation called *equivalence modulo* $n$ on the set $\Z$ of all integers as follows:
 > $$\text{for } a,b\in\mathbb{Z},\quad aRb \text{ if and only if } a-b \text{ is divisible by n}$$
 > For this relation, $aRb$ is written $a\equiv b\bmod{n}$. For example, $17\equiv 2\bmod{5}$

^574496

**Tags:** #Algebra/Groups #Definition #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Equivalence Relation](..\Individuals\Equivalence%20Relation.md)
 > A [relation](..\Individuals\Relation.md#149542) $\sim$ is called an *equivalence relation* on X if it satisfies the following three axioms:
 > 
 > * **R. (Reflexive):** $x\sim x$ for all $x\in X$
 > * **S. (Symmetric):** $x\sim y$ implies that $y\sim x$ for all $x,y\in X$
 > * **T. (Transitive):** $x\sim y$ and $y\sim z$ implies that $x\sim z$ for all $x,y,z\in X$

^853398

**Tags:** #Algebra/Groups #Definition #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Equivalence Class](..\Individuals\Equivalence%20Class.md)
 > If $\sim$ is an [Equivalence Relation](..\Individuals\Equivalence%20Relation.md) on a set $X$, then the set $X$ is partitioned into pieces called the *equivalence classes*. In our previous picture
 > ![Pasted image 20230215204505.png](..\Images\Pasted%20image%2020230215204505.png)
 > the shaded region is the equivalence class containing $x$, which *by definition*, is just all the elements that are related to $x$. It is denoted $cl(x)$. In mathematical symbols, the shaded region is defined as
 > $$cl(x) :={\text{all elements that are related to } x}={s\in X , | , x \sim s}$$

^6dbdfd

**Tags:** #Algebra/Groups #Notation #Course/FPM 

 > 
 > \[!Notation\]+ Ntn: [Coset Notation](..\Individuals\Coset%20Notation.md)
 > Let $A,B$ be subsets of a group $G$, and let $g\in G$. Then
 > $$AB:={ab ,|, a\in A, b\in B}, \qquad gA := {ga,|,a\in A}$$
 > and similarly for other obvious variants.

^5f041f

**Tags:** #Algebra/Groups #Definition #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Definition of a Coset](..\Individuals\Definition%20of%20a%20Coset.md)
 > Let $H\le G$ and let $g\in G$. Then a *left coset* of  $H$ in $G$ is a subset of $G$ of the form $gH$, for some $g\in G$.
 > We denote the set of left cosets of $H$ in $G$ by $G/H$

^6eae3f

 > 
 > \[!Example\]+ Ex: [Example of a Coset](Coset.md)
 > Consider $\Z\_{4}$ under addition, and let $H={0,2}$ ($e=0$.) The cosets of $H$ in $G$ are:
 > $$\begin{align}
 > eH = e * H = {e * h,|,h\in H} = {0+h,|, h\in H} = {0,2} \\
 > 1H = 1 * H = {1 * h,|,h\in H} = {1+h,|, h\in H} = {1,3} \\
 > 2H = 2 * H = {2 * h,|,h\in H} = {2+h,|, h\in H} = {0,2} \\
 > 3H = 3 * H = {3 * h,|,h\in H} = {3+h,|, h\in H} = {1,3}
 > \\end{align}
 > $$
 > Hence there are two cosets, namely
 > $$0 * H=2 * H={0,2} \quad\text{and}\quad 1 * H=3 * H={1,3}$$
 > The above shows that $g\_{1}H=g\_{2}H$ is possible, even when $g\_{1}\ne g\_{2}$
 > We also have
 > $$G/H={eH=2H,1H=3H} = {{0,2}, {1,3}}$$

**Tags:** #Algebra/Groups #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Coset Rules](..\Individuals\Coset%20Rules.md)
 > Let $H\le G$.
 > 
 > 1. For all $h\in H$, $hH=H$. In particular $eH=H$
 > 1. For $g\_{1},g\_{2}\in G$, the following are equivalent
 > 
 > * $g\_{1}H=g\_{2}H$
 > * there exists $h\in H$ such that $g\_{2}=g\_{1}h$
 > * $g\_{2}\in g\_{1} H$
 > 
 > 3. For $g\_{1},g\_{2}\in G$, define $g\_{1}\sim g\_{2}$ if and only if $g\_{1}H=g\_{2}H$. Then $\sim$ defines an equivalence relation on $G$.

^e0f9d3

###### [Lagrange's Theorem](Lagrange's%20Theorem.md)

%%eof%%