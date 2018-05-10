from __future__ import with_statement
from contextlib import contextmanager

@contextmanager
def context():
     print ('entering the zone')
     try:
          yield
     except Exception:
        print ('with an error (%s)' % e)
        raise e
     else:
        print ('with no error')


context()
