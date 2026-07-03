import time

import requests

from src.config import OLLAMA_URL, MODEL, WAIT_TIMEOUT_SEC, POLL_INTERVAL_SEC, QUIT_TIMEOUT_SEC


def wait_for_ollama():

    start = time.time()

    while True:

        try:
            r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=2)

            if r.status_code == 200:
                return

        except Exception:
            pass

        if time.time() - start > WAIT_TIMEOUT_SEC:
            raise TimeoutError("Ollama did not start.")

        time.sleep(POLL_INTERVAL_SEC)


def generate(prompt):

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "stream": False,
    }

    r = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json=payload,
        timeout=120,
    )

    r.raise_for_status()

    return r.json()["message"]["content"]


def handle_commands(context=None):
    if context is None:
        from src.context import get_default_context
        context = get_default_context()

    while True:
        try:
            user = input("\nowl> ").strip()

            if user in ("exit", "quit"):
                print("\nBye, friend!")
                time.sleep(QUIT_TIMEOUT_SEC)
                break

            if not user:
                continue

            prompt = context.build_prompt(user)
            answer = generate(prompt)
            print()
            print(answer)

        except KeyboardInterrupt:
            print("\nBye.")
            time.sleep(QUIT_TIMEOUT_SEC)
            break

