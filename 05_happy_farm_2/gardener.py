from potato_garden_and_potato import PotatoGarden


class Gardener:

    def __init__(self, name, potato_amount):
        self.name = name
        self.garden = PotatoGarden(potato_amount)

    def care_of_the_garden(self):
        if self.garden.potatoes != 0:
            self.garden.all_grow()
            self.garden.are_all_ripe()
        else:
            print(f'У садовника пока не за чем ухаживать!')

    def harvest(self):
        return [potato for potato in self.garden.potatoes]

    def plant_potatoes(self, potato_amt):
        self.garden = PotatoGarden(potato_amt)

    def print_gardener_info(self):
        if self.garden.potatoes != 0:
            print(f'\nСадовник: {self.name}\n  Ухаживает за: {self.garden.name}, на которой:')
            for potato in self.garden.potatoes:
                potato.print_state()
        else:
            print(f'У садовника пока не за чем ухаживать!')