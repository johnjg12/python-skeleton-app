# Python API Project Example

Welcome to my Python API project! This repository is an exciting guide on building a robust and scalable API
application using Python and FastAPI. It's designed for developers who are passionate about creating clean, efficient,
and well-structured API services.

## 🚀 Features

- **Modern Python with FastAPI**: Utilizing the fast and efficient FastAPI framework.
- **Structured Schemas**: Defined with Pydantic for accurate data validation and serialization.
- **Custom JSON Encoding**: Handling complex data types like `datetime`.
- **Middleware Integration**: Track requests with a unique ID.
- **Comprehensive Testing**: Examples using Pytest and FastAPI's TestClient.

## 📚 What You'll Learn

- Crafting high-performance APIs in Python.
- Organizing API responses with generic and specific models.
- Implementing middleware for enhanced functionality.
- Writing effective tests for API endpoints.

## 🛠️ Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/python-api-example.git
   cd python-api-example
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   uvicorn app.main:app --reload
   ```

   Visit `http://127.0.0.1:8000` in your browser to see it in action!

5. **Running Tests**

   ```bash
   pytest
   ```

## 🔍 Explore the Endpoints

- `GET /`: Root endpoint welcoming you to the API.
- `GET /example/hello_world`: Returns a classic "Hello World" message.
- `GET /example/list`: Demonstrates a response with a list of items and pagination.
- `GET /example/error`: An example error response.

## 📖 Documentation

FastAPI auto-generates interactive API documentation using Swagger UI. Once the server is running, you can access it
at `http://127.0.0.1:8000/docs`.

## 🤖 Tech Stack

- **FastAPI**: High-performance web framework.
- **Pydantic**: Data validation and settings management.
- **pytest**: Powerful testing framework.
- **Uvicorn**: Lightning-fast ASGI server.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

# More Details

## Project Layout

```
/project_root
│
├── app                     # Application source code.
│   ├── api                 # Endpoints and route definitions.
│   │   ├── endpoints       # Specific routes (e.g., devices, playbooks, tasks).
│   │   └── middleware      # Dependency injection and tools for middlewae, like auth and trackingid
│   │
│   ├── core                # Application configuration, utils, logging, etc.
│   │
│   │
│   ├── schemas             # Pydantic models for request and response data.
│   │
│   ├── services            # Business logic services.
│   │
│   ├── main.py             #  FastAPI application creation.
│   │
│   └── __init__.py
│
├── bin                     # Executable scripts
│
├── docs                    # Supporting documentation
│
├── tests                   # Test suite for the application.
│   ├── api                 # Tests for the API routes.
│   └── ...
│
├── .dockerignore           # Specifies files to ignore from passing into docker build contexts (should look similar to .gitignore).
│
├── .env                    # Environment variables for local development.
│
├── .env.template           # Template for creating .env files.
│
├── .gitignore              # Specifies intentionally untracked files to ignore.
│
├── docker-compose.yml      # Docker-Compose configuration file.
│
├── Dockerfile              # Instructions for building the Docker image.
│
├── LICENSE                 # License file.
│
├── README.md               # Project overview and development instructions.
│
└── requirements.txt        # Project dependencies.
```

Explanation of key components:

- app/: Contains all the source code of the application.
- app/api/: Where you define your endpoint routes grouped by resource or functionality and include routers in your main
  application.
- app/crud/: Separation of CRUD functions that interact with database models for better code reusability and clarity.
- app/db/: Encapsulates database management, including models for ORM and migration scripts.
- app/schemas/: Using Pydantic models for consistent data validation and serialization throughout the application.
- app/services/: Business logic layer where the main functionalities of your application are implemented.
- app/core/: Configuration and essentials of the application not related to business logic such as application setup and
  logging.
- tests/: All your test cases which can be run to ensure the application works as expected.
- Dockerfile: Defines the steps to create a Docker container for your application.
- docker-compose.yml: If you use Docker Compose, this file orchestrates your application containers including databases,
  caches, etc.
- requirements.txt: Lists all Python dependencies for the project.
- .env and .env.template: Stores configuration and sensitive information that should not be hard-coded into the
  application.

This layout allows for:

- Clear separation of concerns making the structure intuitive to navigate.
- Easy addition of new routes, models, and CRUD operations.
- Flexibility to expand for more complex services or to include a frontend later.
- Dockerization through the Dockerfile and potential docker-compose.yml for managing multi-container setups.

Make sure your Dockerfile is configured to include only the necessary components and to respect Python best practices
for a production build, such as not running your application as root.

## Useful tips:

