import socket
import os


def detect_client_location():
    """
    Open a UDP socket to a machine on the internet, to get the local IPv4 and IPv6
    addresses of the requesting client.
    Try to determine the sitename automatically from common environment variables,
    in this order: SITE_NAME, ATLAS_SITE_NAME, OSG_SITE_NAME. If none of these exist
    use the fixed string 'ROAMING'.
    """

    ip = '0.0.0.0'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        pass

    ip6 = '::'
    try:
        s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        s.connect(("2001:4860:4860:0:0:0:0:8888", 80))
        ip6 = s.getsockname()[0]
    except Exception:
        pass

    site = os.environ.get('SITE_NAME',
                          os.environ.get('ATLAS_SITE_NAME',
                                         os.environ.get('OSG_SITE_NAME',
                                                        'ROAMING')))

    return {'ip': ip,
            'ip6': ip6,
            'fqdn': socket.getfqdn(),
            'site': site}


print('location:', detect_client_location())
