#  GhostHop v2.0 - Proxy Rotation Tool

**GhostHop** é uma ferramenta de rotação dinâmica de tráfego escrita em Python. 
Ela permite distribuir requisições entre múltiplos nós (servidores) de forma sequencial (Round Robin), ideal para testes de carga e estudos de redes.

##  Funcionalidades
- **Giro de 10 nós**: Suporta múltiplos servidores de saída.
- **Interface ASCII**: Banner personalizado em vermelho brilhante.
- **Multi-thread**: Capaz de lidar com várias conexões simultâneas.

##  Instalação (Kali Linux / Windows)
```bash
git clone [https://github.com/seu-usuario/ghosthop.git](https://github.com/seu-usuario/ghosthop.git)
cd ghosthop
pip install .


## Como usar
-basta apenas q vc digite no terminal:ghosthop --port 8080