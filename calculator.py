# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 12:12:54 2025

@author: dryae
"""

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Hata: Sıfıra bölünemez!"
        return x / y