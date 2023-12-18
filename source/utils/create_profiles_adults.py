from utils.norwegian_lists import jobs,income_brackets,exercise_habits,marital_statuses, educations, influencers, movies, books, intresser, norwegianCounties, norwegianLivingConditions, boy_names, girl_names, last_names
import random
import os
import toml

def get_random_number(min, max):
    return random.randint(min, max)



def generate_persona(gender=None, age_range=(18, 70)):
    if not gender:
        gender = random.choice(["male", "female"])
    if gender == "male":
        first_name = random.choice(boy_names)
    else:
        first_name = random.choice(girl_names)
    full_name = first_name + " " + random.choice(last_names)    
    age = random.randint(*age_range)
    
    # Vektet fylke-valg
    fylke_weights = [1.5 if f in ["Oslo", "Akershus", "Vestland"] else 1 for f in norwegianCounties]
    fylke = random.choices(norwegianCounties, weights=fylke_weights, k=1)[0]

    person = {
        "name": full_name,
        "gender": gender,
        "age": {
            "years": age
        },
        "location": {
            "fylke": fylke,
            "living_condition": random.choice(norwegianLivingConditions)
        },
        "interests": {
            "hobbies": random.sample(intresser, k=get_random_number(0,5)),
            "languages": ["Norsk"],
            "favorite_books": random.sample(books, k=get_random_number(0,5)),

            "favorite_movies": random.sample(movies, k=get_random_number(0,5)),
            
            "favorite_influencers": random.sample(influencers, k=get_random_number(0,5))
        },
        "occupation": {
            "job": random.choice(jobs),
            "education": random.choice(educations),
            "annual_income": random.choice(income_brackets)
        },

        "health_and_fitness": {
            "exercise_habits": random.choice(exercise_habits)
        },
        "personal_life": {
            "marital_status": random.choice(marital_statuses)
        },
        "personality": {
            "openness": random.randint(40, 60),
            "conscientiousness": random.randint(40, 60),
            "extraversion": random.randint(40, 60),
            "agreeableness": random.randint(40, 60),
            "neuroticism": random.randint(40, 60)
        }
    }

    return person


def save_to_toml(person_data, filename):
    with open(filename, 'w', encoding='utf8') as file:
        toml.dump(person_data, file)

def create_random_personas(session_name, pop_number=200, gender=None, age_range=(7, 18), ):


    base_dir = 'source/sessions'  # Update with your desired path

    # Create a directory for the new session
    session_dir = os.path.join(base_dir, session_name)
    if not os.path.exists(session_dir):
        os.makedirs(session_dir)

    for i in range(pop_number):
        random_person = generate_persona(gender, age_range=age_range)
        profile_path = os.path.join(session_dir, "profiles")

        # Ensure directory exists or create it
        if not os.path.exists(profile_path):
            os.makedirs(profile_path)
        
        save_to_toml(random_person, os.path.join(profile_path, f"person_{i}.toml"))
