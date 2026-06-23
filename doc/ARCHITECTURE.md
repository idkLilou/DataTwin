# Architecture

## 🧠 Principe

DataTwin est une API SaaS qui expose un moteur de comparaison abstrait.

Aucune API réelle n’est connue du système.

---

## 🧱 Couches

### 1. Core Engine
- normalisation
- comparaison
- scoring

---

### 2. API Layer (FastAPI)

Endpoints :

- POST /compare
- GET /report/{id}
- GET /health

---

### 3. Persistence Layer

- PostgreSQL
- stockage des comparaisons
- historique des runs

---

### 4. Infrastructure

- Docker
- env vars
- stateless API core

---

## 🔁 Flux

```

Client → FastAPI → Core Engine → DB → Response

```