#!/usr/bin/env python3

from src.context import Context
from src.ollama import wait_for_ollama, generate, handle_commands


BANNER = r"""
         ,_,
        (O,O)
        (   )
        -"-"-
      OWL DROID
"""


def main():

    print(BANNER)

    print("[BOOT] Waiting for Ollama...")

    wait_for_ollama()

    print("[BOOT] Ollama online")

    context = Context()

    prompt = context.build_greeting_prompt()

    print("[BOOT] Generating greeting...\n")

    response = generate(prompt)

    print("=" * 60)
    print(response)
    print("=" * 60)

    handle_commands(context)


if __name__ == "__main__":
    main()
