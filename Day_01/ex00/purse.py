def add_ingot(purse):
    my_purse = purse.copy()
    my_purse['gold_ingots'] = my_purse.get('gold_ingots', 0) + 1
    return my_purse


def get_ingot(purse):
    my_purse = purse.copy()
    if 'gold_ingots' in my_purse.keys() and my_purse['gold_ingots'] != 0:
        my_purse['gold_ingots'] -= 1
    return my_purse


def empty(purse):
    return {}
