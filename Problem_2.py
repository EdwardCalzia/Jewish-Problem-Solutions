import sympy as sp

def g(x):
    return (x**2 - 3*x)/(x - 3)

x = sp.Symbol('x')
a = 3 + sp.Rational(1, 100)

pw = sp.Piecewise((x, x > 0), (-x, x < 0), (0, True))

f = pw.subs(x, x - a) - pw.subs(x, x + a)
f = sp.simplify(f)
s = sp.series(g(x)*f, x, x0=3, n=6)
print(s)

