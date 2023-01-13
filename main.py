# Strict-Transport-Security: max-age=<expire-time>
# Strict-Transport-Security: max-age=<expire-time>; includeSubDomains
# Strict-Transport-Security: max-age=<expire-time>; includeSubDomains; preload
# https://www.sentinelstand.com/article/http-strict-transport-security-hsts-canonical-www-redirects
#!/usr/bin/env python
"""
Determine whether a website supports HSTS.
"""

import requests
import sys


def has_hsts(site):
    """
    Connect to target site and check its headers."
    """
    try:
        req = requests.get('https://' + site)
    except requests.exceptions.SSLError as error:
        print ("doesn't have SSL working properly (%s)" % (error, ))
        return False
    if 'strict-transport-security' in req.headers:
        # print(req.headers)
        print("yes")
        return True
    else:
        print("no")
        return False


def main(site):
    """
    Main functionality.
    """
    print ('[+] checking whether %s supports HSTS...' % (site, ),)
    return has_hsts(site)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: %s [domains to check]' % (sys.argv[1], ))
        exit(1)

    for domain in sys.argv[1:]:
        main(domain)

    exit(0)



