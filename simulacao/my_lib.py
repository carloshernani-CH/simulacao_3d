import numpy as np
import pygame
from math import sin, cos

class Figura3D:
    def __init__(self):
        self.pontos = self._criar_pontos()
        self.conexoes = self._criar_conexoes()
        self.rotacao = [0, 0, 0]
        self.velocidade_rotacao = [0.02, 0.02, 0.02]
        self.posicao = np.array([0, 0, -5])

    def _criar_pontos(self):
        return np.array([
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
        ])

    def _criar_conexoes(self):
        return [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

    def _matriz_rotacao(self, eixo, angulo):
        if eixo == 'x':
            return np.array([
                [1, 0, 0],
                [0, cos(angulo), -sin(angulo)],
                [0, sin(angulo), cos(angulo)]
            ])
        elif eixo == 'y':
            return np.array([
                [cos(angulo), 0, sin(angulo)],
                [0, 1, 0],
                [-sin(angulo), 0, cos(angulo)]
            ])
        else:  # eixo z
            return np.array([
                [cos(angulo), -sin(angulo), 0],
                [sin(angulo), cos(angulo), 0],
                [0, 0, 1]
            ])

    def _projetar(self, ponto):
        z = max(ponto[2], 0.1)
        fator = 2 / (2 + z)
        return np.array([ponto[0] * fator, ponto[1] * fator])

    def _transformar(self, ponto):
        for eixo, angulo in zip(['x', 'y', 'z'], self.rotacao):
            ponto = np.dot(self._matriz_rotacao(eixo, angulo), ponto)
        return ponto + self.posicao

    def atualizar(self):
        self.rotacao = [r + v for r, v in zip(self.rotacao, self.velocidade_rotacao)]

    def desenhar(self, superficie):
        pontos_2d = []
        for ponto in self.pontos:
            transformado = self._transformar(ponto)
            projetado = self._projetar(transformado)
            pontos_2d.append(projetado * 150 + np.array([300, 300]))

        for inicio, fim in self.conexoes:
            pygame.draw.line(superficie, (255, 255, 255), pontos_2d[inicio], pontos_2d[fim], 2)

        for ponto in pontos_2d:
            pygame.draw.circle(superficie, (255, 0, 0), ponto.astype(int), 4)

class Piramide(Figura3D):
    def _criar_pontos(self):
        return np.array([
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
            [0, 0, 1]
        ])

    def _criar_conexoes(self):
        return [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (0, 4), (1, 4), (2, 4), (3, 4)
        ]

def executar_simulacao():
    pygame.init()
    tela = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Simulação 3D")
    relogio = pygame.time.Clock()

    objetos = [Figura3D(), Piramide()]
    objeto_atual = 0

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    objeto_atual = (objeto_atual + 1) % len(objetos)

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            objetos[objeto_atual].velocidade_rotacao = [v * 1.1 for v in objetos[objeto_atual].velocidade_rotacao]
        if teclas[pygame.K_DOWN]:
            objetos[objeto_atual].velocidade_rotacao = [v * 0.9 for v in objetos[objeto_atual].velocidade_rotacao]

        tela.fill((0, 0, 0))
        objetos[objeto_atual].atualizar()
        objetos[objeto_atual].desenhar(tela)
        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()

if __name__ == "__main__":
    executar_simulacao()
