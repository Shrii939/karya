"""
Date parsing utilities for Karya
"""
from datetime import datetime, timedelta
from dateutil import parser
import click

def parse_due_date(due_date_input_str, priority_str):
    """Parse natural language due dates"""
    now = datetime.now().replace(second=0, microsecond=0)
    if not due_date_input_str:
        return now + {
            'high': timedelta(hours=1),
            'medium': timedelta(hours=3),
            'low': timedelta(hours=5)
        }[priority_str]

    s = due_date_input_str.strip().lower()

    if s.upper().endswith(('MIN', 'M', 'MINUTE', 'MINUTES')):
        n = int(''.join(filter(str.isdigit, s)))
        return now + timedelta(minutes=n)

    if s.upper().endswith(('HR', 'H', 'HOUR', 'HOURS')):
        n = int(''.join(filter(str.isdigit, s)))
        return now + timedelta(hours=n)

    if s.upper() in ['TOMORROW', 'TOM', 'TMR']:
        return (now + timedelta(days=1)).replace(hour=9, minute=0)

    if s.upper().endswith(('DAY', 'D', 'DAYS')):
        n = int(''.join(filter(str.isdigit, s)))
        return now + timedelta(days=n)

    try:
        return parser.parse(s)
    except Exception:
        raise click.BadParameter(f"Unrecognized due date format: '{due_date_input_str}'")