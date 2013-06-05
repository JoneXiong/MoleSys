"""Test the ThreadingLocal module."""

__version__ = '1.1'
__revision__ = "$Rev: 8218 $"
__date__ = "$Date: 2011-08-14 13:57:11 +0200 (So, 14. Aug 2011) $"


import sys
from threading import Thread
import unittest

sys.path.insert(1, '../..')
from DBUtils.ThreadingLocal import local


class TestThreadingLocal(unittest.TestCase):

    def test0_GetAttr(self):
        mydata = local()
        mydata.number = 42
        self.assertEqual(mydata.number, 42)

    def test1_Dict(self):
        mydata = local()
        mydata.number = 42
        self.assertEqual(mydata.__dict__, {'number': 42})
        mydata.__dict__.setdefault('widgets', [])
        self.assertEqual(mydata.widgets, [])

    def test2_ThreadLocal(self):
        def f():
            items = mydata.__dict__.items()
            items.sort()
            log.append(items)
            mydata.number = 11
            log.append(mydata.number)
        mydata = local()
        mydata.number = 42
        log = []
        thread = Thread(target=f)
        thread.start()
        thread.join()
        self.assertEqual(log, [[], 11])
        self.assertEqual(mydata.number, 42)

    def test3_SubClass(self):
        class MyLocal(local):
            number = 2
            initialized = 0
            def __init__(self, **kw):
                if self.initialized:
                    raise SystemError
                self.initialized = 1
                self.__dict__.update(kw)
            def squared(self):
                return self.number ** 2
        mydata = MyLocal(color='red')
        self.assertEqual(mydata.number, 2)
        self.assertEqual(mydata.color, 'red')
        del mydata.color
        self.assertEqual(mydata.squared(), 4)
        def f():
            items = mydata.__dict__.items()
            items.sort()
            log.append(items)
            mydata.number = 7
            log.append(mydata.number)
        log = []
        thread = Thread(target=f)
        thread.start()
        thread.join()
        self.assertEqual(log,
            [[('color', 'red'), ('initialized', 1)], 7])
        self.assertEqual(mydata.number, 2)
        self.assert_(not hasattr(mydata, 'color'))
        class MyLocal(local):
            __slots__ = 'number'
        mydata = MyLocal()
        mydata.number = 42
        mydata.color = 'red'
        thread = Thread(target=f)
        thread.start()
        thread.join()
        self.assertEqual(mydata.number, 7)


if __name__ == '__main__':
    unittest.main()
