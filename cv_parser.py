import os
from text_preprocessing import preprocess_text
from structured_extraction import extract_years_of_experience, extract_location, extract_skills
from scoring import calculate_score
import pdfminer.high_level
import docx
import tkinter as tk
from tkinter import filedialog

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        text = pdfminer.high_level.extract_text(pdf_path)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return ""

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file."""
    try:
        doc = docx.Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from {docx_path}: {e}")
        return ""

def extract_text(cv_path):
    """Extract and preprocess text from a CV file."""
    raw_text = ""
    if cv_path.endswith(".pdf"):
        raw_text = extract_text_from_pdf(cv_path)
    elif cv_path.endswith(".docx"):
        raw_text = extract_text_from_docx(cv_path)
    else:
        print(f"Unsupported file format: {cv_path}")
        return ""
    
    return preprocess_text(raw_text)

def extract_structured_data(cv_text):
    """Extract structured information from CV text (Experience, Location, Skills)."""
    experience = extract_years_of_experience(cv_text)
    location = extract_location(cv_text)
    skills = extract_skills(cv_text)
    return experience, location, skills

def select_cv_file():
    """Open a file dialog to select a CV file."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select CV File", filetypes=[("PDF Files", "*.pdf"), ("Word Files", "*.docx")])
    return file_path

if __name__ == "__main__": 

    cv_path = select_cv_file() # User input
    
    if cv_path:
        print(f"\nExtracting text and structured data from: {cv_path}")
        text = extract_text(cv_path)
        experience, location, skills = extract_structured_data(text)

        # Reference job posting
        job_posting = {
            'experience': 3,  # Required years of experience
            'location': ['india'],  # Required location
            'skills': ['python', 'tensorflow', 'pytorch', 'java']  # Required skills
        }
        
        weights = {
            'cv_quality': 20,
            'experience': 25,
            'years_experience': 15,
            'location': 10,
            'skills': 30
        }
        
        cv_data = {
            'experience': experience,
            'location': location,
            'skills': skills
        }

        print(f"Experience: {experience} years")
        print(f"Location: {location}")
        print(f"Skills: {skills}")

        # Calculate the candidate's score
        score = calculate_score(cv_data, job_posting, weights)
        print(f"Calculated Score: {score:.2f}")
    else:
        print("No file selected.")
