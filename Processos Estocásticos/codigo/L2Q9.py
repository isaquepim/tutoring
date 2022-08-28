from random import random
from scipy.stats import norm, beta
from math import sqrt, sin, asin

import matplotlib.pyplot as plt
import numpy as np

def experimento(debug = False):
    P = [[0.3,0.2,0.5],
         [0.5,0.1,0.4],
         [0.0,0.0,1.0]]
    
    state = 0
    t = 0

    while state != 2:
        x = random()
        accum = 0
        for idx, p in enumerate(P[state]):
            if x < (accum + p):
                state = idx
                break
            accum += p
        t += 1
        if debug:print(state, t)
    
    if t % 2:
        return 1
    return 0

def wald_interval(p_hat, n, alpha):
    z = norm.ppf(1-alpha/2)
    return (p_hat - z*sqrt(p_hat*(1-p_hat)/n), p_hat + z*sqrt(p_hat*(1-p_hat)/n))

def main() -> None:
    n_sim = 100000

    soma = 0
    for _ in range(n_sim):
        soma += experimento()

    p_hat = soma/n_sim
    print(f'Estimador de p: {p_hat:.5f}')
    print(f'Valor real de p: {90/133:.5f}')
    wald = wald_interval(p_hat, n_sim, 0.05)
    print(f'Intervalo de confiança de Wald: ({wald[0]:.5f},{wald[1]:.5f})')

if __name__ == '__main__':
    #print(experimento(True))
    main()