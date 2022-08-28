from random import random
from scipy.stats import norm, beta
from math import sqrt, sin, asin

import matplotlib.pyplot as plt
import numpy as np


def experimento():
    P = [[1.0, 0.0, 0.0, 0.0],
         [0.1, 0.2, 0.5, 0.2],
         [0.1, 0.2, 0.6, 0.1],
         [0.2, 0.2, 0.3, 0.3]]
    
    state = 1

    while state not in [0,2]:
        x = random()

        accum = 0
        for idx, p in enumerate(P[state]):
            if x < (accum + p):
                state = idx
                break
            accum += p
    if state:
        return 0
    return 1 

def wald_interval(p_hat, n, alpha):
    z = norm.ppf(1-alpha/2)
    return (p_hat - z*sqrt(p_hat*(1-p_hat)/n), p_hat + z*sqrt(p_hat*(1-p_hat)/n))

def agresti_coull(n, ns, alpha):
    z = norm.ppf(1-alpha/2)
    n_ = n + z*z
    p_ = (1/n_)*(ns + z*z/2)
    return (p_ - z*sqrt(p_*(1-p_)/n_), p_ + z*sqrt(p_*(1-p_)/n_))

def arcsine_interval(p_hat, n, alpha):
    z = norm.ppf(1-alpha/2)
    return (sin(asin(sqrt(p_hat))-z/(2*sqrt(n)))**2, sin(asin(sqrt(p_hat))+z/(2*sqrt(n)))**2)

def posterior_jeffrey(n, ns):
    a = ns + 0.5
    b = n - ns + 0.5

    fig, ax = plt.subplots(1, 1)
    x = np.linspace(beta.ppf(0.01, a, b),
                beta.ppf(0.99, a, b), 100)
    ax.plot(x, beta.pdf(x, a, b),
       'r-', lw=5, alpha=0.6)
    plt.show()







def main() -> None:

    n_sim = 1000

    soma = 0
    for _ in range(n_sim):
        soma += experimento()

    p_hat = soma/n_sim
    wald = wald_interval(p_hat, n_sim, 0.05)
    a_coull = agresti_coull(n_sim, soma, 0.05)
    arcsin = arcsine_interval(p_hat, n_sim, 0.05)

    print(f'Probabilidade estimada: {p_hat}')
    print(f'Intervalo de confiança de Wald: ({wald[0]:.5f},{wald[1]:.5f})')
    print(f'Intervalo de confiança Agresti-Coull: ({a_coull[0]:.5f},{a_coull[1]:.5f})')
    print(f'Intervalo de confiança com Arco-seno: ({arcsin[0]:.5f},{arcsin[1]:.5f})')

    posterior_jeffrey(n_sim, soma)


if __name__ == '__main__':
    main()