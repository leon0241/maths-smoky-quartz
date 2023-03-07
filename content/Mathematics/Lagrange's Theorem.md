---
---

**Tags:** #Algebra/Groups #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Lagrange's Theorem](Lagrange's%20Theorem.md)
 > Let $G$ be a *finite group* and let $H$ be a *subgroup* of $G$. Then $\lvert H \rvert$ divides $\lvert G \rvert$
 > Another way of thinking of this is to say that the [order](../Individuals/Order%20of%20a%20Group.md#order-of-a-group) of $H$ is a factor of the order of $G$. More precisely, $/lvert G /rvert = m/lvert G /rvert$ where m is the number of different [left cosets](Coset.md) of $H$ in $G$

###### Reaching Lagrange's Theorem

**Tags:** #Algebra/Groups #Definition #Course/FPM 

 > 
 > \[!Notation\]+ Ntn: [Equivalence Modulo Notation](../Individuals/Equivalence%20Modulo%20Notation.md)
 > Let $G$ be a group, let $H$ be a subgroup of $G$ and let $a,b\in G$. We say that $a$ is *equivalent* to $b$ modulo $H$ and write $a\equiv b$ mod $H$, if $b^{-1}a\in H$.

^af5467

###### Examples of Equivalence Mod

 > 
 > \[!example\]+ Ex: [Equivalence modulo n](../Individuals/Equivalence%20Modulo%20Notation.md)
 > For a group in additive notation, the condition $b^{-1}a\in H$ becomes $a-b\in H$. For example, let $G=\Z$ and $H=5\Z$, the subgroup consisting of all the multiples of $5$. Then for $a,b\in \Z,,a\equiv b \text{ mod } H$ precisely when $a-b\in H$, that is when $a-b$ is a multiple of $5$.
 > Thus, when $H=5\Z$, equivalence modulo $H$ is exactly the same as [equivalence modulo](..\Individuals\Relation.md#574496) 5

**Tags:** #Algebra/Groups #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Equivalence Modulo Theorem](../Individuals/Equivalence%20Modulo%20Theorem.md)
 > Let $G$ be a group, and let $H$ be a subgroup of $G$. Then [equivalence modulo](../Individuals/Equivalence%20Modulo%20Notation.md) $H$ is an [equivalence relation](../Individuals/Equivalence%20Modulo%20Notation.md) on $G$

^6a9f28

###### Proof

By the definition of an [Equivalence Relation](../Individuals/Equivalence%20Relation.md), we must show that the relation is reflexive, symmetric, and transitive.

* **Reflexive:** if $a \in G$ then $a^{-1}a=e\in H$ and so $a\equiv a \text{ mod } H$.
* **Symmetric:** let $a,b\in G$ be such that $a\equiv b\text{ mod } H$. Then $b^{-1}a\in H$. Now $a^{-1}b=(b^{-1}a)^{-1}\in H$ and so $b\equiv a \text{ mod } H$
* **Transitive:** let $a,b,c\in G$ be such that $a \equiv b \text{ mod } H$ and $b\equiv c\text{ mod } H$. Then, $b^{-1}a\in H$ and $c^{-1}b\in H$, so $c^{-1}a=c^{-1}bb^{-1}a\in H$. Thus $a\equiv c \text{ mod } H$.

**Tags:** #TODO #Algebra/Groups #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Coset Partition Theorem](../Individuals/Coset%20Partition%20Theorem.md)
 > Let $G$ be a group, $H$ be a subgroup of $G$ and $a\in G$. The [Equivalence Class](../Individuals/Equivalence%20Class.md) $\overline{a}$ of $a$ under equivalence modulo $H$ is the [left coset](../Individuals/Equivalence%20Class.md) $aH$. Hence, the left cosets of $H$ in $G$ form a partition of $G$

^f2d141

**Tags:** #Theorem #Algebra/Groups #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Consequences of Coset partitions](../Individuals/Consequences%20of%20Coset%20partitions.md)
 > Let $G$ be a group, $H$ be a subgroup of $G$ and let $a,b\in G$. Then
 > 
 > * $aH=bH$ if and only if $b^{-1}a\in H$
 > * $eH=H$
 > * $aH=H$ if and only if $a\in H$
 > * if $a\in bH$ then $aH=bH$

^e57a1f

###### [Applications of Lagrange](../Individuals/Applications%20of%20Lagrange.md)
