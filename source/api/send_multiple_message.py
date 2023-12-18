from api.api_parallel_processor import run_parallel_processor
from api.utils.read_responses import read_responses


def main():
    requests_filepath = "source\\api\messages\\my_requests.jsonl"
    save_filepath = "source\\api\\session\\session_1.jsonl"
    request_url="https://api.openai.com/v1/chat/completions"
    run_parallel_processor(requests_filepath, save_filepath, request_url=request_url)

def send_multiple_messages(filename, save_filepath):
    requests_filepath = filename
    request_url="https://api.openai.com/v1/chat/completions"
    run_parallel_processor(requests_filepath, save_filepath, request_url=request_url)

    
if __name__ == "__main__":
    # main()
    responses = read_responses("source\\api\\session\\session_1.jsonl")
    print(responses)
    