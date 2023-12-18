import toml
import os

def remove_question_and_answer_from_file(filepath):
    # Load the TOML file
    with open(filepath, 'r') as file:
        data = toml.load(file)

    # Remove the question_and_answer section if it exists
    if 'question_and_answer' in data:
        del data['question_and_answer']

    # Write the modified data back to the TOML file
    with open(filepath, 'w') as file:
        toml.dump(data, file)

def process_directory(directory):
    # Traverse the directory structure
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".toml"):
                filepath = os.path.join(root, file)
                remove_question_and_answer_from_file(filepath)

sessions = [
"session_ga_g8-12"
            ]

if __name__ == "__main__":

    for session_name in sessions:
        reset_dir = "source/api/session/" + session_name +"/profiles"
 
        process_directory(reset_dir)
