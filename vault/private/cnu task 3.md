
$$(1)\qquad u_{0}^2 y''(x)=-g\left(1-e^{-(y(x)-a)/b}\right)-\kappa u_{0} y'(x)$$
$$(2a)\qquad y'(x)\approx \frac{y_{n+1} - y_{n-1}}{2\Delta x}$$
$$(2b)\qquad y''(x)\approx \frac{y_{n+1}-2y_{n}+y_{n-1}}{\Delta x^2}$$
modified 1
$$\begin{align}
u_{0}^2 y''(x) &=-g\left(1-e^{-(y(x)-a)/b}\right)-\kappa u_{0} y'(x) \\
\frac{u_{0}^2(y_{n+1}-2y_{n}+y_{n-1})}{\Delta x^2}&\approx -g\left(1-e^{-(y_{n}-a)/b}\right) - \frac{\kappa u_{0}(y_{n+1}-y_{n-1})}{2\Delta x} \\
\frac{u_{0}^2y_{n+1}}{\Delta x^2} + \frac{\kappa u_{0}y_{n+1}}{2\Delta x} &\approx -g\left(1-e^{-(y_{n}-a)/b}\right) + \frac{\kappa u_{0}(y_{n-1})}{2\Delta x}-\frac{u_{0}^2(-2y_{n}+y_{n-1})}{\Delta x^2} \\
\frac{2u_{0}^2y_{n+1} + \Delta x \kappa u_{0}y_{n+1}}{2\Delta x^{2}} &\approx -g\left(1-e^{-(y_{n}-a)/b}\right) + \frac{\kappa u_{0}(y_{n-1})}{2\Delta x}-\frac{u_{0}^2(-2y_{n}+y_{n-1})}{\Delta x^2} \\
\frac{y_{n+1}(2u_{0}^2 + \Delta x \kappa u_{0})}{2\Delta x^{2}} &\approx -g\left(1-e^{(-y_{n}-a)/b}\right) + \frac{\kappa u_{0}(y_{n-1})}{2\Delta x}-\frac{u_{0}^2(-2y_{n}+y_{n-1})}{\Delta x^2} \\
y_{n+1}(2u_{0}^2 + \Delta x \kappa u_{0}) &\approx -2\Delta x^{2}g\left(1-e^{-(y_{n}-a)/b}\right) + \kappa \Delta x u_{0}(y_{n-1})-2u_{0}^2(-2y_{n}+y_{n-1}) \\
y_{n+1}(u_{0}(2u_{0} + \Delta x \kappa)) &\approx -2\Delta x^{2}g\left(1-e^{-(y_{n}-a)/b}\right) + u_{0}(\kappa \Delta x(y_{n-1})-2u_{0}(-2y_{n}+y_{n-1})) \\
y_{n+1} &\approx \frac{-2\Delta x^{2}g\left(1-e^{-(y_{n}-a)/b}\right)}{u_{0}(2u_{0} + \Delta x \kappa)} + \frac{u_{0}(\kappa \Delta x(y_{n-1})-2u_{0}(-2y_{n}+y_{n-1}))}{u_{0}(2u_{0} + \Delta x \kappa)} \\
y_{n+1} &\approx \frac{-2\Delta x^{2}g\left(1-e^{-(y_{n}-a)/b}\right)}{u_{0}(2u_{0} + \Delta x \kappa)} + \frac{\kappa \Delta x(y_{n-1})-2u_{0}(-2y_{n}+y_{n-1}))}{2u_{0} + \Delta x \kappa}
\end{align}
$$
- $y_{0} = u_{0}$

$$\begin{align}
y''(0) &\approx 2 \frac{y_{1}-y_{0}}{\Delta x^{2}} & \implies y''(0)\Delta x^{2} \approx 2(y_{1}-y_{0})\\
&\implies \frac{y''(0)\Delta x^{2}}{2}\approx y_{1}-y_{0} \\
&\implies y_{1}\approx \frac{y''(0)\Delta x^{2}}{2} + y_{0}
\end{align}$$
From (1),
$$u_{0}^2 y''(x)=-g\left(1-e^{-(y(x)-a)/b}\right)-\kappa u_{0} y'(x)$$
Therefore:
$$y''(x)=\frac{-g\left(1-e^{-(y(x)-a)/b}\right)-\kappa u_{0} y'(x)}{u_{0}^2}$$

Substituting into the equation:
$$\begin{align}
y_{1} &\approx \frac{\Delta x^{2}\left(-g\left(1-e^{-(y(0)-a)/b}\right)-\kappa u_{0} y'(0)\right)}{2u_{0}^{2}} +y_{0} \\
y_{1} &\approx \frac{-\Delta x^{2} g\left(1-e^{-(y_{0}-a)/b}\right)}{2u_{0}^{2}} +y_{0}
\end{align}
$$
Therefore:
$$\begin{align}
y_{0}&\approx y_{0} \\
y_{1}&\approx \frac{-\Delta x^{2} g\left(1-e^{-(y_{0}-a)/b}\right)}{2u_{0}^{2}} +y_{0}\\
y_{n+1} &\approx \frac{-2\Delta x^{2}g\left(1-e^{-(y_{n}-a)/b}\right)}{u_{0}(2u_{0} + \Delta x \kappa)} + \frac{\kappa \Delta x(y_{n-1})-2u_{0}(-2y_{n}+y_{n-1}))}{2u_{0} + \Delta x \kappa}
\end{align}
$$
