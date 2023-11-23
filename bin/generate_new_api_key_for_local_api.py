import secrets
import json
import os

API_KEYS_FILENAME = os.getenv('API_KEYS_JSON_PATH', "local_resources/api_keys.json")


def generate_api_key() -> str:
    return secrets.token_urlsafe(32)  # Adjust the byte size as needed


def load_api_keys(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        raise RuntimeError("The API keys file is as readable as ancient hieroglyphs. Please check its format.")


def save_api_keys(filename, api_keys):
    with open(filename, 'w') as file:
        json.dump(api_keys, file, indent=4)


if __name__ == "__main__":
    api_keys = load_api_keys(API_KEYS_FILENAME)

    username = input("Enter your username or app name for the API key: ")
    if username in api_keys:
        confirmation = input(
            f"An API key for '{username}' already exists. Do you want to create another? (y/n): ").lower()
        if confirmation != 'y':
            print("Alright, no new key for you. Come back when you change your mind!")
            exit()

    new_api_key = generate_api_key()
    api_keys[new_api_key] = username
    save_api_keys(API_KEYS_FILENAME, api_keys)

    print(
        f"Success! Your API key has been generated and saved.\nWOA_API_KEY={new_api_key}\nThis was saved to "
        "{API_KEYS_FILENAME}. Make sure to restart the FastAPI service to pick up the new APIKEY "
        "and keep it secret, keep it safe!")
