'''
This is seriously all there is.
'''
import dns.resolver


def can_hijack(domain):
    '''
    Check if domain is potentially hijackable.

    Args:
        domain (str): the hostname to check

    Returns:
        bool: The return value. True if hijacking probable, false otherwise.
    '''

    try:
        a = dns.resolver.query(domain)
    except dns.resolver.NXDOMAIN:
        #This domain just plain don't exist
        return False
    except dns.resolver.NoAnswer:
        #this domain MIGHT exist, let's do more stuff
        pass
    else:
        #This domain is clear
        return False

    try:
        a = dns.resolver.query(domain, 'CNAME')
    except dns.resolver.NoAnswer:
        return False
    else:
        return True


        

