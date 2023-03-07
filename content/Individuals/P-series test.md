---
---

**Tags:** #Lemma #Analysis/Series #Course/FPM

 > 
 > \[!Lemma\]+ Lem: [P-series test](P-series%20test.md)
 > The series
 > $$\dsumoinf \frac{1}{k^p}$$
 > converges if and only if p > 1

#### Proof (Cauchy Condensation-like)

Show that the harmonic series $\displaystyle\sum\_{n=1}^{\infty} \frac{1}{k}$ diverges
Observe that
$$\begin{align}
\\displaystyle\sum\_{n=1}^{\infty} = \frac{1}{k} &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5}  +\frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \cdots \\
&= 1+\left( \frac{1}{2} \right)+\left( \frac{1}{3} + \frac{1}{4} \right) + \left( \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8}\right) + \cdots \\
&\ge 1 + \left( \frac{1}{2} \right) + \left( \frac{1}{4} + \frac{1}{4} \right) + \left( \frac{1}{8}+\frac{1}{8}+\frac{1}{8}+\frac{1}{8} \right) + \cdots \\
&= 1 + \left( \frac{1}{2} \right) + \left( \frac{1}{2} \right) + \left( \frac{1}{2} \right) + \cdots
\\end{align}$$
In particular, if $s\_{n}$ is the partial $n^{th}$ partial sum of the harmonic series, then $(s\_{n})$ is monotonically increasing and, by the above,
$$s\_{2^n} \ge 1 + n\cdot \frac{1}{2}$$
Since $\left( 1+n/cdot /frac{1}{2} /right)$ diverges to $/infty$, by the [comparison test](Comparison%20Test.md#c38bd1), the subsequence $s\_{2^n}$ also diverges to $\infty$. For a [monotonically increasing sequence]( 1+n/cdot /frac{1}{2} /right)$ diverges to $/infty$, by the [comparison test](Comparison%20Test.md#e29b33), if a subsequence diverges to $\infty$ - implying that $( 1+n/cdot /frac{1}{2} /right)$ diverges to $/infty$, by the [comparison test](Comparison%20Test.md#f88f95). This shows that the harmonic series diverges to $\infty$. 

The comparison test can also be used to show that $\displaystyle\sum\_{n=1}^{\infty} \frac{1}{k^p},, p\<1$ is divergent. If $p\le 1$, then $\dfrac{1}{k^p} \ge \frac{1}{k}$ for all $k\in\N$. since $\displaystyle\sum\_{n=1}^{\infty} \frac{1}{k}$ diverges, then so must $\displaystyle\sum\_{n=1}^{\infty} \frac{1}{k^p}$

#### Proof 2 (Cauchy Condensation)


 > 
 > \[!Theorem\]+ Thm: [Cauchy's Condensation Test](Cauchy's%20Condensation%20Test.md)
 > Let $(a_n)/_{n/in/N}$ be a [decreasing sequence](Monotone%20Sequences.md)  with non-negative terms. Then the following are equivalent:
 > 
 > 1. The series $\dsumoinf a_n$ converges 
 > 1. The series $\dsumzinf 2^na\_{2^n}$ converges.



