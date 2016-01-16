import sys

DEFAULT_NUMBER_OF_DISKS = 4

class HanoiTower(object):

    def __init__(self, number_of_disks):
        self.peg1 = []
        self.peg2 = []
        self.peg3 = []
        for x in range(number_of_disks, 0, -1):
            self.peg1.append(x)
        self.print_tower()

    def solve_tower(self, tower_height, start, auxillary, final):
        if tower_height <= 0:
            raise Exception('Length of starting peg is zero')
        elif tower_height == 1:
            self.move(start, final)
        else:
            self.solve_tower(tower_height - 1, start, final, auxillary)
            self.move(start, final)
            self.solve_tower(tower_height - 1, auxillary, start, final)

    def move(self, from_peg, to_peg):
        disk = from_peg.pop()
        to_peg.append(disk)
        self.print_tower()

    def print_tower(self):
        print '{} {} {}'.format(len(self.peg1), len(self.peg2), len(self.peg3))

if __name__ == '__main__':
    try:
        number_of_disks = int(sys.argv[1])
    except IndexError:
        number_of_disks = DEFAULT_NUMBER_OF_DISKS
    tower = HanoiTower(number_of_disks)
    tower.solve_tower(number_of_disks, tower.peg1, tower.peg2 ,tower.peg3)
