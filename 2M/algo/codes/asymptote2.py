import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(7.5, 8, 1000)
# sig =1 + 2*(x**(1/2) - x) / x**5
# sig =np.cos(x)*np.cos(x)
sig = np.pow(x,2) + np.exp(2,x) + 4


fig, ax = plt.subplots()
#ax.axhline(y=1.0, color="green", linestyle="--")
ax.axvline(color="gray")
#ax.plot(x, sig, color='red', linewidth=2, label=r"$f(x) = 1 + \frac{4 * x^{2} - 1}{x^{4}}$")
ax.plot(x, sig, color='red', linewidth=2)
ax.set(xlim=(0, 10), xlabel="x")
ax.legend(fontsize=14)
plt.show()
