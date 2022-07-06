class Water:
    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm.name
        elif isinstance(other, Fire):
            return Steam.name
        elif isinstance(other, Ground):
            return Dirt.name
        elif isinstance(other, Wind):
            return Wave.name
        return None


class Air:
    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning.name
        elif isinstance(other, Ground):
            return Dust.name
        elif isinstance(other, Water):
            return Storm.name
        return None


class Fire:
    name = 'Огнь'

    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava.name
        elif isinstance(other, Air):
            return Lightning.name
        elif isinstance(other, Water):
            return Steam.name
        return None


class Ground:
    name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt.name
        elif isinstance(other, Air):
            return Dust.name
        elif isinstance(other, Fire):
            return Lava.name
        elif isinstance(other, Wind):
            return Tornado.name
        return None


class Wind:
    name = 'Ветер'

    def __add__(self, other):
        if isinstance(other, Water):
            return Wave.name
        elif isinstance(other, Ground):
            return Tornado.name
        return None



class Storm:
    name = 'Шторм'


class Steam:
    name = 'Пар'


class Dirt:
    name = 'Грязь'


class Lightning:
    name = 'Молния'


class Dust:
    name = 'Пыль'


class Lava:
    name = 'Лава'


class Wave:
    name = 'Волна'


class Tornado:
    name = 'Торнадо'


a = Water()
b = Ground()
c = a + b
print(c)
