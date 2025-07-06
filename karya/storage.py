"""
Task storage and file operations
"""
import json
import os

TASK_FILE = os.path.expanduser('karya_data.json')

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def get_next_task_id(tasks):
    """Get the next available task ID"""
    return 1 if not tasks else max(task['id'] for task in tasks) + 1