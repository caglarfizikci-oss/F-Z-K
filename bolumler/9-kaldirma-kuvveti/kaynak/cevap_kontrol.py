# Kaldırma kuvveti bağlamı: cevap kontrolü (assert)
veri = {  # cisim: (malzeme, hacim_kat, havada_N, suda_N, tasan_su_N)
    "K": ("alüminyum", 1, 5, 3, 2),
    "L": ("demir", 1, 16, 14, 2),
    "M": ("alüminyum", 2, 10, 6, 4),
}
Fk = {c: h - s for c, (_, _, h, s, _) in veri.items()}
assert Fk == {"K": 2, "L": 2, "M": 4}
for c, v in veri.items():
    assert Fk[c] == v[4]                      # kaldırma = taşan suyun ağırlığı
# yoğunluk/su oranları gerçekçi mi? (Al ~2,7  Fe ~7,9)
assert abs(5/2 - 2.7) < 0.3 and abs(16/2 - 7.9) < 0.2 and abs(10/4 - 2.7) < 0.3
# Örnek cevabı: K 2 N, L 2 N, M 4 N; taşan su ile eşit

# Soru 1A: hacim etkisi -> aynı malzeme, farklı hacim; ağırlık etkisi -> aynı hacim, farklı ağırlık
cift = lambda a, b: (veri[a][0] == veri[b][0], veri[a][1] == veri[b][1])
hacim_cifti = [p for p in [("K","L"),("K","M"),("L","M")] if cift(*p) == (True, False)]
agirlik_cifti = [p for p in [("K","L"),("K","M"),("L","M")] if cift(*p) == (False, True)]
assert hacim_cifti == [("K","M")] and agirlik_cifti == [("K","L")]
s1A = {"A": (("K","L"),("K","M")), "B": (("K","M"),("K","L")), "C": (("L","M"),("K","L")),
       "D": (("K","M"),("L","M")), "E": (("L","M"),("K","M"))}
assert [k for k, v in s1A.items() if v == (hacim_cifti[0], agirlik_cifti[0])] == ["B"]
# aynı malzemedeki K ve L'nin kaldırma kuvveti eşit (ağırlığa bağlı değil), M'nin 2 katı (hacme bağlı)
assert Fk["K"] == Fk["L"] and Fk["M"] == 2 * Fk["K"]

# Soru 1B: M tuzlu suda (yoğunluk > su), tamamen batık -> batan hacim aynı
d_oran = 1.2
Fk_tuz = Fk["M"] * d_oran
okunan_su, okunan_tuz = 10 - Fk["M"], 10 - Fk_tuz
tasan_su, tasan_tuz = Fk["M"], Fk_tuz
yon = lambda a, b: "Artar" if b > a else ("Azalır" if b < a else "Değişmez")
dogru1B = (yon(okunan_su, okunan_tuz), yon(tasan_su, tasan_tuz))
s1B = {"A": ("Artar","Değişmez"), "B": ("Değişmez","Artar"), "C": ("Azalır","Değişmez"),
       "D": ("Azalır","Artar"), "E": ("Değişmez","Değişmez")}
assert [k for k, v in s1B.items() if v == dogru1B] == ["D"]

# Soru 1C: yüzen bardak; para eklenince hâlâ yüzüyor -> Fk = toplam ağırlık, taşan su = toplam ağırlık
G_bardak, G_para = 1, 2
Fk_once, Fk_sonra = G_bardak, G_bardak + G_para
I = Fk_sonra > Fk_once                         # kaldırma kuvveti artmıştır
II = Fk_sonra == G_bardak + G_para              # toplam ağırlığa eşit
III = Fk_sonra < G_bardak + G_para              # taşan su toplam ağırlıktan küçük (yanlış)
dogru = tuple(i for i, d in zip(["I","II","III"], [I, II, III]) if d)
s1C = {"A": ("I",), "B": ("II",), "C": ("I","II"), "D": ("I","III"), "E": ("II","III")}
assert [k for k, v in s1C.items() if v == dogru] == ["C"]
print("Tüm kontroller geçti. Cevaplar: 1A B, 1B D, 1C C")
