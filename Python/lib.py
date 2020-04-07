# Return number of bits in 'num'
def bit_size(num):
    try:
        return num.bit_length()
    except AttributeError:
        raise TypeError('Oops, it seems that bit_size function only supports integers, not %r' % type(num))

# Convert bytes to integer
def bytes2int(raw_bytes):
    return int(binascii.hexlify(raw_bytes), 16)

# Generate a random odd integer of approximately nbits bits.
def read_random_odd_int(nbits):
    value = read_random_int(nbits)
    return value | 1

# Generate a seq of 'nbits' random bits
def read_random_bits(nbits):
    nbytes, rbits = divmod(nbits, 8)
    randomdata = os.urandom(nbytes)
    if rbits > 0:
        randomvalue = ord(os.urandom(1))
        randomvalue >>= (8 - rbits)
        randomdata = byte(randomvalue) + randomdata
    return randomdata

# Generate a random integer of approximately 'nbits' bits.
def read_random_int(nbits):
    randomdata = read_random_bits(nbits)
    value = bytes2int(randomdata)
    value |= 1 << (nbits - 1)
    return value

# Generate a random integer 'x' with 1 <= x <= 'maxvalue'
def randint(maxvalue):
    bit_size = bit_size(maxvalue)
    tries = 0
    while True:
        value = read_random_int(bit_size)
        if value <= maxvalue:
            break
        if tries and tries % 10 == 0:
            bit_size -= 1
        tries += 1
    return value
    
# Returns minimum number of rounds for Miller-Rabing primality testing
# See: http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf for precisions
def get_primality_testing_rounds(number):
    bitsize = bit_size(number)
    if bitsize >= 1536:
        return 3
    if bitsize >= 1024:
        return 4
    if bitsize >= 512:
        return 7
    return 10
