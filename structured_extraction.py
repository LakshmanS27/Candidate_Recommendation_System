import re
import spacy

#spaCy's model for NER
nlp = spacy.load("en_core_web_sm")

# Predefined skill set (for simplicity, this can be expanded as needed)
skills_keywords = {
    'python', 'java', 'c++', 'c', 'flutter', 'html', 'r', 'css', 'javascript', 'react js', 'node js', 
    'php', 'xml', 'go', 'scikit-learn', 'tensorflow', 'nltk', 'keras', 'pandas', 'pytorch', 'mysql', 
    'bigquery', 'postgresql', 'tableau', 'power bi', 'predictive analytics', 'deep learning', 
    'natural language processing', 'statistical modeling', 'computer vision', 'aws', 'azure'
}

def extract_years_of_experience(text):
    """Extract years of experience from CV text."""
    match = re.search(r'(\d+)\s*(years?|yr|y)\s*of\s*(experience|work)', text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return 0  # If no match, return 0

def extract_location(text):
    """Extract location (city, country) from CV using spaCy NER."""
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return locations if locations else None

def extract_skills(text):
    """Extract skills from CV text based on a predefined list."""
    found_skills = [skill for skill in skills_keywords if skill in text.lower()]
    return found_skills

# Example usage
if __name__ == "__main__":
    sample_text = """I have 5 years of experience in Python, Machine Learning, and AI development. I live in San Francisco, USA."""
    print("Years of Experience:", extract_years_of_experience(sample_text))
    print("Location:", extract_location(sample_text))
    print("Skills:", extract_skills(sample_text))
