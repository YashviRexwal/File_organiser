# File Organiser 🗂️

A Python CLI tool that automatically sorts files in any folder into subfolders by file type — so you never have a messy Downloads folder again.

---

## What it does

Run one command → every file gets moved into the right subfolder automatically.

```
Downloads/
├── report.pdf        →    Documents/report.pdf
├── photo.jpg         →    Images/photo.jpg
├── song.mp3          →    Audio/song.mp3
├── script.py         →    Code/script.py
├── video.mp4         →    Videos/video.mp4
└── archive.zip       →    Archives/archive.zip
```

A log file is saved every time you run it — so you always know what moved where.

---

## Why I built this

This is my Week 1 project while learning MLOps and automation from scratch.

The goal was to practise: Python file handling, the `os` and `shutil` modules, JSON config files, logging, and writing clean reusable functions — skills that directly apply to building data pipelines and ML infrastructure.

---

## How to use it

**1. Clone the repo**
```bash
git clone https://github.com/YashviRexwal/File_organiser.git
cd file-organiser
```

**2. Organise your Downloads folder (default)**
```bash
python organiser.py
```

**3. Organise any folder you choose**
```bash
python organiser.py /path/to/your/folder
```

---

## Customise the rules

Open `config/config.json` and add or change file extensions to your liking:

```json
{
  "rules": {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images":    [".jpg", ".png", ".gif"],
    "Code":      [".py", ".js", ".html"]
  }
}
```

Any file type not listed goes into an `Others/` folder automatically.

---

## Project structure

```
file-organiser/
├── organiser.py        # main script
├── config/
│   └── config.json     # file type rules (customisable)
├── logs/               # auto-created, stores run logs
└── README.md
```

---

## What I learned building this

- How Python's `pathlib` and `shutil` modules work for file system operations
- How to separate configuration from code using JSON files
- How to add proper logging so scripts are debuggable in production
- How to handle edge cases — duplicate filenames, hidden files, missing folders

---

## What's next

This project is part of my MLOps learning journey. Next I'll be containerising a machine learning model with Docker and deploying it to AWS.

Follow my progress on LinkedIn → [https://www.linkedin.com/in/yashvi-rexwal-7823b4405/]
Read my weekly blog → [https://hashnode.com/@yashvirexwal]

---

## Tech used

- Python 3.x
- Standard library only — no installs needed (`os`, `shutil`, `pathlib`, `logging`, `json`)