"""
dlg_example_cmpts component module.

This is the module of daliuge_component_examples containing DALiuGE data
components. Here you put your main data classes and objects.

Typically a component project will contain multiple components and will
then result in a single EAGLE palette.

Be creative! do whatever you need to do!
"""
import logging
import io

from dlg.ddap_protocol import DROPStates
from dlg.data.drops.memory import InMemoryDROP
from dlg.data.io import MemoryIO

logger = logging.getLogger(__name__)

##
# @brief MyData
# @details Template app for demonstration only!
# Replace the documentation with whatever you want/need to show in the DALiuGE
# workflow editor. The dataclass parameter should contain the relative
# Pythonpath to import MyApp.
#
# @par EAGLE_START
# @param category File
# @param dataclass DropClass/dlg_example_cmpts.data.MyDataDROP/String/ComponentParameter/readonly//False/False/Import direction for data class # noqa: E501
# @param content Content parameter/Hello World/String/ApplicationArgument/readwrite//False/False/Content modifyable parameter # noqa: E501
# @param dummy Dummy out//float/OutputPort/readwrite//False/False/Dummy consumer port # noqa: E501
# @par EAGLE_END

# Data components usually directly inhert from the AbstractDROP class. Please
# refer to the Developer Guide for more information.

import logging
from dlg.meta import dlg_string_param

logger = logging.getLogger(__name__)


class MyDataDROP(InMemoryDROP):
    """
    A MemoryDROP that allows to define string content.
    """

    content = dlg_string_param("content", "Hello World")

    def initialize(self, *args, **kwargs):
        self._buf = io.BytesIO(self.content.encode("utf-8"))

    @property
    def dataURL(self) -> str:
        return "null://data.url/Hello"
