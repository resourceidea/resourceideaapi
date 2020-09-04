from common.utils.string_generator import generate_random_string


def verify_name_slug(name_slug: str, usage_count: int) -> str:
    """Verify that name slug has not been used before.
       If used, concatenate the count to the name slug, making it unique."""
    if usage_count > 0:
        random_slug_suffix = generate_random_string(size=4)
        name_slug = f'{name_slug}-{random_slug_suffix}'

    return name_slug
