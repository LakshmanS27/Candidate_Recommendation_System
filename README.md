# Candidate Recommendation System

## Overview
This Candidate Recommendation System evaluates CVs based on the job posting criteria. It extracts structured data from a CV (experience, location, skills) and calculates a score based on how well it matches the required job criteria.

The system supports both **PDF** and **DOCX** CV files, and the score is calculated by comparing the CV’s experience, location, and skills against the job posting’s requirements.

## Features
- **Text Extraction:** Extracts text from **PDF** and **DOCX** files.
- **Text Preprocessing:** Cleans and preprocesses the extracted text by tokenizing and lemmatizing.
- **Structured Data Extraction:** Extracts **years of experience**, **location**, and **skills** from the CV.
- **Job Posting Comparison:** Compares the extracted CV data with a job posting and calculates a score based on defined criteria.
- **Scoring:** Calculates the final score based on job posting requirements and defined weights for each criterion.

## Installation

### Prerequisites
- Python 3.11.9 or higher
- Required Python libraries

### Dependencies
You can install all necessary dependencies via `pip`. Here is a list of required packages:

```bash
pip install -r requirements.txt
