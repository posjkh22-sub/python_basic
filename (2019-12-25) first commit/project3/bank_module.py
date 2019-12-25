
class Bank:
    def __init__(self, total):
        self.total = total
        self.version = 'V27'

    def input_money(self, _input):
        self.total += _input
        print("[ATM] total balance: ", self.total)

    def withdraw_money(self, _output):
        if self.total < _output:
            print("[error] Not enough balance.")
        else:
            self.total -= _output
            print("[ATM] total balance: ", self.total)

    def show_information(self):
        print("[ATM] This machine is avaiable (", self.version, ")")


if __name__ == '__main__':
    machine_a = Bank(100)
    machine_a.input_money(5000)
    machine_a.withdraw_money(400)
    machine_a.show_information()



