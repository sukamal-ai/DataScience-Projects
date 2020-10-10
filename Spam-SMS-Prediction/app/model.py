import pickle
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from string import punctuation

punc = list(punctuation)

stop_words = nltk.corpus.stopwords.words('english')

stop_words_punc = stop_words + punc

model = pickle.load(open('model.pkl','rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))

def preprocess_document(text):
     
    # lower the string and strip spaces    
    text = text.lower()
    text = text.strip()
    
    
    # tokenize the words in document
    word_tokens = nltk.WordPunctTokenizer().tokenize(text)
    
    # remove stopwords, punctuations
    # select tokens with only alphabets
    filtered_tokens = [token for token in word_tokens if token not in stop_words_punc]
    
    # join document from the tokens
    text = ' '.join(filtered_tokens)
    
    return text

def predict(text):
    # preprocess and vectorize the text
    clean_text = preprocess_document(text)
    text_tfidf = tfidf.transform([text])
    
    #return model's predicted output
    return model.predict(text_tfidf)[0]