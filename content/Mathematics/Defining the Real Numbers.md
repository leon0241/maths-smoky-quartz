---
---

**Tags:** #Main #Analysis/Reals #Course/FPM

 > 
 > \[!Definition\]+ Def: [Definition of the Reals](Defining%20the%20Real%20Numbers.md)
 > The definition of the Real numbers, denoted by $\R$ is built from 3 parts and defined by Axioms (rules that we take as a given and don't need to prove)
 > 
 > 1. Field which is an algebraic object
 > 1. Ordering which is compatible with the field
 > 1. Completeness which ensures there is no "gaps" in the field

#### Defining a Field of $\R$


 > 
 > \[!Definition\]+ Def: [Field Axioms of R](../Individuals/Field%20Axioms%20of%20R.md)
 > The set $\R$ is equipped with the algebraic operations $+$ and $\cdot$ (Domain $\R\times\R$, and range $\R$). We assume that the triple ($\R,+,\cdot$) is a field which means it satisfies the following for every $a, b,c\in\R$
 > 
 > * **F1 - Closure:** $a + b$ and $a \cdot b$ belong to $\R$
 > * **F2 - Associativity:** $(a+b)+c=a+(b+c)$ and $(a\cdot b)\cdot c = a \cdot(b\cdot c)$.
 > * **F3 - Commutativity:** $a+b = b+a$ and $a\cdot b = b\cdot a$
 > * **F4 - Existence of the Additive Identity:** There is a unique element $0\in\R$ such that $0 + a = a$ for all $a\in\R$
 > * **F5 - Existence of the Multiplicative Identity:** There is a unique element $1\in\R$ such that $1\ne0$ and $1\cdot a = a$ for all $a\in\R$ (one consequence of this is that fields must have at least two elements)
 > * **F6 - Existence of Additive Inverses:** For every $a\in\R$ there is a unique element $-a\in\R$ such that $a+(-a)=0$
 > * **F7 - Existence of Multiplicative Inverses:** For every $a\in\R$ and $a\ne0$ there is a unique element $a^{-1}\in\R$ such that $a\cdot(a^{-1})=1$
 > * **F8 - Distributive Law:** 
 >   * $a\cdot (b+c) = a\cdot b + a\cdot c$
 >   * $(b+c)\cdot a=(b\cdot a) + (c\cdot a)$ 
 >   * (this is the only law connecting addition with multiplication)


#### Ordering the Field of $\R$


 > 
 > \[!Definition\]+ Def: [Order Axioms of R](../Individuals/Order%20Axioms%20of%20R.md)
 > The set of real numbers is **ordered**, in other words there is a concept of "less than", and "more than". There is a relation \< on $\R$ that has the following properties:
 > 
 > * **O1 - Trichotomy Property:** Given $a,b\in\R$, one and only one of the following statements hold:
 >   $$a\<b,\hspace{30pt} b \< a,\hspace{30pt}a=b$$
 > * **O2 - Transitive Property:** $a\<b$ and $b\<c$ imply $a\<c$
 > * **O3 - Additive Property:** $a\<b$ and $c\in\R$ imply $a+c\<b+c$
 > * **O4 - Multiplicative Properties:**
 >   $$a\<b\hspace{20pt} \text{and}\hspace{20pt} c>0\hspace{20pt}\text{imply}\hspace{20pt}ac\<bc$$
 >   and
 >   $$a\<b\hspace{20pt} \text{and}\hspace{20pt} c\<0\hspace{20pt}\text{imply}\hspace{20pt}bc\<ac$$


#### Intermediate Knowledge

* [Defining Subsets of R - N,Z,Q](../Individuals/Defining%20Subsets%20of%20R%20-%20N,Z,Q.md)
* [Defining the Absolute Value](../Individuals/Defining%20the%20Absolute%20Value.md)

#### Axiom of Completeness for $\R$


 > 
 > \[!Definition\]+ Def: [Axiom of Completeness](../Individuals/Axiom%20of%20Completeness.md)
 > If $E \subset \R$ is non-empty and bounded above, then $E$ has a supremum.


#### Conceptualising the reals

The way we can think about completeness is that if we consider the set of rational numbers between $\pm \sqrt{ 2 }$, or
$$A := { x\in\Q: x^{2}\<2 }\quad \text{or} \quad A := { x\in\Q:0\le r \text{ and } r^{2}\le 2}$$

* The set is bounded above (e.g $6$ or $2$ is larger than any element in the set)
* The least upper bound of the set is the smallest lower bound, or a number that's slightly larger than the infinitely closest rational value to $\sqrt{2}$, or in other words, $\sqrt{2}$ exactly.

If we start with $\Q$, and add in all the least upper bounds from every set that is bounded above, then we will include irrational numbers like $\sqrt{2}$ in our set. Doing this for every single set A will form a complete set of real numbers $\R$. This method of defining the axioms for $\R$ will also ensure that complex numbers like $3+2i$ are not included in the set


 > 
 > \[!Definition\]+ Def: [Least Upper Bound Property](../Individuals/Least%20Upper%20Bound%20Property.md)
 > Let $S$ be an ordered field (like $\R$). Then $S$ has the *least upper bound property* if given any nonempty $A\subseteq S$ where $A$ is bounded above, $A$ has a least upper bound in $S$. In other words, $sup(A)\in S$ for every such $A$.
 > Such a set is called *complete*


 > 
 > \[!Remark\]+ Rem: [Uniqueness of Suprema](../Individuals/Axiom%20of%20Completeness.md)
 > If a set has a supremum, it only has one supremum, i.e., the supremum is unique whenever it exists.

 > 
 > \[!Remark\]+ Rem: [Inclusion of Natural Suprema](../Individuals/Axiom%20of%20Completeness.md)
 > If $E\subset\N$ has a supremum, then $sup(E)\in E$

#### Consequences of completeness


 > 
 > \[!Theorem\]+ [Archimedean Principle](../Individuals/Archimedean%20Principle.md)
 > Given positive real numbers $a,b\in\R$ there is an integer $n\in\N$ such that $b\<na$



 > 
 > \[!Theorem\]+ Thm: [Density of the Rational Numbers](../Individuals/Density%20of%20the%20Rational%20Numbers.md)
 > Let $a\<b$ be real numbers. Then there exists a $q\in\Q$ such that $a \< q \< b$.





 > 
 > \[!Definition\]+ Def: [Least Upper Bound Property](../Individuals/Least%20Upper%20Bound%20Property.md)
 > Let $S$ be an ordered field (like $\R$). Then $S$ has the *least upper bound property* if given any nonempty $A\subseteq S$ where $A$ is bounded above, $A$ has a least upper bound in $S$. In other words, $sup(A)\in S$ for every such $A$.
 > Such a set is called *complete*


#### The final formal definition of $\R$


 > 
 > \[!Theorem\]+ Thm: [Existence and Uniqueness of R](../Individuals/Existence%20and%20Uniqueness%20of%20R.md)
 > There exists a unique complete ordered field. We call this field *the real numbers*, $\R$.



