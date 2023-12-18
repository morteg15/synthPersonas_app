import json
import os

def load_profile(filename):
    with open(filename, 'r' , encoding="utf8") as file:
        return file.read()

def create_initial_message(profile):
    content = "tre in i rollen som den personen som er beskrevet her og svar som personen er det spørsmål med manglene informasjon finn på noe som passer :\n" + profile
    return {
        "model": "gpt-4",
        "messages": [{"role": "system", "content": content}]
    }

def append_message_to_json(data, text):
    data["messages"].append({"role": "user", "content": text})
    return data

def process_profiles_with_message(message: str, folder_path: str, output_path: str, number_of_profiles: int = 100):
    all_data = []

    # Load each background and create an initial message for it
    for filename in os.listdir(folder_path):
        if filename.endswith(".toml"):  # Assuming the backgrounds are stored in .toml files
            profile_path = os.path.join(folder_path, filename)
            profile = load_profile(profile_path)
            data = create_initial_message(profile)
            all_data.append(data)

    all_data = all_data[0:number_of_profiles]

    with open(output_path, "w", encoding="utf8") as file:
        for data in all_data:
            file.write(json.dumps(data) + '\n')
    print(f"Initial messages for {len(all_data)} backgrounds added to {output_path}")

    # Append the message to all the JSON structures
    for i in range(len(all_data)):
        all_data[i] = append_message_to_json(all_data[i], message)

    with open(output_path, "w" , encoding="utf8") as file:
        for data in all_data:
            file.write(json.dumps(data) + '\n')
    print(f"Message appended to all JSONs in {output_path}")

# Example usage:
# process_profiles_with_message("Hello, how are you?", "data\\profiles", "output.jsonl")


# process_profiles_with_message("Hello, how are you?", "data\\profiles", "output_test.jsonl")