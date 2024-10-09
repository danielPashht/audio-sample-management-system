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


# Request example:
# @_add_cursor_wrapper
# def get_library_books(cur, library_id):
#     cur.execute(
#         '''
#         SELECT id, library_id, title, author, status FROM book
#         WHERE library_id = %s
#         ''',
#         (library_id,)
#     )
#     return cur.fetchall()


class RawBackend(BaseBackend):

	def __init__(self):
		# create tables if not exist
		self._populate_default_categories()

	@_add_cursor_wrapper
	def _populate_default_categories(self, cur):
		pass

	@_add_cursor_wrapper
	def get_sample(self, cur,  name):
		pass

	@_add_cursor_wrapper
	def get_samples_by_category(self, cur, category_id):
		pass

	@_add_cursor_wrapper
	def add_sample(self, cur, sample, category_name):
		pass

	@_add_cursor_wrapper
	def delete_sample(self, cur, sample_name):
		pass

	@_add_cursor_wrapper
	def add_category(self, cur, category):
		pass

	@_add_cursor_wrapper
	def delete_category(self, cur, category_id):
		pass

	@_add_cursor_wrapper
	def get_category_id(self, cur, category_name):
		pass
