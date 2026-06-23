# Testing Strategy

## 🎯 Objectif

Garantir :

- API fiable
- core déterministe
- reproductibilité totale
- indépendance des fournisseurs API

---

## 🧪 Types de tests

### Unit tests
- comparison engine
- normalization layer
- scoring system

### API tests (FastAPI)
- endpoints /compare
- validation payload
- error handling

### Integration tests
- full pipeline via API
- mock connectors

---

## 🧰 Outils

- pytest
- httpx (FastAPI test client)
- responses (mock HTTP)
- hypothesis

---

## 🧱 Règles

- aucune API réelle
- datasets simulés uniquement
- résultats reproductibles