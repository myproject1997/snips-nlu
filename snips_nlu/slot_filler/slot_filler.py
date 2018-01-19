from abc import ABCMeta, abstractmethod

from snips_nlu.pipeline.processing_unit import ProcessingUnit


class SlotFiller(ProcessingUnit):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_slots(self, text):
        raise NotImplementedError

    @abstractmethod
    def fit(self, dataset, intent):
        raise NotImplementedError