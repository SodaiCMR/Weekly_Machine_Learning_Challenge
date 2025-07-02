# 🧠 Weekly Machine Learning Project Challenge

Welcome to the **Weekly Machine Learning Project Challenge**!  
This repository serves as a playground for weekly hands-on machine learning projects designed to strengthen practical ML skills through diverse challenges.

---

## 📅 Project Schedule

Each week introduces a new machine learning project focusing on different domains, datasets, and techniques.  
Projects will range from computer vision and natural language processing to tabular modeling and reinforcement learning.

---

## 📦 Week 1: Image Classifier 🎴

### 🧩 Objective

Build a computer vision model capable of identifying different images (i specifically used anime characters but you are free to use any kind of images).

### 🛠️ Steps Overview

1. **Web Scraping**:  
   Created my own dataset of anime character images using a web scraper from https://myanimelist.net/character.php website.

2. **Image Preprocessing**:
   - Resize, normalize images.
   - Organize into labeled directories for supervised learning.

3. **Model Building**:
   - Train a CNN (using TensorFlow, Keras...).
   - Evaluate using accuracy.

> 📌 **More details in [`week1/readme.md`](week1/readme.md)**
---
## 📦 Week 2: Intent-Based AI Chat 🧠💬

### 🧩 Objective

Design and implement an **AI chatbot** capable of understanding user inputs and responding based on **predicted intent**. This challenge introduces basic NLP techniques and prepares the ground for more advanced conversational agents.

### 🛠️ Steps Overview

1. **Dataset Preparation**:  
   - Create or use a small intent-classification dataset (e.g., JSON with tags like `greeting`, `goodbye`, `help`, `thanks`, etc.).
   - Each intent includes example user phrases and associated responses.

2. **Text Preprocessing**:
   - Tokenization, stemming/lemmatization.
   - Transform text into numerical representations (Bag-of-Words, TF-IDF, or embeddings).

3. **Model Building**:
   - Train a classifier (e.g., a simple feedforward neural network or LSTM) to map user inputs to intent labels.
   - Evaluate using accuracy or F1-score.

4. **Chatbot Interface**:
   - Build a simple CLI or GUI (e.g., Streamlit or Tkinter) that:
     - Accepts user input.
     - Predicts intent.
     - Replies with a predefined response for that intent.

5. **(Optional) Enhancements**:
   - Add confidence threshold and fallback responses.
   - Add contextual memory or chaining multiple intents.

> 📌 **More details in [`week2/readme.md`](week2/readme.md)**
