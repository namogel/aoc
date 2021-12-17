from functools import reduce, partial
import operator

HEX_TO_BIN = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def star(func, args):
    return func(*args)


def to_int(v):
    return int(v, 2)


OPERATORS = {
    0: sum,
    1: partial(reduce, operator.mul),
    2: min,
    3: max,
    5: partial(star, operator.gt),
    6: partial(star, operator.lt),
    7: partial(star, operator.eq),
}


class Parser:
    def __init__(self, debug=False):
        self.i = 0
        self.debug = debug
        if debug:
            print(bits)

    def print(self, message):
        if self.debug:
            print(message)

    def read(self, n, log):
        start = self.i
        ret = to_int(bits[self.i:self.i+n])
        self.i += n
        self.print(f'{" " * start}{bits[start:self.i]} {log}={ret}')
        return ret

    def parse_header(self):
        _ = self.read(3, "version")
        return self.read(3, "type_id")

    def parse_literal(self):
        start = self.i
        ret = ""
        while True:
            part = bits[self.i:self.i+5]
            ret += part[1:]
            self.i += 5
            if part[0] == "0":
                parsed = to_int(ret)
                self.print(f'{" " * start}{bits[start:self.i]} literal={parsed}')
                return parsed

    def parse_packet(self):
        type_id = self.parse_header()
        if type_id == 4:
            return self.parse_literal()

        length_type_id = self.read(1, "length_type_id")
        if length_type_id == 0:
            length = self.read(15, "length")
            stop = self.i + length
            values = []
            while self.i < stop:
                values.append(self.parse_packet())
        elif length_type_id == 1:
            sub_packets_nb = self.read(11, "sub_packets_nb")
            values = [self.parse_packet() for _ in range(sub_packets_nb)]
        else:
            raise ValueError

        return int(OPERATORS[type_id](values))


with open("input") as fd:
    bits = "".join(HEX_TO_BIN[c] for c in fd.readlines()[0].strip())

print(Parser().parse_packet())
