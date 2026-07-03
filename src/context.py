from src.config import LATITUDE, LONGITUDE, GIT_REPO_PATH
from src.modules.time_context import TimeContextModule
from src.modules.weather import WeatherContextModule, OpenMeteoProvider
from src.modules.git_context import GitContextModule


MODULES = [
    TimeContextModule(),
    WeatherContextModule(OpenMeteoProvider(), LATITUDE, LONGITUDE),
    GitContextModule(GIT_REPO_PATH),
]


def get_time_context():
    ctx = {}

    for module in MODULES:
        ctx.update(module.get_context())

    return ctx


def build_prompt(ctx):
    sections = []

    for module in MODULES:
        sections.append(module.get_prompt_section(ctx))

    context_block = "\n".join(sections)

    return f"""
        You are Owl Droid.

        Current context:

        {context_block}

        Greet the user naturally.

        Mention each context item in one short sentence, naturally.
    """
