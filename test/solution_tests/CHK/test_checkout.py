from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("AABACADD") == 260

    def test_invalid_input(self):
        assert checkout_solution.checkout("AK") == -1

    def test_new_offers(self):
        assert checkout_solution.checkout("AAAAABBCDDEEE") == 400

    def test_many_a_offers(self):
        assert checkout_solution.checkout("AAAAAAAAAAAAAABCDDEE") == 710

    def test_f_offer(self):
        assert checkout_solution.checkout("AAAAABBCDDEEEFFFF") == 430
