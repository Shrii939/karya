# Karya 🎯

> A task manager that honors your work  
> 
> *In Sanskrit, Karya means work, duty, and purpose.*

---

## ✨ Features

- **Natural language due dates**: Add tasks with intuitive due dates like `2hr`, `tomorrow`, `3days`, etc.
- **Smart priorities**: Choose from High, Medium, Low — each with its own default due duration.
- **Color-coded output**: Terminal output uses intuitive color mapping for task statuses.
- **Flexible filtering**: List tasks by status, priority, due date, or completion.
- **Batch operations**: Delete or update multiple tasks easily.
- **Persistent storage**: Tasks are saved to a JSON file by default.
- **Extensible design**: Structured CLI with Click, easy to migrate to database later.
- **Cultural touch**: Inspired by Sanskrit, "Karya" brings purpose-driven task tracking.

---

## 🚀 Installation

### From PyPI (Coming Soon)

```bash
pip install karya
```

### From Source

```bash
git clone https://github.com/Shrii939/karya
cd karya
pip install -e .
```

---

## 🔧 Usage

Once installed, use the `karya` command:

### Add a Task

```bash
karya add "Buy groceries" -p 2 -d tomorrow
```

### List Tasks

```bash
karya list
```

### Filter Tasks

```bash
karya list -p high -s "In Progress"
```

### Mark Task Complete

```bash
karya update 4 -s 0
```

### Delete Task(s)

```bash
karya delete 4 5 6
```

---

## 🧠 CLI Options Overview

- **`add`**: Add a task
- **`list`**: List tasks
- **`update`**: Complete or update status
- **`delete`**: Delete task(s)

### Priority Levels

| Code | Level   |
|------|---------|
| 1    | High    |
| 2    | Medium  |
| 3    | Low     |

### Status Codes

| Code | Status        |
|------|---------------|
| 0    | Completed     |
| 1    | In Progress   |
| 2    | Backlog       |
| 3    | Yet to pick   |

---

## 🛠 Future Improvements

- PostgreSQL or SQLite backend support
- UI (TUI/GUI) integration
- AI-enhanced task analysis (MCP protocol support)
- Export/import tasks
- Notification reminders

---

## 📄 License

MIT [LICENSE](./LICENSE) © 2025 Shridhar S Sherugar