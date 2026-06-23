# Besoins du projet

## 🧠 Vision

Créer un moteur universel de comparaison d’APIs totalement agnostique, exposé sous forme de service backend.

DataTwin doit pouvoir analyser et comparer n’importe quelle API sans connaître sa structure ni son fournisseur.

---

## 🔑 Fonctionnel

- abstraction totale des APIs
- support multi-authentification :
  - API key
  - OAuth
  - Bearer token
  - headers personnalisés

- comparaison structurelle :
  - détection des correspondances de champs
  - analyse des structures
  - alignement des schémas

- détection des différences :
  - champs manquants
  - champs supplémentaires
  - incohérences de type

- système de scoring :
  - score de similarité
  - résultats explicables

---

## ⚙️ Technique

- moteur core en Python
- architecture modulaire
- système de connecteurs (plugins)
- logs structurés (format JSON)
- export des résultats :
  - JSON
  - HTML (futur)

---

## 📦 Évolutions futures

- API backend FastAPI (REST)
- interface web (dashboard)
- stockage des comparaisons (PostgreSQL)
- exécution planifiée des comparaisons (workers)

---

## 🔒 Sécurité

- gestion des secrets via variables d’environnement uniquement
- aucune clé en dur dans le code
- anonymisation des logs
- exécution sandboxée des requêtes externes
- isolation stricte des connecteurs

---

## 📬 Reporting

- génération automatique de rapports
- envoi d’emails (futur)
- templates de rapports personnalisables
- export machine + humain