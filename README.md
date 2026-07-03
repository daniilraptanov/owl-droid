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
