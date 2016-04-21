from hamcrest import assert_that, equal_to, is_

from controlbox.controller import Controlbox, Container, RootContainer, SystemProfile

import unittest


class ControllerTest(unittest.TestCase):
    """ unit test for the controller
    """

    def test_containers_equal(self):
        c = Controlbox()
        p = SystemProfile(c, 1)
        r = RootContainer(p)
        c1 = Container(c, r, 0)
        c2 = Container(c, r, 0)
        assert_that(c1, is_(equal_to(c2)))
        assert_that(c2, is_(equal_to(c1)))


if __name__ == '__main__':
    unittest.main()