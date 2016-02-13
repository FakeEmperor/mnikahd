
def merge_dicts(first: dict, second: dict):
    """ Merges b into a
    @param first dict Destination dictionary. This dictionary will hold the results
    @param second dict Another dictionary for merge
    """
    def merge(a, b, path: list = None):
        if path is None:
            path = []
        for key in b:
            if key in a:
                # Merge subdicts
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    merge(a[key], b[key], path + [str(key)])
                # Merge sublists
                elif not isinstance(a[key], str) and not isinstance(b[key], str):
                    a[key] += b[key]
                # same leaf value
                elif a[key] == b[key]:
                    pass
                else: # Not consistent
                    raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
            else:
                a[key] = b[key]
        return a

    return merge(first, second)
