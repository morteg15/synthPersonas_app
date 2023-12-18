import os
from api.utils.read_responses import read_responses, get_answers
from api.utils.write_to_json  import process_profiles_with_message
from api.send_multiple_message import send_multiple_messages
from api.resonator_creator import generate_jsonl_structure
from api.send_message import send_request_to_openai
from api.update_session_profiles import update_profiles


def create_session(session_path: str):
    if not os.path.exists(session_path):
        os.mkdir(session_path)


def get_next_session_nr():
    session_nr = 0
    for file in os.listdir("source\\api\\session"):
        if file.startswith("session_"):
            session_nr += 1
    return session_nr

def session(text_message: str, session_name: str = None):
    if session_name is None:
        session_name = "session_" + str(get_next_session_nr())
        new_session = True
    else:
        new_session = False

    session_path = os.path.join("source\\sessions", session_name)
    profile_path =   os.path.join("data\\profiles") if new_session else os.path.join(session_path, "profiles")
    number_of_profiles = len(os.listdir(profile_path)) if not new_session else 50
    user_request_path = os.path.join(session_path, "users_request.jsonl")
    user_response_path = os.path.join(session_path, "users_response.jsonl")
    resonator_request_path = os.path.join(session_path, "resonator_request.jsonl")
    resonator_response_path = os.path.join(session_path, "resonator_response.jsonl")
    create_session(session_path)
    process_profiles_with_message(text_message, profile_path, user_request_path, number_of_profiles)
    # delete user_response.jsonl if exist
    if os.path.exists(user_response_path):
        os.remove(user_response_path)
    send_multiple_messages(user_request_path, user_response_path)
    answers = get_answers(read_responses(user_response_path))
    generate_jsonl_structure(text_message, answers, resonator_request_path)
    send_request_to_openai(resonator_request_path, resonator_response_path)
    update_profiles(session_path, new_session)



def ask_without_resonator(text_message: str, session_path: str):
 
    profile_path = os.path.join(session_path, "profiles")
    user_request_path = os.path.join(session_path, "users_request.jsonl")
    user_response_path = os.path.join(session_path, "users_response.jsonl")

    process_profiles_with_message(text_message, profile_path, user_request_path, number_of_profiles=200)
    
    # Delete user_response.jsonl if it exists
    if os.path.exists(user_response_path):
        os.remove(user_response_path)
    
    send_multiple_messages(user_request_path, user_response_path)    
    update_profiles(session_path)


if __name__ == "__main__":
    session("Hello, what animal do you like most of mouse and cat", "session_8")


    