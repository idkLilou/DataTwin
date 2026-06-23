# Guide de contribution

Merci de prendre le temps de contribuer à ce projet 🙌

DataTwin est un moteur de comparaison d’APIs totalement générique, qui ne connaît ni les APIs, ni leurs structures, ni leurs noms. Toutes les contributions doivent respecter cette philosophie.

---

## 📌 Code de conduite

En participant à ce projet, vous vous engagez à :

- Être respectueux et constructif dans vos échanges
- Accepter les retours de review sans conflit
- Favoriser un environnement ouvert et inclusif
- Éviter tout comportement toxique ou dénigrant

---

## 🚀 Comment contribuer

Vous pouvez contribuer de plusieurs façons :

- 🐛 Remonter des bugs
- ✨ Ajouter de nouvelles fonctionnalités
- 🧪 Améliorer ou ajouter des tests
- 📚 Améliorer la documentation
- ⚙️ Améliorer CI/CD ou les outils
- 🧠 Proposer des améliorations d’architecture

---

## 📦 Démarrage rapide

### 1. Fork du projet

Cliquez sur le bouton **Fork** sur GitHub.

---

### 2. Cloner votre fork

```bash
git clone https://github.com/idkLilou/DataTwin.git
cd DataTwin
```

---

### 3. Créer une branche

Utilisez un nom explicite :

```bash
git checkout -b feat/ajout-normalisation
```

---

## 🧱 Principes fondamentaux du projet

⚠️ Ces règles sont STRICTES

### ❌ Interdit :

* Utiliser des noms d’API concrets
* Dépendre d’un fournisseur API spécifique
* Coupler le code à un format de données réel
* Logger des informations sensibles (tokens, clés)
* Contourner les couches d’abstraction

---

### ✅ Obligatoire :

* Tout doit être **agnostique des APIs**
* Travailler uniquement avec des modèles abstraits
* Garder une architecture modulaire
* Garantir des résultats déterministes
* Écrire du code testable

---

## 🧠 Architecture à respecter

Le projet est structuré en couches :

* **Connector Layer** → récupère les réponses brutes
* **Normalization Layer** → transforme en structure abstraite
* **Comparison Engine** → calcule les différences
* **Reporting Layer** → génère les rapports
* **Logging Layer** → trace l’exécution

👉 Il est interdit de bypass une couche.

---

## ✨ Convention de commits

Nous utilisons des commits structurés avec emoji.

### Format :

```
emoji type(scope): message
```

---

### Exemples :

* ✨ feat(engine): ajout du moteur de comparaison
* 🐛 fix(normalizer): correction des valeurs nulles
* 🚀 enhance(comparator): amélioration des performances
* ♻️ refactor(core): simplification du pipeline
* 🧪 test(engine): ajout de tests unitaires
* 📝 docs(readme): mise à jour de la documentation
* 🔧 chore(ci): mise à jour GitHub Actions
* 🔖 release(v0.2.0): préparation de version

---

## 🧪 Tests

Toute modification fonctionnelle doit être testée.

### Lancer les tests :

```bash
pytest
```

---

### Règles de tests :

* Tests unitaires obligatoires pour la logique
* Tests d’intégration pour les pipelines
* Aucune API réelle ne doit être appelée
* Utilisation exclusive de mocks

---

## 🧰 Environnement de développement

### Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

### Lancer le projet :

```bash
python main.py
```

---

## 🧹 Qualité du code

* Fonctions courtes et lisibles
* Code typé si possible
* Logique pure privilégiée
* Zéro dépendance inutile
* Respect strict de l’architecture

---

## 🔁 Processus de Pull Request

1. Synchroniser votre branche avec `main`
2. Vérifier que les tests passent
3. Vérifier le linting
4. Ouvrir une Pull Request claire

---

### Une PR doit contenir :

* Description du changement
* Motivation du changement
* Méthode de test
* Impacts éventuels

---

## 📊 Critères de review

Les PR sont évaluées sur :

* Respect de l’architecture
* Qualité du code
* Couverture de tests
* Performance
* Respect du modèle agnostique

---

## 🚨 Causes de rejet

Une PR sera refusée si :

* Elle dépend d’une API spécifique
* Elle casse l’abstraction
* Elle manque de tests
* Elle complexifie inutilement le système
* Elle duplique du code existant

---

## 🧠 Philosophie du projet

>[!NOTE]
> “Aucune API ne doit jamais être connue du système.”

Tout doit rester abstrait, modulaire et extensible.

---

## 🙌 Merci

Chaque contribution aide à construire un moteur universel de comparaison d’APIs, capable de fonctionner avec n’importe quel système existant ou futur.