def remove_duplicates(alist):
    unique = list()
    for elt in alist:
        if not exists_in(elt,unique):
            unique.append(elt)            
    return unique

def exists_in(given_elt,alist):
    for elt in alist:
        if elt == given_elt:
            return True
    return False


