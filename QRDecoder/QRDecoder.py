import zxing

def DecodeQR(pic_name = "test.jpg"):

    ''' Decode a given img of QR code into text

    args:
    pic_name: name of the file to decode (With absolute path)

    return: no return

    '''

    decoder = zxing.BarCodeReader()
    res = decoder.decode(pic_name)
    print(res.parsed)

DecodeQR(pic_name = "I:\\DigitalCircuit\\test_output\\gifBGDQR.gif")