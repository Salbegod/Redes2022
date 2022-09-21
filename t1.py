import sys
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

def main():
    if sys.argv[1] == "codificador":
        if sys.argv[2] == "nrzi":
            print(NRZIEncoder(sys.argv[3]))
        elif sys.argv[2] == "mdif":
            print(MDIFEncoder(sys.argv[3]))
    elif sys.argv[1] == "decodificador":
        if sys.argv[2] == "nrzi":
            print(NRZIDecoder(sys.argv[3]))
        elif sys.argv[2] == "mdif":
            print(MDIFDecoder(sys.argv[3]))

main()