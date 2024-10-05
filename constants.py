DB_DATA = {
    'host': 'localhost',
    'dbname': 'audio_sample_library',
    'user': 'postgres',
    'password': '946815',
}

DB_URL = 'postgresql://{user}:{password}@{host}:5432/{dbname}'.format(**DB_DATA)
