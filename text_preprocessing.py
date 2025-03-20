import re
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Load SpaCy English model
nlp = spacy.load("en_core_web_sm")


nltk.download("stopwords")
nltk.download("punkt")
stop_words = set(stopwords.words("english"))

def clean_text(text):
    """Remove extra spaces, special characters, and digits."""
    text = re.sub(r'\s+', ' ', text)  #extra spaces
    text = re.sub(r'[^\w\s]', '', text)  #special characters
    text = re.sub(r'\d+', '', text)  #digits
    return text.strip().lower()

def preprocess_text(text):
    """Tokenize, remove stopwords, and lemmatize."""
    text = clean_text(text)
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Lemmatization
    doc = nlp(" ".join(filtered_tokens))
    lemmatized_tokens = [token.lemma_ for token in doc]
    
    return " ".join(lemmatized_tokens)

# Example Usage
if __name__ == "__main__":
    sample_text = "I have 5 years of experience in Python, Machine Learning, and AI development!"
    print("Original:", sample_text)
    print("Processed:", preprocess_text(sample_text))
