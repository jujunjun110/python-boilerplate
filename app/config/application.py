import yaml
from orator import DatabaseManager, Model


def entry():
    init_orator()


def init_orator():
    with open('./db/orator.yml') as f:
        config = yaml.load(f.read())
        db = DatabaseManager(config['databases'])
        Model.set_connection_resolver(db)
