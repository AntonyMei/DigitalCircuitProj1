import qrcode

def GenerateQRCode(
        data = "Default",
        version  = None,
        fill_color = "Black",
        back_color = "White",
        error_correction = qrcode.ERROR_CORRECT_L,
        border = 1,
        box_size = 10
    ):

    ''' Generate QR code

    args:
    data: string to encode into QR code
    version: controls the size of QR code (a 1 to 40 integer)
            version = 1: 21x21 matrix
            version = None: returns a matrix fitting input size
    fill_color: printing color of QR
    back_color: background color of QR
    error_correction: qrcode.ERROR_CORRECT_L 7% 
                      qrcode.ERROR_CORRECT_M 15%
                      qrcode.ERROR_CORRECT_Q 25%
                      qrcode.ERROR_CORRECT_H 30%
    border: border width of output matrix
            e.g. if we choose version=1 and border=1, then the 
            output will be 23*23
    box_size: number of pixel for each matrix entry (minimal is 4)

    return: an image object of QR

    '''

    # initialize QR
    qr = qrcode.QRCode(
        version = version,
        error_correction = error_correction,
        box_size = box_size,
        border = border,
    )

    # add data to QR
    qr.add_data(data=data)
    qr.make(fit= True)

    # Get image, with color settings
    img = qr.make_image(fill_color = fill_color, back_color = back_color)
    return img

GenerateQRCode("Test").show()