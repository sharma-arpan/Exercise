import os
import requests
import click


API_KEY = os.environ.get("MERRIAM_WEBSTER_API_KEY")
BASE_URL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"


def get_word_definition(word):
    url = f"{BASE_URL}{word}?key={API_KEY}"
    response = requests.get(url)
    print(url)
    try:
        response.raise_for_status()  # Check for HTTP errors (e.g., 404, 500)
        data = response.json()
        if isinstance(data, list):
            if data:
                return data[0]['hwi']['hw'], data[0]['fl'], data[0]['shortdef'][0]
            else:
                return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except requests.exceptions.JSONDecodeError as json_err:
        print(f"JSON decode error occurred: {json_err}")
    return None

@click.command()
@click.argument("word")
def main(word):
    result = get_word_definition(word)
    if result:
        pronunciation, word_type, definition = result
        print(f"{pronunciation} ({word_type}): {definition}")
    else:
        print(f"Sorry, the definition for '{word}' could not be found.")

if __name__ == "__main__":
    main()
