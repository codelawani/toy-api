## Toy flask project

### Tasks
1. Create a "Users" table. A user has an ID (primary key), name, age, location
2. Create a POST method for adding new users to the table
3. Create a GET method with a query parameter (user id) for retrieving information about a specific user
4. Create a GET method for retrieving all the users from the database

### User model Snapshot (SQLAlchemy)
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

### User Endpoints
1. POST api/users: Create a new user
2. GET api/users?id=1: Get a user by id
3. GET api/users: Get all users


### How to run
1. Clone the repo
   ```bash
    git clone https://github.com/codelawani/toy-api.git
   ```
2. Create a virtual environment
   ```bash
    cd toy-api
    python3 -m venv venv
    source venv/bin/activate
   ```
3. Install the requirements
   ```bash
    pip install -r requirements.txt
   ```
4. Add env variables to a .env file - `DB_USER`, `DB_PASS`, `DB_HOST`, `DB_NAME`, `DB_PORT`
5. Run  db setup script `db_setup.sh` (make sure you have mysql installed and take a look at the script before running it)
   ```bash
    chmod +x db_setup.sh
    sudo ./db_setup.sh
   ```
6. Run the app
    ```bash
    python -m app.api
    ```
