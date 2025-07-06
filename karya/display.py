"""
Display formatting and colors for Karya
"""
from colorama import init, Fore, Style
from tabulate import tabulate
from karya.models import COLOR_MAP

init(autoreset=True)

def format_task_table(tasks):
    """Format tasks into a colored table"""
    table = []
    for task in reversed(tasks):
        color = COLOR_MAP.get(task['status'], Fore.WHITE)
        row = [
            color + str(task['id']),
            color + task['description'],
            color + task['priority'],
            color + task['status'],
            color + task['due_date'],
            color + ('✔' if task.get('completed') else '✘'),
            color + (task.get('completed_time') or '-')
        ]
        table.append(row)   

    headers = [Style.BRIGHT + "ID", "Description", "Priority", "Status", "Due Date", "Done", "Completed Time"]
    return tabulate(table, headers=headers, tablefmt="fancy_grid")