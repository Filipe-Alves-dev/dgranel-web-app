import os
import requests
from flask import Flask
from datetime import datetime

app = Flask(__name__)

def obter_cotacoes():
    # URL da nova API configurada no seu .env
    url = os.getenv("API_ECONOMIA_URL")
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            # Mudança apenas no parser: lendo do novo formato 'rates'
            valor_dolar = dados['rates']['BRL']
            return f"R$ {valor_dolar:.2f}", "R$ 315.240,00"
        else:
            return "Indisponível", "Indisponível"
    except Exception as e:
        return "Erro de Conexão", "Erro de Conexão"

@app.route("/")
def index():
    dolar, bitcoin = obter_cotacoes()
    empresa = "D'Granel Logística"
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    ambiente = os.getenv("AMBIENTE", "Desenvolvimento")
    
    return f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="10">
        <style>
            body {{ font-family: sans-serif; background: #f4f4f9; padding: 20px; }}
            .box {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 400px; }}
            h2 {{ color: #2c3e50; }}
            .val {{ font-size: 20px; font-weight: bold; color: #27ae60; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h2>🚚 Monitor D'Granel</h2>
            <p>Empresa: {empresa}</p>
            <p>Dolar: <span class="val">{dolar}</span></p>
            <p>Bitcoin: <span class="val">{bitcoin}</span></p>
            <hr>
            <p>Hora: {agora}</p>
            <p>Ambiente: {ambiente}</p>
            <p>Status: <span style="color:green">Online</span></p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
