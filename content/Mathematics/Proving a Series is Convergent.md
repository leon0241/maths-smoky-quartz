---
---

**Tags:** #Collection #Analysis/Series #Course/FPM


 > 
 > \[!Theorem\]+ Thm: [Divergence Test](../Individuals/Divergence%20Test.md)
 > 
 > * If $(a_n)\_{n\in\N}$ converges, then $a_n\to0$.
 > * If $(a_n)\_{n\in\N}$ doesn't converge to $0$, then $\dsumoinf a_n$ diverges.
 > * The converse is not true! $a_n\to0$ does not imply $\dsumoinf a_n$ converges



 > 
 > \[!Theorem\]+ Thm: [Bounded Theorem](../Individuals/Bounded%20Theorem.md)
 > Let $(a_n)\_{n\in\N}$ be a sequence with non-negative terms. The following are equivalent:
 > 
 > 1. The series $\dsumoinf a_n$ converges.
 > 1. the sequence $(S_n)\_{n\in\N}$ of partial sums is bounded above.



 > 
 > \[!Theorem\]+ Thm: [Comparison Test](../Individuals/Comparison%20Test.md)
 > Let $(a_n)*{n\in\N}$ and $(b_n)*{n\in\N}$ be two sequences such that $0\leq a_n\leq b_n$ for all n.
 > 
 > 1. If $\sum_n b_n$ converges, then $\sum_n a_n$ converges as well.
 > 1. If $\sum_n a_n$ diverges, then $\sum_n b_n$ diverges as well.



 > 
 > \[!Theorem\]+ Thm: [Limit Comparison Test](../Individuals/Limit%20Comparison%20Test.md)
 > Let $(a_n)*{n\in\N}$ and $(b_n)*{n\in\N}$ be two real sequences with $a_n\geq0$ and $b_n\geq0$ for all n. Assume that $\dfrac{a_n}{b_n} \to L$ for some $L\in(0,\infty)$. Then, $\dsumoinf a_n$ converges iff $\dsumoinf b_n$ converges.



 > 
 > \[!Theorem\]+ Thm: [Root Test](../Individuals/Root%20Test.md)
 > Let $\dsumzinf a_n$ be a series with non-negative terms such that
 > $$\sqrt\[n\]{a_n} \to L$$
 > where $0 \le L \le +\infty$.
 > 
 > * If $0\le L \< 1$ then the series $\dsumzinf a_n$ converges.
 > * If $L > 1$ then the series $\dsumzinf a_n$ diverges.
 > * If $L = 1$, the series may or may not converge



 > 
 > \[!Theorem\]+ Thm: [Ratio Test](../Individuals/Ratio%20Test.md)
 > Let $\dsumzinf a_n$ be a series with positive terms such that $\dfrac{a\_{n+1}}{a_n} \to L$, where $0\le L \le +\infty$.
 > 
 > * If $0\le L \< 1$ then the series $\dsumzinf a_n$ converges.
 > * If $L > 1$ then the series $\dsumzinf a_n$ diverges.
 > * If $L = 1$:
 >   * If $a_n = \dfrac{1}{n}$, then $\dfrac{a\_{n+1}}{a_n} = \dfrac{n}{n + 1} \to 1$, and $\dsumzinf \frac{1}{n}$ diverges.>
 >   * If $a_n = \dfrac{1}{n^2}$, then $\dfrac{a\_{n+1}}{a_n} = \dfrac{n^2}{(n + 1)^2} \to 1$, and $\dsumzinf \frac{1}{n^2}$ converges.



 > 
 > \[!Theorem\]+ Thm: [Cauchy's Condensation Test](../Individuals/Cauchy's%20Condensation%20Test.md)
 > Let $(a_n)/_{n/in/N}$ be a [decreasing sequence](../Individuals/Monotone%20Sequences.md)  with non-negative terms. Then the following are equivalent:
 > 
 > 1. The series $\dsumoinf a_n$ converges 
 > 1. The series $\dsumzinf 2^na\_{2^n}$ converges.



 > 
 > \[!Theorem\]+ Thm: [Alternating Series Test](../Individuals/Alternating%20Series%20Test.md)
 > Let $(b_n)\_{n\in\N}$ be a **Decreasing** sequence of non-negative real numbers that converges to zero. Then the series
 > $$\dsumoinf (-1)^{n-1}b_n$$
 > converges.


 


 > 
 > \[!Theorem\]+ Thm: [Integral Test](../Individuals/Integral%20Test.md)
 > Suppose that $f:\[1,\infty)\to\R$ is non-negative and decreasing on $\[1,\infty)$. Let $a_k = f(k), k = 1,2,3,\dots$. Then, $\dsumoinf a_k = \dsumoinf f(k)$ converges iff the improper integral
 > $$\int^{\infty}\_1 f(x)dx \< \infty$$ 



 > 
 > \[!Theorem\]+ Thm: [Monotone Convergence Theorem](../Individuals/Monotone%20Convergence%20Theorem.md)
 > If a sequence of real numbers $(s/_{n})$ is increasing and bounded above, or decreasing and bounded below, then $(s/_{n})$ is convergent (and converges to the [supremum/infinum](../Individuals/Bounds,%20Suprema%20and%20Infima.md#35189a) of the set ${x\_{n},\vert,n\in\N}$ respectively).



 > 
 > \[!Theorem\]+ Thm: [Geometric Series Test](../Individuals/Geometric%20Series%20Test.md)
 > Assume that $a$ and $r$ are non-zero real numbers. Then
 > $$\displaystyle\sum\_{n=1}^{\infty} a\cdot r^k = \begin{cases}
 > \\dfrac{a}{1-r} &\text{if } \lvert r \rvert \< 1 \\
 > \\text{diverges} &\text{if } \lvert r \rvert \ge 1
 > \\end{cases}
 > $$
 > Notice that $a$ is always the first term in the series, and $r$ is the *common ratio*



