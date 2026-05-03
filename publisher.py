import os
import subprocess
from datetime import datetime

class TechIdeasPublisher:
    def __init__(self, local_dir="."):
        self.local_dir = local_dir
        # In GitHub Actions, we don't need a token in the URL if we use actions/checkout
        # and configure git user. But for simplicity, we'll keep the logic.
        self.token = os.getenv("GITHUB_TOKEN")

    def _run_git(self, args):
        result = subprocess.run(["git"] + args, cwd=self.local_dir, capture_output=True, text=True)
        return result

    def publish(self, idea_html_fragment):
        index_path = os.path.join(self.local_dir, "index.html")
        
        if not os.path.exists(index_path):
            return False

        with open(index_path, "r") as f:
            content = f.read()

        marker = "<!-- IDEAS_START -->"
        if marker not in content:
            return False

        updated_content = content.replace(marker, f"{marker}\n{idea_html_fragment}")

        with open(index_path, "w") as f:
            f.write(updated_content)

        # Git configuration (needed for GitHub Actions)
        self._run_git(["config", "user.name", "Gemini AI"])
        self._run_git(["config", "user.email", "gemini-ai@example.com"])

        # Git operations
        self._run_git(["add", "index.html"])
        self._run_git(["commit", "-m", f"Add new tech idea - {datetime.now().strftime('%Y-%m-%d')}"])
        
        # In GitHub Actions, we can just push
        res = self._run_git(["push"])
        return res.returncode == 0
