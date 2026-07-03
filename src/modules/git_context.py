import subprocess

from src.modules.base import BaseModule


class GitContextModule(BaseModule):
    """Provides read-only git repository context (branch, status, last commit)."""

    def __init__(self, repo_path):
        self.repo_path = repo_path

    def _run(self, *args):
        """Run a read-only git command and return its stdout."""

        result = subprocess.run(
            ["git", "-C", self.repo_path, *args],
            capture_output=True,
            text=True,
            timeout=5,
        )

        if result.returncode != 0:
            return None

        return result.stdout.strip()

    def get_context(self):
        branch = self._run("rev-parse", "--abbrev-ref", "HEAD")

        last_commit = self._run("log", "-1", "--format=%s (%ar)")

        status_output = self._run("status", "--porcelain")

        modified = 0
        untracked = 0

        if status_output:
            for line in status_output.splitlines():
                if line.startswith("??"):
                    untracked += 1
                else:
                    modified += 1

        return {
            "git_branch": branch or "unknown",
            "git_last_commit": last_commit or "no commits",
            "git_modified": modified,
            "git_untracked": untracked,
        }

    def get_prompt_section(self, ctx):
        parts = [
            f"Git branch: {ctx['git_branch']}",
            f"Last commit: {ctx['git_last_commit']}",
        ]

        if ctx["git_modified"] or ctx["git_untracked"]:
            changes = []

            if ctx["git_modified"]:
                changes.append(f"{ctx['git_modified']} modified")

            if ctx["git_untracked"]:
                changes.append(f"{ctx['git_untracked']} untracked")

            parts.append(f"Changes: {', '.join(changes)}")

        return "\n".join(parts)
