# MiniRAG — Production-Grade Retrieval Augmented Generation System

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Celery](https://img.shields.io/badge/Celery-5.3%2B-37814A?logo=celery&logoColor=white)](https://docs.celeryq.dev)
[![Redis](https://img.shields.io/badge/Redis-Running-DC382D?logo=redis&logoColor=white)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-336791?logo=postgresql&logoColor=white)]()
[![Docker Ready](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://docker.com)
[![Grafana](https://img.shields.io/badge/Monitoring-Grafana-F46800?logo=grafana&logoColor=white)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-0d6efd?logo=open-source-initiative&logoColor=white)](LICENSE)
[![Stars](https://img.shields.io/github/stars/your-username/mini-rag?style=social)](https://github.com/your-username/mini-rag)

A **full-stack, production-ready RAG platform** with background ingestion, hybrid search, real-time monitoring, and support for local & cloud LLMs.

### Features
- FastAPI + OpenAPI/Swagger UI  
- Asynchronous file processing & indexing via Celery  
- PostgreSQL + SQLAlchemy 2.0 + Alembic migrations  
- Redis broker & result backend  
- Prometheus + Grafana observability stack  
- Flower task monitoring dashboard  
- Works with OpenAI, Anthropic, or Ollama (local LLMs)  
- Background progress tracking & WebSocket updates  
- Clean, modular, scalable architecture  

## Quick Start (Docker Compose — Recommended)

```bash
git clone https://github.com/your-username/mini-rag.git
cd mini-rag

cp .env.example .env
cp docker/.env.example docker/.env

# Edit both .env files → add your API keys (OPENAI_API_KEY, etc.)

cd docker
sudo docker compose up -d



Service,URL,Credentials
FastAPI Docs,http://localhost:8000/docs,—
API,http://localhost:8000,—
Flower Dashboard,http://localhost:5555,admin / password (from .env)
Grafana,http://localhost:3000,admin / admin
Prometheus,http://localhost:9090,—



# 1. System deps (Ubuntu/Debian)
sudo apt update && sudo apt install -y libpq-dev gcc python3-dev

# 2. Create conda env
conda create -n mini-rag python=3.10 -y
conda activate mini-rag

# 3. Install Python packages
pip install -r requirements.txt

# 4. Copy env & configure
cp .env.example .env
# → Edit .env with your keys

# 5. Run migrations
alembic upgrade head





