from purse import add_ingot


def split_booty(*args):
    sum_gold_ingots = sum(purse.get('gold_ingots', 0) for purse in args)
    purses = [{}, {}, {}]
    while sum_gold_ingots > 0:
        for i in range(len(purses)):
            purses[i] = add_ingot(purses[i]) if sum_gold_ingots > 0 else purses[i]
            sum_gold_ingots -= 1
    return tuple(purses)
