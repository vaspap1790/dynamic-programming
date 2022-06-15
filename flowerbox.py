# Max Subset Sum No Adjacent
def flowerbox_bottom_up(nutrient_values):
    fl1 = 0
    fl2 = 0
    for val in nutrient_values:
        fl1, fl2 = fl2, max(fl1 + val, fl2)
    return fl2


print(flowerbox_bottom_up([2, 5, 3, 6, 1]))
