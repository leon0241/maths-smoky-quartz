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

**Tags:** #Analysis/Reals #Definition #Course/FPM 

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

^eefa7b

#### Other Information

 > 
 > \[!Remark\]
 > Sets that don't satisfy all of these are important in other contexts.
 > 
 > * Properties F1 - F4 and F6 together mean that $(/R,+)$ is a commutative ([Abelian](../Individuals/Abelian%20Group.md)) group. 
 > * Properties F1 - F3, F5, F6 mean that ($/R/backslash{0}, /cdot$) is a commutative ([Abelian](../Individuals/Abelian%20Group.md)) group.

#### Ordering the Field of $\R$

**Tags:** #Definition #Analysis/Reals #Course/FPM 

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

^8b3819

#### Intermediate Knowledge

* [Defining Subsets of R (N,Z,Q)](../Individuals/Defining%20Subsets%20of%20R%20%28N,Z,Q%29.md)
* [Defining the Absolute Value](../Individuals/Defining%20the%20Absolute%20Value.md)

#### Axiom of Completeness for $\R$

**Tags:** #Main #Analysis/Reals #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Axiom of Completeness](../Individuals/Axiom%20of%20Completeness.md)
 > If $E \subset \R$ is non-empty and bounded above, then $E$ has a supremum.

^5b377d

#### Idea

For the rational numbers $\Q$, if $q$ is rational then $\sqrt{q}$ isn't neccesarily rational. An example is $2$ and $\sqrt{ 2 }$. In other words, if q is rational, there may not be a rational number $x$ such that $x^2=q$.
The completeness axiom will fill in the gaps and ensure the reals include any number.

**Tags:** #Analysis/Reals #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Bounds, Suprema and Infima](../Individuals/Bounds,%20Suprema%20and%20Infima.md)
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
 > \[!Definition\]+ Def: [Least Upper Bound Property](../Individuals/Least%20Upper%20Bound%20Property.md)
 > Let $S$ be an ordered field (like $\R$). Then $S$ has the *least upper bound property* if given any nonempty $A\subseteq S$ where $A$ is bounded above, $A$ has a least upper bound in $S$. In other words, $sup(A)\in S$ for every such $A$.
 > Such a set is called *complete*

^85a6f1

 > 
 > \[!Remark\]+ Rem: [Uniqueness of Suprema](../Individuals/Axiom%20of%20Completeness.md)
 > If a set has a supremum, it only has one supremum, i.e., the supremum is unique whenever it exists.

 > 
 > \[!Remark\]+ Rem: [Inclusion of Natural Suprema](../Individuals/Axiom%20of%20Completeness.md)
 > If $E\subset\N$ has a supremum, then $sup(E)\in E$

#### Consequences of completeness

**Tags:** #Analysis/Reals  #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ [Archimedean Principle](../Individuals/Archimedean%20Principle.md)
 > Given positive real numbers $a,b\in\R$ there is an integer $n\in\N$ such that $b\<na$

^7feff5

#### Idea

Shows that even if $a$ is quite small, and $b$ is quite large then some integer multiple of $a$ will exceed $b$. This is like saying a bathtub can be emptied with a spoon given enough time.

#### Proof

If $b\<a$ then we set $n=1$ and it is trivially true.
Otherwise, denote the set $E$ as the set ${ k\in\mathbb{N}: ka\le b }$. $E$ is nonempty since $1\in E$. $E$ is also bounded because $ka\le b \iff k\le \frac{b}{a}$, therefore $\frac{b}{a}$ is an upper bound of $E$. Then, by the completeness axiom $s = sup(E)$ exists. Also from [Inclusion of Natural Suprema](../Individuals/Axiom%20of%20Completeness.md#inclusion-of-natural-suprema), since $E\in\N$, then $s\in E$. Set $n=s +1$ and therefore $n\in\N$ and $na>b$ so the claim holds.

**Tags:** #Analysis/Reals #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Density of the Rational Numbers](../Individuals/Density%20of%20the%20Rational%20Numbers.md)
 > Let $a\<b$ be real numbers. Then there exists a $q\in\Q$ such that $a \< q \< b$.

^800178

**Tags:** #Definition #Analysis/Reals #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Least Upper Bound Property](../Individuals/Least%20Upper%20Bound%20Property.md)
 > Let $S$ be an ordered field (like $\R$). Then $S$ has the *least upper bound property* if given any nonempty $A\subseteq S$ where $A$ is bounded above, $A$ has a least upper bound in $S$. In other words, $sup(A)\in S$ for every such $A$.
 > Such a set is called *complete*

^85a6f1

#### The final formal definition of $\R$

**Tags:** #Theorem #Analysis/Reals #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Existence and Uniqueness of R](../Individuals/Existence%20and%20Uniqueness%20of%20R.md)
 > There exists a unique complete ordered field. We call this field *the real numbers*, $\R$.

^4113f2
