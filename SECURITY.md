# Security Policy

## 🔐 Versions supportées

Toutes versions actives du backend API sont supportées.

---

## 🚨 Reporting

Ne pas ouvrir d’issue publique.

Contact :
- dufaulilou16@gmail.com

---

## 🧱 Surface d’attaque

DataTwin API interagit avec :

- APIs externes (non fiables)
- authentification (tokens, OAuth)
- données sensibles
- base PostgreSQL

---

## 🔒 Principes

- aucune clé en dur
- secrets via env vars
- logs sans données sensibles
- isolation des connecteurs
- validation stricte API input

---

## 🛡️ Objectif

- API sécurisée
- sandbox des appels externes
- protection des credentials