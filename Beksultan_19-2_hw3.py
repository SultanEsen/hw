class Computer:

    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f'Computer summary:\nCPU - {self.__cpu} GHz, RAM - {self.__memory} GB\n'

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:

    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            print(f'Calling to {call_to_number} from sim-card 1 - {self.__sim_cards_list[0]}...')
        elif sim_card_number ==2:
            print(f'Calling to {call_to_number} from sim-card 2 - {self.__sim_cards_list[1]}...')
        else:
            print(f'Choose sim-card 1 or 2')

    def __str__(self):
        return f'Phone summary:\nList of sim cards - {self.__sim_cards_list}\n'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Route to {location} created. Foolow it.\n')

    def __str__(self):
        return f'Smartphone summary:\nCPU - {self.cpu} GHz, RAM - {self.memory} GB, Sim-cards - {self.sim_cards_list}\n'


comp1 = Computer(2.4, 8)
comp2 = Computer(2.4, 4)
phone1 = Phone(['Beeline', 'Megacom'])
sm1 = SmartPhone(2.4, 2, ['Beeline', 'Megacom'])
sm2 = SmartPhone(2.4, 4, ['Megacom', 'O!'])
sm1.use_gps('Paris')
list = [comp1,comp2, phone1, sm1, sm2]
for i in list:
    print(i)
print(comp1.make_computations())
print(comp1 == comp2)
print(comp1 != comp2)
print(comp1 > comp2)
print(comp1 < comp2)
print(comp1 >= comp2)
print(comp1 <= comp2)
phone1.call(1, '0555000001')