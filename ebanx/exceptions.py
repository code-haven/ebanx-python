
class InvalidEnvironmentException(Exception):
    def __init__(self,*args,**kwargs):
        print(args)
        print(kwargs)
        Exception.__init__(self, "Invalid environment '%s', valid values are: sandbox or production" % kwargs['environment'])
