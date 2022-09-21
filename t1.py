
def invert(signal):
    if signal == "+":
        return "-"
    if signal == "-": 
        return "+"

def NRZIEncoder(hexValue):
    binary = bin(int('1'+hexValue,16))[3:]
    result = ""
    signal = "-"
    for bit in binary:
        if bit == '1':
            signal = invert(signal)
        result += signal
    return result

def NRZIDecoder(encodedString):
    result = ""
    current = "-"
    for signal in encodedString:
        if signal != current:
            current = invert(current)
            result += '1'
        else:
            result += '0'
    return f'{int(result, 2):X}'

def MDIFEncoder(hexValue):
    binary = bin(int('1'+hexValue,16))[3:]
    result = ""
    signal = "-"
    for bit in binary:
        if bit == '1':
            result += (signal + invert(signal))
            signal = invert(signal)
        else:
            result += (invert(signal) + signal)
    return result

def MDIFDecoder(encodedString):
    result = ""
    current = "-"
    skip = False
    for signal in encodedString:
        if skip:
            skip = False
            continue
        if signal != current:
            result += '0'
            skip = True
        else:
            current = invert(current)
            result += '1'
            skip = True
    return f'{int(result, 2):X}'