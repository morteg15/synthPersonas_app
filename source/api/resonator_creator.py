import json

# Configuration
CONFIG = {
    "question": "What is your opinion on topic X?",  # Specify the question here
    "mode": "opinion",  # Change to "answer" for the other mode
    "output_file": "output.jsonl"
}

def generate_jsonl_structure(question, user_messages, outputfile, mode="opinion"):
    """
    Generate a JSONL structure based on a question, user messages, and a mode.

    Parameters:
    - question (str): The question that user messages are responding to.
    - user_messages (list): A list of messages from the user.
    - mode (str): Either "opinion" or "answer".

    Returns:
    - dict: The generated JSONL structure.
    """
    
    # Validate mode
    if mode not in ["opinion", "answer"]:
        raise ValueError("Mode should be either 'opinion' or 'answer'.")

    # Base structure
    jsonl_structure = {
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": question},  # Question as the first system message
            {"role": "system", "content": "jeg er tenkeren jeg leser igjenom kommentarer å finner den generelle meningen jeg ignorer kommentarer som ikke fokuserer på spørsmålet. Jeg skriver den generelle meningen å lister opp fordelingen slik [' n%',  n%, ...] husk at meldinende skal representere en større gruppe oppgi svaret i %"}
        ]
    }

    # Add user messages
    for message in user_messages:
        jsonl_structure["messages"].append({"role": "user", "content": message})

    # Add system response based on mode
    if mode == "opinion":
        jsonl_structure["messages"].append({"role": "user", "content": "Bassert på kommentarene hva er den generelle meningen det som er mest populeært og skriv den og vis forholdene i chatlogen med prosenti en liste"})
    else:
        jsonl_structure["messages"].append({"role": "user", "content": "Based on the messages, the most likely correct result is [result]."})

    # Save to file
    with open(outputfile, 'w', encoding='utf8') as f:
        f.write(json.dumps(jsonl_structure))
    print(f"Resonator saved to " + outputfile)

    # return jsonl_structure

# user_messages = []
# responses = read_responses("source\\api\\session\\session_1.jsonl")
# for response in responses:
#     user_messages.append(response[-1])
    

# # # Example usage
# # user_messages = ["This is the first message.", "Here's another message.", "And one more for good measure."]
# jsonl_structure = generate_jsonl_structure(CONFIG["question"], user_messages, CONFIG["mode"])

# # Save to file
# with open(CONFIG["output_file"], 'w') as f:
#     f.write(json.dumps(jsonl_structure, indent=2))

# print(f"Resonator saved to {CONFIG['output_file']}")
