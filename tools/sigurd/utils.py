

def get_class_by_path( kls ):
    '''
    Get class object by python path string
    See: http://stackoverflow.com/questions/452969/does-python-have-an-equivalent-to-java-class-forname
    '''
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m