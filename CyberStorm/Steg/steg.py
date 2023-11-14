#Team Pterodactyl 
#Chat GPT was used in the coding and debugging of this program  


import sys
import argparse

# This sentinel is a sequence of bytes that indicates the end of the file.
SENTINEL = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])

def store_byte_method(wrapper, hidden, offset, interval):
    """
    Hide the data in the 'hidden' bytearray into the 'wrapper' bytearray using the byte method.
    Data is hidden starting at 'offset' and at every 'interval' bytes.
    """

    # Iterate over each byte in the hidden data and insert it into the wrapper.
    for byte in hidden:
        wrapper[offset] = byte
        offset += interval

    # After hiding all data, append the sentinel to indicate the end of hidden data.
    for byte in SENTINEL:
        wrapper[offset] = byte
        offset += interval

    return wrapper

def retrieve_byte_method(wrapper, offset, interval):
    """
    Extract hidden data from the 'wrapper' bytearray using the byte method.
    """

    hidden = bytearray()
    sentinel_index = 0

    # Iterate over the wrapper to extract hidden bytes.
    while offset < len(wrapper):
        byte = wrapper[offset]

        # Check if the current byte is part of the sentinel.
        if byte == SENTINEL[sentinel_index]:
            sentinel_index += 1
            # If the full sentinel sequence is found, we stop extraction.
            if sentinel_index == len(SENTINEL):
                break
        else:
            # If only a part of the sentinel was found before this byte, we add that part to hidden data.
            if sentinel_index:
                hidden.extend(SENTINEL[:sentinel_index])
                sentinel_index = 0
            hidden.append(byte)
        offset += interval

    return hidden

def store_bit_method(wrapper, hidden, offset, interval):
    """
    Hide the data in the 'hidden' bytearray into the 'wrapper' bytearray using the bit method.
    Only the least significant bit of each byte in the wrapper is changed.
    """

    # Iterate over each byte in the hidden data.
    for byte in hidden:
        for _ in range(8):  # Go over each bit in the byte.
            wrapper[offset] &= 0b11111110  # Clear the last bit.
            wrapper[offset] |= (byte & 0b10000000) >> 7  # Set the least significant bit.
            byte <<= 1
            offset += interval

    # Append the sentinel to indicate the end of hidden data.
    for byte in SENTINEL:
        for _ in range(8):
            wrapper[offset] &= 0b11111110
            wrapper[offset] |= (byte & 0b10000000) >> 7
            byte <<= 1
            offset += interval

    return wrapper

def retrieve_bit_method(wrapper, offset, interval):
    """
    Extract hidden data from the 'wrapper' bytearray using the bit method.
    """

    hidden = bytearray()
    sentinel_index = 0

    # Extract data byte by byte from the least significant bits.
    while offset < len(wrapper) - 7:
        byte = 0
        for _ in range(8):  # Construct each byte bit by bit.
            byte = (byte << 1) | (wrapper[offset] & 1)
            offset += interval

        # Check if the current byte matches the sentinel.
        if byte == SENTINEL[sentinel_index]:
            sentinel_index += 1
            # If the full sentinel sequence is found, we stop extraction.
            if sentinel_index == len(SENTINEL):
                break
        else:
            # If only a part of the sentinel was found before this byte, we add that part to hidden data.
            if sentinel_index:
                hidden.extend(SENTINEL[:sentinel_index])
                sentinel_index = 0
            hidden.append(byte)

    return hidden

def main():
    # Argument parsing for the steganography tool.
    parser = argparse.ArgumentParser(description="Steganography tool")
    parser.add_argument('-s', action='store_true', help='Store mode')
    parser.add_argument('-r', action='store_true', help='Retrieve mode')
    parser.add_argument('-b', action='store_true', help='Bit method')
    parser.add_argument('-B', action='store_true', help='Byte method')
    parser.add_argument('-o', metavar='OFFSET', type=int, default=0, help='Offset')
    parser.add_argument('-i', metavar='INTERVAL', type=int, default=1, help='Interval')
    parser.add_argument('-w', metavar='WRAPPER', type=str, help='Wrapper file')
    parser.add_argument('-H', metavar='HIDDEN', type=str, help='Hidden file')

    args = parser.parse_args()

    # Mode and method determination based on user inputs.
    if args.s:
        mode = 'store'
    elif args.r:
        mode = 'retrieve'
    else:
        print("You must specify either -s (store) or -r (retrieve) mode.")
        return

    if args.b:
        method = 'bit'
    elif args.B:
        method = 'byte'
    else:
        print("You must specify either -b (bit) or -B (byte) method.")
        return

    # Load the wrapper data.
    with open(args.w, 'rb') as f:
        wrapper = bytearray(f.read())

    # Handle storing and retrieval based on the chosen mode and method.
    if mode == 'store':
        with open(args.H, 'rb') as f:
            hidden = bytearray(f.read())

        # Call the respective method based on user choice.
        if method == 'byte':
            result = store_byte_method(wrapper, hidden, args.o, args.i)
        else:  # bit
            result = store_bit_method(wrapper, hidden, args.o, args.i)
        sys.stdout.buffer.write(result)

    else:  # retrieve
        if method == 'byte':
            hidden = retrieve_byte_method(wrapper, args.o, args.i)
        else:  # bit
            hidden = retrieve_bit_method(wrapper, args.o, args.i)
        sys.stdout.buffer.write(hidden)

if __name__ == '__main__':
    main()
