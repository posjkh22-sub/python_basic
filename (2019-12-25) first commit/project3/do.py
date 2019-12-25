import bank_module

if __name__ == '__main__':
    machine_b = bank_module.Bank(500)
    machine_b.withdraw_money(100)
    machine_b.input_money(1000)
    machine_b.show_information()
