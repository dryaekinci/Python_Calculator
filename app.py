# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 12:13:43 2025

@author: dryae
"""

from calculator import Calculator

calc = Calculator()

print("=== Python Hesap Makinesi ===")
print("Çıkış için q yazabilirsiniz.\n")

while True:
    islem = input("İşlem seçin (+, -, *, /, q): ")

    if islem == "q":
        print("Program sonlandırıldı.")
        break

    try:
        x = float(input("Birinci sayı: "))
        y = float(input("İkinci sayı: "))
    except ValueError:
        print("Hata: Lütfen sayı girin!")
        continue

    if islem == "+":
        print("Sonuç:", calc.add(x, y))
    elif islem == "-":
        print("Sonuç:", calc.subtract(x, y))
    elif islem == "*":
        print("Sonuç:", calc.multiply(x, y))
    elif islem == "/":
        print("Sonuç:", calc.divide(x, y))
    else:
        print("Geçersiz işlem!")
    
    print("-" * 20)
