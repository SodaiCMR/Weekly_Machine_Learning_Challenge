# 🎌 Anime Character Classifier

## 🧠 Description

Ce projet de **deep learning** permet de **classifier des personnages d'anime à partir d'images**. Les images sont collectées, traitées, puis utilisées pour entraîner un **modèle de classification CNN** avec TensorFlow/Keras.

---

## ✨ Fonctionnalités

* 🖼️ **Scraping d'images** : Téléchargement depuis *MyAnimeList* via `BeautifulSoup`.
* 📏 **Redimensionnement** : Mise à l’échelle des images à **300x300 px** avec `Pillow`.
* 🧹 **Prétraitement** : Séparation en **train / validation / test**.
* 🧠 **Modèle CNN** : Construction d’un **Convolutional Neural Network** pour la classification.
* 📊 **Visualisation** : Affichage des **performances** et **prédictions**.

---

## 🗂️ Structure du projet

```
📁 anime-character-classifier/
├── scraper.py                   # Script de téléchargement des images
├── resizer.py                   # Redimensionnement des images
├── Anime Character Classifier.ipynb # Notebook principal
├── datasets/                    # Images originales par classe
└── files/                       # Images divisées (train/val/test)
```

---

## ⚙️ Étapes principales

### 1. 🔍 Collecte des données

* Scraping des images de personnages via **MyAnimeList**.
* Attribution d’un **ID unique** et stockage par dossier.

### 2. 🧼 Prétraitement

* Redimensionnement des images à **300x300 px**.
* Séparation :

  * **Entraînement** : 60%
  * **Validation** : 20%
  * **Test** : 20%

### 3. 🏋️ Entraînement du modèle

* Architecture :

  ```python
  model = Sequential([
      Conv2D(...),
      MaxPooling2D(...),
      Flatten(),
      Dense(...)
  ])
  ```
* Optimisation : `Adam`, perte : `categorical_crossentropy`

### 4. 📈 Évaluation & prédictions

* Évaluation sur l’ensemble de test.
* Prédictions sur des images spécifiques pour vérifier la précision du modèle.

---

## 🏁 Résultats

* Le modèle atteint une **précision satisfaisante** sur les données de test.
* Il est capable de **reconnaître correctement des personnages connus**.

---

## 🧰 Prérequis

* `Python 3.9`
* `TensorFlow`
* `BeautifulSoup`
* `Pillow`
* `NumPy`
* `Matplotlib`
* `Pandas`

---

## 🚀 Installation

```bash
git clone https://github.com/SodaiCMR/anime-character-classifier.git
cd anime-character-classifier
```
