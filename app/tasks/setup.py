import yaml
import pymysql
from config import application

application.entry()

with open('./db/orator.yml') as f:
    config = yaml.load(f.read())['databases']['mysql']
    conn = pymysql.connect(
        host=config['host'],
        user=config['user'],
        password=config['password']
    )
    query = 'create database if not exists {}'.format(config['database'])
    conn.cursor().execute(query)
