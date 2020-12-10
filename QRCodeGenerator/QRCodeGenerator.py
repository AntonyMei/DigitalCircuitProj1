import sys
import os
import qrcode
from MyQR import myqr

def GenerateQRCode(
        data = "Default",
        output_directory = "I:\\DigitalCircuit",
        output_pic_name = "test.png",
        version  = None,
        fill_color = "Black",
        back_color = "White",
        error_correction = qrcode.ERROR_CORRECT_L,
        border = 1,
        box_size = 10
    ):

    ''' Generate a normal QR code image

    args:
    data: string to encode into QR code
    output_pic_name: output file name
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
    qr.add_data(data = data)
    qr.make(fit = True)

    # Get image, with color settings
    img = qr.make_image(fill_color = fill_color, back_color = back_color)
    img.save(output_directory + "\\" + output_pic_name)

def GenerateQRCodeWithBGD(
        data = "Default",
        version  = 1,
        input_pic_name = "input.jpg",
        output_pic_name = "testout.gif"
    ):

    ''' Generate QR code

    args:
    data: string to encode into QR code
    version: controls the size of QR code (a 1 to 40 integer)
            version = 1: 21x21 matrix
            version = None: returns a matrix fitting input size
    input_pic_name: filename for input picture (Can be .jpg, .png, .gif)
    output_pic_name: filename for output picture (Can be .jpg, .png, .gif)

    return: an gif object of QR

    '''
    print(input_pic_name, output_pic_name)
    myqr.run(words = data,
        version = version,
        picture = input_pic_name,
        colorized = True,
        save_name = output_pic_name)

GenerateQRCode(data = "DigitalCircuitProj1",
 output_directory = "I:\\DigitalCircuit\\test_output",
 output_pic_name = "plainQR.png")
GenerateQRCodeWithBGD(data = "DigitalCircuitProj1", version = 10,
 input_pic_name = "I:\\DigitalCircuit\\test_input\\input1.jpg",
 output_pic_name = "I:\\DigitalCircuit\\test_output\\jpgBGDQR.png")
GenerateQRCodeWithBGD(data = "DigitalCircuitProj1", version = 10,
 input_pic_name = "I:\\DigitalCircuit\\test_input\\input2.gif",
 output_pic_name = "I:\\DigitalCircuit\\test_output\\gifBGDQR.gif")