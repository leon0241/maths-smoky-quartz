---
---

**Tags:** #Algebra/Groups #Main #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Subgroup](Subgroups.md)
 > Let $G$ be a [group](Groups.md). We say that a non-empty subset $H$ of $G$ is a *subgroup* of $G$ if $H$ itself is a group (under the operation from $G$). We write $H\le G$ if $H$ is a subgroup of $G$. If also $H\ne G$, we write $H\<G$ and say that $H$ is a proper subgroup

 > 
 > \[!Lemma\] Lem: [Inherited elements of subgroups](Subgroups.md)
 > Suppose that $H\le G$. Then,
 > 
 > 1. $e\_{H} = e\_{G}$
 > 1. if $h\in H$, the inverse of $h$ in $H$ equals the inverse of $h$ in $G$

**Tags:** #Algebra/Groups #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Test for a subgroup](../Individuals/Test%20for%20a%20subgroup.md)
 > $H\subseteq G$ is a subgroup of $G$ if and only if:
 > 
 > * **S1:** $H$ is not empty
 > * **S2:** If $h,k\in H$ then $h\ast k\in H$
 > * **S3:** If $h\in H$ then $h^{-1}\in H$
 > 
 > Alternative test for subgroups:
 > 
 > * $\widetilde{S1}$: $H$ is not empty.
 > * $\widetilde{S2}$: If $h,k\in H$ then $h\*k^{-1}\in H$

^32f826

###### [Examples of a subgroup](../Individuals/Examples%20of%20a%20subgroup.md)

**Tags:** #Algebra/Groups #Notation #Course/FPM 

 > 
 > \[!Notation\]+ Ntn: [Notation of dropping operators](../Individuals/Subgroup%20notation.md)
 > When dealing with a general group $G$, as much as possible we will write $gh$ for $g\*h$

^d87590

###### Reasoning

Just to make life easier, but when dealing with groups under addition it may be confusing as we are used to $\*$ for multiplication.

 > 
 > \[!Notation\]+ Ntn: [Notation of power operators](../Individuals/Subgroup%20notation.md)
 > It is useful to have a shorthand for expression such as $g\*\\dots*g$. If $G$ is a group, $g\in G$ and $k\in\Z$, we define the power $g^k$ by
 > $$g^k := \begin{cases}
 > \\hspace{12pt}\overbrace{g*\\dots*g}^{k} &\text{if } k>0 \\
 > \\hspace{30pt} e &\text{if } k = 0 \\
 > \\underbrace{ g^{-1}*\\dots\*g^{-1} }\_{ -k } &\text{if } k \< 0
 > \\end{cases}
 > $$

^f1b3b9

**Tags:** #Algebra/Groups #Notation #Course/FPM 

 > 
 > \[!Notation\]+ Ntn: [Notation of dropping operators](../Individuals/Subgroup%20notation.md)
 > When dealing with a general group $G$, as much as possible we will write $gh$ for $g\*h$

^d87590

###### Reasoning

Just to make life easier, but when dealing with groups under addition it may be confusing as we are used to $\*$ for multiplication.

 > 
 > \[!Notation\]+ Ntn: [Notation of power operators](../Individuals/Subgroup%20notation.md)
 > It is useful to have a shorthand for expression such as $g\*\\dots*g$. If $G$ is a group, $g\in G$ and $k\in\Z$, we define the power $g^k$ by
 > $$g^k := \begin{cases}
 > \\hspace{12pt}\overbrace{g*\\dots*g}^{k} &\text{if } k>0 \\
 > \\hspace{30pt} e &\text{if } k = 0 \\
 > \\underbrace{ g^{-1}*\\dots\*g^{-1} }\_{ -k } &\text{if } k \< 0
 > \\end{cases}
 > $$

^f1b3b9

**Tags:** #Algebra/Groups #Definition #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Order of a Group](../Individuals/Order%20of%20a%20Group.md)
 > A *finite group* $G$ is one with only a finite number of elements. The *order* of a finite group, written $\lvert G \rvert$, is the number of elements in $G$. (Note that if $X$ is a set, we also often write $\lvert X \rvert$ to be the number of elements in $X$.)

^9b31d6

 > 
 > \[!Definition\]+ Def: [Order of an element](../Individuals/Order%20of%20a%20Group.md)
 > Let $G$ be a group and $g\in G$. Then the *order* $o(g)$ of $g$ is the *least* natural number $n$ such that
 > $$g^n = e$$
 > If no such $n$ exists, we say that $g$ has infinite order

^34c240

 > 
 > \[!Example\]+ Ex: [Example of Order](../Individuals/Order%20of%20a%20Group.md)
 > Consider $1\in\Z$ under addition. Then $1*1=1+1=2,,1*1*1=3,\dots$
 > $$\underbrace{1*\\dots\*1}\_{n} = n \ne 0 =e$$
 > for any $n>0$. Hence, $1\in\Z$ has infinite order.

