# import pyqrcode
# qr = pyqrcode.create("HORN O.K. PLEASE.") ;
# qr.png("horn.png", scale=6);

from qrCode import QrCode ;
qr=  QrCode('frame.png');
print(qr.getData());







