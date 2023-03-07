---
---

**Tags:** #Collection #Analysis/Series #Course/FPM
**Tags:** #Theorem #Analysis/Series #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Divergence Test](../Individuals/Divergence%20Test.md)
 > 
 > * If $(a_n)\_{n\in\N}$ converges, then $a_n\to0$.
 > * If $(a_n)\_{n\in\N}$ doesn't converge to $0$, then $\dsumoinf a_n$ diverges.
 > * The converse is not true! $a_n\to0$ does not imply $\dsumoinf a_n$ converges

^b26127

###### Proof

If $\dsumoinf a_n$ converges, then $S_n\to S\in\R$.
Observe: 
$$a_n = S_n - S\_{n-1}, n \ge2,$$
therefore
$$a_n \to S - S = 0$$

**Tags:** #Theorem #Analysis/Series #Course/FPM

 > 
 > \[!Theorem\]+ Thm: [Bounded Theorem](../Individuals/Bounded%20Theorem.md)
 > Let $(a_n)\_{n\in\N}$ be a sequence with non-negative terms. The following are equivalent:
 > 
 > 1. The series $\dsumoinf a_n$ converges.
 > 1. the sequence $(S_n)\_{n\in\N}$ of partial sums is bounded above.

^03396c

**Tags:** #Theorem #Analysis/Series #Course/FPM

 > 
 > \[!Theorem\]+ Thm: [Comparison Test](../Individuals/Comparison%20Test.md)
 > Let $(a_n)*{n\in\N}$ and $(b_n)*{n\in\N}$ be two sequences such that $0\leq a_n\leq b_n$ for all n.
 > 
 > 1. If $\sum_n b_n$ converges, then $\sum_n a_n$ converges as well.
 > 1. If $\sum_n a_n$ diverges, then $\sum_n b_n$ diverges as well.

^c38bd1

###### Proof

We prove the first part (the second part is the contrapositive of the first part).
Since $a_n\leq b_n$ for all $n$, it follows that 
$$0\leq a_1 + a_2 + \cdots+a_n \le b_1 + b_2 + \cdots + b_n$$
If $\sum_n b_n$ converges, then $b_1 + b_2 + \cdots + b_n$ is bounded, therefore $a_1 + a_2 + \cdots + a_n$ is bounded as well, therefore $\sum_n a_n$ converges

**Tags:** #Theorem #Analysis/Series #Course/FPM

 > 
 > \[!Theorem\]+ Thm: [Limit Comparison Test](../Individuals/Limit%20Comparison%20Test.md)
 > Let $(a_n)*{n\in\N}$ and $(b_n)*{n\in\N}$ be two real sequences with $a_n\geq0$ and $b_n\geq0$ for all n. Assume that $\dfrac{a_n}{b_n} \to L$ for some $L\in(0,\infty)$. Then, $\dsumoinf a_n$ converges iff $\dsumoinf b_n$ converges.

^f9d4a7

###### Proof

