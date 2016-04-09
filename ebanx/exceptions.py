
class InvalidEnvironmentException(Exception):
    def __init__(self,*args,**kwargs):
        super(InvalidEnvironmentException, self).__init__("Invalid environment '%s', valid values are: sandbox or production" % kwargs['environment'])
