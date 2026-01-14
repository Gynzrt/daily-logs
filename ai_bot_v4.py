#!/usr/bin/env python3
"""
AI-Powered Autonomous Bot v4.0
Enhanced with Gemini AI for real content generation
Author: blogecoin
Features: AI learning notes, code challenges, smart patterns
"""

import json
import os
import random
from datetime import datetime, timezone
from pathlib import Path
import google.generativeai as genai

class AIBot:
    """AI-Powered bot with Gemini integration"""

    def __init__(self):
        self.config_file = Path("bot_config.json")
        self.log_file = Path("autonomous_logs.txt")
        self.status_file = Path("bot_status.json")
        self.readme_file = Path("README.md")

        # Directories
        self.notes_dir = Path("ai_notes")
        self.challenges_dir = Path("coding_challenges")
        self.snippets_dir = Path("ai_snippets")
        self.quotes_file = Path("daily_quotes.txt")

        # Load config
        self.config = self.load_config()

        # Initialize Gemini AI
        self.setup_gemini()

        # Learning topics pool
        self.learning_topics = [
            "Python async/await patterns",
            "Design patterns in Python",
            "Algorithm complexity analysis",
            "Git best practices",
            "REST API design principles",
            "Database indexing strategies",
            "Unit testing best practices",
            "Code refactoring techniques",
            "Security best practices",
            "Performance optimization"
        ]

        # Coding challenge types
        self.challenge_types = [
            "Array manipulation",
            "String processing",
            "Linked list operations",
            "Binary tree traversal",
            "Dynamic programming",
            "Hash table applications",
            "Graph algorithms",
            "Sorting algorithms",
            "Recursion problems",
            "Bit manipulation"
        ]

    def setup_gemini(self):
        """Setup Gemini AI with API key"""
        api_key = os.environ.get('GEMINI_API_KEY')
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
            self.ai_enabled = True
            print("AI Mode: ENABLED (Gemini 2.5 Flash)")
        else:
            self.ai_enabled = False
            print("AI Mode: DISABLED (fallback to templates)")

    def load_config(self):
        """Load bot configuration"""
        default_config = {
            "bot_name": "blogecoin Bot",
            "version": "4.0",
            "mode": "ai_enhanced",
            "commits_per_day": {"min": 2, "max": 5},
            "ai_features": {
                "learning_notes": True,
                "coding_challenges": True,
                "smart_patterns": True
            },
            "enabled": True
        }

        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                return {**default_config, **config}
            except Exception:
                pass

        self.config_file.write_text(json.dumps(default_config, indent=2), encoding='utf-8')
        return default_config

    def get_utc_timestamp(self):
        """Get current UTC timestamp"""
        return datetime.now(timezone.utc)

    def format_timestamp(self, dt):
        """Format timestamp for logs"""
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def ensure_directories(self):
        """Ensure all directories exist"""
        self.notes_dir.mkdir(exist_ok=True)
        self.challenges_dir.mkdir(exist_ok=True)
        self.snippets_dir.mkdir(exist_ok=True)

    def generate_ai_learning_note(self, topic):
        """Generate AI-powered learning note"""
        if not self.ai_enabled:
            return self.generate_fallback_note(topic)

        try:
            prompt = f"""Write a concise technical learning note about: {topic}

Requirements:
- 150-250 words
- Include practical examples
- Add key takeaways
- Use markdown format
- Be educational and actionable

Format:
# {topic}

## Overview
[Brief introduction]

## Key Concepts
[Main concepts with examples]

## Practical Example
[Code or real-world example]

## Key Takeaways
- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]
"""

            response = self.model.generate_content(prompt)
            return response.text

        except Exception as e:
            print(f"AI generation failed: {e}")
            return self.generate_fallback_note(topic)

    def generate_fallback_note(self, topic):
        """Fallback note when AI is unavailable"""
        return f"""# {topic}

## Overview
Exploring {topic.lower()} and its practical applications in modern software development.

## Key Concepts
Understanding the fundamental principles and best practices for implementing {topic.lower()}.

## Practical Example
```python
# Example implementation
def example():
    # TODO: Implement {topic.lower()}
    pass
```

## Key Takeaways
- Important for scalable applications
- Requires careful consideration
- Best learned through practice
"""

    def generate_ai_coding_challenge(self, challenge_type):
        """Generate AI-powered coding challenge solution"""
        if not self.ai_enabled:
            return self.generate_fallback_challenge(challenge_type)

        try:
            prompt = f"""Create a coding challenge and solution for: {challenge_type}

Requirements:
- Medium difficulty level
- Include problem description
- Provide Python solution with comments
- Add time/space complexity analysis
- Keep code under 30 lines

Format:
# Challenge: [Title]

## Problem
[Clear problem description]

## Solution
```python
[Well-commented Python code]
```

## Analysis
- Time Complexity: O(?)
- Space Complexity: O(?)

## Explanation
[Brief explanation of approach]
"""

            response = self.model.generate_content(prompt)
            return response.text

        except Exception as e:
            print(f"AI challenge failed: {e}")
            return self.generate_fallback_challenge(challenge_type)

    def generate_fallback_challenge(self, challenge_type):
        """Fallback challenge when AI is unavailable"""
        return f"""# Challenge: {challenge_type}

## Problem
Implement a solution for {challenge_type.lower()}.

## Solution
```python
def solve(arr):
    # TODO: Implement solution
    return arr
```

## Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## Explanation
Standard approach for {challenge_type.lower()}.
"""

    def update_ai_learning_note(self):
        """Create AI-generated learning note"""
        topic = random.choice(self.learning_topics)
        timestamp = self.get_utc_timestamp()
        date_str = timestamp.strftime("%Y-%m")

        notes_file = self.notes_dir / f"learning_{date_str}.md"

        print(f"Generating AI note: {topic}...")
        content = self.generate_ai_learning_note(topic)

        separator = "\n\n" + "="*60 + "\n\n"

        if notes_file.exists():
            with open(notes_file, 'a', encoding='utf-8') as f:
                f.write(separator)
                f.write(f"*Generated: {self.format_timestamp(timestamp)} UTC*\n\n")
                f.write(content)
        else:
            header = f"# AI Learning Notes - {date_str}\n\n"
            header += "*Auto-generated by AI Bot v4.0 using Gemini*\n\n"
            with open(notes_file, 'w', encoding='utf-8') as f:
                f.write(header)
                f.write(f"*Generated: {self.format_timestamp(timestamp)} UTC*\n\n")
                f.write(content)

        return str(notes_file)

    def update_coding_challenge(self):
        """Create AI-generated coding challenge"""
        challenge_type = random.choice(self.challenge_types)
        timestamp = self.get_utc_timestamp()
        date_str = timestamp.strftime("%Y-%m-%d")

        challenge_file = self.challenges_dir / f"challenge_{date_str}.md"

        print(f"Generating challenge: {challenge_type}...")
        content = self.generate_ai_coding_challenge(challenge_type)

        header = f"# Daily Coding Challenge - {date_str}\n\n"
        header += "*Auto-generated by AI Bot v4.0*\n\n"

        with open(challenge_file, 'w', encoding='utf-8') as f:
            f.write(header)
            f.write(content)

        return str(challenge_file)

    def update_main_log(self):
        """Update main autonomous logs"""
        utc_now = self.get_utc_timestamp()
        timestamp_str = self.format_timestamp(utc_now)

        if not self.log_file.exists():
            self.log_file.write_text(
                "# AI-Powered Autonomous Bot Logs\n"
                "# Version 4.0 - Gemini AI Enhanced\n\n",
                encoding='utf-8'
            )

        with open(self.log_file, 'a', encoding='utf-8') as f:
            mode = "AI" if self.ai_enabled else "Template"
            f.write(f"[{mode}] Update at {timestamp_str} UTC\n")

        return "autonomous_logs.txt"

    def is_weekday(self):
        """Check if today is weekday"""
        return self.get_utc_timestamp().weekday() < 5

    def should_skip_today(self):
        """Smart pattern: randomly skip some days"""
        # 5% chance to skip (simulate vacation/busy days)
        return random.random() < 0.05

    def get_commits_count(self):
        """Smart pattern: different commits on weekday/weekend"""
        if self.is_weekday():
            # Weekday: More active
            return random.randint(3, 5)
        else:
            # Weekend: Lighter activity
            return random.randint(1, 3)

    def update_status(self):
        """Update bot status file"""
        status = {
            "bot_name": self.config["bot_name"],
            "version": self.config["version"],
            "last_run": self.format_timestamp(self.get_utc_timestamp()),
            "status": "active",
            "mode": "ai_enhanced" if self.ai_enabled else "template",
            "total_runs": self.get_total_runs() + 1,
            "ai_enabled": self.ai_enabled
        }

        with open(self.status_file, 'w', encoding='utf-8') as f:
            json.dump(status, f, indent=2)

        print(f"Status updated: Run #{status['total_runs']}")

    def get_total_runs(self):
        """Get total number of runs"""
        if self.status_file.exists():
            try:
                with open(self.status_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return data.get('total_runs', 0)
            except Exception:
                pass
        return 0

    def update_readme(self):
        """Update README with AI stats"""
        stats = {
            "bot_name": self.config["bot_name"],
            "version": self.config["version"],
            "total_runs": self.get_total_runs() + 1,
            "last_run": self.format_timestamp(self.get_utc_timestamp()),
            "ai_mode": "Gemini AI" if self.ai_enabled else "Template Mode"
        }

        readme = f"""# AI-Powered Autonomous Bot v4.0

**Gemini AI Enhanced** - Real content generation

[![Bot Status](https://img.shields.io/badge/Bot-Active-success)](https://github.com/Gynzrt/daily-logs)
[![Version](https://img.shields.io/badge/Version-4.0-blue)](https://github.com/Gynzrt/daily-logs)
[![AI](https://img.shields.io/badge/AI-Gemini-purple)](https://github.com/Gynzrt/daily-logs)

## Live Statistics

```
Bot Name:        {stats['bot_name']}
Version:         {stats['version']}
Total Runs:      {stats['total_runs']}
AI Mode:         {stats['ai_mode']}
Last Update:     {stats['last_run']} UTC
Status:          ACTIVE
```

## v4.0 Features

### AI-Powered Content
- **Learning Notes**: AI-generated technical explanations
- **Coding Challenges**: Daily algorithm problems with solutions
- **Smart Patterns**: Weekday/weekend activity variance

### Technology
- **Gemini AI**: Google's latest AI model
- **Python 3.9**: Modern Python features
- **GitHub Actions**: Fully automated

### Content Quality
- Real educational value
- Unique AI-generated content
- Professional explanations
- Practical code examples

## Project Structure

```
auto-daily-logs/
├── ai_notes/           # AI learning notes
├── coding_challenges/  # Daily challenges
├── ai_snippets/        # AI code snippets
├── autonomous_logs.txt # Activity log
├── README.md           # This file (auto-updated)
└── ai_bot_v4.py        # AI bot core
```

## How It Works

1. **Gemini AI generates** real learning content
2. **Smart patterns** mimic natural developer behavior
3. **Multiple commits/day** with diverse content
4. **Fully autonomous** on GitHub Actions

---

**AI-Powered | Last updated: {stats['last_run']} UTC**
"""

        self.readme_file.write_text(readme, encoding='utf-8')
        return "README.md"

    def run(self):
        """Main bot execution"""
        if not self.config.get("enabled", True):
            print("Bot is disabled in configuration")
            return False

        print("=" * 50)
        print(f"AI Bot v{self.config['version']}")
        print(f"Mode: {'Gemini AI' if self.ai_enabled else 'Template'}")
        print("=" * 50)

        # Smart pattern: skip occasionally
        if self.should_skip_today():
            print("Smart skip: Simulating busy day")
            return True

        try:
            self.ensure_directories()
            modified_files = []

            # Core updates
            modified_files.append(self.update_main_log())
            modified_files.append(self.update_readme())

            # AI content generation
            ai_updates = []

            if self.config.get("ai_features", {}).get("learning_notes", True):
                ai_updates.append(self.update_ai_learning_note)

            if self.config.get("ai_features", {}).get("coding_challenges", True):
                ai_updates.append(self.update_coding_challenge)

            # Random selection
            num_updates = random.randint(1, len(ai_updates))
            selected = random.sample(ai_updates, num_updates)

            for update_func in selected:
                file_path = update_func()
                modified_files.append(file_path)
                print(f"Created: {file_path}")

            # Update status
            self.update_status()
            modified_files.append("bot_status.json")

            print(f"\nAI Bot completed successfully")
            print(f"Modified files: {len(modified_files)}")
            print(f"Files: {', '.join(modified_files)}")

            return True

        except Exception as e:
            print(f"AI Bot failed: {e}")
            import traceback
            traceback.print_exc()
            return False


def main():
    """Main execution"""
    bot = AIBot()
    success = bot.run()
    exit(0 if success else 1)


if __name__ == "__main__":
    main()
