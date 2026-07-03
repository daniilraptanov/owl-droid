from src.config import LATITUDE, LONGITUDE
from src.modules.time_context import TimeContextModule
from src.modules.weather import WeatherModule, OpenMeteoProvider


MODULES = [
    TimeContextModule(),
    WeatherModule(OpenMeteoProvider(), LATITUDE, LONGITUDE),
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

        Mention the current context naturally.

        Suggest up to three useful things to do.

        Keep the answer under one line sentence.
    """
