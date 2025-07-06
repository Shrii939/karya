"""
Data models and constants for Karya
"""
from datetime import datetime
from colorama import Fore

STATUS_CODES = {
    '0': 'Completed',
    '1': 'In Progress',
    '2': 'Backlog',
    '3': 'Yet to pick'
}

PRIORITY_CODES = {
    '1': 'high',
    '2': 'medium',
    '3': 'low'
}

STATUSES = list(STATUS_CODES.values())
PRIORITIES = list(set(PRIORITY_CODES.values()))

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

COLOR_MAP = {
    'Completed': Fore.GREEN,
    'In Progress': Fore.BLUE,
    'Backlog': Fore.RED,
    'Yet to pick': Fore.YELLOW
}