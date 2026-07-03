import datetime

from src.modules.base import BaseModule


class TimeContextModule(BaseModule):
    """Provides current time, date, and day phase context."""

    def get_context(self):
        now = datetime.datetime.now()

        if 5 <= now.hour < 12:
            phase = "morning"
        elif 12 <= now.hour < 18:
            phase = "day"
        elif 18 <= now.hour < 23:
            phase = "evening"
        else:
            phase = "night"

        return {
            "time": now.strftime("%H:%M"),
            "date": now.strftime("%A, %d %B %Y"),
            "phase": phase,
        }

    def get_prompt_section(self, ctx):
        return (
            f"Time: {ctx['time']}\n"
            f"Date: {ctx['date']}\n"
            f"Phase: {ctx['phase']}"
        )
