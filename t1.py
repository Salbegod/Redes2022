import sys
def invert(signal):
    if signal == "+":
        return "-"
    if signal == "-": 
        return "+"
    if signal == "0":
        return "0"

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

def HDB3Encoder(hexValue):
    binary = bin(int('1'+hexValue,16))[3:]
    result = ""
    signal = "-"
    numberOnes = 0
    numberZeroes = 0
    for bit in binary:
        if bit == '1':
            if numberZeroes > 0 and numberZeroes < 4:
                result += (numberZeroes*"0")
                numberZeroes = 0
            numberOnes += 1
            result += invert(signal)
            signal = invert(signal)
        else:
            numberZeroes += 1
            if numberZeroes == 4:
                numberZeroes = 0
                if numberOnes%2 == 0:
                    result += (invert(signal) + "00" + invert(signal))
                else:
                    result += ("000" + signal)
    if numberZeroes != 0:
        result += (numberZeroes*"0")
    return result

def HDB3Decoder(encodedString):
    result = ""
    current = "-"
    for signal in encodedString:
        if signal == "0":
            result += '0'
        if signal == invert(current):
            current = invert(current)
            result += '1'
        elif signal == current:
            current = invert(current)
            result = result[:4] + "0000"
    return f'{int(result, 2):X}'

def main():
    if sys.argv[1] == "codificador":
        if sys.argv[2] == "nrzi":
            print(NRZIEncoder(sys.argv[3]))
        elif sys.argv[2] == "mdif":
            print(MDIFEncoder(sys.argv[3]))
        elif sys.argv[2] == "hdb3":
            print(HDB3Encoder(sys.argv[3]))
    elif sys.argv[1] == "decodificador":
        if sys.argv[2] == "nrzi":
            print(NRZIDecoder(sys.argv[3]))
        elif sys.argv[2] == "mdif":
            print(MDIFDecoder(sys.argv[3]))
        elif sys.argv[2] == "hdb3":
            print(HDB3Decoder(sys.argv[3]))

main()