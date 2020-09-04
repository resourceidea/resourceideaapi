import secrets
import string


def generate_random_string(size: int = 8, chars: str = string.ascii_lowercase + string.digits) -> str:
    """Generate a random string of a given size containing letters and digits"""
    random_string = ''.join(secrets.SystemRandom().choice(chars) for _ in range(size))
    return random_string
