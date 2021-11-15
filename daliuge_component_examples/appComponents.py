"""
daliuge_component_examples appComponent module.

This is the module of daliuge_component_examples containing DALiuGE
application components.
Here you put your main application classes and objects.

Typically a component project will contain multiple components and will
then result in a single EAGLE palette.

Be creative! do whatever you need to do!
"""

__version__ = "0.1.0"
from dlg import droputils
from dlg.drop import BranchAppDrop

import pickle
import logging

logger = logging.getLogger(__name__)

##
# @brief MyBranch
# @details Simple app to demonstrate how to write a branch actually making a
# decision and passing data on.
# Most of the code is boilerplate and can be copied verbatim. Note that a
# branch app is allowed
# to have multiple inputs, but just exactly two outputs. This example is using
# just a single input. There is an associated logical graph available on
# github:
#
#    https://github.com/ICRAR/EAGLE-graph-repo/examples/branchDemo.graph
#
# The application assumes to receive a random floating point array with values
# in the range [0,1] on input. It will calculate the mean of that array and
# then branch depending on whether the mean is smaller or larger than 0.5.
#
# @par EAGLE_START
# @param category PythonApp
# @param[in] param/appclass Application Class/branch.MyBranch/String/readonly/
#     \~English Import direction for application class
# @param[in] port/array Array/float/
#     \~English Port receiving the input array
# @param[out] port/Y Y/float/
#     \~English Port carrying the mean value of the array if mean < 0.5
# @param[out] port/N N/float/
#     \~English Port carrying the mean value of the array if mean >= 0.5
# @par EAGLE_END


class MyBranch(BranchAppDrop):
    def initialize(self, **kwargs):
        BranchAppDrop.initialize(self, **kwargs)

    def run(self):
        """
        Just reading the input array and calculating the mean.
        """
        input = self.inputs[0]
        data = pickle.loads(droputils.allDropContents(input))
        self.value = data.mean()

    def writeData(self):
        """
        Prepare the data and write to port (self.ind) identified by condition.
        """
        output = self.outputs[self.ind]
        d = pickle.dumps(self.value)
        output.len = len(d)
        logger.info(f">>>>>>> Writing value {self.value} to output {self.ind}")
        output.write(d)

    def condition(self):
        """
        Check value, call write method and return boolean.
        """
        if self.value < 0.5:
            self.ind = 0
            result = True
        else:
            self.ind = 1
            result = False
        self.writeData()
        return result
