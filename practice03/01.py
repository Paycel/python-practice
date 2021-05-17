import struct as s

SIZE_E = 8 + 2 + 4 + 8 + 2
SIZE_D = 1 + 2
SIZE_C = 8 + SIZE_D * 6 + 1 + 4 + 4 * 4 + 1
SIZE_B = 8 + 4 + 4 + 4 + 2
SIZE_A = 4 + 8 + 8 * 2


def parse_e(offset, byte_string):
    e_bytes = byte_string[offset: offset + SIZE_E]
    e_parsed = s.unpack('=dHIqH', e_bytes)
    e2_bytes = byte_string[e_parsed[2]: e_parsed[2] + e_parsed[1] * 2]
    e2_parsed = s.unpack('=' + 'H' * e_parsed[1], e2_bytes)
    return {'E1': e_parsed[0],
            'E2': list(e2_parsed),
            'E3': e_parsed[3],
            'E4': e_parsed[4]}


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset: offset + SIZE_D]
    d_parsed = s.unpack('=bH', d_bytes)
    return {'D1': d_parsed[0],
            'D2': d_parsed[1]}


def parse_c(offset, byte_string):
    c1_bytes = byte_string[offset: offset + 8]
    c1_parsed = s.unpack('=d', c1_bytes)

    c2_parsed = [parse_d(offset + 8 + i * SIZE_D, byte_string) for i in range(6)]

    c3456_bytes = byte_string[offset + 8 + SIZE_D * 6: offset + SIZE_C]
    c3456_parsed = s.unpack('=bIiiiib', c3456_bytes)

    return {'C1': c1_parsed[0],
            'C2': c2_parsed,
            'C3': c3456_parsed[0],
            'C4': parse_e(c3456_parsed[1], byte_string),
            'C5': [c3456_parsed[i] for i in range(2, 6)],
            'C6': c3456_parsed[6]}


def parse_b(offset, byte_string):
    b_bytes = byte_string[offset: offset + SIZE_B]
    b_parsed = s.unpack('=fdIIh', b_bytes)
    return {'B1': b_parsed[0],
            'B2': b_parsed[1],
            'B3': parse_c(b_parsed[2], byte_string),
            'B4': b_parsed[3],
            'B5': b_parsed[4]}


def parse_a(offset, byte_string):
    a_bytes = byte_string[offset: offset + SIZE_A]
    a_parsed = s.unpack('=Iqqq', a_bytes)
    return {'A1': parse_b(a_parsed[0], byte_string),
            'A2': a_parsed[1],
            'A3': [a_parsed[i] for i in range(2, 4)]}


def f31(byte_string):
    return parse_a(4, byte_string)
