from base_backend import BaseBackend
from database.orm_connection import get_session, engine
from models import Sample, Category, Base


class ORMBackend(BaseBackend):
	def __init__(self):
		self.session = get_session()

	Base.metadata.create_all(engine)

	def get_sample(self, sample_id):
		with self.session as session:
			return session.query(Sample).get(sample_id)

	def get_samples_by_category(self, category_id):
		with self.session as session:
			session.query(Sample).filter_by(category_id=category_id)

	def add_sample(self, sample):
		with self.session as session:
			session.add(sample)
			session.commit()

	def delete_sample(self, sample_id):
		with self.session as session:
			session.query(Sample).filter_by(Sample.id == sample_id).delete()
			session.commit()

	def add_category(self, category):
		with self.session as session:
			session.add(category)
			session.commit()

	def delete_category(self, category_id):
		with self.session as session:
			samples = session.query(Sample).filter_by(Sample.category_id == category_id).all()
			for s in samples:
				s.category_id = None
			session.query(Category).filter_by(Category.id == category_id).delete()
			session.commit()
