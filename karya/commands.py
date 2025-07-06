"""
CLI commands for Karya
"""
import click
from datetime import datetime
from dateutil import parser

from .storage import load_tasks, save_tasks, get_next_task_id
from .models import STATUS_CODES, PRIORITY_CODES, STATUSES, PRIORITIES, TIME_FORMAT
from .parsers import parse_due_date
from .display import format_task_table, Fore


@click.command(name='add', short_help="Add a new task")
@click.argument('task_description')
@click.option('-d', '--due_date', type=str, help="Due date in 'YYYY-MM-DD HH:MM:SS'")
@click.option('-p', '--priority', default='2', help="Priority (1:high, 2:medium, 3:low)")
@click.option('-s', '--status', default='3', help="Status (0:Completed, 1:In Progress, 2:Backlog, 3:Yet to pick)")
def add_task(task_description, due_date, priority, status):
    """Add a new task to your karya list"""
    priority_str = PRIORITY_CODES.get(priority, 'medium')
    status_str = STATUS_CODES.get(status, 'Yet to pick')

    due_date_str = parse_due_date(due_date, priority_str).strftime(TIME_FORMAT)

    tasks = load_tasks()
    if any(t['description'] == task_description for t in tasks):
        click.confirm("Task with same description exists. Continue?", abort=True)

    now_str = datetime.now().strftime(TIME_FORMAT)
    task_data = {
        'id': get_next_task_id(tasks),
        'description': task_description,
        'due_date': due_date_str,
        'priority': priority_str,
        'status': status_str,
        'completed': status == '0',
        'completed_time': now_str if status == '0' else None,
        'created_time': now_str
    }

    tasks.append(task_data)
    save_tasks(tasks)
    click.echo(Fore.GREEN + f"[+] Task Added: '{task_description}' | Due: {due_date_str} | Priority: {priority_str} | Status: {status_str}")


@click.command(name='list', short_help="List all tasks")
@click.option('-s', '--status', type=click.Choice(STATUSES, case_sensitive=False), help="Filter by status")
@click.option('-p', '--priority', type=click.Choice(PRIORITIES, case_sensitive=False), help="Filter by priority")
@click.option('-d', '--due_date', type=str, help="Filter by due date (YYYY-MM-DD)")
@click.option('-c', '--completed', is_flag=True, help="Show only completed tasks")
@click.option('-a', '--all', is_flag=True, help="Show all tasks regardless of filters")
def list_tasks(status, priority, due_date, completed, all):
    """List your karya tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo(Fore.YELLOW + "No tasks found.")
        return

    # Filter out completed tasks by default (unless --all or --completed is used)
    if not all and not completed:
        tasks = [t for t in tasks if not t.get('completed', False)]

    if not all:
        if status:
            tasks = [t for t in tasks if t['status'].lower() == status.lower()]
        if priority:
            tasks = [t for t in tasks if t['priority'].lower() == priority.lower()]
        if due_date:
            try:
                due_date_obj = parser.parse(due_date)
                tasks = [t for t in tasks if parser.parse(t['due_date']).date() == due_date_obj.date()]
            except ValueError:
                click.echo(Fore.RED + "[!] Invalid due date format. Use 'YYYY-MM-DD'.")
                return
        if completed:
            tasks = [t for t in tasks if t.get('completed') == completed]

    if not tasks:
        click.echo(Fore.YELLOW + "No tasks match given filters.")
        return

    click.echo(format_task_table(tasks))


@click.command(name='delete', short_help="Delete task(s)")
@click.argument('task_ids', type=int, nargs=-1)
def delete_tasks(task_ids):
    """Delete one or more tasks by ID"""
    if not task_ids:
        click.echo(Fore.RED + "[!] No task IDs provided.")
        return

    tasks = load_tasks()
    id_set = set(task_ids)
    remaining = [t for t in tasks if t['id'] not in id_set]
    deleted_ids = id_set - {t['id'] for t in remaining}

    if not deleted_ids:
        click.echo(Fore.RED + "[!] No matching task IDs found.")
        return

    save_tasks(remaining)
    deleted_list = ', '.join(map(str, sorted(deleted_ids)))
    click.echo(Fore.RED + f"[-] Deleted task(s) with ID(s): {deleted_list}")


@click.command(name='update', short_help="Update task status")
@click.argument('task_id', type=int)
@click.option('-s', '--status', required=True, help="New status (0:Completed, 1:In Progress, 2:Backlog, 3:Yet to pick)")
def update_task(task_id, status):
    """Update the status of a task"""
    status_str = STATUS_CODES.get(status)
    if not status_str:
        click.echo(Fore.RED + "[!] Invalid status code.")
        return

    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status_str
            if status == '0':
                task['completed'] = True
                task['completed_time'] = datetime.now().strftime(TIME_FORMAT)
            else:
                task['completed'] = False
                task['completed_time'] = None
            save_tasks(tasks)
            click.echo(Fore.GREEN + f"[~] Task {task_id} updated to status '{status_str}'.")
            return
    click.echo(Fore.RED + f"[!] Task {task_id} not found.")