# Cinéphoria desktop

Tableau de bord **employé** pour le cinéma : films, séances, salles, réservations, avis, comptes et incidents.

Client lourd Python branché sur l'API de [Cinéphoria](https://github.com/Meriem1403/Cinephoria). Il ne porte pas de base propre : toutes les données viennent de l'API.

<p align="center">
  <img src="https://img.shields.io/badge/python-3-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/ttkbootstrap-ui-1F6FEB" alt="ttkbootstrap" />
  <img src="https://img.shields.io/badge/api-Cinéphoria-78BCC4" alt="API Cinéphoria" />
</p>

<p align="center">
  <strong>Dépôt :</strong> <a href="https://github.com/Meriem1403/cinephoria-desktop">github.com/Meriem1403/cinephoria-desktop</a>
</p>

---

## Sommaire

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Stack technique](#stack-technique)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Sécurité](#sécurité)
- [Structure du projet](#structure-du-projet)

---

## Présentation

L'écran d'accueil ouvre une navigation par section. Chaque vue interroge l'API puis affiche le résultat dans un tableau ttkbootstrap. Le programme est prévu pour un poste employé sur le réseau du cinéma, avec l'API déjà démarrée.

---

## Fonctionnalités

| Section | Contenu |
|---------|---------|
| **Films** | Catalogue remonté par l'API |
| **Séances** | Créneaux et salles |
| **Salles** | Salles du cinéma |
| **Réservations** | Places réservées |
| **Avis** | Notes laissées par les spectateurs |
| **Comptes** | Utilisateurs connus de l'API |
| **Incidents** | Signalements d'exploitation |

---

## Stack technique

| Couche | Technologies |
|--------|----------------|
| Interface | Python, ttkbootstrap |
| Accès données | `requests` vers l'API Symfony |
| Configuration | Variable d'environnement `API_URL` |

---

## Prérequis

- **Python 3**
- L'API [Cinéphoria](https://github.com/Meriem1403/Cinephoria) joignable (Docker ou PHP local)
- Paquets `ttkbootstrap` et `requests`

---

## Installation

```bash
git clone https://github.com/Meriem1403/cinephoria-desktop.git
cd cinephoria-desktop
python3 -m venv .venv
source .venv/bin/activate
pip install ttkbootstrap requests
export API_URL=http://localhost:8000/api-client
python app.py
```

Sans `API_URL`, le client retombe sur `http://localhost:8000/api-client`.

---

## Configuration

| Variable | Rôle | Défaut |
|----------|------|--------|
| `API_URL` | Racine de l'API client | `http://localhost:8000/api-client` |

Pointer cette variable vers l'API de l'environnement (local, recette, salle). Ne pas figer une adresse de réseau local dans le code.

---

## Sécurité

- Aucun secret dans le dépôt : l'authentification reste celle de l'API.
- L'URL d'API se donne à l'exécution, pas dans Git.
- Le client n'écrit pas de fichier de configuration contenant un mot de passe.

---

## Structure du projet

```
cinephoria-desktop/
└── app.py        # Fenêtre, navigation et appels API
```

---

<p align="center">
  <sub>Client employé de Cinéphoria. Les données vivent dans l'API, pas dans ce dépôt.</sub>
</p>
