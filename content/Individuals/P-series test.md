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
Since $\left( 1+n\cdot \frac{1}{2} \right)$ diverges to $\infty$, by the [comparison test](Comparison%20Test.md#c38bd1), the subsequence $s\_{2^n}$ also diverges to $\infty$. For a [monotonically increasing sequence](Monotone%20Sequences.md#e29b33), if a subsequence diverges to $\infty$ - implying that $(s\_{n})$ is unbounded - the entire sequence also diverges to $\infty$ by the [monotone convergence theorem](Monotone%20Convergence%20Theorem.md#f88f95). This shows that the harmonic series diverges to $\infty$. 

The comparison test can also be used to show that $\displaystyle\sum\_{n=1}^{\infty} \frac{1}{k^p},, p\<1$ is divergent. If $p\le 1$, then $\dfrac{1}{k^p} \ge \frac{1}{k}$ for all $k\in\N$. since $\displaystyle\sum\_{n=1}^{\infty} \frac{1}{k}$ diverges, then so must $\displaystyle\sum\_{n=1}^{\infty} \frac{1}{k^p}$

#### Proof 2 (Cauchy Condensation)

**Tags:** #Theorem #Analysis/Series #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Cauchy's Condensation Test](Cauchy's%20Condensation%20Test.md)
 > Let $(a_n)\_{n\in\N}$ be a [decreasing sequence](Monotone%20Sequences.md)  with non-negative terms. Then the following are equivalent:
 > 
 > 1. The series $\dsumoinf a_n$ converges 
 > 1. The series $\dsumzinf 2^na\_{2^n}$ converges.

^51fa82

###### Proof

^a8f3be

For $n\in\N$ define

* $S_n = a_1 + a_2 + a_3 + \cdots + a_n$,
* $T_n = A_1 + 2a_2 + 4a_4 + 8a_8 + \cdots + 2^{n-1}a\_{2^{n-1}}$

Group the terms in $S\_{2^n}$ like
$$S\_{2^n} = a_1 + a_2 + (a_3 + a_4) + (a_5 + a_6+a_7+a_8)+\cdots+(a\_{2^{n-1}+1} +a\_{2^{n-1}+2} +\cdots+a\_{2^n})$$
Since $a_n$ has to be decreasing, $(a_3+a_4) > 2a_4$ and the same follows for the rest
$$
\\begin{align}
S\_{2^n} &= \ccolO a_1 \ccolD+ \ccolB a_2 \ccolD+ \ccolR (a_3 + a_4) \ccolD +\ccolG(a_5 + a_6+a_7+a_8) \ccolD+\cdots+ \ccolY (a\_{2^{n-1}+1} +a\_{2^{n-1}+2} +\cdots+a\_{2^n})\\
&\ge \ccolO a_1 \ccolD + \ccolB a_2 \ccolD + \ccolR 2a_4 \ccolD + \ccolG 4a_8 \ccolD +\cdots+ \ccolY 2^{n-1}a\_{2^n} \\
&=\ccolD\frac{1}{2}\ccolO a_1 + \ccolD\frac{1}{2}(\ccolO a_1 \ccolD+\ccolB 2a_2 \ccolD+\ccolR 4a_4 \ccolD+ \ccolG8a_8 \ccolD+\cdots+ \ccolY 2^na\_{2^n}) \\
&=\ccolD\frac{1}{2}\ccolO a_1 + \ccolD\frac{1}{2}(\ccolO a_1 \ccolD+\ccolB 2a_2 \ccolD+\ccolR 4a_4 \ccolD+ \ccolG8a_8 \ccolD+\cdots+ \ccolY 2^na\_{2^n}) \\
&=\frac{1}{2}\ccolO a_1 \ccolD + \frac{1}{2}T\_{n+1} \quad\implies\quad T\_{n+1} \le 2(S\_{2^n} - \frac{\ccolO a_1}{\ccolD 2})
\\end{align}
$$
Similarly,
$$
\\begin{align}
S\_{2^n} &= \ccolO a_1 \ccolD+ \ccolB a_2 \ccolD+ \ccolR (a_3 + a_4) \ccolD +\ccolG(a_5 + a_6+a_7+a_8) \ccolD+\cdots+ \ccolY (a\_{2^{n-1}+1} +a\_{2^{n-1}+2} +\cdots+a\_{2^n})\\
&\le \ccolO a_1 \ccolD + \ccolB a_2 \ccolD + \ccolR 2a_2 \ccolD + \ccolG 4a_4 \ccolD +\cdots+ \ccolY 2^{n-1}a\_{2^{n-1}} \\
&= a_2 + T_n
\\end{align}
$$
Using these two conclusions,

* If $\dsumoinf a_n$ converges, then $(S_n)*{n\in\N}$ is bounded. By (1), $(T_n)*{n\in\N}$ is bounded, therefore $\dsumzinf 2^na_n$ converges.
* If $\dsumzinf 2^na_n$ converges, then $(T_n)*{n\in\N}$ is bounded. By (2), $(S*{2^n})*{n\in\N}$ is bounded, therefore $(S_n)*{n\in\N}$ is bounded (because $S_n \le S\_{2^n}$), therefore $\dsumoinf a_n$ converges.

#### Examples

 > 
 > \[!example\] Ex: [P-series test verification](Cauchy's%20Condensation%20Test.md)
 > The series $\dsumoinf \dfrac{1}{n^p}$ converges iff $p > 1$.
 > 
 > * Assume that $p > 0$. Then, $\dfrac{1}{n^p}$ is decreasing. By Cauchy's Condensation Test, the series $\dsumoinf \dfrac{1}{n^p}$ converges iff the series $\dsumzinf 2^n\dfrac{1}{(2^n)^p}$ converges. Observe that
 >   $$2^n\dfrac{1}{(2^n)^p} = 2^{-np+n} = 2^{-(p-1)n} = \Big( \dfrac{1}{2^{p-1}}\Big)^n$$
 >   The geometric series $\dsumzinf \bigg(\dfrac{1}{2^{p-1}}\bigg)^n$ converges iff $\dfrac{1}{2^{p-1}} \< 1$ ([geometric series test](Geometric%20Series%20Test.md#691af3)), which is equivalent to $p>1$.
 > * If $p\le0$, then $\dfrac{1}{n^p} = n^{-p} \not\to 0$, therefore the series $\dsumoinf \dfrac{1}{n^p}$ diverges.

^fd4b54

%%eof%%