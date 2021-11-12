from typing import List

class Item(object):
    def __init__(self, name: str, weight: int, value: int) -> None:
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self) -> str:
        return f'A {self.name} worth {self.value} that weighs {self.weight}'


def get_best_backpack(items: List[Item], max_capacity: int) -> List[Item]:
    def backpack(items,pack,idx,capacity,value):
        if capacity==0 or idx==0:
            return value,pack.copy()
        else:
            if items[idx-1].weight>capacity:
                return backpack(items,pack,idx-1,capacity,value)
            else:
                value1,res1= backpack(items,pack,idx-1,capacity,value)
                pack.append(items[idx-1])
                value2,res2 = backpack(items,pack,idx-1,
                                  capacity-items[idx-1].weight,value+items[idx-1].value)
                pack.pop()
                if value1<value2:
                    return value2,res2.copy()
                else:
                    return value1,res1.copy()
    res,ret = backpack(items,[],len(items),max_capacity,0)
    return res,ret


if __name__ =='__main__':
    # items = [
    #     Item("Ring",43,43),
    #     Item("Earring",36,2),
    #     Item('NeckLace',80,1),
    #     Item('Diamond',70,68)
    # ]
    #
    # maxValue,compos = get_best_backpack(items,80)
    # print(maxValue)
    # print([item.name for item in compos])

    for i in range(1,11):
        s = str(i)
        s = s.rjust(10,'t')
        print(s)
