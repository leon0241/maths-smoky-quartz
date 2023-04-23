$$\left[\begin{matrix}
1&1&1&1 \\
\beta_{1}&\beta_{2}&\beta_{3}&b_{4} \\
(\beta_{1})^{2}&(\beta_{2})^{2}&(\beta_{3})^{2}&(\beta_{4})^{2} \\
(\beta_{1})^{3}&(\beta_{2})^{3}&(\beta_{3})^{3}&(\beta_{4})^{3} \\
(\beta_{1})^{4}&(\beta_{2})^{4}&(\beta_{3})^{4}&(\beta_{4})^{4} \\
\end{matrix}\right]\left[\begin{matrix}
0 \\
1 \\
0 \\
0 \\
0
\end{matrix}\right]$$
i.e.
$$\begin{align}
\alpha_{1}+\alpha_{2}+\alpha_{3}+\alpha_{4}&=0 \\
\beta_{1}\alpha_{1}+\beta_{2}\alpha_{2}+\beta_{3}\alpha_{3}+\beta_{4}\alpha_{4}&=1 \\
\beta_{1}^{2}\alpha_{1}+\beta_{2}^{2}\alpha_{2}+\beta_{3}^{2}\alpha_{3}+\beta_{4}^{2}\alpha_{4}&=0 \\
\beta_{1}^{3}\alpha_{1}+\beta_{2}^{3}\alpha_{2}+\beta_{3}^{3}\alpha_{3}+\beta_{4}^{3}\alpha_{4}&=0 \\
\beta_{1}^{4}\alpha_{1}+\beta_{2}^{4}\alpha_{2}+\beta_{3}^{4}\alpha_{3}+\beta_{4}^{4}\alpha_{4}&=0 \\
\end{align}
$$
This fits into
$$F'(x)\approx \frac{1}{\Delta x}\sum_{i=1}^{N}a_{i}F(x+b_{i}\Delta x)$$

#### *Ex: centered difference approximation,*
$$N=2,\quad \begin{cases}
\alpha_{1}=\frac{1}{2},\quad&\alpha_{2}=-\frac{1}{2}, \\
\beta_{1}=1,\quad &\beta_{2}=-1,
\end{cases}
$$
$$\text{Therefore},\, F'(x)\approx \frac{1}{2\Delta x}(F(x+\Delta x) - F(x - \Delta x))$$
To get the values of $\alpha$ from $\beta$, we sub into the matrix
$$\left[\begin{matrix}
1&1 \\
1&-1
\end{matrix}\right]\left[\begin{matrix}
0 \\
1
\end{matrix}\right]$$
Linear solving gives:
$$[\alpha_{1},a_{2}] = \left[ -\frac{1}{2}, \frac{1}{2} \right]$$
Why does 
$$\alpha_{1}\beta_{1}+\alpha_{2}\beta_{2}=1 \implies F'(x)\approx \frac{1}{\Delta x}\sum_{i=1}^{N}a_{i}F(x+b_{i}\Delta x)\text{ is N-1 order accurate}$$
