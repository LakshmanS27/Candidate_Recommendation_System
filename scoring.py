def calculate_score(cv_data, job_data, weights):
    """
    Function to calculate candidate's score based on job posting criteria
    :param cv_data: A dictionary containing the CV data (experience, skills, location)
    :param job_data: A dictionary containing the job posting data (experience, skills, location)
    :param weights: A dictionary containing the weights for each criterion
    :return: The total score out of 100
    """
    # Extract CV and job posting data
    experience = cv_data.get("experience", 0)
    location = cv_data.get("location", [])
    skills = cv_data.get("skills", [])

    job_experience_required = job_data.get("experience", 0)
    job_location = job_data.get("location", [])
    job_skills = job_data.get("skills", [])

    # Calculate the experience quality score
    experience_score = min(experience / job_experience_required, 1) * 100
    years_experience_score = min(experience / 10, 1) * 100
    location_score = 100 if any(loc in job_location for loc in location) else 0
    skills_score = (len(set(job_skills) & set(skills)) / len(job_skills)) * 100 if job_skills else 0
    cv_quality_score = 100 # Total CV quality marks

    # Calculate the total score based on weights
    total_score = (cv_quality_score * weights['cv_quality'] +
                   experience_score * weights['experience'] +
                   years_experience_score * weights['years_experience'] +
                   location_score * weights['location'] +
                   skills_score * weights['skills']) / 100

    return total_score
