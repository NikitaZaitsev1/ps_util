from abc import ABC, abstractmethod


class Information(ABC):
    info = {}
    template = '{}\n'

    @abstractmethod
    def get(self):
        ...

    @abstractmethod
    def _prepare(self):
        ...

    def show(self):
        self._prepare()
        print(self.template.format(**self.info))
