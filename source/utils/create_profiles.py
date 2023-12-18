# import toml
# import random
# import os
# from generate_mock_data.norwegian_lists import movies, books, intresser, norwegianCounties, norwegianLivingConditions, influencers, boy_names, girl_names, last_names

# def get_random_number(min, max):
#     return random.randint(min, max)

# def generate_person(gender=None, age_range=(7, 18)):
#     if not gender:
#         gender = random.choice(["male", "female"])
#     if gender == "male":
#         first_name = random.choice(boy_names)
#     else:
#         first_name = random.choice(girl_names)
#     full_name = first_name + " " + random.choice(last_names)    
#     age = random.randint(*age_range)
    
#     person = {
#         "name": full_name,
#         "gender": gender,
#         "age": {
#             "years": age
#         },
#         "location": {
#             "fylke": random.choice(norwegianCounties),
#             "living_condition": random.choice(norwegianLivingConditions)
#         },
#         "interests": {
#             "hobbies": random.sample(intresser, k=get_random_number(0,5)),
#             "languages": ["Norsk"],
#             "favorite_books": random.sample(books, k=get_random_number(0,5)),
#             "favorite_movies": random.sample(movies, k=get_random_number(0,5)),
#             "favorite_influencers": random.sample(influencers, k=get_random_number(0,5))
#         },
#         "personality": {
#             "openness": random.randint(0, 100),
#             "conscientiousness": random.randint(0, 100),
#             "extraversion": random.randint(0, 100),
#             "agreeableness": random.randint(0, 100),
#             "neuroticism": random.randint(0, 100)
#         }
#     }

#     return person

# def save_to_toml(person_data, filename):
#     with open(filename, 'w', encoding='latin1') as file:
#         toml.dump(person_data, file)

# def create_session(session_name="session", pop_number=200, gender=None, age_range=(7, 18), ):

#     # Ensure directory exists or create it
#     if not os.path.exists(profile_path):
#         os.makedirs(profile_path)


#     for i in range(pop_number):
#         random_person = generate_person(gender, age_range=age_range)
#         profile_path = os.path.join(session_path, "profiles")

        
#         # Ensure directory exists or create it
#         if not os.path.exists(profile_path):
#             os.makedirs(profile_path)
        
#         save_to_toml(random_person, os.path.join(profile_path, f"person_{i}.toml"))

