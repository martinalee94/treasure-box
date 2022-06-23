import os 

MYSQL_SERVER_CONF = {
    'host' : os.getenv('MYSQL_ENDPOINT'),
    'port' : 3306,
    'user' : os.getenv('MYSQL_USER'),
    'password' : os.getenv('MYSQL_PASSWORD'),
    'db' : os.getenv('MYSQL_DB')    
}