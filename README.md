###  setup

## Prerequisites
.Python 3.8+
.PostgreSQL
.Pipenv
.Git

## install Flask and all dependencies required

#  clone the project
.set up the project by cloning git clone https://github.com/travinne/late-show-api-challenge.git
.then run 'cd late-show-api-challenge'  to access the project in your vs code.

# install dependencies
pipenv install flask, flask_sqlalchemy, flask_migrate, flask-jwt-extended, psycopg2-binar,y python-dotenv
.run 'pipenv shell' to get into  the environment.

### How to Run

## Apply Migrations
# Initialize and apply database migrations:
flask db init
flask db migrate -m "initial migration"
flask db upgrade

# Seed the Database
python server/seed.py

# run the application 
python run.py
The API runs on http://localhost:5000.

### Route List + Sample Request/Response

## Public Routes
# GET /episodes
.Request: curl http://localhost:5000/episodes
.Response: [{"id": 1, "date": "2025-06-22", "number": 101}, ...] (200)

# GET /episodes/
.Request: curl http://localhost:5000/episodes/1
.Response: {"id": 1, "date": "2025-06-22", "number": 101} (200)

## Protected Routes
# POST /appearances
Request: curl -X POST http://localhost:5000/appearances -H "Authorization:
Bearer <jwt-token>" -H "Content-Type: application/json" -d '{"rating": 5, "guest_id": 1, "episode_id": 1}'
Response: {"message": "Appearance added", "id": 1} (201)
# DELETE /episodes/
Request: curl -X DELETE http://localhost:5000/episodes/1 -H "Authorization: Bearer <jwt-token>"
Response: {"message": "Episode deleted"} (200)

### Postman Usage Guide
1. Import Collection: Import challenge-4-lateshow.postman_collection.json into Postman.
2. Set Environment: Create a new environment and set baseUrl to http://localhost:5000.
3. Test Endpoints:
    .Register: Send a POST request to /register with a JSON body {"username": "user1", "password": "pass123"}.
    .Login: Send a POST request to /login with the same credentials to get a token.
    .Protected Routes: Use the token in the Authorization header (e.g., Bearer <token>) for routes  like /    appearances or /episodes/1.
4. Verify Responses: Check the status codes and JSON responses match the expected output.

### GITHUB REPO LINK
https://github.com/travinne/Two-Late-Show.git