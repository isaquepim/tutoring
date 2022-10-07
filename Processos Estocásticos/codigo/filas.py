from scipy.stats import expon
import numpy as np

class Fila:

    def __init__(self,lamb, mu) -> None:

        self.clients = 1
        self.lamb = lamb
        self.inv_lamb = 1/lamb
        self.mu = mu
        self.inv_mu = 1/mu

    def simulate(self):

        tempo_total = expon.rvs(scale = self.inv_lamb)
        t_lamb = expon.rvs(scale = self.inv_lamb)
        t_mu   = expon.rvs(scale = self.inv_mu)

        N_clients = 0

        while self.clients > 0:
            if t_lamb < t_mu:
                self.clients += 1
                tempo_total += t_lamb
                t_mu -= t_lamb
                t_lamb = expon.rvs(scale = self.inv_lamb)

            else:
                self.clients -= 1
                tempo_total += t_mu
                t_lamb -= t_mu
                t_mu = expon.rvs(scale = self.inv_mu)

                N_clients += 1

        self.clients = 1
        return [tempo_total, N_clients]

    def run(self, N_sim):

        values = np.array([self.simulate() for _ in range(N_sim)])

        print('---SIMULAÇÕES---')
        print(f'\t Tempo médio de retorno: {values[:,0].mean():.2f}')
        print(f'\t Desvio padrão do tempo de retorno: {values[:,0].std():.2f}')
        print(f'\t Média de clientes atendidos: {values[:,1].mean():.2f}')
        print()
        print(f'---RESULTADOS TEÓRICOS---')
        print(f'\t Tempo médio de retorno = {1/(self.lamb*(1-self.lamb/self.mu))}')
        print(f'\t Média de clientes atendidos = {self.mu * (1/(self.lamb*(1-self.lamb/self.mu))-1/self.lamb):.2f}')
        

def main():
    lamb = 0.6
    mu = 3.6

    N_sim = 1000

    fila = Fila(lamb=lamb, mu=mu)
    fila.run(N_sim)



if __name__ == '__main__':
    main()