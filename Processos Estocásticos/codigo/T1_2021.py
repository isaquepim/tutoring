from random import random
from scipy.stats import norm, beta
from math import sqrt, sin, asin

import matplotlib.pyplot as plt
import numpy as np


def experimento_b():

    P = [[0.2, 0.4, 0.2, 0.2],
        [0.3, 0.3, 0.3, 0.1],
        [0.0, 0.0, 0.4, 0.6],
        [0.0, 0.0, 0.8, 0.2]]

    state = 0

    while state == 0:
        x = random()

        accum = 0
        for idx, p in enumerate(P[state]):
            if x < (accum + p):
                state = idx
                break
            accum += p

    if state == 1:
        return 0
    return 1

def experimento_c():
    P = [[0.2, 0.4, 0.2, 0.2],
        [0.3, 0.3, 0.3, 0.1],
        [0.0, 0.0, 0.4, 0.6],
        [0.0, 0.0, 0.8, 0.2]]

    state = 0

    while state not in [2,3]:
        x = random()

        accum = 0
        for idx, p in enumerate(P[state]):
            if x < (accum + p):
                state = idx
                break
            accum += p

    if state == 2:
        return 1
    return 0


def wald_interval(p_hat, n, alpha):
    z = norm.ppf(1-alpha/2)
    return (p_hat - z*sqrt(p_hat*(1-p_hat)/n), p_hat + z*sqrt(p_hat*(1-p_hat)/n))

def main() -> None:
    n_sim = 100000

    soma = 0 
    for _ in range(n_sim):
        soma += experimento_c()
    
    p_hat_b = soma/n_sim
    wald = wald_interval(p_hat_b, n_sim, 0.05)

    print(f'Valor verdadeiro: {0.5}')
    print(f'Estimativa do item b: {p_hat_b}')
    print(f'Intervalo de confiança de Wald: ({wald[0]:.5f},{wald[1]:.5f})')


    print('-'*30)
    soma = 0 
    for _ in range(n_sim):
        soma += experimento_c()
    
    p_hat_c = soma/n_sim
    wald = wald_interval(p_hat_c, n_sim, 0.05)

    print(f'Valor verdadeiro: {13/22:.5f}')
    print(f'Estimativa do item b: {p_hat_c}')
    print(f'Intervalo de confiança de Wald: ({wald[0]:.5f},{wald[1]:.5f})')





if __name__ == '__main__':
    main()