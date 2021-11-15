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
    def test_myBranch_class(self):
        """
        Test creates a random array in memory, reads it into the branch and
        checks whether the mean is < 0.5. Depending whether it is or not,
        it writes the mean to another memory drop and compares the content
        with the independently calculated mean of the input array.
        """
        i = NullDROP("i", "i")  # just to be able to start the execution
        # create and configure the creation of the random array.
        a = RandomArrayApp("a", "a")
        a.integer = False
        a.high = 1
        m = InMemoryDROP("m", "m")  # the receiving drop
        b = MyBranch("b", "b")  # the branch drop
        n = InMemoryDROP("n", "n")  # the memory drop for the NO branch
        y = InMemoryDROP("y", "y")  # the memory drop for the YES branch

        # connect the graph nodes
        i.addConsumer(a)
        m.addProducer(a)
        m.addConsumer(b)
        b.addOutput(y)
        b.addOutput(n)

        # start the graph
        with droputils.DROPWaiterCtx(self, b, timeout=1):
            i.setCompleted()

        # read the array back from the intermediate memory drop
        data = pickle.loads(droputils.allDropContents(m))
        # calculate the mean
        mean = np.mean(data)

        # check which branch should have been taken
        t = [y if mean < 0.5 else n][0]
        while t.status < 2:
            # make sure the graph has reached this point
            # status == 2 is COMPLETED, anything above is not expected
            sleep(0.001)
        # load the mean from the correct branch memory drop
        res = pickle.loads(droputils.allDropContents(t))
        # and check whether it is the same as the calculated one
        self.assertEqual(res, mean)

    def test_myData_class(self):
        """
        Dummy getIO method test for data drop
        """
        assert MyDataDROP("a", "a").getIO() == "Hello from MyDataDROP"

    def test_myData_dataURL(self):
        """
        Dummy dataURL method test for data drop
        """
        assert MyDataDROP("a", "a").dataURL == "Hello from the dataURL method"
