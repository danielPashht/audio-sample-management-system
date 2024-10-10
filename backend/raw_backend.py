from backend.base_backend import BaseBackend
from constants import DEFAULT_CATEGORIES
from database.connection import RawDBConnect
from constants import DB_DATA


db = RawDBConnect(**DB_DATA)


def _add_cursor_wrapper(func):
	def wrapper(*args, **kwargs):
		with db.get_connection().cursor() as cur:
			return func(cur, *args, **kwargs)

	return wrapper


class RawBackend(BaseBackend):

	def __init__(self):
		# create tables if not exist
		self._populate_default_categories()

	@_add_cursor_wrapper
	def _populate_default_categories(self, cur):
		cur.execute(
			'''
			CREATE TABLE IF NOT EXISTS category (
				id SERIAL PRIMARY KEY,
				name VARCHAR(255) NOT NULL UNIQUE
			)
			'''
		)
		cur.execute(
			f'''
			INSERT INTO category (id, name) VALUES
			    (1, 'mp3'),
			    (2, 'wav'),
			    (3, 'ogg'),
			    (4, 'flac'),
			    (5, 'aac'),
			    (6, 'wma'),
			    (7, 'm4a'),
			    (8, 'aiff'),
			    (9, 'alac'),
			    (10, 'pcm');
            '''
		)

	@_add_cursor_wrapper
	def get_sample(self, cur, name):
		cur.execute(
			'''
			SELECT name, category_id FROM sample
			WHERE name = %s
			''',
			(name,)
		)
		cur.fetchone()

	@_add_cursor_wrapper
	def get_samples_by_category(self, cur, category_id):
		cur.execute(
			'''
			SELECT name FROM sample
			WHERE category_id = %s
			''',
			(category_id,)
		)
		cur.fetchall()

	@_add_cursor_wrapper
	def add_sample(self, cur, sample, category_name):
		cur.execute(
			'''
			INSERT INTO sample (name, category_id)
			VALUES (%s, %s)
			''',
			(sample, category_name)
		)

	@_add_cursor_wrapper
	def delete_sample(self, cur, sample_name):
		cur.execute(
			'''
			DELETE FROM sample
			WHERE name = %s
			''',
			(sample_name,)
		)

	@_add_cursor_wrapper
	def add_category(self, cur, category):
		cur.execute(
			'''
			INSERT INTO category (name)
			VALUES (%s)
			''',
			(category,)
		)

	@_add_cursor_wrapper
	def delete_category(self, cur, category_id):
		cur.execute(
			'''
			DELETE FROM category
			WHERE id = %s
			''',
			(category_id,)
		)

	@_add_cursor_wrapper
	def get_category_id(self, cur, category_name):
		cur.execute(
			'''
			SELECT id FROM category
			WHERE name = %s
			''',
			(category_name,)
		)
		cur.fetchone()
