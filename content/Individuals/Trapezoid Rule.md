---
---

**Tags:** #Python/Numpy #Definition #Course/CNU 

 > 
 > \[!Definition\]+ Def: [Trapezoid Rule](Trapezoid%20Rule.md)
 > 
 > 1. Choose nodes $x\_{0}=-1, x\_{1}=1$
 > 1. With 2 nodes, the *interpolating polynomial* has degree 1
 > 1. We therefore need the [quadrature rule](Quadrature%20Rules.md) to integrate degree-1 polynomials exactly i.e. to have [degree of precision](Quadrature%20Rules.md) of at least 1
 > 1. Use elementary polynomials of degree 0 and 1 to find the weights

$$\int\_{-1}^{1}f(x)  , dx \approx \displaystyle\sum\_{k=0}^{N-1} W\_{k}f(x\_{k)}$$
We need for $f(x)=p(x)=qx+l,\quad q,,l\in\R,\quad \displaystyle\int\_{-1}^{1} f(x) , dx=\displaystyle\sum\_{k=0}^{1}W\_{k}f(x\_{k})$
We need this to be true for $p(x)=1$ and $p(x)=x$
$p(x)=1$ (degree 0)
$$\int\_{-1}^{1} 1 , dx =\displaystyle\sum\_{k=0}^{1} W\_{k} p(x\_{k}) \implies 2 = W\_{0}p(-1)+w\_{1}p(1)=w\_{0}+w\_{1}$$
$p(x)=x$ (degree 1)
$$\int\_{-1}^{1} x , dx =w\_{0}p(-1)+w\_{1}p(1)\implies 0=-wp\_{0}+w\_{1}$$
$$\implies w\_{0}=w\_{1}=1 \text{ is the weights for trapezoid rule}$$
$\implies$for arbitrary f(x), $\displaystyle\int\_{-1}^{1} f(x) , dx \approx f(-1)+f(1)$
