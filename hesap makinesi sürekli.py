# -*- coding: cp1254 -*-
# PYTHON'DA SÜREKLİ ÇALIŞAN HESAP MAKİNESİ
from __future__ import division
a=1
while a==1:
    print"""
    TOPLAMA [1]
    CIKARMA [2]
    CARPMA  [3]
    BOLME   [4]
    """
    islem = raw_input(" LUTFEN YAPACAGINIZ ISLEMIN NUMARASINI GIRINIZ:")
    if islem == "1":
        print"TOPLAMA ISLEMINI SECTINIZ!"
        sayi1 = int(raw_input(" ILK SAYIYI GIRINIZ:"))
        sayi2 = int(raw_input(" IKINCI SAYIYI GIRINIZ:"))
        print sayi1,"+",sayi2,"=",sayi1+sayi2
    if islem == "2":
        print"CIKARMA ISLEMINI SECTINIZ!"
        sayi1 = int(raw_input(" ILK SAYIYI GIRINIZ:"))
        sayi2 = int(raw_input(" IKINCI SAYIYI GIRINIZ:"))
        print sayi1,"-",sayi2,"=",sayi1-sayi2
    if islem == "3":
        print"CARPMA ISLEMINI SECTINIZ!"
        sayi1 = int(raw_input(" ILK SAYIYI GIRINIZ:"))
        sayi2 = int(raw_input(" IKINCI SAYIYI GIRINIZ:"))
        print sayi1,"x",sayi2,"=",sayi1*sayi2
    if islem == "4":
        print"BOLME ISLEMINI SECTINIZ!"
        sayi1 = int(raw_input(" ILK SAYIYI GIRINIZ:"))
        sayi2 = int(raw_input(" IKINCI SAYIYI GIRINIZ:"))
        print sayi1,"/",sayi2,"=",sayi1/sayi2

