---
---

**Tags:** #Main #Analysis/Reals #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Axiom of Completeness](Axiom%20of%20Completeness.md)
 > If $E \subset \R$ is non-empty and bounded above, then $E$ has a supremum.

^5b377d

#### Idea

For the rational numbers $\Q$, if $q$ is rational then $\sqrt{q}$ isn't neccesarily rational. An example is $2$ and $\sqrt{ 2 }$. In other words, if q is rational, there may not be a rational number $x$ such that $x^2=q$.
The completeness axiom will fill in the gaps and ensure the reals include any number.

**Tags:** #Analysis/Reals #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Bounds, Suprema and Infima](Bounds,%20Suprema%20and%20Infima.md)
 > Let $S$ be an ordered field (like $\R$) and $A\subseteq S$ be nonempty.
 > 
 > 1. The set $A$ is *bounded above* if there exists some $b\in S$ such that $x\le b$ for all $x\in A$; in this case, $b$ is called an *upper bound* of $A$.
 > 1. The *least upper bound* of A - if it exists - is some $b\_{0}\in S$ such that (1) $b\_{0}$ is an upper bound of $A$, and (2) if $b$ is any other upper bound of $A$, then $b\_{0}\le b$. Such a $b\_{0}$ is also called the *supremum* of $A$ and is denoted by $sup(A)$.
 > 1. The set $A$ is *bounded below* if there exists some $b\in S$ such that $x\ge b$ for all $x\in A$; in this case, $b$ is called an *lower bound* of $A$.
 > 1. The greatest lower bound\* of A - if it exists - is some $b\_{0}\in S$ such that (1) $b\_{0}$ is an lower bound of $A$, and (2) if $b$ is any other lower bound of $A$, then $b\_{0}\ge b$. Such a $b\_{0}$ is also called the *inimum* of $A$ and is denoted by $inf(A)$.
 > 1. If a set is both bounded above and bounded below, then it is simply called *bounded*.

^35189a

#### Conceptualising the reals

The way we can think about completeness is that if we consider the set of rational numbers between $\pm \sqrt{ 2 }$, or
$$A := { x\in\Q: x^{2}\<2 }\quad \text{or} \quad A := { x\in\Q:0\le r \text{ and } r^{2}\le 2}$$

* The set is bounded above (e.g $6$ or $2$ is larger than any element in the set)
* The least upper bound of the set is the smallest lower bound, or a number that's slightly larger than the infinitely closest rational value to $\sqrt{2}$, or in other words, $\sqrt{2}$ exactly.

If we start with $\Q$, and add in all the least upper bounds from every set that is bounded above, then we will include irrational numbers like $\sqrt{2}$ in our set. Doing this for every single set A will form a complete set of real numbers $\R$. This method of defining the axioms for $\R$ will also ensure that complex numbers like $3+2i$ are not included in the set

**Tags:** #Definition #Analysis/Reals #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Least Upper Bound Property](Least%20Upper%20Bound%20Property.md)
 > Let $S$ be an ordered field (like $\R$). Then $S$ has the *least upper bound property* if given any nonempty $A\subseteq S$ where $A$ is bounded above, $A$ has a least upper bound in $S$. In other words, $sup(A)\in S$ for every such $A$.
 > Such a set is called *complete*

^85a6f1

 > 
 > \[!Remark\]+ Rem: [Uniqueness of Suprema](Axiom%20of%20Completeness.md)
 > If a set has a supremum, it only has one supremum, i.e., the supremum is unique whenever it exists.

 > 
 > \[!Remark\]+ Rem: [Inclusion of Natural Suprema](Axiom%20of%20Completeness.md)
 > If $E\subset\N$ has a supremum, then $sup(E)\in E$

#### Consequences of completeness

**Tags:** #Analysis/Reals  #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ [Archimedean Principle](Archimedean%20Principle.md)
 > Given positive real numbers $a,b\in\R$ there is an integer $n\in\N$ such that $b\<na$

^7feff5

#### Idea

Shows that even if $a$ is quite small, and $b$ is quite large then some integer multiple of $a$ will exceed $b$. This is like saying a bathtub can be emptied with a spoon given enough time.

#### Proof

If $b\<a$ then we set $n=1$ and it is trivially true.
Otherwise, denote the set $E$ as the set ${ k\in\mathbb{N}: ka\le b }$. $E$ is nonempty since $1\in E$. $E$ is also bounded because $ka\le b \iff k\le \frac{b}{a}$, therefore $\frac{b}{a}$ is an upper bound of $E$. Then, by the completeness axiom $s = sup(E)$ exists. Also from [Inclusion of Natural Suprema](Axiom%20of%20Completeness.md#inclusion-of-natural-suprema), since $E\in\N$, then $s\in E$. Set $n=s +1$ and therefore $n\in\N$ and $na>b$ so the claim holds.

**Tags:** #Analysis/Reals #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Density of the Rational Numbers](Density%20of%20the%20Rational%20Numbers.md)
 > Let $a\<b$ be real numbers. Then there exists a $q\in\Q$ such that $a \< q \< b$.

^800178
