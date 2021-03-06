import os
import sys
import unittest

from brewpi.connector.controlbox.integration_test.base_test import GeneralControllerTests
from brewpi.connector.controlbox.integration_test.control_loop_test import ControlLoopTest
from brewpi.connector.controlbox.integration_test.indirect_value_test import IndirectValueTest
from brewpi.connector.controlbox.integration_test.persistence_test import PersistentValueTest, PersistentChangeValueTest
from brewpi.connector.controlbox.integration_test.time_test import SystemTimeTest, ValueProfileTest
from nose.plugins.attrib import attr

from brewpi.controlbox.objects import CrossCompileController
from controlbox.config.config import configure_module
from controlbox.connector.processconn import ProcessConnector

cross_compile_exe = None

configure_module(sys.modules[__name__])


# for now this is windows only - will add the cross compile executable to
# the build so we can test with CI
@unittest.skipUnless(cross_compile_exe, "cross-compile exe not defined")
@attr(os='windows')
class BaseCrossCompileTestCase:
    """ Uses the cross-compiled "arduino" code to test the main functionality of the v03x connector. """

    def __init__(self, name):
        super().__init__(name)
        setattr(self, name, super().__getattribute__(name))

    def create_connector(self):
        return ProcessConnector(os.path.expanduser(cross_compile_exe), None)

    def create_controller(self):
        return CrossCompileController(self.connector)


class CrossCompileTestCase(BaseCrossCompileTestCase, GeneralControllerTests):
    __test__ = True


class CrossCompileSysTimeTestCase(BaseCrossCompileTestCase, SystemTimeTest, ValueProfileTest):
    __test__ = True


class CrossCompileIndirectValueTestCase(BaseCrossCompileTestCase, IndirectValueTest):
    __test__ = True


class CrossCompilePersistenceTestCase(BaseCrossCompileTestCase, PersistentValueTest, PersistentChangeValueTest):
    __test__ = True


class CrossCompileControlLoopTestCase(BaseCrossCompileTestCase, ControlLoopTest):
    __test__ = True
