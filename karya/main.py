"""
Karya - A task manager that honors your work
Main entry point for the CLI application
"""
import click
from .commands import add_task, list_tasks, delete_tasks, update_task

@click.group(name='karya')
@click.version_option(version='0.1.0')
def main():
    """
    Karya - A task manager that honors your work

    In Sanskrit, Karya means work, duty, and purpose.
    """
    pass

# Add all commands to the main group
main.add_command(add_task, name='add')
main.add_command(list_tasks, name='list')
main.add_command(delete_tasks, name='delete')
main.add_command(update_task, name='update')

if __name__ == '__main__':
    main()