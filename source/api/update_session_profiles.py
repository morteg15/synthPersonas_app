import os
import json
from api.utils.read_responses import get_all_profiles, id_the_responses, get_question_and_answer


def update_profiles(session_path, new_session: bool = False):
    response_filename = os.path.join(session_path, "users_response.jsonl")
    
    with open(response_filename, 'r', encoding="utf8") as f:
        profiles = get_all_profiles(session_path, new_session)
        responses = [json.loads(line) for line in f]
        profiles_dict = id_the_responses(responses, profiles)

        for filename, response in profiles_dict.items():
            question, answer = get_question_and_answer(response)
            answer = answer.replace('"', "").replace("'", "").replace("\n", "")
            updated_profile = profiles[filename] + f"\n\n[[question_and_answer]]\nquestion = \"{question}\"\nanswer = \"{answer}\""
            
            # Ensure the profiles directory exists
            profiles_dir = os.path.join(session_path, "profiles")
            if not os.path.exists(profiles_dir):
                os.mkdir(profiles_dir)
            
            # Save the updated profile
            with open(os.path.join(profiles_dir, filename), 'w', encoding="utf8") as f:
                f.write(updated_profile)