import time
import unittest


class TestInit(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.stime = 0
        self.etime = 0

    def setUp(self) -> None:
        print(self.__module__)
        print("MethodName:", self._testMethodName)
        self.stime = time.time()
        return super().setUp()

    def tearDown(self) -> None:
        self.etime = time.time()
        print("Time:", self.etime - self.stime)
        print()
        return super().tearDown()
