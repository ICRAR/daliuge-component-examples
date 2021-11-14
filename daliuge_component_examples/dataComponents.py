"""
daliuge_component_examples component module.

This is the module of daliuge_component_examples containing DALiuGE data components.
Here you put your main data classes and objects.

Typically a component project will contain multiple components and will
then result in a single EAGLE palette.

Be creative! do whatever you need to do!
"""
from dlg.drop import AbstractDROP
from dlg.meta import dlg_float_param, dlg_string_param
from dlg.meta import dlg_bool_param, dlg_int_param
from dlg.meta import dlg_component, dlg_batch_input
from dlg.meta import dlg_batch_output, dlg_streaming_input

import pickle, base64, os
import logging

logger = logging.getLogger(__name__)

##
# @brief MyData
# @details Template app for demonstration only!
# Replace the documentation with whatever you want/need to show in the DALiuGE
# workflow editor. The dataclass parameter should contain the relative Pythonpath
# to import MyApp.
#     
# @par EAGLE_START
# @param category DataDrop
# @param[in] param/appclass Drop Class/daliuge_component_examples.MyData/String/readonly/
#     \~English Import direction for application class
# @param[in] param/dummy Dummy parameter/ /String/readwrite/
#     \~English Dummy modifyable parameter
# @param[in] port/dummy Dummy in/float/
#     \~English Dummy producer port
# @param[out] port/dummy Dummy out/float/
#     \~English Dummy consumer port
# @par EAGLE_END

# Data components usually directly inhert from the AbstractDROP class. Please
# refer to the Developer Guide for more information.

class MyDataDROP(AbstractDROP):
    """
    A dummy dataDROP that points to nothing.
    """

    def initialize(self, **kwargs):
        pass

    def getIO(self):
        return f"Hello from {__class__.__name__}"

    @property
    def dataURL(self):
        return f"Hello from the dataURL method"
