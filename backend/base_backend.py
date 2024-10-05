from abc import ABC, abstractmethod


class BaseBackend(ABC):
    @abstractmethod
    def add_sample(self):
        pass

    @abstractmethod
    def delete_sample(self):
        pass

    @abstractmethod
    def get_sample(self):
        pass

    @abstractmethod
    def get_samples_by_category(self):
        pass
