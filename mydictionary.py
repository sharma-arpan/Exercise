import requests
import click

API_KEY = "4e5cc1cd-e756-41de-893d-170355338012"
BASE_URL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"

def get_word_definition(word):
    url = f"{BASE_URL}{word}?key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list):
            if data:
                return data[0]['hwi']['hw'], data[0]['fl'], data[0]['shortdef'][0]
            else:
                return None
        else:
            return None
    else:
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
