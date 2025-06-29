# Anime Character Classifier

## Description
Ce projet utilise un modèle de deep learning pour classifier des images de personnages d'anime en fonction de leur classe. Les données sont collectées, prétraitées et utilisées pour entraîner un modèle de classification basé sur TensorFlow/Keras.

## Fonctionnalités
- **Scraping des images** : Téléchargement d'images de personnages d'anime depuis MyAnimeList à l'aide de `BeautifulSoup`.
- **Redimensionnement des images** : Redimensionnement des images à une taille standard (300x300) avec `Pillow`.
- **Prétraitement des données** : Division des données en ensembles d'entraînement, de validation et de test.
- **Modèle de classification** : Modèle CNN (Convolutional Neural Network) construit avec TensorFlow/Keras pour classifier les images.
- **Visualisation des résultats** : Affichage des performances du modèle et prédictions sur des images spécifiques.

## Structure du projet
- `scraper.py` : Script pour télécharger les images des personnages.
- `resizer.py` : Script pour redimensionner les images téléchargées.
- `Anime Character Classifier.ipynb` : Notebook contenant le code pour le prétraitement des données, l'entraînement du modèle et l'évaluation.
- `datasets/` : Dossier contenant les images des personnages organisées par classe.
- `files/` : Dossier contenant les données divisées en ensembles d'entraînement, de validation et de test.

## Étapes principales
1. **Collecte des données** :
   - Les images des personnages sont téléchargées depuis MyAnimeList.
   - Chaque personnage est associé à un identifiant unique et un dossier.

2. **Prétraitement des données** :
   - Les images sont redimensionnées à 300x300 pixels.
   - Les données sont divisées en ensembles d'entraînement (60%), de validation (20%) et de test (20%).

3. **Entraînement du modèle** :
   - Un modèle CNN est construit avec des couches `Conv2D`, `MaxPool2D`, `Flatten` et `Dense`.
   - Le modèle est compilé avec la perte `categorical_crossentropy` et l'optimiseur `Adam`.

4. **Évaluation et prédictions** :
   - Les performances du modèle sont évaluées sur l'ensemble de test.
   - Des prédictions sont effectuées sur des images spécifiques pour vérifier la précision.

## Résultats
- Le modèle atteint une précision satisfaisante sur les données de test.
- Les prédictions sur des images spécifiques montrent que le modèle peut correctement classifier les personnages.

## Prérequis
- Python 3.9
- TensorFlow
- BeautifulSoup
- Pillow
- NumPy
- Matplotlib
- Pandas

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/SodaiCMR/anime-character-classifier.git