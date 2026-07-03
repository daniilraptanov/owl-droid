#!/usr/bin/env python3

from src.context import get_time_context, build_prompt
from src.ollama import wait_for_ollama, generate, handle_commands


def main():

    print("[BOOT] Waiting for Ollama...")

    wait_for_ollama()

    print("[BOOT] Ollama online")

    ctx = get_time_context()

    prompt = build_prompt(ctx)

    print("[BOOT] Generating greeting...\n")

    response = generate(prompt)

    print("=" * 60)
    print(response)
    print("=" * 60)

    handle_commands()


if __name__ == "__main__":
    main()
