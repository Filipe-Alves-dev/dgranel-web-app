# 🚚 Logistics Cloud Connect - Projeto de Infraestrutura DevOps

Este repositório contém a arquitetura de uma aplicação de logística containerizada, com foco em alta disponibilidade, segurança e automação de deploy (CI/CD) utilizando nuvem AWS.

## 🎯 Objetivo do Projeto
O objetivo deste laboratório é demonstrar a transição de um ambiente de infraestrutura tradicional para um modelo **Cloud Native**, automatizando o ciclo de vida da aplicação desde o desenvolvimento local (WSL2) até a produção na AWS.

## 🏗️ Arquitetura e Fluxo de Dados
A solução foi desenhada para ser resiliente e escalável:

1.  **Desenvolvimento**: Ambiente isolado em **Docker** no Windows Subsystem for Linux (WSL2).
2.  **Versionamento**: Controle de versão no Git com estratégia de **Feature Branch** (`melhorias-site`) e proteção da branch principal.
3.  **Segurança**: Implementação de política de **Secret Management**, utilizando arquivos `.env` ignorados pelo Git para prevenir vazamento de credenciais.
4.  **CI/CD (Pipeline)**: Automação via **GitHub Actions** que sincroniza o código com a instância na nuvem.
5.  **Nuvem (AWS)**: Hospedagem em instância **EC2 (Ubuntu)** otimizada com **Docker Compose V2**.



## 🛠️ Tecnologias e Ferramentas
* **Engine**: Docker & Docker Compose (Orquestração de Containers).
* **Cloud**: AWS (EC2, Security Groups, IAM).
* **CI/CD**: GitHub Actions.
* **Backend**: Python Flask (Logística API).
* **Segurança**: Git Hygiene (.gitignore) e Environment Variables.

## 📦 Como Executar o Ambiente Local

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Filipe-Alves-dev/Projeto-Docker-EC2-Git-Actions.git](https://github.com/Filipe-Alves-dev/Projeto-Docker-EC2-Git-Actions.git)
    ```
2.  **Configure suas variáveis de ambiente:**
    Crie um arquivo `.env` na raiz e adicione suas chaves.
3.  **Suba os containers:**
    ```bash
    docker compose up -d --build
    ```

## 🧠 Aprendizados Chave (Expertise DevOps)
* **Migração Bare-metal para Cloud**: Substituição de conceitos de virtualização tradicional (como Nutanix) por instâncias elásticas (EC2).
* **Imutabilidade**: Garantia de que o ambiente de teste é idêntico ao de produção através de imagens Docker.
* **Automação de Deploy**: Redução do erro humano e do tempo de entrega (Time-to-Market) através de pipelines automatizados.
