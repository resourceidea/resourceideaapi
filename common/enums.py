import enum


class Status(enum.Enum):
    """Status enumeration."""
    ACTIVE = 'ACTIVE'
    DISABLED = 'DISABLED'
    ARCHIVED = 'ARCHIVED'
    DELETED = 'DELETED'


class ProgressStatus(enum.Enum):
    """Enumeration indicates the different
    stages of the progress made on an engagement,
    job or task."""

    NOT_STARTED = 'NOT STARTED'
    RUNNING = 'RUNNING'
    IN_REVIEW = 'IN REVIEW'
    REVIEWED = 'REVIEWED'
    CLOSED = 'CLOSED'
