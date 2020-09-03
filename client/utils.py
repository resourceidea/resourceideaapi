from uuid import UUID

from rest_framework.reverse import reverse


def get_client_link_url(client_id: UUID) -> str:
    """Get the url link for the client whose ID has been supplied.

    Args:
        client_id(UUID): Client ID

    Returns:
        Client link url as a string.
    """
    link_url: str = reverse('client-detail', args=[client_id])
    return link_url
