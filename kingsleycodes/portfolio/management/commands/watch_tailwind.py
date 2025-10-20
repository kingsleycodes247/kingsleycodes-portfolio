import subprocess
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.management.base import BaseCommand

class TailwindEventHandler(FileSystemEventHandler):
    def __init__(self, css_input, css_output):
        self.css_input = css_input
        self.css_output = css_output

    def on_any_event(self, event):
        if event.src_path.endswith(('.html', '.css', '.js', '.py')):
            print("🔄 Change detected — rebuilding Tailwind CSS...")
            try:
                subprocess.run([
                    "npx", "tailwindcss",
                    "-i", self.css_input,
                    "-o", self.css_output,
                    "--minify"
                ], check=True)
                print("✅ Tailwind rebuilt successfully!")
            except Exception as e:
                print(f"❌ Tailwind rebuild failed: {e}")

class Command(BaseCommand):
    help = "Watch project files and rebuild Tailwind CSS on changes."

    def handle(self, *args, **options):
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        css_input = os.path.join(project_root, "src", "input.css")
        css_output = os.path.join(project_root, "portfolio", "static", "css", "styles.css")

        event_handler = TailwindEventHandler(css_input, css_output)
        observer = Observer()
        observer.schedule(event_handler, path=project_root, recursive=True)

        print("👀 Watching for changes... (Press CTRL+C to stop)")
        observer.start()

        try:
            while True:
                pass
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
