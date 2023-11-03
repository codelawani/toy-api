#!/bin/bash

# To run this script
# sudo bash db_setup.sh

env_file=.env
if [ "$env_file" ]; then
    # shellcheck source=/dev/null
    source "$env_file"
else
    echo "Error: U need to create .env file"
    exit 1
fi
# set env variables
# DB_USER
# DB_PASS
# DB_NAME

mysql -e "DROP DATABASE IF EXISTS $DB_NAME;"

# Create project development database
mysql -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

# Create new user with privileges
mysql -e "CREATE USER IF NOT EXISTS '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASS';"

# Grant privileges to the new user
mysql -e "GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';"

#Allow user to observe db server performance metrics
mysql -e "GRANT SELECT ON performance_schema.* TO '$DB_USER'@'localhost';"

# Flush privileges
mysql -e "FLUSH PRIVILEGES;"
