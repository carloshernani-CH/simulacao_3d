# simulacao

APS4

Integrantes:

- Carlos Hernani
- Pedro Fardin

Se você vai *desenvolver* deste repositório, vá para o [guia de desenvolvimento](README_DEV.md).

## Instalando simulacao:

Lembre-se de seguir essas instruções de dentro do seu ambiente virtual preferido:

    conda create -n simulacao python=3.11
    conda activate simulacao

A primeira maneira é clonar o repositório e fazer uma instalação local:

    git clone https://github.com/carloshernani-CH/simulacao_3d.git
    cd simulacao_3d
    pip install .

A segunda maneira é instalar diretamente

    pip install git+https://github.com/carloshernani-CH/simulacao_3d.git

Para desinstalar, use:

    pip uninstall install simulacao

## Uso

Para encontrar todos os comandos implementados, execute:

    simulacao-cli --help

Para iniciar a simulação, execute:

    simulacao-cli run

### Controles da simulação:

- **Barra de espaço**: Alterna entre os objetos 3D (cubo e pirâmide)
- **Seta para cima**: Aumenta a velocidade de rotação do objeto atual
- **Seta para baixo**: Diminui a velocidade de rotação do objeto atual
- **Fechar a janela**: Encerra a simulação

