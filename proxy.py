import sys
import os
import logging
from flask import Flask, request
import requests
import argparse
import colorama
from colorama import Fore, Style

# SILENCIADOR DO FLASK
os.environ['WERKZEUG_RUN_MAIN'] = 'true'
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

colorama.init(autoreset=True)
app = Flask(__name__)

SERVIDORES = [f"http://127.0.0.1:{5000 + i}" for i in range(1, 11)]
contador = 0

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    global contador
    indice = contador % len(SERVIDORES)
    alvo = SERVIDORES[indice]
    contador += 1
    print(Fore.CYAN + f"[{indice + 1}/10] " + Fore.YELLOW + f"Saltando via: {alvo}")
    try:
        resposta = requests.get(f"{alvo}/{path}", timeout=3)
        return (resposta.content, resposta.status_code, list(resposta.headers.items()))
    except:
        return f"Erro no nó {indice + 1}", 502

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()

    # O AVIÃO CORRIGIDO (SEM ESPAÇOS SOBRANDO)
    banner = r"""
              _   _
             | | | |
  __ _ _ __   __| | | |
 / _` | '_ \ / _` | | |
| (_| | | | | (_| | |_|
 \__,_|_| |_|\__,_| (_)

             .o+`
            `ooo/
           `+oooo:
          `+oooooo:
         -+oooooo+:
        `/: -:++oooo+:
       `/++++/+++++++:
      `/+++++++++++++++:
     `/+++oooooooooooooo/`
    ./ooossssso++ossssssso+`
   .oossssso-````/ossssss+`
   -ossssso.      :ssssssso.
   :osssssss/      osssso+++.
   /osssssss/      +ssssooo/-
   `/ossssso+/: -   -: /+osssso+-
    `+sso+:-`          `.-/+oso:
     `++: .                   `-/+
      `.
    """
    
    # LIMPA A TELA ANTES DE MOSTRAR
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Fore.LIGHTRED_EX + banner)
    print(Fore.GREEN + f" [+] GhostHop v2.3 | {len(SERVIDORES)} nós ativos")
    print(Fore.RED + " [+] Dev: FOREVER")
    print(Fore.WHITE + " " + "-"*45)
    print(Fore.CYAN + f" [*] Escutando na porta: {args.port}")

    app.run(port=args.port, threaded=True, debug=False, use_reloader=False)

if __name__ == '__main__':
    main()
