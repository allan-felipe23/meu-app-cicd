# 🚀 CI/CD Pipeline com AWS

Pipeline completa de CI/CD usando AWS CodePipeline, CodeBuild e ECS.

## 📋 Arquitetura

```text
GitHub (Source)
↓ Webhook
CodePipeline (Orquestracao)
├─ Stage 1: Source (clone codigo)
├─ Stage 2: Build (testes + Docker)
└─ Stage 3: Deploy (ECS)
↓
ECS Cluster (produção)
├─ Container 1
└─ Container 2
```

---

## 🎯 O que faz

- Detecta push no GitHub
- Executa testes automaticamente
- Cria imagem Docker
- Faz push para ECR
- Deploy automático em ECS
- Monitoramento com CloudWatch

## 🛠️ Tecnologias

- AWS CodePipeline
- AWS CodeBuild
- AWS ECS
- AWS ECR
- Docker
- Python + Flask
- GitHub

## 📦 Endpoints da API

- `GET /` - Home
- `GET /health` - Health check
- `GET /api/users` - Lista de usuários
- `GET /api/health/detailed` - Health check detalhado
- `GET /version` - Versão da aplicação

## 🚀 Como usar

### Localmente

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar testes
pytest tests/

# Rodar aplicação
python app.py

# Acessar
curl http://localhost:5000

---
Com Docker
# Build
docker build -t meu-app .

# Run
docker run -p 5000:5000 seu-app:latest

# Test
curl http://localhost:5000/health
```
---

📊 Monitoramento
- CloudWatch Logs: /ecs/seu-app
- CloudWatch Metrics: CPU, Memória, Requests
- SNS Alerts: Notificações de falhas

🔄 Fluxo de Deploy
Developer faz git push

- GitHub notifica CodePipeline
- CodeBuild executa testes
- Se tudo OK, faz Docker build
- Push para ECR
- CodeDeploy atualiza ECS
- Nova versão em produção
- Tudo automático em ~5 minutos!


📝 License
MIT

👤 Autor
Allan Borge 
