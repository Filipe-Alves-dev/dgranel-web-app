import os
import requests
from flask import Flask
from datetime import datetime

app = Flask(__name__)

def obter_cotacoes():
    url = os.getenv("API_ECONOMIA_URL")
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            valor_dolar = dados['rates']['BRL']
            return f"R$ {valor_dolar:.2f}", "R$ 315.240,00"
        else:
            return "Indisponível", "Indisponível"
    except Exception as e:
        print(f"Erro na conexão: {e}")
        return "Erro de Rede", "Erro de Rede"

@app.route("/")
def index():
    dolar, bitcoin = obter_cotacoes()
    empresa = "Logistica de Preços"
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    ambiente = os.getenv("AMBIENTE", "Produção")

    return f"""
    <html>
    <head>
        <title> 📈 Monitor De Preços</title>
        <meta http-equiv="refresh" content="300">
        <style>
            body {{ font-family: sans-serif; background: #f4f4f9; padding: 20px; display: flex; justify-content: center; }}
            .box {{ background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 100%; max-width: 400px; }}
            h2 {{ color: #2c3e50; margin-top: 0; border-bottom: 2px solid #f1c40f; padding-bottom: 10px; }}
            p {{ color: #34495e; font-size: 16px; margin: 15px 0; }}
            .val {{ font-size: 22px; font-weight: bold; color: #27ae60; float: right; }}
            .footer {{ margin-top: 20px; font-size: 12px; color: #95a5a6; border-top: 1px solid #eee; padding-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h2> 📈 Monitor De Preços</h2>
            <p><strong>Engenheiro responsável: Filipe</strong></p>
            <p>Empresa: {empresa}</p>
            <p>Dolar: <span class="val">{dolar}</span></p>
            <p>Bitcoin: <span class="val">{bitcoin}</span></p>
            <div class="footer">
                <hr>
                <p>Hora: {agora}</p>
                <p>Ambiente: {ambiente}</p>
                <p>Status: <span style="color:green; font-weight:bold;">Online</span></p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
