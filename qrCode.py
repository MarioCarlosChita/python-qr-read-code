from pyzbar.pyzbar import decode
from PIL import Image

class QrCode:
     def __init__(self , filename):
           self.filename = filename;

     def  getData(self):  
           listData =  list();
           response = decode(Image.open(self.filename))
           for  k  in response:
               listData.append(k.data);
           return listData;