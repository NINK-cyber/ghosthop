import sys
from flask import Flask, request
import requests
import argparse
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)
app = Flask(__name__)

# --- CONFIGURAÇÃO DE 10 SERVIDORES ---
# Aqui você pode colocar IPs reais, Proxies ou portas locais
SERVIDORES = [f"http://127.0.0.1:{5000 + i}" for i in range(1, 11)]
# Isso gera automaticamente: http://127.0.0.1:5001 até 5010

contador = 0

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    global contador
    
    # Seleciona o servidor atual (Giro de 1 a 10)
    indice = contador % len(SERVIDORES)
    alvo = SERVIDORES[indice]
    contador += 1
    
    # Log visual no terminal
    print(Fore.CYAN + f"[{indice + 1}/10] " + Fore.YELLOW + f"Saltando via: {alvo}")
    
    try:
        # Timeout de 3 segundos para não travar se um servidor cair
        resposta = requests.get(f"{alvo}/{path}", timeout=3)
        return (resposta.content, resposta.status_code, resposta.headers.items())
    except Exception as e:
        print(Fore.RED + f"[!] Erro no nó {alvo}: Servidor Offline")
        return f"Falha no Salto: O nó {indice + 1} está fora do ar.", 502

def main():
    parser = argparse.ArgumentParser(description="GhostHop - High Speed Proxy Rotation")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()

    # O SEU BANNER (Avião Vermelho)
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
    print(Fore.LIGHTRED_EX + banner)
    print(Fore.GREEN + f"[+] GhostHop v2.0 Ativado com {len(SERVIDORES)} nós.")
    print(Fore.RED + "[+] Dev: FOREVER")
    print(Style.RESET_ALL)

    app.run(port=args.port, threaded=True) # Threaded=True para aguentar mais carga

if __name__ == '__main__':
    main()