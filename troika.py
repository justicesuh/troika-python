class Troika(object):
    COLUMNS = 9
    ROWS = 3
    SLICES = 27
    SLICESIZE = COLUMNS * ROWS
    STATESIZE = SLICESIZE * SLICES
    NUM_SBOXES = STATESIZE / ROWS

    PADDING = 0x1

    def __init__(self):
        self.state = [0] * Troika.STATESIZE

    def absort(self):
        pass

    def squeeze(self):
        pass

    def permutation(self):
        pass

    def sub_trytes(self):
        pass

    def shift_rows(self):
        pass

    def shift_lanes(self):
        pass

    def add_column_parity(self):
        pass

    def add_round_constant(self):
        pass

    def print_slice(self, slice):
        print('#### Slice {} ####'.format(slice))
        for row in range(Troika.ROWS):
            for column in range(Troika.COLUMNS):
                print('{} '.format(self.state[slice * Troika.SLICES + row * Troika.COLUMNS + column]), end='')
            print('')
        print('------------------')
        for i in range(Troika.COLUMNS):
            print('{} '.format((
                self.state[slice * Troika.SLICES + 0 * Troika.COLUMNS + i] +
                self.state[slice * Troika.SLICES + 1 * Troika.COLUMNS + i] +
                self.state[slice * Troika.SLICES + 2 * Troika.COLUMNS + i]
            ) % 3), end='')
        print('')

    def print_state(self):
        for s in range(Troika.SLICES):
            self.print_slice(s)


if __name__ == '__main__':
    t = Troika()
    t.print_slice(0)
