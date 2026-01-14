#!/usr/bin/env python3
"""
🤖 Enhanced Autonomous Daily Logs Bot
Version 3.0 - Natural & Diverse Activity
Author: blogecoin
Features: Random timing, diverse content, multi-file commits, auto README
"""

import json
import os
import random
from datetime import datetime, timezone, timedelta
from pathlib import Path

class EnhancedBot:
    """🤖 Enhanced bot with natural behavior"""

    def __init__(self):
        self.config_file = Path("bot_config.json")
        self.log_file = Path("autonomous_logs.txt")
        self.status_file = Path("bot_status.json")
        self.readme_file = Path("README.md")

        # New feature files
        self.notes_dir = Path("notes")
        self.snippets_dir = Path("snippets")
        self.quotes_file = Path("daily_quotes.txt")

        # Load configuration
        self.config = self.load_config()

        # Content databases
        self.commit_messages = [
            "Update daily progress",
            "Add learning notes",
            "Document new insights",
            "Update code snippets",
            "Refactor documentation",
            "Add daily reflections",
            "Update knowledge base",
            "Enhance project structure",
            "Add productivity tips",
            "Update technical notes"
        ]

        self.quotes = [
            "Code is like humor. When you have to explain it, it's bad. - Cory House",
            "First, solve the problem. Then, write the code. - John Johnson",
            "The best error message is the one that never shows up. - Thomas Fuchs",
            "Clean code always looks like it was written by someone who cares. - Robert C. Martin",
            "Make it work, make it right, make it fast. - Kent Beck",
            "Simplicity is the soul of efficiency. - Austin Freeman",
            "Code never lies, comments sometimes do. - Ron Jeffries",
            "Testing leads to failure, and failure leads to understanding. - Burt Rutan",
            "A language that doesn't affect the way you think is not worth knowing. - Alan Perlis",
            "The only way to learn a new programming language is by writing programs in it. - Dennis Ritchie"
        ]

        self.learning_topics = [
            "Python async/await patterns",
            "Git workflow best practices",
            "Clean code principles",
            "Algorithm optimization techniques",
            "Design patterns overview",
            "API design guidelines",
            "Testing strategies",
            "Code review best practices",
            "Performance optimization tips",
            "Security best practices"
        ]

    def load_config(self):
        """📋 Load bot configuration"""
        default_config = {
            "bot_name": "blogecoin Bot",
            "version": "3.0",
            "mode": "enhanced_autonomous",
            "commits_per_day": {"min": 2, "max": 5},
            "enabled": True
        }

        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                return {**default_config, **config}
            except Exception:
                pass

        # Update config to v3.0
        self.config_file.write_text(json.dumps(default_config, indent=2), encoding='utf-8')
        return default_config

    def get_utc_timestamp(self):
        """⏰ Get current UTC timestamp"""
        return datetime.now(timezone.utc)

    def format_timestamp(self, dt):
        """📅 Format timestamp for logs"""
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def get_random_offset_time(self):
        """🎲 Get random time offset for natural commits"""
        # Random hour between 8 AM and 11 PM UTC
        hour = random.randint(8, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        return f"{hour:02d}:{minute:02d}:{second:02d}"

    def ensure_directories(self):
        """📁 Ensure all directories exist"""
        self.notes_dir.mkdir(exist_ok=True)
        self.snippets_dir.mkdir(exist_ok=True)

    def update_daily_quote(self):
        """💡 Add daily quote"""
        quote = random.choice(self.quotes)
        timestamp = self.format_timestamp(self.get_utc_timestamp())

        if not self.quotes_file.exists():
            self.quotes_file.write_text(f"# Daily Quotes & Inspiration\n\n", encoding='utf-8')

        with open(self.quotes_file, 'a', encoding='utf-8') as f:
            f.write(f"\n## {timestamp}\n{quote}\n")

        return "daily_quotes.txt"

    def update_learning_notes(self):
        """📚 Add learning notes"""
        topic = random.choice(self.learning_topics)
        timestamp = self.format_timestamp(self.get_utc_timestamp())
        date_str = self.get_utc_timestamp().strftime("%Y-%m")

        notes_file = self.notes_dir / f"learning_{date_str}.md"

        if not notes_file.exists():
            notes_file.write_text(f"# Learning Notes - {date_str}\n\n", encoding='utf-8')

        with open(notes_file, 'a', encoding='utf-8') as f:
            f.write(f"\n## {timestamp}\n")
            f.write(f"**Topic:** {topic}\n\n")
            f.write(f"Exploring {topic.lower()}. Key insights and practical applications.\n")

        return str(notes_file)

    def update_code_snippet(self):
        """💻 Add code snippet"""
        timestamp = self.get_utc_timestamp()
        date_str = timestamp.strftime("%Y-%m-%d")
        snippet_file = self.snippets_dir / f"snippet_{date_str}.py"

        snippets = [
            '# Python decorator example\ndef timer(func):\n    def wrapper(*args, **kwargs):\n        import time\n        start = time.time()\n        result = func(*args, **kwargs)\n        print(f"Time: {time.time()-start:.2f}s")\n        return result\n    return wrapper\n',
            '# List comprehension\nsquares = [x**2 for x in range(10)]\nprint(squares)\n',
            '# Context manager\nwith open("file.txt", "r") as f:\n    content = f.read()\n    print(content)\n',
            '# Lambda function\nsum_func = lambda a, b: a + b\nresult = sum_func(5, 3)\n',
            '# Dictionary comprehension\nsquared = {x: x**2 for x in range(5)}\nprint(squared)\n'
        ]

        snippet = random.choice(snippets)
        snippet_file.write_text(
            f"# Code Snippet - {date_str}\n# Auto-generated by Enhanced Bot\n\n{snippet}",
            encoding='utf-8'
        )

        return str(snippet_file)

    def update_main_log(self):
        """📝 Update main autonomous logs"""
        utc_now = self.get_utc_timestamp()
        timestamp_str = self.format_timestamp(utc_now)

        if not self.log_file.exists():
            self.log_file.write_text(
                "# Enhanced Autonomous Bot Logs\n"
                "# Version 3.0 - Natural & Diverse Activity\n\n",
                encoding='utf-8'
            )

        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"[OK] Update at {timestamp_str} UTC\n")

        return "autonomous_logs.txt"

    def update_readme_stats(self):
        """📊 Update README with live stats"""
        stats = self.get_current_stats()

        readme_content = f"""# 🤖 Enhanced Autonomous Daily Logs Bot

**Version 3.0 - Natural & Diverse Activity** 🚀

[![🤖 Bot Status](https://img.shields.io/badge/Bot-Active-success)](https://github.com/Gynzrt/daily-logs)
[![Version](https://img.shields.io/badge/Version-3.0-blue)](https://github.com/Gynzrt/daily-logs)

## 📊 Live Statistics

```
🤖 Bot Name:        {stats['bot_name']}
📈 Total Runs:      {stats['total_runs']}
⏱️  Uptime:          {stats['uptime_days']} days
📅 Last Update:     {stats['last_run']} UTC
🔥 Status:          {stats['status'].upper()}
```

## ✨ Features v3.0

### 🎯 Natural Behavior
- ✅ Random commit times (8 AM - 11 PM UTC)
- ✅ Multiple commits per day (2-5 commits)
- ✅ Diverse commit messages
- ✅ Multi-file updates

### 📚 Diverse Content
- 💡 **Daily Quotes** - Inspiration and wisdom
- 📝 **Learning Notes** - Tech insights and tips
- 💻 **Code Snippets** - Practical examples
- 📊 **Auto Stats** - Live metrics

### 🗂️ Project Structure

```
auto-daily-logs/
├── 📁 notes/              # Learning notes by month
├── 📁 snippets/           # Code snippets collection
├── 📝 autonomous_logs.txt # Main activity log
├── 💡 daily_quotes.txt    # Daily inspiration
├── 📊 README.md           # This file (auto-updated)
├── ⚙️  bot_config.json    # Bot configuration
└── 📈 bot_status.json     # Runtime statistics
```

## 🚀 How It Works

1. **GitHub Actions** triggers automatically
2. **Random timing** - commits at natural hours
3. **Multiple updates** - 2-5 commits per day
4. **Diverse content** - quotes, notes, snippets
5. **Auto stats** - README updates with metrics

## 📈 Activity Breakdown

- 📝 Main logs updated daily
- 💡 Random quote added
- 📚 Learning note documented
- 💻 Code snippet saved
- 📊 Stats auto-refreshed

## ⚙️ Configuration

Edit `bot_config.json` to customize:

```json
{{
  "bot_name": "{stats['bot_name']}",
  "version": "3.0",
  "commits_per_day": {{"min": 2, "max": 5}},
  "enabled": true
}}
```

## 🎯 Benefits

✅ **Natural patterns** - Looks like real activity
✅ **Diverse content** - Multiple file types
✅ **Auto maintenance** - Zero user intervention
✅ **Professional** - Clean, documented code
✅ **Insightful** - Real learning value

---

**🤖 100% Autonomous | Last updated: {stats['last_run']} UTC**
"""

        self.readme_file.write_text(readme_content, encoding='utf-8')
        print("README stats updated")
        return "README.md"

    def get_current_stats(self):
        """📈 Get current statistics"""
        stats = {
            "bot_name": self.config.get("bot_name", "Enhanced Bot"),
            "total_runs": self.get_total_runs(),
            "uptime_days": self.calculate_uptime(),
            "last_run": self.format_timestamp(self.get_utc_timestamp()),
            "status": "active"
        }
        return stats

    def get_total_runs(self):
        """📈 Get total number of runs"""
        if self.status_file.exists():
            try:
                with open(self.status_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return data.get('total_runs', 0)
            except Exception:
                pass
        return 0

    def calculate_uptime(self):
        """⏱️ Calculate bot uptime in days"""
        if not self.log_file.exists():
            return 0

        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]

            if len(lines) < 1:
                return 0

            # Parse first timestamp
            first_line = lines[0]
            if "at " in first_line:
                first_date_str = first_line.split("at ")[1].split(" UTC")[0]
                first_date = datetime.strptime(first_date_str, "%Y-%m-%d %H:%M:%S")
                current_date = self.get_utc_timestamp().replace(tzinfo=None)
                return (current_date - first_date).days
        except Exception:
            pass

        return 0

    def update_status(self):
        """📊 Update bot status file"""
        status = {
            "bot_name": self.config["bot_name"],
            "version": self.config["version"],
            "last_run": self.format_timestamp(self.get_utc_timestamp()),
            "status": "active",
            "mode": "enhanced_autonomous",
            "total_runs": self.get_total_runs() + 1,
            "uptime_days": self.calculate_uptime()
        }

        with open(self.status_file, 'w', encoding='utf-8') as f:
            json.dump(status, f, indent=2)

        print(f"Status updated: Run #{status['total_runs']}")

    def run(self):
        """🚀 Main enhanced bot execution"""
        if not self.config.get("enabled", True):
            print("Bot is disabled in configuration")
            return False

        print("=" * 50)
        print(f"Bot: {self.config['bot_name']} v{self.config['version']}")
        print(f"Mode: Enhanced Autonomous")
        print("=" * 50)

        try:
            # Ensure directory structure
            self.ensure_directories()

            modified_files = []

            # Core updates (always)
            modified_files.append(self.update_main_log())
            modified_files.append(self.update_readme_stats())

            # Random diverse content (select 1-2)
            content_updates = [
                self.update_daily_quote,
                self.update_learning_notes,
                self.update_code_snippet
            ]

            num_updates = random.randint(1, 2)
            selected_updates = random.sample(content_updates, num_updates)

            for update_func in selected_updates:
                file_path = update_func()
                modified_files.append(file_path)
                print(f"Updated: {file_path}")

            # Update status
            self.update_status()
            modified_files.append("bot_status.json")

            print("\nEnhanced operation completed successfully")
            print(f"Modified files: {len(modified_files)}")
            print(f"Files: {', '.join(modified_files)}")

            return True

        except Exception as e:
            print(f"Enhanced operation failed: {e}")
            import traceback
            traceback.print_exc()
            return False

def main():
    """Main execution function"""
    bot = EnhancedBot()
    success = bot.run()
    exit(0 if success else 1)

if __name__ == "__main__":
    main()
