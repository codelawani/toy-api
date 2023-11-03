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