- Always make sure your code has proper type hints to maintain strict typing. It not only helps with readability but
  also improves the developer experience with better IDE integrations.
- Extensively document your code and API endpoints. FastAPI has built-in support for generating documentation via
  Swagger UI and ReDoc, which can be enhanced with your docstrings.
- Consider using a version control system like Git, and set up a .gitignore file to avoid committing unnecessary files.

## Adding Authentication

When picking authentication you need to first know who needs access and how.
If you are just setting up a simple API for machine consumption then you can use a simple API key.
If you need to manage users and their permissions then you will need to use a more complex authentication method.
In this case you should likely opt to use SSO or SAML and use a 3rd party service (i.e. Oauth2).

For using FastAPI I recomment using fastapi-users and/or fastapi-security.  
Both fastapi-users and fastapi-security are designed to simplify various aspects of user management and security in
FastAPI applications, but they serve slightly different purposes.

fastapi-users is a more comprehensive solution that is designed to handle a wide range of user management tasks such as:

    User registration
    User authentication (with multiple backends such as email/password, OAuth)
    Password hashing and resetting
    Email verification
    JWT token management

It is a good pick if you're looking for an all-in-one package that covers the entire user lifecycle and you don't want
to manually implement these features.

fastapi-security is more focused on security aspects, particularly OAuth2 scopes and roles. It is a more lightweight
option compared to fastapi-users and is suitable if you're primarily concerned with securing your endpoints with
specific permissions and less with the full suite of user management features.

Choosing between the two depends on your specific needs:

    If you need a full-fledged user management system with out-of-the-box features, go for fastapi-users.
    If you need fine-grained security controls with scopes and roles and plan to handle user management separately, fastapi-security might be the better choice.

You typically wouldn't use both together because fastapi-users already includes the functionalities to secure your
application. Using both could lead to redundancy and unnecessary complexity.

## Example with fastapi-security and simple API KEYS stored in a local json file for persistence

This example uses a local file to store APIKEYs. This is fine to do for small projects or PoCs, but this shouldn't be
used in production. use something like redis or another db/cache service.

```markdown
## API Authentication

APIKEYS must be manually generated and added to `local_resources/api_keys.json`

Example api_keys.json file:

```json
{
  "apikey123": "username1",
  "apikey456": "username2"
}
```

To generate a new api key in python you can use the following code:

```python
import secrets

print(secrets.token_urlsafe(32))
```

Then you can create an `auth.py` file in your project with the following code:

```python
import os

from fastapi import HTTPException, Depends, status
from fastapi.security.api_key import APIKeyHeader
from typing import Dict
import json

API_KEY_NAME = "access_token"
API_KEYS_FILENAME = os.getenv('API_KEYS_JSON_PATH', "local_resources/api_keys.json")

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def load_api_keys() -> Dict[str, str]:
    try:
        with open(API_KEYS_FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_api_keys(api_keys: Dict[str, str]):
    with open(API_KEYS_FILENAME, "w") as file:
        json.dump(api_keys, file, indent=4)


API_KEYS = load_api_keys()


async def get_api_key(
        api_key_header: str = Depends(api_key_header),
):
    if api_key_header not in API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials"
        )
    return API_KEYS[api_key_header]

# Remember to call save_api_keys(API_KEYS) when updating the API_KEYS dictionary

```

Then you apply the auth to your endpoints like so:

```python
from auth import get_api_key


@app.get("/", response_model=SuccessResponse)
async def root(username: str = Depends(get_api_key)):
    return SuccessResponse(data={"message": f"Welcome to my python powered API, {username}!"})
```

In this structure, the `get_api_key` function acts as a dependency that FastAPI will call when a request is made to a
protected route. It will check the `access_token` header for a valid API key, validate it against the loaded API keys,
and return the associated username which you can then use within your route function.

### Authenticating with an API Key

To authenticate with the API, you need to pass your API key in the header of each request.

### Header Structure

The API key should be included in the headers as follows:

```
access_token: YOUR_API_KEY_HERE
```

Replace `YOUR_API_KEY_HERE` with your actual API key.

### Example with `curl`

Here is an example of making a request with `curl` using the API key:

```bash
curl -H "access_token: YOUR_API_KEY_HERE" https://api.yourdomain.com/protected-route
```

### Notes

- Ensure that you keep your API key secret.
- Do not expose your API key in publicly accessible areas such GitHub, client-side code, and so forth.
- If you believe your API key has been compromised, contact us immediately to issue a new one.

This documentation gives your users the necessary information to authenticate with your API using the custom
header `access_token`.
