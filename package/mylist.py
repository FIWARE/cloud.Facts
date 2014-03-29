__author__ = 'fla'


class mylist(object):
    "store file metadata"
    def __init__(self, data=None):
        self.insert(data)

    def insert(self, data):
        if isinstance(data, list) == False:
            self.data = []
        else:
            if isinstance(data[0], list) or isinstance(data[0], int):
                self.data = data
            else:
                if isinstance(data[0], str):
                    p4 = []

                    for i in range(0, len(data)):
                        p3 = data[i].lstrip().replace('[','').replace(']','').split(',')

                        p3 = [int(j) for j in p3]

                        p4.append(p3)

                        self.data = p4

    def delete(self):
        self.data = []

    @staticmethod
    def sum(data):
        '''
        if len(data) > 1:
            return mylist(data[0]) + mylist.sum(data[1:])
        elif len(data) == 1:
            return mylist(data[0])
        else:
            return float(0)
        '''
        aux = mylist(data).get()
        if len(aux) > 1:
            return mylist(aux[0]) + mylist.sum(data[1:])
        elif len(aux) == 1:
            return mylist(aux[0])
        else:
            return float(0)

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        """ add the values of the list except the first one,
        """
        if isinstance(other, mylist):
            result = mylist()
            result.data = self.data

            for i in range(1, len(self.data)-1):
                result.data[i] = self.data[i] + other.data[i]

            return result

    def __div__(self, other):
        """ div the list by a integer number
        """
        if isinstance(other, int):
            result = mylist(self.data)
            #result.data = self.data
            for i in range(1, len(self.data)-1):
                result.data[i] = self.data[i] / float(other)

            return result


    def get(self):
        return self.data

    @classmethod
    def isdata(self, data):
        '''check that data is a valid data'''
        if isinstance(data, mylist) and isinstance(data.get(), list):
            if len(data) == 4:
                return True
            else:
                return False
        else:
            return False
