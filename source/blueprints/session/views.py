# Assuming utils and all necessary functions are accessible within the blueprint
from time import sleep
from flask import render_template, request, redirect, url_for, flash
from . import session_blueprint
import os
from api.create_session import session as ask_question_from_api
from api.utils.read_responses import get_all_profiles, id_the_updated_responses
from utils.create_profiles_adults import create_random_personas
import toml
import json


SESSION_PATH = 'source\\sessions'  # Define the path to your sessions directory


def load_jsonl(file_path):
    with open(file_path, "r", encoding="utf8") as file:
        return [json.loads(line) for line in file]


def extract_question(data):
    for entry in data:
        for message in entry[0]["messages"]:
            if message["role"] == "user":
                return message["content"]


def extract_general_opinion(resonor_data):
    return resonor_data[0]["choices"][0]["message"]["content"]

@session_blueprint.route('/session/<session_name>', methods=['GET'])
def session(session_name):
    current_session_path = os.path.join(SESSION_PATH, session_name)
    user_response_file = os.path.join(current_session_path, "users_response.jsonl")
    if not os.path.exists(user_response_file):
        return render_template('session/new_session.html', session_name=session_name)

    user_response = load_jsonl(user_response_file)
    value = os.path.join(current_session_path, "resonator_response.jsonl")
    resonor_response = load_jsonl(value)
    question = extract_question(user_response)
    general_opinion = extract_general_opinion(resonor_response)
    profiles = get_all_profiles(current_session_path, new_session=False)
    profiles_dict = id_the_updated_responses(user_response, profiles)


    return render_template('session/session.html', 
                           session_name=session_name, 
                           question=question, 
                           general_opinion=general_opinion, 
                           profiles_dict=profiles_dict)


@session_blueprint.route('/create_session', methods=['POST', 'GET'])
def create_session():
    if request.method == 'POST':
        session_name = request.form.get('session_name')
        num_personas = int(request.form.get('num_personas'))

        # Call the function to create a folder and personas
        create_random_personas(session_name, num_personas)

        flash('Session created successfully.', 'success')
        return redirect(url_for('.session', session_name=session_name))  # Redirect to the session view
    
    return render_template('session/create_session.html')




@session_blueprint.route("/ask", methods=["POST"])
def ask_question():
    question = request.form.get("question")
    current_session_name = request.form.get("session_name", None)
    if not current_session_name:
        # create popup if session name is not provided
        print("no session name")
        sleep(5)
        return redirect(url_for("index"))  # Redirect to an appropriate page
    ask_question_from_api(question, current_session_name)
    # redirect to the @session_blueprint.route('/session/<session_name>', methods=['GET'])
    return redirect(url_for('.session', session_name=current_session_name))


