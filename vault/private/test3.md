Prove that $\displaystyle\sum_{n=0}^{\infty} \frac{f^n(0)}{n!} x^n$ converges to $f(x)$ in $[-1,1]$

Equivalent to
$\displaystyle\lim_{n \to \infty} \sum_{n=0}^{n} \frac{f^k(0)}{k!} x^k + R_{n}(x)$ converges to $\displaystyle\sum_{n=0}^{\infty} \frac{f^k(0)}{k!} x^k$
Equivalent to
$$\displaystyle\lim_{n \to \infty} R_{n}(x) \to 0$$
Equivalent to
$$\lim_{n \to \infty} \frac{f^{n+1}(c)}{(n+1)!}x^{n+1} \to 0$$
Since
$$\lvert f^n(x) \rvert \le M$$
This means that
$$\frac{f^{n+1}(c)}{(n+1)!}x^{n+1} \leq \frac{M}{(n+1)!}x^{n+1}$$
$$\frac{Mx^{n+1}}{(n+1)!}\to 0$$
$$\left\lvert  \frac{\frac{Mx^{n+2}}{(n+2)!}}{\frac{Mx^{n+1}}{(n+1)!}} \right\rvert \implies \left\lvert \frac{(n+1)!Mx^{n+2}}{(n+2)!Mx^{n+1}} \right\rvert \implies \left\lvert  \frac{x}{n+2}  \right\rvert $$
Since $s \in [-1,1]$ this means that the limit obviously goes to $0$
Therefore, $R_{N}(x)$ converges to $0$

Therefore the limit converges to $f(x)$ as $$\displaystyle\lim_{n \to \infty}\sum_{n=0}^{n} \frac{f^k(0)}{k!}x^k+R_{n}(x) \to \sum_{n=0}^{\infty} \frac{f^k(0)}{k!}x^k = f(x)$$

Infinite diff => continuous

If $f^n(x)$ $n$ is the amount of times derived
then $f(x)$ is where $n=0$. So therefore $A^n$ would have to be $A^0=1$

Sinx -> cosx -> -sinx -> -cosx etc etc
this is all bounded by $[-1,1]$
$\lvert f^n(x) |$ is bounded as well by 
$$0 \leq \lvert f^n(x) \rvert \le 1 \le A^n$$
therefore an exmaple of a function that satisfies the hypothesis is $f(x) = \sin(x)$
