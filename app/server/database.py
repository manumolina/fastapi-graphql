from orator import DatabaseManager, Schema, Model

DATABASES = {
    'sqlite': {
        'driver': 'sqlite',
        'database': 'blog.db',
        'prefix': ''
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)