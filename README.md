![The Recipe book](recipebook.jpg)

# The Recipe book
## About the project
This is a simple recipe-sharing web application, that is called "The Recipe book". I worked on this project to consolidate my understanding of the RESTful API and put my skills into practice.

This application provides a convenient API interface that allows you to manipulate user data - add and edit recipes, as well as search. There is also a system of user authentication using JWT, confirmation of registration using email. The API allows you to upload an image and output data using pagination and ordering.

Main technological features of this application:
- RESTful API
- Using CRUD method to verify storage
- Authentication services and security with JWT
- Email confirmation
- Working with images
- Pagination, searching, and ordering

## Packages used
|  Libraries             | Version  | Usage                                      |
|------------------------|----------|--------------------------------------------|
|[Flask][1]              |1.1.2     | Main Framework for Web Application         |
|[Flask-RESTful][2]      |0.3.8     | Support for quickly building REST APIs     |
|[Flask-SQLAlchemy][3]   |2.4.4     | Object Relational Mapper                   |
|[Flask-Migrate][4]      |2.5.3     | Handles SQLAlchemy database migrations     |
|[Flask-Caching][5]      |1.9.0     | Caching support                            |
|[Flask-JWT-Extended][6] |3.24.1    | Using JSON Web Tokens (JWT) to Flask       |
|[Flask-Reuploaded][7]   |0.3.2     | Uploading Image Avatar to the user profile |
|[Flask-Limiter][8]      |1.4       | Rate limiting features to flask routes     |
|[httpie][9]             |2.2.0     | HTTP client in order to test our APIs      |
|[psycopg2-binary][10]   |2.8.5     |  PostgreSQL adapter                        |
|[passlib][11]           |1.7.2     | Password hashing library                   |
|[marshmallow][12]       |3.7.1     | Serializing/Deserializing                  |
|[webargs][13]           |6.1.0     | Parsing and validating HTTP request objects|
|[itsdangerous][14]      |1.1.0     | Various helpers to pass data to untrusted environments and back                                           |
|[Pillow][15]            |7.2.0     | Refactoring and compressing images         |

## Examples of HTTP responses
### Login user
Endpoint: `````{{url}}/token`````
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTk3Njg4NzIsIm5iZiI6MTU5OTc2ODg3MiwianRpIjoiNzllMGVhZTUtOTcyMi00MjNmLWFkYTktZTVkNmEyYjVlZjE5IiwiZXhwIjoxNTk5NzY5NzcyLCJpZGVudGl0eSI6NSwiZnJlc2giOnRydWUsInR5cGUiOiJhY2Nlc3MifQ.Ef3_T0b_LZFkbIYKOgWDVx7S-Kqnwt4jcbAEjqnzdwE",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTk3Njg4NzIsIm5iZiI6MTU5OTc2ODg3MiwianRpIjoiY2VmZDA5YWMtOWU2NC00NjNlLWE1OWMtMzM0ZDZlMjk1ODQ2IiwiZXhwIjoxNjAyMzYwODcyLCJpZGVudGl0eSI6NSwidHlwZSI6InJlZnJlc2gifQ.c9zDAEj67FxAn2kKzHA7dPxkDmy8rDs-zIjrhVxMA_o"
}
```
### User detail
Endpoint: ```{{url}}/users/james```
```json
{
    "id": 5,
    "username": "james",
    "created_at": "2020-08-26T23:38:18.900389",
    "updated_at": "2020-08-26T23:38:18.900389",
    "avatar_url": "http://localhost:5000/static/images/assets/default_avatar.jpg"
}
```
### Get the recipe
Endpoint: ```{{url}}/recipes/8```
```json
{
    "id": 8,
    "name": "Cheese Pizza",
    "description": "This is a lovely cheese pizza",
    "num_of_servings": 2,
    "cook_time": 30,
    "directions": "This is how you make it",
    "ingredients": null,
    "is_publish": false,
    "cover_url": "http://localhost:5000/static/images/recipes/2efa8c8c-00ae-4b32-81a6-0a5ace2a1d43.jpg",
    "author": {
        "id": 7,
        "username": "john",
        "created_at": "2020-08-30T21:38:55.711128",
        "updated_at": "2020-08-30T21:38:55.711128",
        "avatar_url": "http://localhost:5000/static/images/avatars/ce8beb51-b2b0-40d5-be12-94e1222d655a.jpg"
    },
    "created_at": "2020-09-03T21:39:59.615800",
    "updated_at": "2020-09-03T21:43:56.777227"
}
```
### Get all recipes
Endpoint: ```{{url}}/recipes```
```json
{
    "links": {
        "first": "http://localhost:5000/recipes?page=1",
        "last": "http://localhost:5000/recipes?page=1"
    },
    "page": 1,
    "pages": 1,
    "per_page": 20,
    "total": 11,
    "data": [
        {
            "id": 18,
            "name": "Pesto Pizza",
            "description": "This is a lovely Pesto Pizza",
            "num_of_servings": 3,
            "cook_time": 30,
            "directions": "This is how you make it",
            "ingredients": "1 pre-baked pizza crust, 1/2 cup pesto, 1 ripe tomato",
            "is_publish": true,
            "cover_url": "http://localhost:5000/static/images/assets/default-recipe-cover.jpg",
            "author": {
                "id": 7,
                "username": "john",
                "created_at": "2020-08-30T21:38:55.711128",
                "updated_at": "2020-08-30T21:38:55.711128",
                "avatar_url": "http://localhost:5000/static/images/avatars/ce8beb51-b2b0-40d5-be12-94e1222d655a.jpg"
            },
            "created_at": "2020-09-06T00:38:20.194599",
            "updated_at": "2020-09-07T01:39:37.437151"
        }
            ]
}
```
## Email confirmation
![email_confirmation](email_confirmation.jpg)
## Book
[Python API Development Fundamentals](https://www.amazon.com/Python-API-Development-Fundamentals-application/dp/1838983996)

[1]: https://flask.palletsprojects.com/en/1.1.x/
[2]: https://flask-restful.readthedocs.io/en/latest/index.html
[3]: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
[4]: https://flask-migrate.readthedocs.io/en/latest/
[5]: https://flask-caching.readthedocs.io/en/latest/
[6]: https://flask-jwt-extended.readthedocs.io/en/stable/
[7]: https://github.com/jugmac00/flask-reuploaded
[8]: https://flask-limiter.readthedocs.io/en/stable/
[9]: https://httpie.org/
[10]: https://www.psycopg.org/
[11]: https://passlib.readthedocs.io/en/stable/
[12]: https://marshmallow.readthedocs.io/en/stable/index.html
[13]: https://webargs.readthedocs.io/en/latest/
[14]: https://itsdangerous.palletsprojects.com/en/1.1.x/
[15]: https://pillow.readthedocs.io/en/stable/