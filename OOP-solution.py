
class Pod_Racer:
    def __init__(self,max_speed,condition,price,owner):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
        self.owner = owner

    def reqair(self):
        self.condition = 'repaired'


class Anakins_Pod(Pod_Racer):
    def __init__(self,max_speed,condition,price,owner = 'Anakin'):
        super().__init__(max_speed,condition,price,owner)
    def boost(self):
        self.max_speed *= 2

class Sebulba_Pod(Pod_Racer):
    def __init__(self,max_speed,condition,price,owner = 'Sebulba'):
        super().__init__(max_speed,condition,price,owner)

    def flame_jet(self,other_pod):
        other_pod.condition = 'trashed'
    

anakins_pod = Anakins_Pod(25,'perfect',1000)
sebulba_pod = Sebulba_Pod(50,'perfect',100000)

print(anakins_pod.condition)
print(sebulba_pod.condition)