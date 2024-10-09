from fuzzywuzzy import process

from backend.base_backend import BaseBackend
from database.orm_connection import get_session, engine
from models import Sample, Category, Base
from constants import DEFAULT_CATEGORIES


class ORMBackend(BaseBackend):
	def __init__(self):
		Base.metadata.create_all(engine)
		self._populate_default_categories()

	@staticmethod
	def _populate_default_categories():
		with get_session() as session:
			if not session.query(Category).first():
				for category_name in DEFAULT_CATEGORIES.strip():
					category = Category(name=category_name)
					session.add(category)

	def get_sample(self, name):
		with get_session() as session:
			sample = session.query(Sample).filter_by(name=name).first()
			if sample:
				session.refresh(sample)  # Ensure the sample is bound to the session
				return sample
			else:
				return None

	def get_samples_by_category(self, category_id):
		with get_session() as session:
			session.query(Sample).filter_by(category_id=category_id)

	def add_sample(self, sample, category_name):
		with get_session() as session:
			if category_name:
				categories = [category.name for category in session.query(Category).all()]
				best_match, score = process.extractOne(category_name, categories)
				if score >= 70:
					category = session.query(Category).filter_by(name=best_match).first()
					sample.category_id = category.id if category else None
			session.add(sample)
			session.commit()
			return category.name if category else None

	def delete_sample(self, sample_name):
		with get_session() as session:
			session.query(Sample).filter(Sample.name == sample_name).delete()
			session.commit()

	def add_category(self, category):
		with get_session() as session:
			session.add(category)
			session.commit()

	def delete_category(self, category_id):
		with get_session() as session:
			samples = session.query(Sample).filter_by(Sample.category_id == category_id).all()
			for s in samples:
				s.category_id = None
			session.query(Category).filter_by(Category.id == category_id).delete()
			session.commit()

	def get_category_id(self, category_name):
		with get_session() as session:
			return session.query(Category).filter_by(name=category_name).first()