let $\epsilon = L/2$. There exists an index $N$ such that for all indices n with $n\geq N$ we have
$$L-\epsilon\lt\frac{a_n}{b_n}\lt L + \epsilon$$
Therefore: $$\frac{L}{2}\<\\frac{a_n}{b_n}\<\\frac{3L}{2}$$
It follows that $$a_n\<\\frac{3L}{2}b_n$$
for all $n$ with $n\geq N$
By the [comparison test](../Individuals/Comparison%20Test.md#c38bd1), if $\dsumoinf b_n$ converges, then $\dsumoinf b_n$ converges as well.
Also, $$b_n \< \frac{2}{L}a_n$$
for all $n$ with $n\geq N$.
By the Comparison Test, if $\dsumoinf a_n$ converges then $\dsumoinf b_n$ converges as well

**Tags:** #Theorem #Analysis/Series #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Root Test](../Individuals/Root%20Test.md)
 > Let $\dsumzinf a_n$ be a series with non-negative terms such that
 > $$\sqrt\[n\]{a_n} \to L$$
 > where $0 \le L \le +\infty$.
 > 
 > * If $0\le L \< 1$ then the series $\dsumzinf a_n$ converges.
 > * If $L > 1$ then the series $\dsumzinf a_n$ diverges.
 > * If $L = 1$, the series may or may not converge

^ac4c65

###### Logic

If $a_n\ge 0$ for all n, and $\sqrt\[n\]{a_n} \to L \< 1$, then, for every $\epsilon$,
$$\sqrt\[n\]{a_n} \< L + \epsilon \text{, eventually}$$
Choose $\epsilon$ so that $L + \epsilon \< 1$. Then
$$a_n \< (L + \epsilon)^n = r^n \text{ eventually,}$$where $r = L + \epsilon \< 1$. Therefore $\dsumzinf a_n$ converges.

**Tags:** #Theorem #Analysis/Series #Course/FPM

 > 
 > \[!Theorem\]+ Thm: [Ratio Test](../Individuals/Ratio%20Test.md)
 > Let $\dsumzinf a_n$ be a series with positive terms such that $\dfrac{a\_{n+1}}{a_n} \to L$, where $0\le L \le +\infty$.
 > 
 > * If $0\le L \< 1$ then the series $\dsumzinf a_n$ converges.
 > * If $L > 1$ then the series $\dsumzinf a_n$ diverges.
 > * If $L = 1$:
 >   * If $a_n = \dfrac{1}{n}$, then $\dfrac{a\_{n+1}}{a_n} = \dfrac{n}{n + 1} \to 1$, and $\dsumzinf \frac{1}{n}$ diverges.>
 >   * If $a_n = \dfrac{1}{n^2}$, then $\dfrac{a\_{n+1}}{a_n} = \dfrac{n^2}{(n + 1)^2} \to 1$, and $\dsumzinf \frac{1}{n^2}$ converges.

^f43231

###### Logic

If $a_n > 0$ for all n, and $\dfrac{a\_{n+1}}{a_n} \to L \< 1$, then, for every $\epsilon$,
$$\frac{a\_{n+1}}{a_n} \< L + \epsilon \text{, eventually.}$$
Choose $\epsilon$ so that $L + \epsilon \in (0, 1)$, and take $N \in\N$ sufficiently large. Then
$$a_n = \frac{a_n}{a\_{n-1}}\frac{a\_{n-1}}{a\_{n-2}}\cdots\frac{a\_{N+1}}{a_N} a_n \le (L + \epsilon)^{n - N} a_N = Cr^n$$
where $r = L + \epsilon\in(0,1)$, $C = (L + \epsilon)^{-N}a_N$. Therefore $\dsumzinf a_n$ converges.

**Tags:** #Theorem #Analysis/Series #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Cauchy's Condensation Test](../Individuals/Cauchy's%20Condensation%20Test.md)
 > Let $(a_n)/_{n/in/N}$ be a [decreasing sequence](../Individuals/Monotone%20Sequences.md)  with non-negative terms. Then the following are equivalent:
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
 > \[!example\] Ex: [P-series test verification](../Individuals/Cauchy's%20Condensation%20Test.md)
 > The series $\dsumoinf \dfrac{1}{n^p}$ converges iff $p > 1$.
 > 
 > * Assume that $p > 0$. Then, $\dfrac{1}{n^p}$ is decreasing. By Cauchy's Condensation Test, the series $\dsumoinf \dfrac{1}{n^p}$ converges iff the series $\dsumzinf 2^n\dfrac{1}{(2^n)^p}$ converges. Observe that
 >   $$2^n\dfrac{1}{(2^n)^p} = 2^{-np+n} = 2^{-(p-1)n} = \Big( \dfrac{1}{2^{p-1}}\Big)^n$$
 >   The geometric series $\dsumzinf \bigg(/dfrac{1}{2^{p-1}}/bigg)^n$ converges iff $/dfrac{1}{2^{p-1}} /< 1$ ([geometric series test](../Individuals/Geometric%20Series%20Test.md#691af3)), which is equivalent to $p>1$.
 > * If $p\le0$, then $\dfrac{1}{n^p} = n^{-p} \not\to 0$, therefore the series $\dsumoinf \dfrac{1}{n^p}$ diverges.

^fd4b54

**Tags:** #Theorem #Analysis/Series #Course/FPM

 > 
 > \[!Theorem\]+ Thm: [Alternating Series Test](../Individuals/Alternating%20Series%20Test.md)
 > Let $(b_n)\_{n\in\N}$ be a **Decreasing** sequence of non-negative real numbers that converges to zero. Then the series
 > $$\dsumoinf (-1)^{n-1}b_n$$
 > converges.

^117376

 

**Tags:** #Theorem #Analysis/Series #Course/FPM

 > 
 > \[!Theorem\]+ Thm: [Integral Test](../Individuals/Integral%20Test.md)
 > Suppose that $f:\[1,\infty)\to\R$ is non-negative and decreasing on $\[1,\infty)$. Let $a_k = f(k), k = 1,2,3,\dots$. Then, $\dsumoinf a_k = \dsumoinf f(k)$ converges iff the improper integral
 > $$\int^{\infty}\_1 f(x)dx \< \infty$$ 

^cdb867

**Tags:** #Analysis/Series #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Monotone Convergence Theorem](../Individuals/Monotone%20Convergence%20Theorem.md)
 > If a sequence of real numbers $(s/_{n})$ is increasing and bounded above, or decreasing and bounded below, then $(s/_{n})$ is convergent (and converges to the [supremum/infinum](../Individuals/Bounds,%20Suprema%20and%20Infima.md#35189a) of the set ${x\_{n},\vert,n\in\N}$ respectively).

^f88f95

**Tags:** #Analysis/Series #Theorem #Course/FPM 

 > 
 > \[!Theorem\]+ Thm: [Geometric Series Test](../Individuals/Geometric%20Series%20Test.md)
 > Assume that $a$ and $r$ are non-zero real numbers. Then
 > $$\displaystyle\sum\_{n=1}^{\infty} a\cdot r^k = \begin{cases}
 > \\dfrac{a}{1-r} &\text{if } \lvert r \rvert \< 1 \\
 > \\text{diverges} &\text{if } \lvert r \rvert \ge 1
 > \\end{cases}
 > $$
 > Notice that $a$ is always the first term in the series, and $r$ is the *common ratio*

^691af3
