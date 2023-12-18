# the format is in json lines format
import json
import os

# Paths to your folders
PROFILE_FOLDER = 'data\profiles'
SESSION_FOLDER = 'source\\api\session'


def read_responses(path):
    responses = []
    with open(path, 'r', encoding="utf8") as f:
        lines = f.readlines()
        json_objs = [json.loads(line) for line in lines]
        for messages in json_objs:
            history = []
            for message in messages:
                if message.get('messages') != None:
                    history.append(message['messages'][0]['content'])
                    continue
                history.append(message['choices'][0]['message']['content'])
            responses.append(history)
    return responses


def get_answers(responses):
    answers = []
    for response in responses:
        answers.append(response[-1])
    return answers


def get_all_profiles(session_folder, new_session: bool = False):
    profiles = {}
    folder_path = session_folder + "\\profiles" if not new_session else PROFILE_FOLDER
    for profile_file in os.listdir(folder_path):
        with open(os.path.join(folder_path, profile_file), 'r', encoding="utf8") as f:
            profiles[profile_file] = f.read()
    return profiles


def id_the_responses(responses, profiles):
    profile_dict = {}
    for response in responses:
        for message in response[0]['messages']:
            if message['role'] == "system":
                for filename, profile_content in profiles.items():
                    if profile_content in message['content']:
                        profile_dict[filename] = response
                        break
    return profile_dict


def id_the_updated_responses(responses, profiles):
    profile_dict = {}
    for response in responses:
        for message in response[0]['messages']:
            if message['role'] == "system":
                for filename, profile_content in profiles.items():
                    # Exclude the last question from the profile content
                    modified_profile_content = profile_content
                    if '[[question_and_answer]]' in profile_content:
                        questions = profile_content.split('[[question_and_answer]]')
                        modified_profile_content = '[[question_and_answer]]'.join(questions[:-1])
                        modified_profile_content = modified_profile_content.strip()
                    
                    if modified_profile_content in message['content']:
                        profile_dict[filename] = response
                        break
    return profile_dict


def get_question_and_answer(response):
    question = response[0]['messages'][-1]['content']
    answer = response[1]['choices'][0]['message']['content']
    return question, answer