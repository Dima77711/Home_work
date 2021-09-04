class Tomato:
    states = {1: 'small', 2: 'mittle', 3: 'high'}
    def __init__(self, index):
        self._index=index
        self._state=0
    def grow(self):
        self._state+=1
        return 'новая стадия'
    def is_ripe(self):
        if self._state==3:
            print('созрел')
        else:
            print('не созрел')

class TomatoBush:
    def __init__(self,num):
        self.tomatoes=[Tomato(index) for index in range (1, num)]
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
            print(i._state)
    def all_are_ripe(self):
        for i in self.tomatoes:
            i.is_ripe()
    def give_away_all(self):
        self.tomatoes.clear()

to=TomatoBush(2)
print(to.tomatoes)
to.grow_all()
to.grow_all()
to.grow_all()
print(to.all_are_ripe())
print(to.give_away_all())

