from src.config import LATITUDE, LONGITUDE, GIT_REPO_PATH
from src.modules.time_context import TimeContextModule
from src.modules.weather import WeatherContextModule, OpenMeteoProvider
from src.modules.git_context import GitContextModule


MODULES = [
    TimeContextModule(),
    WeatherContextModule(OpenMeteoProvider(), LATITUDE, LONGITUDE),
    GitContextModule(GIT_REPO_PATH),
]


class Context:
    """Manages Owl Droid context from pluggable context modules."""

    context: dict = {}

    def __init__(self, modules=None):
        if modules is None:
            self.modules = MODULES
        else:
            self.modules = modules

        self.context = {}
        self.update_context()

    def update_context(self) -> dict:
        """Fetch context from all registered modules and save to class and instance attributes."""
        ctx = {}
        for module in self.modules:
            ctx.update(module.get_context())

        self.context = ctx
        self.__class__.context = ctx
        return self.context

    def get_context(self, refresh: bool = False) -> dict:
        """Return the stored context dictionary, refreshing if requested or empty."""
        if refresh or not self.context:
            return self.update_context()
        return self.context

    def get_context_block(self, ctx=None) -> str:
        """Combine prompt sections from all modules into a single formatted block."""
        target_ctx = ctx if ctx is not None else self.context
        sections = [module.get_prompt_section(target_ctx) for module in self.modules]
        return "\n".join(sections)

    def build_greeting_prompt(self, ctx=None) -> str:
        """Build the boot greeting prompt."""
        context_block = self.get_context_block(ctx)
        return f"""
            You are Owl Droid. Current context:
                {context_block}
            Greet the user naturally.
            Mention each context item in one short sentence, naturally.
        """

    def build_prompt(self, user_input=None, ctx=None) -> str:
        """Build a prompt for general user queries with the current context included."""
        if isinstance(user_input, dict) and ctx is None:
            ctx = user_input
            user_input = ""
        elif user_input is None:
            user_input = ""

        context_block = self.get_context_block(ctx)

        if user_input:
            return f"""
                You are Owl Droid. Current context:
                    {context_block}
                User query:
                    {user_input}
                Respond to the user query naturally and helpfully based on the context.
            """
        else:
            return f"""
                You are Owl Droid. Current context:
                    {context_block}
            """


_default_context = None

def get_default_context() -> Context:
    global _default_context
    if _default_context is None:
        _default_context = Context()
    return _default_context

