# Turing Test Chatbot (Django + GPT)

Ce projet est une **application web Django** qui simule le **Test de Turing** en permettant à un utilisateur de poser une question à deux "bots" :  
- L’un est une **véritable IA GPT** (via OpenRouter)
- L’autre est un **humain simulé** (réponses aléatoires)

L'utilisateur doit deviner lequel des deux est **l'intelligence artificielle**.

---

## Fonctionnalités

- Interface de chat responsive et moderne
- Intégration avec **GPT-3.5-turbo** via OpenRouter (API gratuite)
- **Réponses croisées de deux bots** (Bot A et Bot B)
- **Devinez qui est l’IA** avec des boutons cliquables
- Affichage d’un message de succès ou d’échec

---

## Objectif pédagogique

Ce projet permet de :
- Illustrer le **Test de Turing** en pratique
- Sensibiliser à la puissance des modèles de langage comme GPT
- Initier les étudiants à l'usage d'**IA via API dans des projets web**
- Explorer la difficulté de distinguer un humain d’une machine

---

## Technologies utilisées

- **Django** (framework web Python)
- **HTML/CSS** pur pour l’interface
- **OpenRouter.ai API** (proxy GPT)
- Hébergement sur **Render.com**

---

## Installation locale

```bash
git clone https://github.com/EJM0101/AI-Test-Turing.git
cd turing-chatbot
pip install -r requirements.txt
python manage.py