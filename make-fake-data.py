import pandas as pd
import numpy as np
import random

n_participants = 60


## questions??
index = [
    'Timestamp', 
    'Name', 
    'Email',
    'Which institute are you located at?\r\n\r\nOf you are affiliated with multiple institutions please give details (e.g. Imperial College London but based at CERN)',
    'In which region are you based?',
    'How will you be attending the meeting?',
    'Which of these best describes your job title?',
    'How long have you worked on T2K?',
    'What are your main areas of research within the collaboration?',
    'Which topics would you like to discuss with your buddy? [Your physics / research interests]',
    'Which topics would you like to discuss with your buddy? [Hobbies and other (non physics) interests - please provide any specific you want to be considered below]',
    'Which topics would you like to discuss with your buddy? [Outreach]',
    'Which topics would you like to discuss with your buddy? [Diversity, equity and inclusion initiatives]',
    'Which topics would you like to discuss with your buddy? [Shared identity (marginalised person in STEM, from a particular background/location etc. - please share details below)]',
    'Which topics would you like to discuss with your buddy? [Current political situation surrounding science (funding, policies etc.)]',
    'Do you have any specific preferences for your buddy? \r\n(e.g someone else who is new to the experiment, LGBTQ+, specific research / software expertise) - If you specified "hobbies and other interests" or "shared identity" above, please provide any details here and we will do our best to accommodate',
    'Do you want to be matched with an early career (EC) member?',
    'Any comments or feedback regarding this form?',
    'If attending online, which timezone will you be attending the meeting from (will be used to determine matches with other online participants)',
    'What languages are you comfortable speaking with your buddy? '
]

## the institute the person is located at
institute_question = 'Which institute are you located at?\n\nOf you are affiliated with multiple institutions please give details (e.g. Imperial College London but based at CERN)'

## how the person will be attending (remote or in-person)
attendance_mode_question = 'How will you be attending the meeting?'

## what career stage is the person
career_stage_question = 'Which of these best describes your job title?'

## which career stages are considered "early career"
ecr_stages = ["PHD student", "Masters student", "Postdoc"]

## whether the person wants to be matched with an ECR participant
early_carreer_member_question = 'Do you want to be matched with an early career (EC) member?'

## what region is the person based in?
region_question = 'In which region are you based?'

## how long have they worked on the experiment?
experiment_time_question = 'How long have you worked on T2K?'

## what do they work on
research_area_question = 'What are your main areas of research within the collaboration?'

## list of questions in the multiple choice grid
multiple_choice_questions = [
    'Which topics would you like to discuss with your buddy? [Your physics / research interests]',
    'Which topics would you like to discuss with your buddy? [Hobbies and other (non physics) interests - please provide any specific you want to be considered below]',
    'Which topics would you like to discuss with your buddy? [Outreach]',
    'Which topics would you like to discuss with your buddy? [Diversity, equity and inclusion initiatives]',
    'Which topics would you like to discuss with your buddy? [Shared identity (marginalised person in STEM, from a particular background/location etc. - please share details below)]',
    'Which topics would you like to discuss with your buddy? [Current political situation surrounding science (funding, policies etc.)]',    
]

## the options for the multiple choice questions
options_dict = {
    "Do not want to talk about": 0,
    "Could talk about": 1,
    "Want to talk about": 2,
    "High priority to talk about": 3,
}

options = list(options_dict.keys())

option_fractions = [
    0.1,
    0.6,
    0.2,
    0.1
]
assert np.abs(np.sum(option_fractions) - 1.0) < 1e5

## Example institutes and their corresponding region
region_institute_pairs = [
    ("Asia",     "The University of Tokyo"),
    ("Asia",     "Kyoto University"),
    ("Asia",     "University of Tokyo"),
    ("Europe",   "CERN"),
    ("Europe",   "Ecole polytechnique"),
    ("Europe",   "Eötvös Loránd University"),
    ("Europe",   "ETH Zürich"),
    ("Europe",   "Imperial College London"),
    ("Europe",   "Johannes Gutenberg University Mainz"),
    ("Europe",   "King's College London"),
    ("Europe",   "Lancaster, UK"),
    ("Europe",   "LLR - France"),
    ("Europe",   "LPNHE - Paris"),
    ("Europe",   "NCBJ Warsaw, Poland"),
    ("Europe",   "Padova University"),
    ("Europe",   "RAL"),
    ("Europe",   "University of Glasgow"),
    ("Europe",   "University of Oxford"),
    ("Europe",   "University of Warsaw"),
    ("Europe",   "University of Geneva"),
    ("Americas", "Louisiana State University"),
    ("Americas", "Stony Brook University"),
    ("Americas", "University of Pennsylvania"),
    ("Americas", "University of Rochester"),
]

## possible career stages
career_stages = [
    "PHD student",
    "Postdoc",
    "Lecturer / professor",
]
## proportion of each career stage
career_stage_fractions = [
    0.5,
    0.3,
    0.2,
]
## better safe than sorry
assert np.sum(career_stage_fractions) == 1.0


## how will the person attend the meeting
attendance_modes = [
    "In-person",
    "Online"
]
attendance_mode_fractions = [
    0.75,
    0.25
]
assert np.sum(attendance_mode_fractions) == 1.0


## how long has the person worked on the experiment
experiment_times = [
    '< 6 months',
    '6 months - 1 year',
    '1-2 years',
    '2-3 years',
    '3 - 6 years',
    '> 6 years'
]
experiment_time_fractions = [
    0.1,
    0.1,
    0.2,
    0.2,
    0.2,
    0.2
]
assert np.sum(experiment_time_fractions) == 1.0

## does the person want to be matched with an ECR
ecr_preferences = [
    'Yes',
    'No',
    'No preference'
]
ecr_preference_fractions = [
    0.25,
    0.05,
    0.7
]
assert np.sum(ecr_preference_fractions) == 1.0


participants = []

for i in range(n_participants):

    name = f'person {i}'
    region, institute = random.choice(region_institute_pairs)
    career_stage = np.random.choice(career_stages, p = career_stage_fractions)
    attendance_mode = np.random.choice(attendance_modes, p = attendance_mode_fractions)
    experiment_time = np.random.choice(experiment_times, p = experiment_time_fractions)
    ecr_preference = np.random.choice(ecr_preferences, p = ecr_preference_fractions)

    print(f'{name:10s} - {region:10s} {institute:40s} {career_stage}')
    
    data = {
        'Name': name,
        institute_question: institute,
        region_question: region,
        attendance_mode_question: attendance_mode,
        career_stage_question: career_stage,
        experiment_time_question: experiment_time,
        early_carreer_member_question: ecr_preference
    }

    ## set up the multiple choice answers
    for question in multiple_choice_questions:

        data[question] = np.random.choice(options, p=option_fractions)

    series = pd.Series(data)
    
    participants.append(series)

df = pd.DataFrame(participants)
df.to_csv("test_data.csv")
