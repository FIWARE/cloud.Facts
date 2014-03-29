__author__ = 'fla'

import redis
from package.mylist import mylist


class Redis(object):
    """ class to create lists on redis distribution. it is asumed
    that there is an installed version of redis in the localhost
    in the port 6379 (by default) and the server executed (redis-server).
    """
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.r.delete('prueba')

    def insert(self, data):
        ''' we need to check that data is a list and the exact number of
        element is equal to 4
        '''
        if isinstance(data, list) and len(data) == 4:
            self.r.rpush('prueba', data)
            self.r.ltrim('prueba', -5, -1)
        else:
            return "error"

    def range(self):
        return self.r.lrange('prueba', -100, 100)

    def media(self, lista):
        return self.sum(lista) / len(lista)

    def sum(self, lista):
        if len(lista) > 1:
            result = mylist.sum(lista)
            return result
        elif len(lista) == 1:
            return lista[0]
        else:
            return '[]'

    def delete(self):
        self.r.delete('prueba')
