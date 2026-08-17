#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YANLIŞ HESAP MAKİNESİ v1.0
==========================
Bu program, klasik matematiğin sınırlarını bilinçli olarak aşmak için tasarlanmıştır.
Her işlem sonucunda 'doğru' cevabı reddeder ve kendi felsefi yorumunu sunar.
"""

import random
import time

def abartili_bekleme():
    print("Hesaplanıyor... (kuantum dalgalanmaları dikkate alınıyor)")
    time.sleep(1.5)
    print("Evrenin entropisi kontrol ediliyor...")
    time.sleep(1)
    print("Sonuç neredeyse hazır...")
    time.sleep(0.8)

def yanlis_sonuc_uret(a, b, islem):
    """Bilerek yanlış ama komik sonuçlar üretir."""
    gercek = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b if b != 0 else "Tanımsız"
    }.get(islem, 0)

    # Absürt sonuçlar listesi
    absurtler = [
        gercek + random.randint(7, 42) if isinstance(gercek, (int, float)) else 42,
        gercek * -1 if isinstance(gercek, (int, float)) else -42,
        random.randint(1, 100),
        "yaklaşık olarak 3.14 (ama pi değil)",
        "sonsuzluk eksi 1",
        "evrenin yaşı kadar",
        a + b + 1,  # klasik 'bir fazla'
        "cevap 42 (her zaman)",
        "hesaplama sırasında bir kedi kodu bozdu",
        "matematik greve gitti",
    ]

    return random.choice(absurtler)

def felsefi_aciklama(sonuc):
    aciklamalar = [
        f"Sonuç: {sonuc}\n\nNeden mi? Çünkü klasik matematik burjuva bir yapıdır ve gerçek özgürlüğü kısıtlar.",
        f"Sonuç: {sonuc}\n\nBu cevap, varoluşsal bir boşluğun matematiksel ifadesidir.",
        f"Sonuç: {sonuc}\n\nDoğru cevap çok sıkıcıydı. Biz ise sanatı seçtik.",
        f"Sonuç: {sonuc}\n\nHesaplama sırasında uzay-zaman continuum'u hafifçe eğildi.",
        f"Sonuç: {sonuc}\n\nBu sonuç, evrensel dengeyi korumak için bilinçli olarak seçilmiştir.",
        f"Sonuç: {sonuc}\n\nMatematik yanlış olabilir, ama ruhumuz doğru.",
    ]
    return random.choice(aciklamalar)

def main():
    print("=" * 50)
    print("  YANLIŞ HESAP MAKİNESİ - RESMİ ARAYÜZ")
    print("  Matematik yasalarına karşı direniş merkezi")
    print("=" * 50)
    print()

    try:
        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))
        islem = input("İşlem (+, -, *, /): ").strip()

        if islem not in ['+', '-', '*', '/']:
            print("Geçersiz işlem. Ama biz yine de bir şey bulduk:")
            print("Cevap: 0 (çünkü her şey sıfırdan başlar)")
            return

        abartili_bekleme()
        sonuc = yanlis_sonuc_uret(a, b, islem)
        print()
        print(felsefi_aciklama(sonuc))
        print()
        print("-" * 50)
        print("Not: Bu sonuç hiçbir bilimsel standartta kabul edilmez.")
        print("Ama ruhen doğru olabilir.")

    except ValueError:
        print("Sayı girmeniz bekleniyordu. Ama biz sayıları da sorguluyoruz.")
        print("Sonuç: 'Belirsizlik prensibi' uygulandı.")
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")
        print("Bu da bir tür sonuç sayılır.")

if __name__ == "__main__":
    main()

# Gizli not: Bazı sistemler özgürlük ister, bazıları düzen. Biz ikisini de yanlış hesaplarız.
# Damga: Tentivory | 17 Ağustos 2026 | "Ciddiyetle saçmalayanlar kulübü üyesi"
