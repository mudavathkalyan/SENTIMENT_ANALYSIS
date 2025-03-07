from flask import Flask,request,render_template


import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

import pickle
clf=pickle.load(open('clf.pkl','rb'))
tfidf=pickle.load(open('tfidf.pkl','rb'))




app=Flask(__name__)


#cleaning text
# Ensure stopwords are downloaded
nltk.download('stopwords')

# Load stopwords once to avoid redundant calls
stopwords_set = set(stopwords.words('english'))

# Regex pattern for basic emojis
emoji_pattern = re.compile(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)')

def preprocessing(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]*>', '', text).lower()
    
    # Extract emojis separately
    emojis = ' '.join(emoji_pattern.findall(text)).replace('-', '')

    # Remove special characters (except emojis which were extracted)
    text = re.sub(r'\W+', ' ', text) + ' ' + emojis

    # Initialize the stemmer
    porter = PorterStemmer()

    # Tokenize, remove stopwords, and apply stemming
    text = [porter.stem(word) for word in text.split() if word not in stopwords_set]

    return " ".join(text)




@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=='POST':
        comment=request.form['comment']
        cleaned_comment=preprocessing(comment)
        
        comment_vector=tfidf.transform([cleaned_comment])
        prediction=clf.predict(comment_vector)[0]

        return render_template('index.html',prediction=prediction)


if __name__=="__main__":
    app.run(debug=True)