---
---

**Tags:** #Main #Analysis/Reals #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Axiom of Completeness](Axiom%20of%20Completeness.md)
 > If $E \subset \R$ is non-empty and bounded above, then $E$ has a supremum.


#### Conceptualising the reals

The way we can think about completeness is that if we consider the set of rational numbers between $\pm \sqrt{ 2 }$, or
$$A := { x\in\Q: x^{2}\<2 }\quad \text{or} \quad A := { x\in\Q:0\le r \text{ and } r^{2}\le 2}$$

* The set is bounded above (e.g $6$ or $2$ is larger than any element in the set)
* The least upper bound of the set is the smallest lower bound, or a number that's slightly larger than the infinitely closest rational value to $\sqrt{2}$, or in other words, $\sqrt{2}$ exactly.

If we start with $\Q$, and add in all the least upper bounds from every set that is bounded above, then we will include irrational numbers like $\sqrt{2}$ in our set. Doing this for every single set A will form a complete set of real numbers $\R$. This method of defining the axioms for $\R$ will also ensure that complex numbers like $3+2i$ are not included in the set


 > 
 > \[!Definition\]+ Def: [Least Upper Bound Property](Least%20Upper%20Bound%20Property.md)
 > Let $S$ be an ordered field (like $\R$). Then $S$ has the *least upper bound property* if given any nonempty $A\subseteq S$ where $A$ is bounded above, $A$ has a least upper bound in $S$. In other words, $sup(A)\in S$ for every such $A$.
 > Such a set is called *complete*


 > 
 > \[!Remark\]+ Rem: [Uniqueness of Suprema](Axiom%20of%20Completeness.md)
 > If a set has a supremum, it only has one supremum, i.e., the supremum is unique whenever it exists.

 > 
 > \[!Remark\]+ Rem: [Inclusion of Natural Suprema](Axiom%20of%20Completeness.md)
 > If $E\subset\N$ has a supremum, then $sup(E)\in E$

#### Consequences of completeness


 > 
 > \[!Theorem\]+ [Archimedean Principle](Archimedean%20Principle.md)
 > Given positive real numbers $a,b\in\R$ there is an integer $n\in\N$ such that $b\<na$



 > 
 > \[!Theorem\]+ Thm: [Density of the Rational Numbers](Density%20of%20the%20Rational%20Numbers.md)
 > Let $a\<b$ be real numbers. Then there exists a $q\in\Q$ such that $a \< q \< b$.



