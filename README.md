# 📝 Sentiment Analysis Web App  
A simple NLP-powered Flask web app that predicts the sentiment (Positive/Negative) of user-input text.  

## 🚀 Demo  
![Demo Screenshot](demo.png)  

## 🔥 Features  
✔ Predicts sentiment using **TF-IDF & Logistic Regression**  
✔ Web-based UI with **Flask & Bootstrap**  
✔ Preprocessing using **NLTK (stemming, stopwords removal, etc.)**  


## Technologies Used

    Python, Flask
    Scikit-learn (TF-IDF, Logistic Regression)
    NLTK (Text preprocessing)
    HTML, CSS, Bootstrap

## How It Works

    User enters a comment.
    The text is preprocessed (HTML tag removal, stemming, stopwords filtering).
    Text is converted into a TF-IDF vector.
    Logistic Regression model predicts sentiment.
    The result (Positive/Negative) is displayed.

## 📦 Installation & Setup  
1. Clone the repo:  
   ```bash
   git clone https://github.com/your-username/sentiment-analysis.git
   cd sentiment-analysis
