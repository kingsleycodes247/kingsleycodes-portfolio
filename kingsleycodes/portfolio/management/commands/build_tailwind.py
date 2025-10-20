import subprocess
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = "Compile Tailwind CSS automatically"

    def handle(self, *args, **kwargs):
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        css_input = os.path.join(project_root, "src", "input.css")
        css_output = os.path.join(project_root, "portfolio", "static", "css", "styles.css")

        try:
            self.stdout.write(self.style.NOTICE("⚙️  Building Tailwind CSS..."))
            subprocess.run([
                "npx", "tailwindcss",
                "-i", css_input,
                "-o", css_output,
                "--minify"
            ], check=True)
            self.stdout.write(self.style.SUCCESS("✅ Tailwind CSS compiled successfully!"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(
                "❌ 'npx' not found. Please install Node.js or run Tailwind manually."))
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR(f"❌ Tailwind build failed: {e}"))
