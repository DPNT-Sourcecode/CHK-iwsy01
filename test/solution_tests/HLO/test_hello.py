from solutions.HLO import hello_solution


class TestHello():
    def test_hello(self):
        assert hello_solution.hello("someone") == "Hello, someone!"

    def test_hello_john(self):
        assert hello_solution.hello("John") == "Hello, John!"
