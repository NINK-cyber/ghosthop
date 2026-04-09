import sys
import os
import logging
from flask import Flask
import requests
import argparse
import colorama
from colorama import Fore, Style

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
        return (resposta.content, response.status_code, list(resposta.headers.items()))
    except:
        return "Erro no nó", 502

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()

    banner = r"""
                  -`
                  .o+`
                 `ooo/
                `+oooo:
               `+oooooo:
               -+oooooo+:
             `/:-:++oooo+:
            `/++++/+++++++:
           `/++++++++++++++:
          `/+++ooooooooooooo/`
         ./ooosssso++osssssso+`
        .oossssso-````/ossssss+`
       -osssssso.      :ssssssso.
      :osssssss/        osssso+++.
     /ossssssss/        +ssssooo/-
   `/ossssso+/:-        -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+/
 .`                                 `/
    """
    
    os.system('clear')
    print(Fore.LIGHTRED_EX + banner)
    print(Fore.GREEN + f" [+] GhostHop v2.5 | {len(SERVIDORES)} nós ativos")
    print(Fore.RED + " [+] Dev: FOREVER")
    print("-" * 55)
    print(Fore.CYAN + f" [*] Escutando na porta: {args.port}")

    app.run(port=args.port, threaded=True, debug=False, use_reloader=False)

if __name__ == '__main__':
    main()
