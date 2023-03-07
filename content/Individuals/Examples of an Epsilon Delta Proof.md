---
---

**Tags:** #Collection #Analysis/Proofs #Course/FPM 

**Tags:** #Definition #Analysis/Proofs #Course/FPM 

 > 
 > \[!Definition\]+ Def: [Epsilon Delta Function Limits](Epsilon%20Delta%20Function%20Limits.md)
 > Let $f:A\to\R$ and let $c$ be a limit point of $A$. Then we say that
 > $$\displaystyle\lim\_{x \to c} f(x) = L$$
 > if for all $\epsilon>0$ there exists some $\delta>0$ such that for every $x\in A$ for which $0\<\\lvert x-c \rvert\<\\delta$, we have
 > $$\lvert f(x)-L \rvert\<\\epsilon $$
 > We also say $\displaystyle\lim\_{x \to c}f(x)$ *converges* to L in such a situation

^e6f084

^87727d

 > 
 > \[!Remark\]+ Rem: [Domain Requirement](Epsilon%20Delta%20Function%20Limits.md)
 > The reason we require that $x\in A$ is just so that $f(x)$ makes sense, since $f:A\to R$, so if $x\not\in A$ then $f(x)$ is not even defined. (Note that we never take $f(c)$ so that's why it's ok if $c\not\in A$).

 > 
 > \[!Remark\]+ Rem: [Approach requirement](Epsilon%20Delta%20Function%20Limits.md)
 > The reason why we require $0\<\\lvert x-c \rvert$ (i.e. $x\ne c$) is because limits only care about what happens as you *approach* the point $c$, and not about what actually happens at the point $c$. $f(c)$ is able to not even be in the domain and the limit would be unaffected. For example, the chart below can still approach $\lim\_{x \to 2}f(x)=1$ even if $f(2) \ne 1$
 > 
 > ````tikz
 > \begin{document}
 > 	\begin{tikzpicture}[domain=0:4,scale=1.5]
 > 		\draw[very thin,color=gray] (-0.1,-0.3) grid (4.2,2.5);
 > 		\draw[->] (-0.2,0) -- (4.2,0) node[right] {$x$};
 > 		\foreach \x in {1,2,3,4}
 > 			\draw (\x cm,1pt) -- (\x cm,-1pt) node[anchor=north] {$\x$};
 > 		\draw[->] (0,-0.3) -- (0,2.5) node[above] {$y$};
 > 		\foreach \y in {1,2}
 > 		    \draw (1pt,\y cm) -- (-1pt,\y cm) node[anchor=east] {$\y$};
 > 		\draw[color=green]    plot (\x,\x/2)             node[right] {$f(x) $};
 > 		\node[circle,draw, scale=0.7] (c) at (2,1){};
 > 		\node[circle,fill,draw, scale=0.7] (c) at (2,2){};
 > \end{tikzpicture}
 > \end{document}
 > ````

 > 
 > \[!Remark\]+ Rem: [Omittance of the first two conditions](Epsilon%20Delta%20Function%20Limits.md)
 > When the context is clear, for convenience we do not always explicitly state the conditions $x \in A$ and $0\< \lvert x-c \rvert$.

 > 
 > \[!Remark\]+ Rem: [Visualising the epsilon delta limit](Epsilon%20Delta%20Function%20Limits.md)
 > For a fixed $\epsilon$ distance away from $L$, we want to find a $\delta$ such that the range of a fixed $\delta$ distance away from $c$ is contained within the range of $\epsilon$
 > 
 > ![Pasted image 20230304182042.png](..\Images\Pasted%20image%2020230304182042.png)
 > We can also define uniform continuity as having a consistent $\delta$ for an $\epsilon$ on any point on a graph. You can see that if the point was moved to the left, the bounds for the size of $\delta$ would shrink. This is not covered on the course however, so it does not matter in this context.

 > 
 > \[!Example\]+ [Example 1: ](Examples%20of%20an%20Epsilon%20Delta%20Proof.md) Let $f(x)=5x+2$. Prove $\displaystyle\lim\_{x \to 3}f(x)=17$
 > Let $\epsilon>0$. We are assuming that $\lvert x-3 \rvert \< \delta$ for whatever $\delta$ we choose. Assume that the conclusion holds,
 > $$\lvert f(x)-L \rvert \< \epsilon $$
 > And then we can substitute to try and unwind this statement to reach the $\delta$ statement above. If we can do this then we can claim that a $\delta$ can be found for every $\epsilon$.
 > $$\begin{align}
 > \\lvert f(x)-L \rvert &\<\\epsilon \\
 > \\lvert 5x+2-(15+2) \rvert &\<\\epsilon \\
 > \\lvert 5x-15 \rvert &\<\\epsilon \\
 > 5\cdot\lvert x-3 \rvert &\<\\epsilon \\
 > \\lvert x-3 \rvert &\<\\frac{\epsilon}{5} \\
 > \\end{align}
 > $$
 > From this, we now have a statement that looks the same as $\lvert x-3 \rvert\<\\delta$. So, therefore we can let $\delta= \displaystyle\frac{\epsilon}{5}$ and then rewrite the above to formally prove that the statement is true.
 > 
 > **Proof:** Let $\epsilon>0$, and let $\delta=\frac{\epsilon}{5} > 0$. Then for any $x$ where $0\<\\lvert x-3 \rvert \< \delta$,
 > $$\begin{align}
 > \\lvert f(x)-L \rvert &= \lvert 5x+2 - (15+2) \rvert \\
 > &= \lvert 5x-15 \rvert  \\
 > &= 5\cdot\lvert x-3 \rvert  \\
 > &\<5\cdot\delta \\
 > &=5\cdot \frac{\epsilon}{5} \\
 > &= \epsilon
 > \\end{align}
 > $$

 > 
 > \[!Example\]+ [Example 2: ](Examples%20of%20an%20Epsilon%20Delta%20Proof.md) For $f(x)=\displaystyle\frac{3x^{2}-12}{x-2}$, Prove $\displaystyle\lim\_{x \to 2}f(x)=12$
 > We are trying to reach $\lvert x-2 \rvert\<\\delta$. Same as above, substitute and unwind the statement
 > $$\begin{align}
 > \\lvert f(x)-L \rvert &\< \epsilon \\
 > \\left\lvert  \displaystyle \frac{3x^{2}-12}{x-2}-12 \right\rvert  & \< \epsilon \\
 > \\left\lvert  \frac{3(x-2)(x+2)}{x-2} \right\rvert  & \<\\epsilon \\
 > \\lvert 3(x+2) - 12\rvert  & \<\\epsilon \\
 > 3\cdot\lvert (x+2)-4 \rvert &\<\\epsilon \\
 > 3\cdot\lvert x-2 \rvert & \<\\epsilon \\
 > \\lvert x-2 \rvert \< \frac{\epsilon}{3} \\
 > \\end{align}
 > $$
 > Therefore since we have reached $\lvert x-2 \rvert$, we can let $\delta= \frac{\epsilon}{3}$.
 > 
 > **Proof:** Let $\epsilon>0$, and let $\delta= \frac{\epsilon}{3}>0$. Then for any $x$ where $0\<\\lvert x-2 \rvert\<\\delta$,
 > $$\begin{align}
 > \\lvert f(x)-L \rvert &= \left\lvert  \frac{3x^{2}-12}{x-2}-12  \right\rvert  \\
 > &=\left\lvert  \frac{3(x-2)(x+2)}{x-2}-12 \right\rvert  \\
 > &= \lvert 3(x+2)-12 \rvert \\
 > &=3\cdot\lvert (x+2)-4 \rvert \\
 > &=3\cdot \lvert x-2 \rvert \\
 > &\<3\cdot\delta \\
 > &=3\cdot \frac{\epsilon}{3} \\
 > &=\epsilon
 > \\end{align}
 > $$

 > 
 > \[!Example\]+ [Example 3:](Examples%20of%20an%20Epsilon%20Delta%20Proof.md) For $f(x)=x^{2}$, Prove $\displaystyle\lim\_{x \to 2}f(x)=4$
 > We are trying to reach $\lvert x-2 \rvert \< \delta$. Substitute and unwind:
 > $$\begin{align}
 > \\lvert f(x)-L \rvert &\< \epsilon \\
 > \\lvert x^{2}-4 \rvert &\< \epsilon \\
 > \\lvert x+2 \rvert \lvert x-2 \rvert &\< \epsilon
 > \\end{align}
 > $$
 > Now, we need an upper bound for $\lvert x+2 \rvert$ to know how small to choose $\delta$. Since we are discussing the limit as $x$ approaches $2$, we can use a process similar to choosing a fittingly large $n$ to show a sequence will eventually converge to a certain point. If we agree that our $\delta$ neighbourhood (denoted by $V\_{\delta}(c)$) around $c=2$ must have radius no bigger than $\delta=1$, then we can get an upper bound of
 > $$\lvert x+2 \rvert \le \lvert 3+2 \rvert =5\text{, for all } x \in V\_{\delta}(c)$$
 > From this, it follows that
 > $$\begin{align}
 > 5\cdot\lvert x-2 \rvert &\<\\epsilon \\
 > \\lvert x-2 \rvert &\< \frac{\epsilon}{5}
 > \\end{align}
 > $$
 > and we can choose $\delta=\min{{1, \epsilon/5}}$. A formal proof can then be written like the examples above.

%%eof%%