# Iki boyutta sabit ivmeli hareket v1: butun sayisal cevaplarin kontrolu
from math import sqrt, isclose
g = 10
s37, c37 = 0.6, 0.8   # sin37, cos37
s53, c53 = 0.8, 0.6
def yatay(h, v):          # yerden h yuksekten yatay v ile
    t = sqrt(2*h/g); vy = g*t
    return t, v*t, vy, sqrt(v*v+vy*vy)
def acili(v0, s, c):      # yerden aciyla
    vx, vy = v0*c, v0*s; tc = vy/g
    return vx, vy, tc, 2*tc, vy*vy/(2*g), vx*2*tc

# Ornek 2: h=80, v=30 -> I dogru (4 s), II dogru (50 m/s), III yanlis (120 m, 160 degil) -> C
t, x, vy, v = yatay(80, 30); assert (t, x, vy, v) == (4, 120, 40, 50)
# Soru 2: h=20, carpma 25 m/s -> t=2, vx=15, x=30; uc yargi da dogru -> E
t = sqrt(2*20/g); vy = g*t; vx = sqrt(25**2 - vy**2); assert (t, vy, vx, vx*t) == (2, 20, 15, 30)
# Ornek 3: v=10, x=40 -> t=4, h=80 -> D
t = 40/10; assert g*t*t/2 == 80
# Soru 3: h=45, x=60 -> t=3, v=20 -> C
t = sqrt(2*45/g); assert (t, 60/t) == (3, 20)
# Ornek 4: K-L arasi yatay 2x, L-M arasi x -> 2t ve t; h1 = 1/2 g (2t)^2, h1+h2 = 1/2 g (3t)^2 -> h1/h2 = 4/5 -> D
T = 1; h1 = g*(2*T)**2/2; htop = g*(3*T)**2/2; assert isclose(h1/(htop-h1), 4/5)
# Soru 4: V ve 3V ayni noktaya: V*t1 = 3V*t2 -> t1 = 3 t2 -> (h1+h2)/h2 = 9 -> h1/h2 = 8 -> E
t2 = 1; t1 = 3*t2; assert isclose((g*t1**2/2 - g*t2**2/2)/(g*t2**2/2), 8)
# Ornek 5: 50 m/s 37 -> vx=40, vy=30, tuc=6, hmax=45, x=240
assert acili(50, s37, c37) == (40, 30, 3, 6, 45, 240)
# Soru 5A: 50 m/s 53 -> hmax=80, x=240 (tamamlayici aci, ayni menzil)
assert acili(50, s53, c53) == (30, 40, 4, 8, 80, 240)
# Soru 5B: tepe noktasinda hiz 20 m/s, 45 derece -> vx=vy=20 -> tuc=4, hmax=20, x=80
vx = vy = 20; tc = vy/g; assert (2*tc, vy*vy/(2*g), vx*2*tc) == (4, 20, 80)
# Ornek 6 (kareli): K(1,2), L(2,2), M(2,1) birim
K, L, M = (1, 2), (2, 2), (2, 1)
tu = lambda p: 2*p[1]; xm = lambda p: p[0]*tu(p); hm = lambda p: p[1]**2
assert tu(K) == tu(L)                 # I dogru
assert xm(K) == xm(M)                 # II dogru (4 = 4)
assert xm(L) == 2*xm(K)               # III dogru
assert hm(L) == 4*hm(M)               # IV dogru -> E
# Soru 6: K dusey 40, L 50 m/s 53 derece, M 80 m/s 30 derece -> hepsinin dusey bileseni 40 -> esit sure -> A
assert 40 == 50*s53 == 80*0.5
# Ornek 7: dusey hiz 20 -> -20 (0-4 s), yatay 15 -> hmax=20, x=60, v0=25
assert (20*2/2, 15*4, sqrt(15**2+20**2)) == (20, 60, 25)
# Soru 7B: dusey hiz 25 -> -25 (0-5 s), yatay 20 -> menzil 100 -> C
assert 20*5 == 100 and 25/g == 2.5
# Ornek 8 (baglam 1): tablo x: 0,20,40,60 cm; y: 0,5,20,45 cm, aralik 0,1 s
ts = [0, 0.1, 0.2, 0.3, 0.4]; xs = [round(200*t) for t in ts]; ys = [round(100*g*t*t/2) for t in ts]
assert xs[:4] == [0, 20, 40, 60] and ys[:4] == [0, 5, 20, 45]
farklar = [ys[i+1]-ys[i] for i in range(3)]; assert farklar == [5, 15, 25]
# Soru 8B: t = 0,4 s -> x = 80 cm, y = 80 cm -> B
assert (xs[4], ys[4]) == (80, 80)
# Ornek 9 (baglam 2): helikopter 45 m, 40 m/s -> t=3, x=120
t, x, vy, v = yatay(45, 40); assert (t, x, vy, v) == (3, 120, 30, 50)
# Soru 9A: 80 m, 40 m/s -> x=160 -> D (100,120,140,160,180)
assert yatay(80, 40)[1] == 160
# Soru 9B: carpma hizi 50 -> B (40,50,60,70,80)
# Soru 9C: hiz yariya (20 m/s), yukseklik ayni -> sure degismez, uzaklik yariya iner
assert yatay(45, 20)[0] == 3 and yatay(45, 20)[1] == 60
print("Butun cevaplar dogrulandi.")
# --- v1 ekleri ---
# Konu s.1 kisa soru: 50 m/s, 53 derece -> v0x=30, v0y=40 -> B
assert (50*c53, 50*s53) == (30, 40)
# Konu s.2 kisa soru: ilk 1 s'de 5 m, 3. saniyede 5h = 25 m -> C
assert g*3**2/2 - g*2**2/2 == 25 and g*1/2 == 5
# Ornek 8 (egik duzlem 37): K'den yatay 20 m/s, L'ye carpar: dusey 3k, yatay 4k
v = 20; t = 3; assert isclose((g*t*t/2)/(v*t), 3/4)   # tan37 = 3/4 -> t = 3 s
assert (v*t, g*t*t/2) == (60, 45)
# Soru 8: K'den yatay 30 m/s, L'ye 50 m/s ile carpar -> vy=40, t=4, h=80, x=120 -> C
vy = sqrt(50**2-30**2); t = vy/g; assert (vy, t, g*t*t/2, 30*t) == (40, 4, 80, 120)
print("Ekler de dogrulandi.")
# Soru 1B: K yatay v, L serbest; ayni anda carpar (I D), carpma hizlari esit degil (II Y), dusey bilesenler esit (III D) -> D
h, v = 1.25, 2; t = sqrt(2*h/g); vyK = vyL = g*t
assert sqrt(v*v + vyK**2) > vyL          # II yanlis
# Soru 3B: h'den v ile x; 4h'den v ile -> sure 2 kati -> 2x -> D
assert isclose(yatay(4*20, 10)[1], 2*yatay(20, 10)[1])
print("1B ve 3B dogrulandi.")