**Tags:** #Algebra/Groups #Definition #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Order of a Group](../Individuals/Order%20of%20a%20Group.md)
 > A *finite group* $G$ is one with only a finite number of elements. The *order* of a finite group, written $\lvert G \rvert$, is the number of elements in $G$. (Note that if $X$ is a set, we also often write $\lvert X \rvert$ to be the number of elements in $X$.)

^9b31d6

 > 
 > \[!Definition\]+ Def: [Order of an element](../Individuals/Order%20of%20a%20Group.md)
 > Let $G$ be a group and $g\in G$. Then the *order* $o(g)$ of $g$ is the *least* natural number $n$ such that
 > $$g^n = e$$
 > If no such $n$ exists, we say that $g$ has infinite order

^34c240

 > 
 > \[!Example\]+ Ex: [Example of Order](../Individuals/Order%20of%20a%20Group.md)
 > Consider $1\in\Z$ under addition. Then $1*1=1+1=2,,1*1*1=3,\dots$
 > $$\underbrace{1*\\dots\*1}\_{n} = n \ne 0 =e$$
 > for any $n>0$. Hence, $1\in\Z$ has infinite order.

**Tags:** #Algebra/Groups #Theorem #Course/FPM #TODO

 > 
 > \[!Theorem\]+ Thm: [Order of a finite group](../Individuals/Order%20of%20a%20finite%20group.md)
 > In a finite group, every element has finite order.

^291b9b

#### Proof

Let $g\in G$. Consider the inifinte sequence $g,g^2,g^3,\dots$ If $G$ is finite, then there must be repititions in this infinite sequence. Hence there exists $m,n\in\N$ with $m>n$ such that $g^m=g^n$. By cancelation, $g^{m-n}$ = e. This shows that $o(g)\le m-n$, and so consequently $o(g)$ is finite.

**Tags:** #Algebra/Groups #Main #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Cyclic Subgroups](../Individuals/Cyclic%20Subgroups.md)
 > A subgroup $H\le G$ is *cyclic* if $H = \langle h \rangle$ for some $h\in H$. In this case, we say that $H$ is the *cyclic subgroup generated by h*. If $G=\langle g \rangle$ for some $g\in G$, then we say that the group $G$ is *cyclic*, and that $g$ is a *generator*.

^a3c4c9

**Tags:** #Algebra/Groups #Definition #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Definition of the power subset](../Individuals/Definition%20of%20the%20power%20subset.md)
 > Let $G$ be a group and let $g\in G$ be an element. We define the subset
 > $$\langle g \rangle := {g^k ,|,k\in\mathbb{Z}} = {\dots,g^{-2}, g^{-1},e,g,g^{2},\dots  }$$
 > Note that if $G$ is finite, then $\langle g \rangle$ (being a subset of $G$) is finite, and we can think of $\langle g \rangle$ as
 > $$\langle g \rangle = {e,\mathbf{g}\dots,g^{o(g)-1}}$$
 > by [order of a finite group](../Individuals/Order%20of%20a%20finite%20group.md#291b9b)

^b27ec4

**Tags:** #Collection #Algebra/Groups #Course/FPM 

 > 
 > \[!Example\]+ Ex: [Examples of a cyclic subgroup](../Individuals/Examples%20of%20a%20cyclic%20subgroup.md)
 > 
 > * $\Z\_{n}$ under addition is cyclic, since $\langle 1 \rangle = \Z\_{n}$
 >   From [power subset](../Individuals/Definition%20of%20the%20power%20subset.md), the group $\langle 1 \rangle$ is defined as
 >   $$\begin{align}
 >   \\langle 1 \rangle &= {1,,1^{2},,1^3,,\dots ,,1^n} \\
 >   &= {1,,1+1, , 1+1+1,, \dots,, \underbrace{1+\dots+1}*{n}} \\
 >   &= {1,,2,,3,,\dots,,n} \\
 >   &= \mathbb{Z}*{n}
 >   \\end{align}$$
 > * In $\Z\_{8}$ the cyclic subgroup generated by $2$ is $\langle 2 \rangle = {0,2,4,6}$. This is strictly contained in $\Z\_{8}$ therefore it is a cyclic subgroup
 > * In $D\_{n}$, the subgroup $H$ consisting of the identity and all the rotations, i.e.
 > * $$H = {e,,g,,g^2,,\dots,,g^{n-1}}$$
 >   is a cyclic subgroup since $H = \langle g \rangle$. Note also that $H=\langle g^{-1} \rangle$

^050108

###### [Consequences of Cyclic subgroups](../Individuals/Consequences%20of%20Cyclic%20subgroups.md)

 
