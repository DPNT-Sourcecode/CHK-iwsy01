from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("AABACADD") == 260

    def test_invalid_input(self):
        assert checkout_solution.checkout("AK") == -1
