import secrets


def generate_api_key() -> str:
    return secrets.token_urlsafe(32)  # You can adjust the byte size as needed


if __name__ == "__main__":
    print(generate_api_key())
