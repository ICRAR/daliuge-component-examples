import pytest, unittest
import pickle

from dlg import droputils

from daliuge_component_examples import MyBranch, MyDataDROP
from dlg.apps.simple import RandomArrayApp
from dlg.drop import InMemoryDROP, NullDROP
from dlg.ddap_protocol import DROPStates
import logging
import numpy as np
from time import sleep

logger = logging.Logger(__name__)

given = pytest.mark.parametrize
class TestMyApps(unittest.TestCase):

    def test_myApp_class(self):
        i = NullDROP('i', 'i')
        a = RandomArrayApp('a', 'a')
        a.integer = False
        a.high = 1
        m = InMemoryDROP('m', 'm')
        b = MyBranch('b', 'b')
        n = InMemoryDROP('n', 'n')
        y = InMemoryDROP('y', 'y')
        i.addConsumer(a)
        m.addProducer(a)
        m.addConsumer(b)
        b.addOutput(y)
        b.addOutput(n)
        with droputils.DROPWaiterCtx(self, b, timeout=1):
            i.setCompleted()

        data = pickle.loads(droputils.allDropContents(m))
        mean = np.mean(data)
        t = [y if mean < 0.5 else n][0]
        while t.status < 2:
            sleep(0.001)
        res = pickle.loads(droputils.allDropContents(t))
        self.assertEqual(res, mean)

    def test_myData_class(self):
        assert MyDataDROP('a', 'a').getIO() == "Hello from MyDataDROP"

    def test_myData_dataURL(self):
        assert MyDataDROP('a', 'a').dataURL == "Hello from the dataURL method"