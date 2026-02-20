# 1. A base do sistema (O chassi do caminhão)
FROM ubuntu:latest

# 2. Instalação do Nginx e ferramentas de debug (O que você aprendeu com o Otávio)
RUN apt-get update && apt-get install -y nginx curl iputils-ping

# 3. O PULO DO GATO: Copia o seu site para a pasta onde o Nginx lê os arquivos
# Formato: COPY <arquivo_na_sua_maquina> <caminho_dentro_do_linux_do_container>
COPY index.html /var/www/html/index.html

# 4. Variável para sua identificação (Bom para o portfólio)
ENV APP_OWNER="Filipe Alves - DevOps Junior"

# 5. Comando para o servidor não desligar (A partida do motor)
CMD ["nginx", "-g", "daemon off;"]
