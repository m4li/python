# -*- coding: cp1254 -*-
# PYTHON'DA HESAP MAKİNESİ
from __future__ import division
print"""
    TOPLAMA [1]
    ÇIKARMA [2]
    ÇARPMA  [3]
    BÖLME   [4]
    """
islem = raw_input(" LUTFEN YAPACAGINIZ ISLEMIN NUMARASINI GIRINIZ:")
if islem == "1":
    print"TOPLAMA ISLEMINI SEÇCTINIZ!"
    sayi1 = int(raw_input(" ILK SAYIYI GIRINIZ:"))
    sayi2 = int(raw_input(" IKINCI SAYIYI GIRINIZ:"))
    print sayi1,"+",sayi2,"=",sayi1+sayi2
if islem == "2":
    print"CIKARMA ISLEMINI SEÇCTINIZ!"
    sayi1 = int(raw_input(" ILK SAYIYI GIRINIZ:"))
    sayi2 = int(raw_input(" IKINCI SAYIYI GIRINIZ:"))
    print sayi1,"-",sayi2,"=",sayi1-sayi2
if islem == "3":
    print"CARPMA ISLEMINI SEÇCTINIZ!"
    sayi1 = int(raw_input(" ILK SAYIYI GIRINIZ:"))
    sayi2 = int(raw_input(" IKINCI SAYIYI GIRINIZ:"))
    print sayi1,"x",sayi2,"=",sayi1*sayi2
if islem == "4":
    print"BOLME ISLEMINI SEÇCTINIZ!"
    sayi1 = int(raw_input(" ILK SAYIYI GIRINIZ:"))
    sayi2 = int(raw_input(" IKINCI SAYIYI GIRINIZ:"))
    print sayi1,"/",sayi2,"=",sayi1/sayi2

