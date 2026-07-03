from abc import ABC, abstractmethod


class BaseModule(ABC):
    """Base class for all Owl Droid modules."""

    @abstractmethod
    def get_context(self):
        """Return a dict with context data for the prompt."""
        ...

    @abstractmethod
    def get_prompt_section(self, ctx):
        """Return a string to be included in the prompt."""
        ...
