import time

from models import Sample, Category
from backend.orm_backend import ORMBackend
from backend.raw_backend import RawBackend


class ConsoleApp:

	possible_extensions = ['mp3', 'wav', 'ogg', 'flac', 'aac', 'wma', 'm4a', 'aiff', 'alac', 'pcm']

	def __init__(self):
		self.backend = None
		self.sample_manager = SampleManager(self)

	def __set_backend_type(self, backend_type: str):
		if backend_type == 'raw':
			self.backend = RawBackend()
		elif backend_type == 'orm':
			self.backend = ORMBackend()
		else:
			raise ValueError('Unknown backend type')

	def _ask_for_backend_type(self):
		mode: str = ''
		while mode not in ('raw', 'orm'):
			mode = input('Choose connection mode (raw/orm): ')
		self.__set_backend_type(mode)
		print('Mode is successfully set to ', mode, '\n')

	@staticmethod
	def _draw_menu():
		print(
			'\nSample management:\n\n'
			'1. Get sample by name -->\n'
			'2. Add sample (+)\n'
			'3. Delete sample (-)\n'
			'4. List samples by category name -->\n\n'
			'Category management\n\n'
			'5. Add category (+)\n'
			'6. Delete category (-)\n'
			'0. Exit\n'
		)

	def run_operation(self):
		if not self.backend:
			self._ask_for_backend_type()
		self._draw_menu()
		choice = input('Choose an operation: ')

		match choice:
			case '1':
				self.sample_manager.get_sample_by_name()
			case '2':
				self.sample_manager.add_sample()
			case '3':
				self.sample_manager.delete_sample()
			case '4':
				self.sample_manager.get_samples_by_category()
			case '5':
				self.sample_manager.add_category()
			case '6':
				self.sample_manager.delete_category()
			case '0':
				print('Exiting...')
				return
			case _:
				print('Invalid choice!')
		self.run_operation()


class SampleManager:
	def __init__(self, console_app):
		self.backend = console_app.backend
		self._possible_extensions = console_app.possible_extensions

	def get_sample_by_name(self):
		sample_name = input('Enter sample name: ')
		sample = self.backend.get_sample(sample_name.lower())
		print(sample) if sample else print(f'Sample "{sample_name}" not found!')

	def add_sample(self):
		file_name = input('Enter correct file name with extension: ')
		category_id = None

		if self._validate_file_name(file_name):
			sample_name = file_name.split('.')[0]

			if self.backend.get_sample(sample_name.lower()):
				print(f'Sample "{sample_name}" already exists')
				time.sleep(1)
			else:
				if input('Want to specify category? (y/n): ').lower() in ('y', 'yes'):
					category = input('Enter category name: ')
					category_id = self.backend.get_category_id(category.lower())
				sample = Sample(
					sample_name=sample_name.lower(),
					extension=file_name.split('.')[-1],
					category_id=category_id if category_id else None
				)
				self.backend.add_sample(sample)
				print(f'Sample "{sample_name}" added')
				time.sleep(1)
		else:
			print(f'Incorrect file name: "{file_name}"')
			time.sleep(1)

	def delete_sample(self):
		sample_name = input('Enter sample name: ')
		sample = self.backend.get_sample(sample_name)

		if sample:
			self.backend.delete_sample(sample.id)
			print(f'Sample "{sample_name}" deleted')
			time.sleep(1)
		else:
			print(f'Sample "{sample_name}" not found')
			time.sleep(1)

	def get_samples_by_category(self):
		category_name = input('Enter category name: ')
		category_id = self.backend.get_category_id(category_name.lower())
		samples = self.backend.get_samples_by_category(category_id)
		if samples:
			number = 1
			for sample in samples:
				print(f'{number}. {sample.name}.{sample.extension}\n')
				number += 1
		else:
			print(f'No samples found for category "{category_name}"')
			time.sleep(1)

	def add_category(self):
		category_name = input('Enter category name: ')
		if not self.backend.get_category_id(category_name.lower()):
			category = Category(name=category_name)
			self.backend.add_category(category)
			print(f'Category "{category_name}" added')
			time.sleep(1)
		else:
			print(f'Category "{category_name}" already exists')
			time.sleep(1)

	def delete_category(self):
		category_name = input('Enter category name: ')
		category_id = self.backend.get_category_id(category_name.lower())
		if not category_id:
			print(f'Category "{category_name}" not found')
			time.sleep(1)
			return
		self.backend.delete_category(category_id)
		print(f'Category "{category_name}" deleted')
		time.sleep(1)

	def _validate_file_name(self, file_name: str):
		if len(file_name.split('.')) == 2 and file_name.split('.')[-1] in self._possible_extensions:
			return True
		else:
			return False


def library_controller():
	app = ConsoleApp()
	app.run_operation()


if __name__ == "__main__":
	library_controller()
