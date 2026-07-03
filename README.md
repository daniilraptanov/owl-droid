```
     ,_,
    (O,O)
    (   )
    -"-"-
  OWL DROID
```

# owl-droid

**Owl Droid** is a local, terminal-first AI assistant powered by Ollama that boots with your system, understands your personal context, and helps you code, organize your workflow, and interact with your computer through extensible tools.

## Setup

Create a `.sh` file to launch the assistant (e.g. `owl-droid.sh`):

```bash
#!/bin/bash

konsole -e python3 /path/to/owl-droid/main.py
```

Replace `/path/to/owl-droid/` with the actual path to the project directory.

Make it executable:

```bash
chmod +x owl-droid.sh
```

Run in the your console:
```
ln -sf ~/path/to/owl-droid/owl-droid.sh   ~/.local/bin/owl 
```

And finally run:
```
owl
```

## Modules

Owl Droid uses pluggable context modules. Each module gathers data and feeds it into the greeting prompt.

---

### Time Context

```
   ,_,
  (O,O)
  (   )
  -"-"-
```

Provides current **time**, **date**, and **day phase** (morning / day / evening / night).

The assistant uses this to greet you naturally depending on the time of day.

- **File:** `src/modules/time_context.py`
- **Context keys:** `time`, `date`, `phase`

---

### Weather Context

```
  \._._./
  ( O,O )
  /(   )\
   -"-"-
```

Fetches current **weather** for configured coordinates via a pluggable provider.

Default provider: **Open-Meteo** (no API key required).

To swap the API — implement `BaseWeatherProvider` and pass it to `WeatherContextModule`.

- **File:** `src/modules/weather/weather_context.py`
- **Provider interface:** `src/modules/weather/provider.py`
- **Context keys:** `temperature`, `weather`, `wind_speed`
- **Config:** `LATITUDE`, `LONGITUDE` in `.env`

---

### Git Context

```
   ,_,
  (O,O)
  /   \
  └─  "-
```

Reads **git repository info** from the current working directory (read-only, never modifies the repo).

Shows current branch, last commit message, and count of modified / untracked files.

- **File:** `src/modules/git_context.py`
- **Context keys:** `git_branch`, `git_last_commit`, `git_modified`, `git_untracked`
- **Config:** `GIT_REPO_PATH` in `.env` (defaults to `cwd`)
