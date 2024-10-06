from abc import ABC, abstractmethod


class BaseBackend(ABC):
    @abstractmethod
    def add_sample(self, sample, category_name):
        pass

    @abstractmethod
    def delete_sample(self, sample_id):
        pass

    @abstractmethod
    def get_sample(self, sample_id):
        pass

    @abstractmethod
    def get_samples_by_category(self, category_id):
        pass

    @abstractmethod
    def add_category(self, category):
        pass

    @abstractmethod
    def delete_category(self, category_id):
        pass

    @abstractmethod
    def get_category_id(self, category_name):
        pass
