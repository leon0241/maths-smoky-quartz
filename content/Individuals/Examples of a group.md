---
---

**Tags:** #Collection #Algebra/Groups #Course/FPM 

###### [Examples of a group](Examples%20of%20a%20group.md)

 > 
 > \[!Example\]+ Ex: [Addition under  Z](Examples%20of%20a%20group.md)
 > The integers $\Z = {\dots,-3,-2,-1,0,1,2,3,\dots }$ form a group under the operation $g\ast h = g+h$.
 > 
 > * **G1 - Closure:** $g+ h\in\Z$ for all $g,h\in\Z$ (infinite and countable)
 > * **G2 - Associativity:** $(g+h)+i=g+(h+i)$ for all $g,h,i\in\Z$
 > * **G3 - Identity:** There exists an integer $0$ such that $g + 0 = g$ for all $g\in\Z$
 > * **G4 - Inverses:** There exists an inverse $(-g)$ such that $(-g) + g = g + (-g)=0$ for all $g\in\Z$

 > 
 > \[!example\]+ Ex: [Addition under N and N0](Examples%20of%20a%20group.md)
 > The natural numbers $\N = { 1,2,3,\dots }$ and $\N\_{0}={ 0,1,2,3,\dots  }$ fail under the operation $g\ast h = g+h$.
 > 
 > * **G1 - Closure:** $g+ h\in\N$ for all $g,h\in\N$ (infinite and countable)
 > * **G2 - Associativity:** $(g+h)+i=g+(h+i)$ for all $g,h,i\in\Z$
 > * **G3 - Identity:** Fails! There exists **no** natural number $e$ such that $g + e = g$ for all $g\in\N$ ($0$ is not included in $\N$)
 > 
 > **G1** - **G3** hold for the set $\N\_{0}$, as there exists an identity element $0$ such that $g+0=g$, but **G4** fails since there is no inverse where $g^{-1} + g = g + g^{-1} = 0$

 > 
 > \[!example\]+ Ex: [Multiplication under Z and Q](Examples%20of%20a%20group.md)
 > 
 > * The set $\Q$ fails under the operation $g\ast h = g\times h$. **G1** - **G3** hold, with identity element $1$, but there is no inverse element for $0$ where $0 \times 0^{-1}=1$. On the other hand, $(\Q\backslash{ 0 },\times)$ is a valid group (Rational numbers excluding $0$) since the edge case is removed, all other numbers have an inverse
 > * A similar argument can be said for $\Z$ under multiplication, but **G4** fails regardless of if $0$ is excluded or not. For example the only possible inverse of $2$ is $\frac{1}{2}$, but that is not an integer. The only elements of $(\Z\backslash{ 0 },\times )$ that have an inverse are ${1,-1}$


 > 
 > \[!Definition\]+ Def: [Dihedral Group](Dihedral%20Group.md)
 > The dihedral group $D\_{n}$ is the group of the symmetries of a n-gon. 


