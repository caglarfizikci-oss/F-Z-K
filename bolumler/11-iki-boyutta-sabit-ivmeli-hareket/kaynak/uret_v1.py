# -*- coding: utf-8 -*-
"""Iki Boyutta Sabit Ivmeli Hareket v1: HTML ureteci.
Calistirma: python3 uret_v1.py  ->  iki_boyutta_v1.html
Sayilar kontrol.py ile dogrulanir."""
import math, os

MAG = "#EC008C"; CAM = "#00AEEF"; PEM = "#F05A89"; SIY = "#231F20"
YES = "#39B54A"; TUR = "#F8992F"

# ---------------------------------------------------------------- yardimcilar
def kesir(p, q):
    return f'<span class="kesir"><span>{p}</span><span>{q}</span></span>'

def vek(a):  # ustu oklu vektor adi
    return f'<span class="vek">{a}</span>'

def ok(x1, y1, x2, y2, renk=MAG, w=1.6, bas=6, kesik=False):
    ang = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - bas * math.cos(ang), y2 - bas * math.sin(ang)
    px, py = -math.sin(ang) * bas * 0.45, math.cos(ang) * bas * 0.45
    d = ' stroke-dasharray="3 2"' if kesik else ''
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{renk}" stroke-width="{w}"{d}/>'
            f'<polygon points="{x2:.1f},{y2:.1f} {bx+px:.1f},{by+py:.1f} {bx-px:.1f},{by-py:.1f}" fill="{renk}"/>')

def cizgi(x1, y1, x2, y2, renk=SIY, w=0.8, kesik=True):
    d = ' stroke-dasharray="3 2"' if kesik else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{renk}" stroke-width="{w}"{d}/>'

def yazi(x, y, t, boy=9, renk=SIY, hiza="middle", kalin=False, italik=False):
    k = ' font-weight="bold"' if kalin else ''
    i = ' font-style="italic"' if italik else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{boy}" fill="{renk}" text-anchor="{hiza}"{k}{i} font-family="Liberation Sans">{t}</text>'

def top(x, y, r=5, renk="#F6C181"):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{renk}" stroke="#8B5A2B" stroke-width="0.8"/>'
            f'<circle cx="{x-r*0.35:.1f}" cy="{y-r*0.35:.1f}" r="{r*0.3:.1f}" fill="#FFFFFF"/>')

def svg(w, h, icerik, gen_mm):
    # Sekil kucultulunce etiketler okunaksiz kalmasin: ana etiketler en az ~2,4 mm (7 punto) olur.
    import re
    olcek = gen_mm / w                      # bir birim kac mm
    en_az = 2.4 / olcek
    def buyut(m):
        v = float(m.group(1))
        return f'font-size="{max(v, en_az) if v >= 7 else max(v, en_az * 0.7):.1f}"'
    icerik = re.sub(r"font-size=[\"']([\d.]+)[\"']", buyut, icerik)
    return (f'<svg width="{gen_mm}mm" height="{gen_mm*h/w:.2f}mm" viewBox="0 0 {w} {h}" '
            f'xmlns="http://www.w3.org/2000/svg">{icerik}</svg>')

def parabol(x0, y0, x1, ytepe, n=40, son=1.0):
    """(x0,y0)'dan baslayip ayni seviyede x1'e inen parabol; ytepe tepe noktasi y'si."""
    pts = []
    for i in range(n + 1):
        u = i / n * son
        x = x0 + (x1 - x0) * u
        y = y0 - 4 * (y0 - ytepe) * u * (1 - u)
        pts.append(f"{x:.1f},{y:.1f}")
    return pts

def yol(pts, renk=SIY, w=1, kesik=True):
    d = ' stroke-dasharray="2.5 2"' if kesik else ''
    return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{renk}" stroke-width="{w}"{d}/>'

def zemin(x1, x2, y):
    s = f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{SIY}" stroke-width="1.4"/>'
    for xx in range(int(x1), int(x2) - 4, 7):
        s += f'<line x1="{xx+6}" y1="{y}" x2="{xx}" y2="{y+5}" stroke="#ACACAC" stroke-width="0.8"/>'
    return s

def ucurum(x, y_ust, y_alt, gen=40):
    """Sol tarafta yuksek bir yer (blok), sag kenari x'te."""
    s = f'<rect x="{x-gen}" y="{y_ust}" width="{gen}" height="{y_alt-y_ust}" fill="#F3B366" stroke="#B9813A" stroke-width="0.8"/>'
    for k in range(int(y_ust) + 8, int(y_alt), 10):
        s += f'<line x1="{x-gen}" y1="{k}" x2="{x}" y2="{k}" stroke="#F6C181" stroke-width="1"/>'
    s += f'<line x1="{x-gen}" y1="{y_ust}" x2="{x}" y2="{y_ust}" stroke="{SIY}" stroke-width="1.2"/>'
    return s

def yatay_fig(h_et, v_et, x_et=None, gen_mm=60, h_px=95, x_px=110, carpma=None):
    """Yuksekten yatay hizla baslayan hareket: blok, top, yorunge, h ve x olculeri."""
    X0, Y0 = 130, 20; YZ = Y0 + h_px
    s = ucurum(X0, Y0, YZ, 45) + zemin(10, X0 + x_px + 40, YZ)
    pts = []
    for i in range(31):
        u = i / 30; pts.append(f"{X0 + x_px*u:.1f},{Y0 + h_px*u*u:.1f}")
    s += yol(pts)
    s += top(X0 + 1, Y0 - 5) + ok(X0 + 8, Y0 - 5, X0 + 34, Y0 - 5) + yazi(X0 + 36, Y0 - 9, v_et, 8.5, hiza="start")
    s += ok(X0 - 52, Y0 + 2, X0 - 52, YZ - 1, CAM, 0.8, 4) + ok(X0 - 52, YZ - 2, X0 - 52, Y0 + 1, CAM, 0.8, 4)
    s += yazi(X0 - 55, (Y0 + YZ) / 2 + 3, h_et, 8.5, hiza="end")
    if x_et:
        s += ok(X0 + 2, YZ + 12, X0 + x_px - 1, YZ + 12, CAM, 0.8, 4) + ok(X0 + x_px - 2, YZ + 12, X0 + 1, YZ + 12, CAM, 0.8, 4)
        s += yazi(X0 + x_px / 2, YZ + 22, x_et, 8.5)
    if carpma:
        s += ok(X0 + x_px, YZ, X0 + x_px + 14, YZ + 16) + yazi(X0 + x_px + 16, YZ + 14, carpma, 8.5, hiza="start")
    return svg(X0 + x_px + 60, YZ + 28, s, gen_mm)

# ---------------------------------------------------------------- sekiller
def fig_strobo(gen_mm=62, etiket=True):
    """Masanin kenarindan yatay cikan K ile ayni anda, ayni yukseklikten masanin disinda birakilan L."""
    X0, Y0, dx = 92, 22, 30          # masa kenari (K'nin cikis noktasi)
    YZ = Y0 + 136
    s = f'<rect x="40" y="{Y0+5}" width="{X0-40}" height="5" fill="#B9813A"/>'
    s += f'<rect x="44" y="{Y0+10}" width="4" height="{YZ-Y0-10}" fill="#8B5A2B"/><rect x="{X0-8}" y="{Y0+10}" width="4" height="{YZ-Y0-10}" fill="#8B5A2B"/>'
    s += f'<rect x="8" y="{Y0-16}" width="30" height="3" fill="#808285"/><line x1="22" y1="{Y0-13}" x2="22" y2="{Y0-5}" stroke="#808285" stroke-width="1"/>'
    s += zemin(2, 235, YZ)
    for n in range(5):
        y = Y0 + 7.4 * n * n
        if n:
            s += cizgi(28, y, X0 + dx * n - 6, y, "#808285", 0.5)
        s += top(X0 + dx * n, y, 4.2, "#F6C181")      # K
        s += top(22, y, 4.2, "#9ED3EE")              # L
    if etiket:
        s += yazi(X0 - 2, Y0 - 9, "K", 9, kalin=True, hiza="end") + yazi(10, Y0 + 3, "L", 9, kalin=True, hiza="end")
        for n in range(1, 5):
            s += yazi(X0 + dx * n + 8, Y0 + 7.4 * n * n + 3, f"{n}t", 7.5, hiza="start")
    s += ok(X0 + 6, Y0 - 9, X0 + 24, Y0 - 9, MAG, 1.2, 5)
    return svg(240, YZ + 10, s, gen_mm)

def fig_bilesen(gen_mm=42):
    X0, Y0 = 25, 105
    s = cizgi(X0, Y0, X0 + 120, Y0, SIY, 0.8, False)
    s += cizgi(X0 + 80, Y0, X0 + 80, Y0 - 60, MAG, 0.8) + cizgi(X0, Y0 - 60, X0 + 80, Y0 - 60, MAG, 0.8)
    s += ok(X0, Y0, X0 + 80, Y0 - 60, MAG, 1.8) + ok(X0, Y0, X0 + 80, Y0, CAM, 1.6) + ok(X0, Y0, X0, Y0 - 60, CAM, 1.6)
    s += f'<path d="M{X0+22},{Y0} A22,22 0 0 0 {X0+17.6},{Y0-13.2}" fill="none" stroke="{SIY}" stroke-width="0.8"/>'
    s += yazi(X0 + 27, Y0 - 5, "α", 9, hiza="start", italik=True)
    s += yazi(X0 + 44, Y0 - 42, "v₀", 10, MAG, kalin=True) + yazi(X0 + 40, Y0 + 13, "v₀ₓ", 9.5, CAM, kalin=True)
    s += yazi(X0 - 4, Y0 - 30, "v₀ᵧ", 9.5, CAM, "end", True)
    return svg(160, 125, s, gen_mm)

def fig_yatay_genel(gen_mm=70):
    X0, Y0, ux, uy = 60, 22, 34, 6  # x adimi, h birimi
    YZ = Y0 + uy * 9 * 2.0
    hh = lambda n: Y0 + uy * 2 * n * n
    s = ucurum(X0, Y0, YZ, 45) + zemin(10, X0 + 3 * ux + 60, YZ)
    pts = [f"{X0 + ux*3*i/30:.1f},{Y0 + uy*2*(3*i/30)**2:.1f}" for i in range(31)]
    s += yol(pts)
    s += top(X0 + 1, Y0 - 5) + ok(X0 + 8, Y0 - 5, X0 + 30, Y0 - 5) + yazi(X0 + 33, Y0 - 9, "v", 9, hiza="start", italik=True)
    for n in (1, 2, 3):
        x, y = X0 + ux * n, hh(n)
        s += cizgi(X0 - 50, y, x, y, "#808285", 0.5) + cizgi(x, y, x, YZ, "#808285", 0.5)
        s += ok(x, y, x + 24, y, CAM, 1.2, 5) + ok(x, y, x, y + 8 * n, CAM, 1.2, 5)
        s += yazi(x + 3, y - 4, f"{n}t", 8, hiza="start")
    s += ok(X0 + 3 * ux, YZ, X0 + 3 * ux + 24, YZ + 22, MAG, 1.5) + yazi(X0 + 3 * ux + 27, YZ + 20, "v", 9, MAG, "start", True, True)
    for n, et in ((1, "h"), (2, "3h"), (3, "5h")):
        s += yazi(X0 - 52, (hh(n - 1) + hh(n)) / 2 + 3, et, 8.5, hiza="end")
        s += ok(X0 - 48, hh(n - 1) + 1, X0 - 48, hh(n) - 1, "#808285", 0.6, 3)
    for n in (1, 2, 3):
        s += yazi(X0 + ux * (n - 0.5), YZ + 12, "x", 8.5, italik=True)
    return svg(X0 + 3 * ux + 70, YZ + 26, s, gen_mm)

def fig_acili_genel(gen_mm=92):
    X0, YZ, L, H = 30, 150, 240, 100
    s = zemin(10, X0 + L + 30, YZ)
    pts = parabol(X0, YZ, X0 + L, YZ - H)
    s += yol(pts)
    tx = X0 + L / 2
    s += cizgi(tx, YZ - H, tx, YZ, "#808285", 0.6)
    s += ok(tx + 10, YZ - 2, tx + 10, YZ - H + 2, CAM, 0.7, 4) + ok(tx + 10, YZ - H + 2, tx + 10, YZ - 2, CAM, 0.7, 4)
    s += yazi(tx + 14, YZ - H / 2, "h", 9, hiza="start", italik=True) + yazi(tx + 20, YZ - H / 2 + 3, "max", 6.5, hiza="start")
    # baslangic
    s += top(X0, YZ - 4, 4.5) + ok(X0, YZ - 4, X0 + 36, YZ - 52, MAG, 1.6) + yazi(X0 + 28, YZ - 56, "v₀", 9.5, MAG, kalin=True)
    s += ok(X0, YZ - 4, X0 + 36, YZ - 4, CAM, 1.2, 5) + ok(X0, YZ - 4, X0, YZ - 52, CAM, 1.2, 5)
    s += yazi(X0 + 18, YZ + 12, "v₀ₓ", 8.5, CAM) + yazi(X0 - 4, YZ - 30, "v₀ᵧ", 8.5, CAM, "end")
    # tepe
    s += top(tx, YZ - H, 4.5) + ok(tx + 5, YZ - H, tx + 41, YZ - H, CAM, 1.4, 5)
    s += yazi(tx, YZ - H - 9, "T (tepe noktası)", 8.5) + yazi(tx + 43, YZ - H + 4, "v₀ₓ", 8.5, CAM, "start")
    # ara noktalar
    for u, et in ((0.25, "A"), (0.75, "B")):
        x = X0 + L * u; y = YZ - 4 * H * u * (1 - u)
        s += top(x, y, 4) + ok(x, y, x + 36, y, CAM, 1.2, 5)
        s += ok(x, y, x, y - (36 if u < 0.5 else -36) * 0.95, CAM, 1.2, 5) + yazi(x - 8, y - 4, et, 9, kalin=True, hiza="end")
    # yere varis
    xe = X0 + L
    s += ok(xe, YZ - 2, xe + 36, YZ - 2, CAM, 1.2, 5) + ok(xe, YZ - 2, xe, YZ + 34, CAM, 1.2, 5)
    s += yazi(xe + 4, YZ + 30, "v₀ᵧ", 8.5, CAM, "start")
    s += ok(X0 + 2, YZ + 22, X0 + L - 2, YZ + 22, "#808285", 0.6, 4) + ok(X0 + L - 2, YZ + 22, X0 + 2, YZ + 22, "#808285", 0.6, 4)
    s += yazi(X0 + L / 2 - 10, YZ + 34, "x", 9, italik=True) + yazi(X0 + L / 2 - 4, YZ + 37, "menzil", 6.5, hiza="start")
    s += f'<path d="M{X0+20},{YZ-4} A20,20 0 0 0 {X0+15.5},{YZ-16.6}" fill="none" stroke="{SIY}" stroke-width="0.8"/>' + yazi(X0 + 24, YZ - 9, "α", 8.5, hiza="start", italik=True)
    return svg(X0 + L + 60, YZ + 42, s, gen_mm)

def grafik(tur, gen_mm=36, baslik="", et_y="", et_x="t (s)", tc=True, deger=None):
    """Kucuk grafik. tur: 'parabol','dogru-azalan','yatay-alt','yatay-ust','dogru-artan','yatay-sifir'"""
    X0, Y0, W, H = 26, 12, 96, 70
    s = ok(X0, Y0 + H, X0, Y0 - 4, SIY, 0.9, 5)
    if tur in ("dogru-azalan", "yatay-alt", "yatay-sifir"):
        ox = Y0 + H / 2
    else:
        ox = Y0 + H
    s += ok(X0, ox, X0 + W + 6, ox, SIY, 0.9, 5)
    s += yazi(X0 + 2, Y0 - 6, et_y, 7.5, hiza="start") + yazi(X0 + W + 6, ox + 10, et_x, 7, hiza="end")
    xs, xu = X0 + W * 0.42, X0 + W * 0.84
    if tur == "parabol":
        pts = parabol(X0, ox, xu, Y0 + 8)
        s += yol(pts, MAG, 1.5, False) + cizgi(xs, Y0 + 8, xs, ox)
        s += yazi(xs, ox + 9, "t", 7, italik=True) + yazi(xs + 3, ox + 11, "ç", 5.5, hiza="start")
        s += yazi(xu, ox + 9, "t", 7, italik=True) + yazi(xu + 3, ox + 11, "u", 5.5, hiza="start")
        s += cizgi(X0, Y0 + 8, xs, Y0 + 8) + yazi(X0 - 3, Y0 + 11, "h<tspan font-size='5.5' dy='1.5'>max</tspan>", 7.5, hiza="end", italik=True)
    elif tur == "dogru-azalan":
        top_ = Y0 + 4; alt = 2 * ox - top_
        s += f'<polygon points="{X0},{ox} {X0},{top_} {xs},{ox}" fill="#FDE9F1"/>'
        s += f'<line x1="{X0}" y1="{top_}" x2="{xu}" y2="{alt}" stroke="{MAG}" stroke-width="1.5"/>'
        s += cizgi(xu, ox, xu, alt) + cizgi(X0, alt, xu, alt)
        s += yazi(X0 - 3, top_ + 3, "v₀ᵧ", 7, hiza="end") + yazi(X0 - 3, alt + 3, "–v₀ᵧ", 7, hiza="end")
        s += yazi(xs, ox - 3, "t", 7, italik=True) + yazi(xu + 4, ox - 3, "t", 7, italik=True)
        s += yazi(xs + 3, ox - 1, "ç", 5.5, hiza="start") + yazi(xu + 7, ox - 1, "u", 5.5, hiza="start")
        s += yazi(X0 + 12, ox - 9, "h", 7.5, MAG, italik=True)
    elif tur == "yatay-alt":
        y = ox + 20
        s += f'<line x1="{X0}" y1="{y}" x2="{xu}" y2="{y}" stroke="{MAG}" stroke-width="1.5"/>' + cizgi(xu, ox, xu, y)
        s += yazi(X0 - 3, y + 3, "–g", 7.5, hiza="end", italik=True)
    elif tur == "yatay-sifir":
        s += f'<line x1="{X0}" y1="{ox}" x2="{xu}" y2="{ox}" stroke="{MAG}" stroke-width="2.2"/>'
        s += yazi(X0 - 3, ox + 3, "0", 7.5, hiza="end")
    elif tur == "yatay-ust":
        y = Y0 + 22
        s += f'<rect x="{X0}" y="{y}" width="{xu-X0}" height="{ox-y}" fill="#FDE9F1"/>'
        s += f'<line x1="{X0}" y1="{y}" x2="{xu}" y2="{y}" stroke="{MAG}" stroke-width="1.5"/>' + cizgi(xu, ox, xu, y)
        s += yazi(X0 - 3, y + 3, "v₀ₓ", 7, hiza="end") + yazi((X0 + xu) / 2, (y + ox) / 2 + 3, "x", 8, MAG, italik=True)
        s += yazi(xu, ox + 9, "t", 7, italik=True) + yazi(xu + 3, ox + 11, "u", 5.5, hiza="start")
    elif tur == "dogru-artan":
        s += f'<line x1="{X0}" y1="{ox}" x2="{xu}" y2="{Y0+8}" stroke="{MAG}" stroke-width="1.5"/>'
        s += cizgi(xu, ox, xu, Y0 + 8) + cizgi(X0, Y0 + 8, xu, Y0 + 8)
        s += yazi(X0 - 3, Y0 + 11, "x", 7.5, hiza="end", italik=True)
        s += yazi(xu, ox + 9, "t", 7, italik=True) + yazi(xu + 3, ox + 11, "u", 5.5, hiza="start")
    return svg(W + 40, H + 26, s, gen_mm)

def fig_dusey_hiz(v0y, tu, vx=None, gen_mm=48, etiket="Hızın düşey bileşeni (m/s)"):
    X0, Y0, W, H = 34, 16, 120, 96
    ox = Y0 + H / 2
    s = ok(X0, Y0 + H + 4, X0, Y0 - 6, SIY, 0.9, 5) + ok(X0, ox, X0 + W + 14, ox, SIY, 0.9, 5)
    s += yazi(X0 + 3, Y0 - 8, etiket, 7.5, hiza="start") + yazi(X0 + W + 14, ox + 12, "t (s)", 7.5, hiza="end")
    xe = X0 + W * 0.9; top_ = Y0 + 4; alt = 2 * ox - top_
    s += f'<line x1="{X0}" y1="{top_}" x2="{xe}" y2="{alt}" stroke="{MAG}" stroke-width="1.6"/>'
    s += cizgi(X0, top_, X0 + 10, top_) + cizgi(X0, alt, xe, alt) + cizgi(xe, ox, xe, alt)
    s += yazi(X0 - 4, top_ + 3, f"{v0y}", 8, hiza="end") + yazi(X0 - 4, alt + 3, f"–{v0y}", 8, hiza="end") + yazi(X0 - 4, ox + 3, "0", 8, hiza="end")
    s += yazi((X0 + xe) / 2, ox - 4, f"{tu/2:g}".replace(".", ","), 8) + yazi(xe + 2, ox - 4, f"{tu}", 8, hiza="start")
    return svg(W + 60, H + 30, s, gen_mm)

def fig_yatay_hiz(vx, tu, gen_mm=48):
    X0, Y0, W, H = 34, 16, 120, 70
    ox = Y0 + H
    s = ok(X0, ox, X0, Y0 - 6, SIY, 0.9, 5) + ok(X0, ox, X0 + W + 14, ox, SIY, 0.9, 5)
    s += yazi(X0 + 3, Y0 - 8, "Hızın yatay bileşeni (m/s)", 7.5, hiza="start") + yazi(X0 + W + 14, ox - 5, "t (s)", 7.5, hiza="end")
    xe = X0 + W * 0.9; y = Y0 + 22
    s += f'<line x1="{X0}" y1="{y}" x2="{xe}" y2="{y}" stroke="{MAG}" stroke-width="1.6"/>' + cizgi(xe, ox, xe, y)
    s += yazi(X0 - 4, y + 3, f"{vx}", 8, hiza="end") + yazi(xe, ox + 11, f"{tu}", 8)
    return svg(W + 60, H + 26, s, gen_mm)

def fig_acili(v_et, aci, h=None, x=None, gen_mm=60, tepe_hiz=None, L=200, H=None, tepe_et=None):
    X0, YZ = 75, 120
    if H is None:
        H = {37: 55, 53: 95, 45: 70}.get(aci, 70)
    s = zemin(10, X0 + L + 20, YZ) + yol(parabol(X0, YZ, X0 + L, YZ - H))
    r = math.radians(aci)
    s += top(X0, YZ - 4, 4.5) + ok(X0, YZ - 4, X0 + 44 * math.cos(r), YZ - 4 - 44 * math.sin(r), MAG, 1.6)
    s += yazi(X0 + 44 * math.cos(r) - 4, YZ - 4 - 44 * math.sin(r) - 2, v_et, 8.5, MAG, "end", True)
    s += f'<path d="M{X0+18},{YZ-4} A18,18 0 0 0 {X0+18*math.cos(r):.1f},{YZ-4-18*math.sin(r):.1f}" fill="none" stroke="{SIY}" stroke-width="0.8"/>'
    s += yazi(X0 + 22, YZ - 8, f"{aci}°", 8, hiza="start")
    tx = X0 + L / 2
    if tepe_hiz:
        s += top(tx, YZ - H, 4) + ok(tx + 5, YZ - H, tx + 36, YZ - H, MAG, 1.4, 5) + yazi(tx + 38, YZ - H + 3, tepe_hiz, 8, MAG, "start", True)
    if tepe_et:
        s += top(tx, YZ - H, 4) + yazi(tx, YZ - H - 8, tepe_et, 9, kalin=True)
    if h:
        s += cizgi(tx, YZ - H, tx, YZ, "#808285", 0.6) + yazi(tx + 5, YZ - H / 3, h, 8.5, hiza="start")
    if x:
        s += ok(X0 + 2, YZ + 12, X0 + L - 2, YZ + 12, "#808285", 0.6, 4) + ok(X0 + L - 2, YZ + 12, X0 + 2, YZ + 12, "#808285", 0.6, 4) + yazi(tx, YZ + 23, x, 8.5)
    return svg(X0 + L + 50, YZ + 28, s, gen_mm)

def fig_kareli(vekt, n_x=4, n_y=3, gen_mm=40, etiketler=True, yer=True):
    """vekt: [(ad, dx, dy, renk)]; A noktasindan cikan vektorler."""
    k = 26; X0, Y0 = 14, 10
    s = ""
    for i in range(n_x + 1):
        s += cizgi(X0 + i * k, Y0, X0 + i * k, Y0 + n_y * k, SIY, 0.5)
    for j in range(n_y + 1):
        s += cizgi(X0, Y0 + j * k, X0 + n_x * k, Y0 + j * k, SIY, 0.5)
    yz = Y0 + n_y * k
    if yer:
        s += zemin(X0 - 6, X0 + n_x * k + 30, yz) + yazi(X0 + n_x * k + 28, yz - 4, "yer", 8, hiza="end")
    for ad, dx, dy, renk in vekt:
        s += ok(X0, yz, X0 + dx * k, yz - dy * k, renk, 1.6)
        if etiketler:
            s += yazi(X0 + dx * k + 3, yz - dy * k - 3, f"v<tspan font-size='6' dy='2'>{ad}</tspan>", 8.5, renk, "start", True)
    s += f'<circle cx="{X0}" cy="{yz}" r="2.2" fill="{SIY}"/>' + yazi(X0 - 3, yz + 11, "A", 8.5, kalin=True)
    return svg(X0 + n_x * k + 34, yz + 16, s, gen_mm)

def fig_egik(v_et, gen_mm=44, carpma=None, olcu=True):
    X0, Y0, u = 95, 34, 30   # K noktasi; L = (X0+4u, Y0+3u)
    XL, YL = X0 + 4 * u, Y0 + 3 * u
    s = f'<rect x="{X0-40}" y="{Y0}" width="40" height="{YL-Y0}" fill="#F3B366" stroke="#B9813A" stroke-width="0.8"/>'
    s += f'<polygon points="{X0},{Y0} {XL},{YL} {X0},{YL}" fill="#F6C181" stroke="#B9813A" stroke-width="0.8"/>'
    s += zemin(X0 - 44, XL + 20, YL)
    s += yol([f"{X0 + 4*u*k/30:.1f},{Y0 + 3*u*(k/30)**2:.1f}" for k in range(31)])
    s += top(X0 + 1, Y0 - 5) + ok(X0 + 8, Y0 - 5, X0 + 32, Y0 - 5) + yazi(X0 + 34, Y0 - 9, v_et, 8.5, MAG, "start", True)
    s += yazi(X0 - 4, Y0 - 6, "K", 9, kalin=True, hiza="end") + yazi(XL + 4, YL - 6, "L", 9, kalin=True, hiza="start")
    s += f'<path d="M{XL-16},{YL} A16,16 0 0 1 {XL-12.8:.1f},{YL-9.6:.1f}" fill="none" stroke="{SIY}" stroke-width="0.8"/>' + yazi(XL - 20, YL - 3, "37°", 7.5, hiza="end")
    if carpma:
        s += ok(XL, YL, XL + 12, YL + 16) + yazi(XL + 14, YL + 14, carpma, 8, MAG, "start", True)
    if olcu:
        s += ok(X0 - 46, Y0 + 1, X0 - 46, YL - 1, CAM, 0.7, 4) + ok(X0 - 46, YL - 1, X0 - 46, Y0 + 1, CAM, 0.7, 4) + yazi(X0 - 49, (Y0 + YL) / 2 + 3, "h", 9, hiza="end", italik=True)
        s += ok(X0 + 1, YL + 10, XL - 1, YL + 10, CAM, 0.7, 4) + ok(XL - 1, YL + 10, X0 + 1, YL + 10, CAM, 0.7, 4) + yazi((X0 + XL) / 2, YL + 21, "x", 9, italik=True)
    return svg(XL + 110, YL + 26, s, gen_mm)

def fig_iki_yorunge(gen_mm=50):
    X0, YZ, L = 20, 110, 200
    s = zemin(5, X0 + L + 20, YZ)
    s += yol(parabol(X0, YZ, X0 + L, YZ - 37.5), "#1678BE", 1.2) + yol(parabol(X0, YZ, X0 + L, YZ - 66.7), MAG, 1.2)
    s += ok(X0, YZ, X0 + 40, YZ - 30, "#1678BE", 1.4) + ok(X0, YZ, X0 + 30, YZ - 40, MAG, 1.4)
    s += yazi(X0 + 44, YZ - 26, "37°", 8, "#1678BE", "start", True) + yazi(X0 + 22, YZ - 44, "53°", 8, MAG, "start", True)
    s += f'<circle cx="{X0+L}" cy="{YZ}" r="2.4" fill="{SIY}"/>' + yazi(X0 + L / 2, YZ + 14, "aynı menzil", 8)
    return svg(X0 + L + 25, YZ + 20, s, gen_mm)

def fig_helikopter(gen_mm=74):
    X0, Y0, YZ = 40, 34, 140
    s = f'<rect x="0" y="0" width="300" height="{YZ}" fill="#E8F4FB"/>'
    # orman ve yangin
    s += f'<rect x="0" y="{YZ}" width="300" height="20" fill="#8DC63F"/>'
    for i, xx in enumerate(range(150, 300, 14)):
        s += f'<polygon points="{xx},{YZ} {xx+7},{YZ-22 - (i%3)*4} {xx+14},{YZ}" fill="#39B54A" stroke="#1E7B34" stroke-width="0.6"/>'
    for xx in (178, 192, 206):
        s += f'<path d="M{xx},{YZ} q-6,-14 2,-24 q2,10 6,6 q4,8 -2,18 z" fill="#F8992F" stroke="#D2232A" stroke-width="0.6"/>'
    # helikopter
    hx, hy = X0, Y0
    s += f'<ellipse cx="{hx}" cy="{hy}" rx="22" ry="10" fill="#D2232A" stroke="#7A1418" stroke-width="0.8"/>'
    s += f'<path d="M{hx+6},{hy-8} q12,0 15,8 l-15,0 z" fill="#9ED3EE" stroke="#1C2630" stroke-width="0.6"/>'
    s += f'<rect x="{hx-50}" y="{hy-4}" width="30" height="5" fill="#D2232A"/>'
    s += f'<rect x="{hx-54}" y="{hy-11}" width="5" height="12" fill="#D2232A"/>'
    s += f'<line x1="{hx-30}" y1="{hy-16}" x2="{hx+30}" y2="{hy-16}" stroke="#58595B" stroke-width="2"/><rect x="{hx-2}" y="{hy-16}" width="4" height="6" fill="#58595B"/>'
    s += f'<line x1="{hx-14}" y1="{hy+12}" x2="{hx+14}" y2="{hy+12}" stroke="#58595B" stroke-width="1.6"/>'
    s += f'<line x1="{hx}" y1="{hy+10}" x2="{hx}" y2="{hy+26}" stroke="#58595B" stroke-width="0.8"/>'
    s += f'<path d="M{hx-6},{hy+26} l12,0 l-2,9 l-8,0 z" fill="#FF8000" stroke="#7A4A00" stroke-width="0.6"/>'
    s += ok(hx + 28, hy - 2, hx + 62, hy - 2, MAG, 1.6) + yazi(hx + 64, hy + 1, "40 m/s", 8.5, MAG, "start", True)
    # su yorungesi
    pts = [f"{hx + 150*u:.1f},{hy+35 + (YZ-hy-35)*u*u:.1f}" for u in [i/30 for i in range(31)]]
    s += yol(pts, "#1678BE", 1.2)
    s += ok(hx - 22, hy + 35, hx - 22, YZ - 1, CAM, 0.7, 4) + ok(hx - 22, YZ - 2, hx - 22, hy + 36, CAM, 0.7, 4) + yazi(hx - 19, (hy + 35 + YZ) / 2, "45 m", 8, hiza="start")
    s += yazi(hx + 150, YZ - 28, "hedef", 8)
    return svg(300, YZ + 20, s, gen_mm)

def fig_iki_cisim(gen_mm=54):
    """Ayni dusey hizada V ve 3V hizli iki cisim, ayni noktaya duser."""
    X0, Y0, YZ = 100, 16, 136
    s = ucurum(X0, Y0, YZ, 40) + zemin(10, X0 + 190, YZ)
    y2 = YZ - 15  # 1/9
    y2 = Y0 + (YZ - Y0) * 8 / 9
    s += f'<rect x="{X0-3}" y="{y2}" width="18" height="3" fill="#8B5A2B"/>'
    xd = X0 + 150
    s += yol([f"{X0 + (xd-X0)*u:.1f},{Y0 + (YZ-Y0)*u*u:.1f}" for u in [i/30 for i in range(31)]])
    s += yol([f"{X0+12 + (xd-X0-12)*u:.1f},{y2 + (YZ-y2)*u*u:.1f}" for u in [i/30 for i in range(31)]])
    s += top(X0 + 1, Y0 - 5) + ok(X0 + 8, Y0 - 5, X0 + 28, Y0 - 5) + yazi(X0 + 31, Y0 - 2, "v", 9, MAG, "start", True, True)
    s += top(X0 + 12, y2 - 5) + ok(X0 + 19, y2 - 5, X0 + 49, y2 - 5) + yazi(X0 + 52, y2 - 2, "3v", 9, MAG, "start", True, True)
    s += f'<circle cx="{xd}" cy="{YZ}" r="2.2" fill="{SIY}"/>'
    s += ok(X0 - 46, Y0 + 1, X0 - 46, y2 - 1, CAM, 0.7, 4) + ok(X0 - 46, y2 - 1, X0 - 46, Y0 + 1, CAM, 0.7, 4)
    s += ok(X0 - 46, y2 + 1, X0 - 46, YZ - 1, CAM, 0.7, 4) + ok(X0 - 46, YZ - 1, X0 - 46, y2 + 1, CAM, 0.7, 4)
    s += yazi(X0 - 49, (Y0 + y2) / 2, "h₁", 9, hiza="end") + yazi(X0 - 49, (y2 + YZ) / 2 + 4, "h₂", 9, hiza="end")
    return svg(X0 + 200, YZ + 10, s, gen_mm)

def fig_klm(gen_mm=56):
    X0, Y0, YZ = 100, 16, 136
    s = ucurum(X0, Y0, YZ, 40) + zemin(10, X0 + 170, YZ)
    xm = X0 + 150
    s += yol([f"{X0 + (xm-X0)*u:.1f},{Y0 + (YZ-Y0)*u*u:.1f}" for u in [i/30 for i in range(31)]])
    xl = X0 + 100; yl = Y0 + (YZ - Y0) * 4 / 9
    s += f'<circle cx="{xl}" cy="{yl}" r="2.4" fill="{SIY}"/>' + yazi(xl + 6, yl - 3, "L", 9, kalin=True, hiza="start")
    s += cizgi(X0 - 40, yl, xl, yl, "#808285", 0.5) + cizgi(xl, yl, xl, YZ, "#808285", 0.5)
    s += top(X0 + 1, Y0 - 5) + ok(X0 + 8, Y0 - 5, X0 + 28, Y0 - 5) + yazi(X0 - 4, Y0 - 6, "K", 9, kalin=True, hiza="end")
    s += f'<circle cx="{xm}" cy="{YZ}" r="2.2" fill="{SIY}"/>' + yazi(xm + 4, YZ - 4, "M", 9, kalin=True, hiza="start")
    s += ok(X0 - 46, Y0 + 1, X0 - 46, yl - 1, CAM, 0.7, 4) + ok(X0 - 46, yl - 1, X0 - 46, Y0 + 1, CAM, 0.7, 4)
    s += ok(X0 - 46, yl + 1, X0 - 46, YZ - 1, CAM, 0.7, 4) + ok(X0 - 46, YZ - 1, X0 - 46, yl + 1, CAM, 0.7, 4)
    s += yazi(X0 - 49, (Y0 + yl) / 2 + 3, "h₁", 9, hiza="end") + yazi(X0 - 49, (yl + YZ) / 2 + 3, "h₂", 9, hiza="end")
    s += ok(X0 + 1, YZ + 10, xl - 1, YZ + 10, CAM, 0.7, 4) + ok(xl - 1, YZ + 10, X0 + 1, YZ + 10, CAM, 0.7, 4)
    s += ok(xl + 1, YZ + 10, xm - 1, YZ + 10, CAM, 0.7, 4) + ok(xm - 1, YZ + 10, xl + 1, YZ + 10, CAM, 0.7, 4)
    s += yazi((X0 + xl) / 2, YZ + 21, "2x", 8.5, italik=True) + yazi((xl + xm) / 2, YZ + 21, "x", 8.5, italik=True)
    return svg(X0 + 180, YZ + 26, s, gen_mm)

def fig_uc_top(gen_mm=60):
    X0, Y0, YZ = 40, 30, 118
    s = f'<rect x="10" y="{Y0+5}" width="200" height="5" fill="#B9813A"/><rect x="16" y="{Y0+10}" width="4" height="{YZ-Y0-10}" fill="#8B5A2B"/><rect x="200" y="{Y0+10}" width="4" height="{YZ-Y0-10}" fill="#8B5A2B"/>'
    s += zemin(5, 250, YZ)
    for i, (ad, renk, hiz) in enumerate((("L", "#9ED3EE", None), ("K", "#F6C181", "v"), ("M", "#F7A8C8", "2v"))):
        x = X0 + 60 * i
        s += top(x, Y0, 4.5, renk) + yazi(x, Y0 - 9, ad, 9, kalin=True)
        if hiz:
            s += ok(x + 6, Y0, x + 6 + (18 if hiz == "v" else 36), Y0) + yazi(x + 8 + (18 if hiz == "v" else 36), Y0 - 4, hiz, 9, MAG, "start", True, True)
    return svg(255, YZ + 10, s, gen_mm)

def fig_uc_top_eski(gen_mm=60):
    X0, Y0, YZ = 70, 22, 110
    s = f'<rect x="20" y="{Y0+5}" width="{X0-20+4}" height="5" fill="#B9813A"/><rect x="24" y="{Y0+10}" width="4" height="{YZ-Y0-10}" fill="#8B5A2B"/><rect x="{X0-4}" y="{Y0+10}" width="4" height="{YZ-Y0-10}" fill="#8B5A2B"/>'
    s += zemin(5, 250, YZ)
    s += top(X0 - 26, Y0, 4.5, "#9ED3EE") + yazi(X0 - 26, Y0 - 9, "L", 9, kalin=True)
    s += top(X0 - 6, Y0, 4.5) + ok(X0, Y0, X0 + 22, Y0) + yazi(X0 - 6, Y0 - 9, "K", 9, kalin=True) + yazi(X0 + 25, Y0 + 3, "v", 9, MAG, "start", True, True)
    s += top(X0 + 50, Y0 - 18, 4.5, "#F7A8C8") + ok(X0 + 56, Y0 - 18, X0 + 92, Y0 - 18) + yazi(X0 + 50, Y0 - 27, "M", 9, kalin=True) + yazi(X0 + 95, Y0 - 15, "2v", 9, MAG, "start", True, True)
    s += f'<rect x="{X0+40}" y="{Y0-13}" width="20" height="4" fill="#8B5A2B"/><rect x="{X0+48}" y="{Y0-9}" width="4" height="{YZ-Y0+9}" fill="#8B5A2B"/>'
    s += yazi(X0 + 120, Y0 + 30, "(M, masanın üstündeki", 7.5, hiza="start") + yazi(X0 + 120, Y0 + 40, "rafın kenarından", 7.5, hiza="start") + yazi(X0 + 120, Y0 + 50, "fırlatılıyor.)", 7.5, hiza="start")
    return svg(255, YZ + 10, s, gen_mm)

def fig_grafikler_s7(gen_mm=78):
    """Soru 7A icin uc kucuk grafik: I dusey konum-zaman (parabol), II yatay hiz-zaman (yatay), III dusey ivme-zaman (+g)."""
    parca = []
    for no, tur, ety in (("I", "parabol", "Düşey konum"), ("II", "yatay-ust", "Yatay hız"), ("III", "ivme-arti", "Düşey ivme")):
        X0, Y0, W, H = 26, 14, 70, 60; ox = Y0 + H
        s = ok(X0, ox, X0, Y0 - 4, SIY, 0.9, 5) + ok(X0, ox, X0 + W + 6, ox, SIY, 0.9, 5)
        s += yazi(X0 + 2, Y0 - 6, ety, 7.5, hiza="start") + yazi(X0 + W + 6, ox + 10, "t", 7.5, hiza="end", italik=True)
        if tur == "parabol":
            s += yol(parabol(X0, ox, X0 + W * 0.85, Y0 + 6), MAG, 1.5, False)
        elif tur == "yatay-ust":
            s += f'<line x1="{X0}" y1="{Y0+20}" x2="{X0+W*0.85}" y2="{Y0+20}" stroke="{MAG}" stroke-width="1.5"/>'
        else:
            s += f'<line x1="{X0}" y1="{Y0+24}" x2="{X0+W*0.85}" y2="{Y0+24}" stroke="{MAG}" stroke-width="1.5"/>' + yazi(X0 - 3, Y0 + 27, "g", 7.5, hiza="end", italik=True)
        s += yazi(X0 + W / 2, ox + 20, no, 9, kalin=True)
        parca.append(f'<g transform="translate({len(parca)*110},0)">{s}</g>')
    return svg(330, 100, "".join(parca), gen_mm)

# ---------------------------------------------------------------- sayfa iskeleti
def bant_soru():
    return ('<div class="bant"><div class="b-sol">K<small>AVRAMA</small> B<small>ÖLÜMÜ</small></div>'
            '<div class="b-orta">İki Boyutta Sabit İvmeli Hareket</div>'
            '<div class="b-sag">U<small>YGULAMA</small> B<small>ÖLÜMÜ</small></div></div>')

def bant_konu():
    return ('<div class="bant"><div class="b-sol konu">K<small>ONU</small> A<small>NLATIMI</small></div>'
            '<div class="b-orta">İki Boyutta Sabit İvmeli Hareket</div>'
            '<div class="b-sag konu2">K<small>UVVET VE</small> H<small>AREKET</small></div></div>')

def alt(no, cevaplar=None):
    s = f'<div class="sayfano"><div class="p"></div><div class="c"></div><div class="n">{no}</div></div>'
    if cevaplar:
        s += '<div class="cevapserit">' + "".join(f'<span>{a}/</span> <b>{b}</b>' for a, b in cevaplar) + '</div>'
    return s

def sayfa_konu(no, icerik):
    cift = no % 2 == 0
    return f'<div class="sayfa{" cift" if cift else ""}">{bant_konu()}<div class="konu-alan">{icerik}</div>{alt(no, KONU_CEVAP.get(no))}</div>'

def sayfa_soru(no, sol, sag, cevaplar):
    cift = no % 2 == 0
    return (f'<div class="sayfa{" cift" if cift else ""}">{bant_soru()}<div class="ayirici"></div>'
            f'<div class="sutun sol">{sol}</div><div class="sutun sag">{sag}</div>{alt(no, cevaplar)}</div>')

def ornek(n, govde):
    return f'<div class="blok"><div class="etiket ornek">Örnek : <b>{n}</b></div>{govde}</div>'

def soru(n, govde):
    return f'<div class="blok"><div class="etiket soru">Soru : <b>{n}</b></div>{govde}</div>'

def cozum(satirlar, cevap):
    return ('<div class="cozum-bas">Çözüm</div>' + "".join(f'<div class="satir">{s}</div>' for s in satirlar)
            + f'<div class="cevap">Cevap: <span>{cevap}</span></div>')

def siklar_tek(s):  # kisa siklar tek satirda (cok kisaysa besi bir satirda)
    import re
    bes = all(len(re.sub(r"<[^>]+>", "", t)) <= 8 for t in s)
    return f'<div class="sik5{" bes" if bes else ""}">' + "".join(f'<span><b>{h})</b> {t}</span>' for h, t in zip("ABCDE", s)) + '</div>'

def siklar_iki(s):
    return '<div class="sik2">' + "".join(f'<span><b>{h})</b> {t}</span>' for h, t in zip("ABCDE", s)) + '</div>'

def siklar_alt(s):
    return '<div class="sikalt">' + "".join(f'<div><b>{h})</b> {t}</div>' for h, t in zip("ABCDE", s)) + '</div>'

def sik_tablo(basliklar, satirlar):
    s = '<table class="siktab"><tr><td class="harf"></td>' + "".join(f'<th>{b}</th>' for b in basliklar) + '</tr>'
    for h, r in zip("ABCDE", satirlar):
        s += f'<tr><td class="harf">{h})</td>' + "".join(f'<td>{c}</td>' for c in r) + '</tr>'
    return s + '</table>'

def onculler(liste):
    return '<div class="oncul">' + "".join(f'<div><b>{r}.</b> {t}</div>' for r, t in zip(["I", "II", "III", "IV"], liste)) + '</div>'

ONCUL5 = ["Yalnız I", "Yalnız II", "I ve II", "I ve III", "I, II ve III"]
G = '(Hava direnci önemsenmiyor. <i>g</i> = 10 m/s²)'

# ================================================================ KONU ANLATIMI
KONU_CEVAP = {1: [("Soru", "B")], 2: [("Soru", "C")], 3: [("Soru", "D")]}

konu1 = f'''
<div class="kutu"><div class="sekme">İKİ BOYUTTA SABİT İVMELİ HAREKET</div>
<div class="yan"><div class="metin">
<p>Kalecinin uzaklara gönderdiği top, parktaki fıskiyeden çıkan su ya da masanın kenarından yuvarlanıp düşen bir bilye <span class="mag">eğrisel</span> bir yol izler. Bu cisimler hem yatayda hem de düşeyde yer değiştirir; yani hareketleri <b>iki boyutludur</b>.</p>
<p>Hava direnci önemsenmezse bu cisimlere yalnızca <b>yer çekimi kuvveti</b> etki eder. Bu yüzden ivmeleri hareket boyunca her an aynıdır: büyüklüğü <i>g</i>, yönü aşağı doğrudur. İvmesi sabit olan ve iki boyutta gerçekleşen bu harekete <span class="mag">iki boyutta sabit ivmeli hareket</span> denir.</p>
</div></div></div>

<div class="kutu"><div class="sekme">HAREKETİN BİLEŞENLERİ</div>
<div class="yan"><div class="metin">
<p>Yandaki şekilde masanın kenarından <b>yatay</b> hızla çıkan K bilyesi ile aynı anda aynı yükseklikten <b>serbest bırakılan</b> L bilyesinin eşit zaman aralıklarındaki konumları gösterilmiştir.</p>
<p>Her anda iki bilye <b>aynı yükseklikte</b> bulunur ve yere <b>aynı anda</b> çarpar. K bilyesinin yatay hızı, düşeydeki hareketini etkilemez.</p>
<p>K bilyesi eşit zaman aralıklarında yatayda <b>eşit yollar</b> alır; düşeyde ise aldığı yollar giderek artar.</p>
<p>Buradan şu sonuca ulaşılır: İki boyutta sabit ivmeli hareket, birbirinden <span class="mag">bağımsız</span> iki hareketin birleşimidir.</p>
</div><div class="sekil">{fig_strobo(60)}</div></div>
<table class="bilgi">
<tr><th>Yatay bileşen</th><th>Düşey bileşen</th></tr>
<tr><td>Yatayda kuvvet yoktur, ivme sıfırdır (<i>a</i>ₓ = 0).<br><b>Sabit hızlı hareket</b> yapılır.</td>
<td>Yer çekimi kuvveti vardır, ivme <i>g</i>'dir ve aşağı yönlüdür.<br><b>Serbest düşme</b> hareketi yapılır.</td></tr>
</table></div>

<div class="kutu"><div class="sekme">İLK HIZIN BİLEŞENLERİ</div>
<div class="yan"><div class="metin">
<p>Cisim yatayla α açısı yapan <i>v</i>₀ hızıyla harekete başlarsa ilk hız, yatay ve düşey <b>bileşenlerine</b> ayrılır. Bileşenler dik üçgende trigonometri ile bulunur:</p>
<div class="formul">v₀ₓ = v₀ · cos α &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; v₀ᵧ = v₀ · sin α</div>
<p>Bileşenler biliniyorsa ilk hızın büyüklüğü Pisagor bağıntısıyla bulunur:</p>
<div class="formul">v₀² = v₀ₓ² + v₀ᵧ²</div>
<p class="kucuk">Sorularda özel açılar kullanılır: sin 37° = 0,6 ve cos 37° = 0,8; sin 53° = 0,8 ve cos 53° = 0,6; sin 30° = cos 60° = 0,5.</p>
</div><div class="sekil">{fig_bilesen(44)}</div></div></div>

<div class="kisasoru"><div class="etiket soru">Soru</div>
<div class="yan"><div class="metin">
<p>Bir cisim yerden, yatayla 53° açı yapan 50 m/s büyüklüğündeki hızla harekete başlıyor.</p>
<p class="kok">Buna göre cismin ilk hızının yatay bileşeni <i>v</i>₀ₓ ve düşey bileşeni <i>v</i>₀ᵧ kaç m/s'dir? <span class="nk">(sin 53° = 0,8, cos 53° = 0,6)</span></p>
</div><div class="sekil">{sik_tablo(["<i>v</i>₀ₓ (m/s)", "<i>v</i>₀ᵧ (m/s)"], [["40", "30"], ["30", "40"], ["50", "40"], ["40", "50"], ["30", "50"]])}</div></div></div>
'''

konu2 = f'''
<div class="kutu"><div class="sekme">YERDEN YÜKSEK BİR NOKTADAN YATAY HIZLA BAŞLAYAN HAREKET</div>
<div class="yan"><div class="metin">
<p>Yerden <i>h</i> yükseklikteki bir noktadan yatay <i>v</i> hızıyla harekete başlayan cismin ilk hızının düşey bileşeni sıfırdır.</p>
<p><b>Yatayda:</b> Cisim sabit <i>v</i> hızıyla ilerler. Eşit zaman aralıklarında yatayda eşit yollar (<i>x</i>, <i>x</i>, <i>x</i>) alır.</p>
<p><b>Düşeyde:</b> Cisim ilk hızı sıfır olan serbest düşme yapar. Eşit zaman aralıklarında düşeyde aldığı yollar <b>h, 3h, 5h</b> biçiminde artar.</p>
<p>Cismin havada kalma süresi yalnızca <b>yüksekliğe</b> bağlıdır; yatay hıza bağlı değildir.</p>
</div><div class="sekil">{fig_yatay_genel(74)}</div></div>
<table class="bilgi formuller">
<tr><th>Yatayda (sabit hızlı hareket)</th><th>Düşeyde (serbest düşme)</th></tr>
<tr><td><i>x</i> = <i>v</i> · <i>t</i></td><td><i>h</i> = {kesir(1,2)} · <i>g</i> · <i>t</i>² &nbsp;&nbsp;&nbsp; <i>v</i>ᵧ = <i>g</i> · <i>t</i></td></tr>
</table>
<p class="ust-bosluk">Cismin herhangi bir andaki hızı, hızın yatay ve düşey bileşenlerinin bileşkesidir: &nbsp;<b><i>v</i>ₜ² = <i>v</i>² + <i>v</i>ᵧ²</b></p>
</div>

<div class="kutu"><div class="sekme">YERDEN AÇIYLA BAŞLAYAN HAREKET</div>
<div class="yan"><div class="metin">
<p>Yerden, yatayla α açısı yapan <i>v</i>₀ hızıyla harekete başlayan cisim için:</p>
<p><b>Yatayda:</b> Hızın yatay bileşeni <i>v</i>₀ₓ hareket boyunca <b>değişmez</b>.</p>
<p><b>Düşeyde:</b> Cisim yukarı doğru yavaşlar, en yüksek noktada (<b>T</b>, tepe noktası) hızın düşey bileşeni <b>sıfır</b> olur. Sonra aşağı doğru hızlanır. Yere, harekete başladığı hızın düşey bileşeniyle aynı büyüklükte bir düşey hızla çarpar.</p>
<p>Çıkış ve iniş süreleri eşittir (<i>t</i>ç = <i>t</i>i).</p>
</div><div class="sekil">{fig_acili_genel(96)}</div></div>
<table class="bilgi formuller">
<tr><th>Yatayda (sabit hızlı hareket)</th><th>Düşeyde (serbest düşme)</th></tr>
<tr><td><i>v</i>₀ₓ = <i>v</i>₀ · cos α<br><i>x</i><sub>menzil</sub> = <i>v</i>₀ₓ · <i>t</i><sub>uçuş</sub></td>
<td><i>v</i>₀ᵧ = <i>v</i>₀ · sin α &nbsp;&nbsp;&nbsp; <i>v</i>ᵧ = <i>v</i>₀ᵧ – <i>g</i> · <i>t</i><br>
<i>t</i>ç = {kesir("<i>v</i>₀ᵧ","<i>g</i>")} &nbsp;&nbsp;&nbsp; <i>t</i><sub>uçuş</sub> = 2 · <i>t</i>ç &nbsp;&nbsp;&nbsp; <i>h</i><sub>max</sub> = {kesir("<i>v</i>₀ᵧ²","2 · <i>g</i>")}</td></tr>
</table></div>

<div class="kisasoru"><div class="etiket soru">Soru</div>
<p>Yerden yüksek bir noktadan yatay hızla harekete başlayan bir cisim, hareketinin ilk 1 saniyesinde düşeyde 5 m yol alıyor. Cisim 3 saniyeden daha uzun süre havada kalıyor. Hava direnci önemsenmiyor.</p>
<p class="kok">Buna göre cisim hareketinin 3. saniyesinde düşeyde kaç metre yol alır?</p>
{siklar_tek(["5", "15", "25", "35", "45"])}
</div>
'''

konu3 = f'''
<div class="kutu"><div class="sekme">HAREKETİN GRAFİKLERİ (YERDEN AÇIYLA BAŞLAYAN HAREKET)</div>
<p class="ic">Hareketin iki bileşeni ayrı ayrı grafiklerle incelenir. Yukarı yön ve harekete başlanan nokta pozitif kabul edilmiştir.</p>
<div class="grafsatir"><div class="grafbas">Düşeyde</div>
<div>{grafik("parabol", 52, et_y="Konum (m)")}</div><div>{grafik("dogru-azalan", 52, et_y="Hız (m/s)")}</div><div>{grafik("yatay-alt", 52, et_y="İvme (m/s²)")}</div></div>
<div class="grafsatir"><div class="grafbas">Yatayda</div>
<div>{grafik("dogru-artan", 52, et_y="Konum (m)")}</div><div>{grafik("yatay-ust", 52, et_y="Hız (m/s)")}</div><div>{grafik("yatay-sifir", 52, et_y="İvme (m/s²)")}</div></div>
<p class="ic">Düşey hız-zaman grafiğinde 0 - <i>t</i>ç arasında kalan alan <i>h</i><sub>max</sub>'ı, yatay hız-zaman grafiğinin altındaki alan menzili (<i>x</i>) verir.</p>
</div>

<div class="aktifnot"><div class="an-etiket">AKTİF NOT</div>
<p>• Hareket boyunca ivme her an <i>g</i>'dir ve aşağı yönlüdür; <b>tepe noktasında da ivme sıfır değildir.</b></p>
<p>• Tepe noktasında hız sıfır değildir; yalnızca hızın düşey bileşeni sıfırdır. Bu noktada cismin hızı <i>v</i>₀ₓ'tir.</p>
<div class="yan"><div class="metin"><p>• Aynı büyüklükteki hızlarla yerden harekete başlayan cisimlerin açıları toplamı 90° ise (ör. 37° ve 53°) menzilleri eşittir. Açı 45° iken menzil en büyük olur.</p></div>
<div class="sekil">{fig_iki_yorunge(52)}</div></div>
</div>

<div class="kisasoru"><div class="etiket soru">Soru</div>
<div class="yan"><div class="metin">
<p>Bir futbolcu yerdeki topa vurarak topu yerden açıyla harekete geçiriyor. Top, şekildeki yolu izleyerek yere düşüyor. Hava direnci önemsenmiyor.</p>
<p class="kok">Topun T tepe noktasındaki hareketiyle ilgili,</p>
{onculler(["Hızının düşey bileşeni sıfırdır.", "İvmesi sıfırdır.", "Hızı, harekete başladığı andaki hızının yatay bileşenine eşittir."])}
<p class="kok">yargılarından hangileri doğrudur?</p>
{siklar_tek(ONCUL5)}
</div><div class="sekil">{fig_acili("v₀", 37, gen_mm=52, L=200, H=60, tepe_et="T")}</div></div></div>
'''

# ================================================================ SORU SAYFALARI
s4_sol = ornek(1, f'''
<p>Yerden aynı yükseklikteki K ve L bilyelerinden K yatay <i>v</i> hızıyla harekete başlarken L aynı anda serbest bırakılıyor. Bilyelerin eşit zaman aralıklarındaki konumları şekildeki gibidir. Hava direnci önemsenmiyor.</p>
<div class="sekil-orta">{fig_strobo(44)}</div>
<p class="kok">Buna göre K ve L bilyelerinin hareketiyle ilgili ne söylenebilir?</p>
{cozum(["Her anda iki bilye aynı yüksekliktedir; K'nin yatay hızı düşey hareketini değiştirmez. Bu yüzden bilyeler yere aynı anda çarpar.",
        "K eşit sürelerde yatayda eşit yollar alır: yatayda sabit hızlı hareket yapar.",
        "Düşeyde iki bilye de serbest düşme yapar."],
       "Bilyeler yere aynı anda çarpar; K yatayda sabit hızlı, düşeyde serbest düşme hareketi yapar.")}
''')
s4_sag = soru("1A", f'''
<p>Bir masanın üzerinde yerden aynı yükseklikte bulunan K, L ve M bilyelerinden K yatay <i>v</i>, M yatay 2<i>v</i> hızıyla harekete başlarken L aynı anda masanın kenarından serbest bırakılıyor. Hava direnci önemsenmiyor.</p>
<div class="sekil-orta">{fig_uc_top(46)}</div>
<p class="kok">Bilyelerin yere düşme süreleri <i>t</i><sub>K</sub>, <i>t</i><sub>L</sub> ve <i>t</i><sub>M</sub> arasındaki ilişki nedir?</p>
{siklar_iki(["<i>t</i><sub>L</sub> > <i>t</i><sub>K</sub> > <i>t</i><sub>M</sub>", "<i>t</i><sub>M</sub> > <i>t</i><sub>K</sub> > <i>t</i><sub>L</sub>", "<i>t</i><sub>K</sub> = <i>t</i><sub>L</sub> = <i>t</i><sub>M</sub>", "<i>t</i><sub>K</sub> = <i>t</i><sub>M</sub> > <i>t</i><sub>L</sub>", "<i>t</i><sub>L</sub> > <i>t</i><sub>K</sub> = <i>t</i><sub>M</sub>"])}
''') + soru("1B", f'''
<p>Masanın kenarından K bilyesi yatay hızla harekete başlarken aynı yükseklikteki L bilyesi aynı anda serbest bırakılıyor. Hava direnci önemsenmiyor.</p>
<p class="kok">Bilyeler için,</p>
{onculler(["Yere aynı anda çarparlar.", "Yere çarpma anındaki hızlarının büyüklükleri eşittir.", "Yere çarpma anında hızlarının düşey bileşenleri eşittir."])}
<p class="kok">yargılarından hangileri doğrudur?</p>
{siklar_tek(ONCUL5)}
''') + soru(2, f'''
<p>Yerden 20 m yükseklikten yatay doğrultuda harekete başlayan bir cisim, şekildeki yolu izleyerek yere 25 m/s büyüklüğündeki hızla çarpıyor.</p>
<div class="sekil-orta">{yatay_fig("h = 20 m", "v", "x", 40, 70, 90, "25 m/s")}</div>
<p class="kok">Buna göre,</p>
{onculler(["Cisim 2 saniyede yere çarpar.", "Cismin ilk hızının büyüklüğü 15 m/s'dir.", "Cismin yatayda aldığı yol <i>x</i> = 30 m'dir."])}
<p class="kok">yargılarından hangileri doğrudur? <span class="nk">(<i>g</i> = 10 m/s²)</span></p>
{siklar_tek(ONCUL5)}
<div class="cozumbosluk"></div>
''')

s4_sol += ornek(2, f'''
<p>Hava direncinin önemsenmediği bir ortamda bir cisim, yerden 80 m yükseklikten yatay doğrultuda 30 m/s hızla şekildeki gibi harekete başlıyor.</p>
<div class="sekil-orta">{yatay_fig("h = 80 m", "30 m/s", "x", 40, 90, 100)}</div>
<p class="kok">Buna göre,</p>
{onculler(["Cisim 4 saniyede yere çarpar.", "Cisim yere 50 m/s büyüklüğündeki hızla çarpar.", "Cisim yatayda 160 m yol alır."])}
<p class="kok">yargılarından hangileri doğrudur? <span class="nk">(<i>g</i> = 10 m/s²)</span></p>
{siklar_tek(ONCUL5)}
{cozum(["Düşeyde: <i>h</i> = ½ · <i>g</i> · <i>t</i>²", "80 = 5 · <i>t</i>²  ise  <i>t</i> = 4 s  (I. yargı doğrudur.)",
        "<i>v</i>ᵧ = <i>g</i> · <i>t</i> = 10 · 4 = 40 m/s", "<i>v</i>² = 30² + 40² = 2500  ise  <i>v</i> = 50 m/s  (II. yargı doğrudur.)",
        "Yatayda: <i>x</i> = <i>v</i> · <i>t</i> = 30 · 4 = 120 m  (III. yargı yanlıştır.)"], "C")}
''')

s5_sol = ornek(3, f'''
<p>Hava direncinin önemsenmediği bir ortamda yatay 10 m/s hızla harekete başlayan cisim, şekildeki yolu izleyerek yatayda 40 m yol aldıktan sonra yere düşüyor.</p>
<div class="sekil-orta">{yatay_fig("h", "10 m/s", "x = 40 m", 40, 90, 100)}</div>
<p class="kok">Buna göre cismin harekete başladığı noktanın yerden yüksekliği <i>h</i> kaç metredir? <span class="nk">(<i>g</i> = 10 m/s²)</span></p>
{siklar_tek(["20", "45", "60", "80", "125"])}
{cozum(["Önce yatay bileşenden süreyi bulalım:", "<i>x</i> = <i>v</i> · <i>t</i>", "40 = 10 · <i>t</i>  ise  <i>t</i> = 4 s",
        "Düşeyde serbest düşme yapar:", "<i>h</i> = ½ · <i>g</i> · <i>t</i>²", "<i>h</i> = ½ · 10 · 4² = 80 m"], "D")}
''') + ornek(4, f'''
<p>Sürtünmesiz ortamda K noktasından yatay hızla harekete başlayan cisim, şekildeki yolu izleyerek L noktasından geçip M noktasında yere çarpıyor.</p>
<div class="sekil-orta">{fig_klm(44)}</div>
<p class="kok">Buna göre {kesir("<i>h</i>₁","<i>h</i>₂")} oranı kaçtır?</p>
{siklar_tek([kesir(3,2), kesir(5,4), kesir(2,3), kesir(4,5), "1"])}
{cozum(["Yatay hız sabit olduğu için K-L arası 2<i>t</i>, L-M arası <i>t</i> sürede alınır.",
        "Düşeyde eşit sürelerde alınan yollar <i>h</i>, 3<i>h</i>, 5<i>h</i> olur.",
        "İlk 2<i>t</i> sürede: <i>h</i>₁ = <i>h</i> + 3<i>h</i> = 4<i>h</i>", "Son <i>t</i> sürede: <i>h</i>₂ = 5<i>h</i>",
        f"Oran: {kesir('<i>h</i>₁','<i>h</i>₂')} = {kesir(4,5)}"], "D")}
''')
s5_sag = soru("3A", f'''
<p>Hava direncinin önemsenmediği bir ortamda yerden 45 m yükseklikten yatay <i>v</i> hızıyla harekete başlayan cisim, şekildeki yolu izleyerek yatayda 60 m yol alıp yere çarpıyor.</p>
<div class="sekil-orta">{yatay_fig("h = 45 m", "v", "x = 60 m", 40, 75, 105)}</div>
<p class="kok">Buna göre cismin ilk hızının büyüklüğü <i>v</i> kaç m/s'dir? <span class="nk">(<i>g</i> = 10 m/s²)</span></p>
{siklar_tek(["15", "20", "25", "30", "35"])}
<div class="cozumbosluk"></div>
''') + soru("3B", f'''
<p>Hava direncinin önemsenmediği bir ortamda <i>h</i> yüksekliğinden yatay <i>v</i> hızıyla harekete başlayan cisim, yatayda <i>x</i> yol alarak yere düşüyor.</p>
<p class="kok">Aynı cisim 4<i>h</i> yüksekliğinden yatay <i>v</i> hızıyla harekete başlarsa yatayda kaç <i>x</i> yol alır?</p>
{siklar_tek([kesir("<i>x</i>", 2), "<i>x</i>", kesir("3<i>x</i>", 2), "2<i>x</i>", "4<i>x</i>"])}
''') + soru(4, f'''
<p>Sürtünmesiz ortamda aynı düşey doğru üzerindeki iki noktadan <i>v</i> ve 3<i>v</i> büyüklüğündeki yatay hızlarla harekete başlayan cisimler şekildeki yolları izleyerek yerde aynı noktaya çarpıyor.</p>
<div class="sekil-orta">{fig_iki_cisim(44)}</div>
<p class="kok">Buna göre {kesir("<i>h</i>₁","<i>h</i>₂")} oranı kaçtır?</p>
{siklar_tek(["1", "2", "4", "6", "8"])}
<div class="cozumbosluk"></div>
''')

s6_sol = ornek(5, f'''
<p>Hava direncinin önemsenmediği bir ortamda bir cisim yerden, yatayla 37° açı yapan 50 m/s büyüklüğündeki hızla şekildeki gibi harekete başlıyor.</p>
<div class="sekil-orta">{fig_acili("50 m/s", 37, "h<tspan font-size='6' dy='2'>max</tspan>", "x", 40, L=200, H=55)}</div>
<p class="kok">Buna göre cismin çıkabileceği en büyük yükseklik <i>h</i><sub>max</sub> ve yatayda aldığı yol <i>x</i> kaç metredir?<br><span class="nk">(<i>g</i> = 10 m/s², sin 37° = 0,6, cos 37° = 0,8)</span></p>
{cozum(["Önce ilk hızı bileşenlerine ayıralım:", "<i>v</i>₀ᵧ = 50 · sin 37° = 50 · 0,6 = 30 m/s", "<i>v</i>₀ₓ = 50 · cos 37° = 50 · 0,8 = 40 m/s",
        "Çıkış süresi: <i>t</i>ç = <i>v</i>₀ᵧ / <i>g</i> = 30 / 10 = 3 s", "Uçuş süresi: <i>t</i><sub>uçuş</sub> = 2 · 3 = 6 s",
        "<i>h</i><sub>max</sub> = <i>v</i>₀ᵧ² / (2 · <i>g</i>) = 900 / 20 = 45 m", "<i>x</i> = <i>v</i>₀ₓ · <i>t</i><sub>uçuş</sub> = 40 · 6 = 240 m"],
       "<i>h</i><sub>max</sub> = 45 m, <i>x</i> = 240 m")}
''') + ornek(6, f'''
<p>Hava direncinin önemsenmediği bir ortamda K, L ve M cisimleri A noktasından eşit bölmeli düzlemde gösterilen hızlarla harekete başlıyor.</p>
<div class="sekil-orta">{fig_kareli([("K", 1, 2, MAG), ("L", 2, 2, YES), ("M", 2, 1, "#1678BE")], 3, 2, 28)}</div>
<p class="kok">Buna göre,</p>
{onculler(["K ve L'nin havada kalma süreleri eşittir.", "K ve M'nin yatayda aldıkları yollar eşittir.", "L'nin yatayda aldığı yol, K'nin aldığı yolun iki katıdır.", "L'nin çıkabileceği en büyük yükseklik, M'ninkinin 4 katıdır."])}
<p class="kok">yargılarından hangileri doğrudur?</p>
{siklar_iki(["I ve II", "I ve III", "II ve IV", "I, II ve III", "I, II, III ve IV"])}
{cozum(["Hız bileşenleri (yatay, düşey): K (1, 2), L (2, 2), M (2, 1)", "Uçuş süresi düşey bileşenle orantılıdır: <i>t</i><sub>K</sub> = <i>t</i><sub>L</sub> = 2<i>t</i>, <i>t</i><sub>M</sub> = <i>t</i>  (I. doğru)",
        "Yatay yol: <i>x</i><sub>K</sub> = 1 · 2<i>t</i> = 2<i>t</i>, <i>x</i><sub>L</sub> = 2 · 2<i>t</i> = 4<i>t</i>, <i>x</i><sub>M</sub> = 2 · <i>t</i> = 2<i>t</i>  (II. ve III. doğru)",
        "En büyük yükseklik düşey bileşenin karesiyle orantılıdır: <i>h</i><sub>L</sub> : <i>h</i><sub>M</sub> = 2² : 1² = 4  (IV. doğru)"], "E")}
''')
s6_sag = soru("5A", f'''
<p>Hava direncinin önemsenmediği bir ortamda bir cisim yerden, yatayla 53° açı yapan 50 m/s büyüklüğündeki hızla harekete başlıyor.</p>
<div class="sekil-orta">{fig_acili("50 m/s", 53, "h<tspan font-size='6' dy='2'>max</tspan>", "x", 40, L=200, H=95)}</div>
<p class="kok">Buna göre <i>h</i><sub>max</sub> ve <i>x</i> aşağıdakilerin hangisinde doğru verilmiştir?<br><span class="nk">(<i>g</i> = 10 m/s², sin 53° = 0,8, cos 53° = 0,6)</span></p>
{sik_tablo(["<i>h</i><sub>max</sub> (m)", "<i>x</i> (m)"], [["45", "240"], ["80", "240"], ["80", "320"], ["45", "320"], ["125", "240"]])}
<div class="cozumbosluk kisa"></div>
''') + soru("5B", f'''
<p>Yerden yatayla 45° açı yapan hızla harekete başlayan cismin T tepe noktasındaki hızının büyüklüğü 20 m/s'dir. Hava direnci önemsenmiyor.</p>
<p class="kok">Buna göre cismin <i>h</i><sub>max</sub> yüksekliği ve yatayda aldığı yol <i>x</i> kaç metredir? <span class="nk">(<i>g</i> = 10 m/s²)</span></p>
{sik_tablo(["<i>h</i><sub>max</sub> (m)", "<i>x</i> (m)"], [["20", "40"], ["40", "80"], ["20", "80"], ["40", "40"], ["80", "80"]])}
<div class="cozumbosluk kisa"></div>
''') + soru(6, f'''
<p>Sürtünmelerin önemsenmediği ortamda K, L ve M cisimleri yerden şekildeki hızlarla harekete başlıyor. K'nin hızı düşey doğrultuda 40 m/s, L'nin hızı yatayla 53° açı yapan 50 m/s, M'nin hızı yatayla 30° açı yapan 80 m/s'dir.</p>
<p class="kok">Cisimlerin havada kalma süreleri <i>t</i><sub>K</sub>, <i>t</i><sub>L</sub> ve <i>t</i><sub>M</sub> arasındaki ilişki nedir?<br><span class="nk">(sin 53° = 0,8, sin 30° = 0,5)</span></p>
{siklar_iki(["<i>t</i><sub>K</sub> = <i>t</i><sub>L</sub> = <i>t</i><sub>M</sub>", "<i>t</i><sub>K</sub> > <i>t</i><sub>L</sub> > <i>t</i><sub>M</sub>", "<i>t</i><sub>M</sub> > <i>t</i><sub>L</sub> > <i>t</i><sub>K</sub>", "<i>t</i><sub>K</sub> > <i>t</i><sub>L</sub> = <i>t</i><sub>M</sub>", "<i>t</i><sub>M</sub> > <i>t</i><sub>K</sub> = <i>t</i><sub>L</sub>"])}
''')

s7_sol = ornek(7, f'''
<p>Yerden açıyla harekete başlayan bir cismin hızının düşey ve yatay bileşenlerinin zamana bağlı grafikleri aşağıda verilmiştir. Hava direnci önemsenmiyor.</p>
<div class="graf2">{fig_dusey_hiz(20, 4, gen_mm=36)}{fig_yatay_hiz(15, 4, gen_mm=36)}</div>
<p class="kok">Buna göre cismin<br>a) çıkabileceği en büyük yükseklik,<br>b) yatayda aldığı yol,<br>c) harekete başladığı andaki hızının büyüklüğü<br>nedir?</p>
{cozum(["a) Düşey hız 2. saniyede sıfır oluyor; cisim tepe noktasına 2 s'de çıkar.", "<i>h</i><sub>max</sub> = (0 - 2 s arasındaki alan) = ½ · 2 · 20 = 20 m",
        "b) Cisim 4 s havada kalır. Yatay hız sabit 15 m/s'dir.", "<i>x</i> = 15 · 4 = 60 m",
        "c) <i>v</i>₀² = 15² + 20² = 625", "<i>v</i>₀ = 25 m/s"], "a) 20 m  b) 60 m  c) 25 m/s")}
''')
s7_sol += ornek(8, f'''
<p>Sürtünmesiz ortamda yatay 20 m/s hızla K noktasından harekete başlayan cisim, şekildeki yolu izleyerek eğik düzlemin L noktasına çarpıyor.</p>
<div class="sekil-orta">{fig_egik("20 m/s", 44, olcu=False)}</div>
<p class="kok">Buna göre cisim kaç saniyede L noktasına çarpar? <span class="nk">(<i>g</i> = 10 m/s², sin 37° = 0,6, cos 37° = 0,8)</span></p>
{cozum(["Eğik düzlemde 37° açısının karşısındaki dik kenar 3<i>k</i>, komşu dik kenar 4<i>k</i> olur.",
        "Cisim K'den L'ye gelene kadar düşeyde 3<i>k</i>, yatayda 4<i>k</i> yol alır.",
        "Yatayda: 4<i>k</i> = 20 · <i>t</i>  ise  <i>k</i> = 5 · <i>t</i>", "Düşeyde: 3<i>k</i> = ½ · 10 · <i>t</i>² = 5 · <i>t</i>²",
        "3 · 5 · <i>t</i> = 5 · <i>t</i>²  ise  <i>t</i> = 3 s"], "3 s")}
''')
s7_sag = soru("7A", f'''
<p>Yerden açıyla harekete başlayan ve yalnızca yer çekimi etkisinde hareket eden bir cisim için yukarı yön pozitif kabul edilerek üç grafik çiziliyor.</p>
<div class="sekil-orta">{fig_grafikler_s7(68)}</div>
<p class="kok">Bu grafiklerden hangileri cismin hareketine ait olabilir?</p>
{siklar_tek(ONCUL5)}
''') + soru("7B", f'''
<p>Yerden açıyla harekete başlayan bir cismin hızının düşey bileşeninin zamana bağlı grafiği şekildeki gibidir. Cismin hızının yatay bileşeni 20 m/s'dir. Hava direnci önemsenmiyor.</p>
<div class="sekil-orta">{fig_dusey_hiz(25, 5, gen_mm=38)}</div>
<p class="kok">Buna göre cismin yatayda aldığı yol kaç metredir?</p>
{siklar_tek(["25", "50", "75", "100", "125"])}
<div class="cozumbosluk orta"></div>
''') + soru(8, f'''
<p>Sürtünmesiz ortamda K noktasından yatay 30 m/s hızla harekete başlayan cisim, şekildeki yolu izleyerek eğik düzlemin L noktasına 50 m/s büyüklüğündeki hızla çarpıyor.</p>
<div class="sekil-orta">{fig_egik("30 m/s", 34, carpma="50 m/s")}</div>
<p class="kok">Buna göre <i>h</i> ve <i>x</i> aşağıdakilerden hangisinde doğru verilmiştir? <span class="nk">(<i>g</i> = 10 m/s²)</span></p>
{sik_tablo(["<i>h</i> (m)", "<i>x</i> (m)"], [["45", "45"], ["45", "90"], ["80", "120"], ["80", "90"], ["45", "120"]])}
''')

# ---------------- baglam 1: bilim kulubu (kolay, hesap az)
tablo8 = ('<table class="veri"><tr><th>Zaman (s)</th><th>0</th><th>0,1</th><th>0,2</th><th>0,3</th></tr>'
          '<tr><td>Yatayda aldığı yol (cm)</td><td>0</td><td>20</td><td>40</td><td>60</td></tr>'
          '<tr><td>Düşeyde aldığı yol (cm)</td><td>0</td><td>5</td><td>20</td><td>45</td></tr></table>')
s8_sol = ornek(9, f'''
<div class="baslik">Bilim kulübünde fotoğraf deneyi</div>
<p>Bilim kulübündeki öğrenciler, masanın kenarından yatay hızla çıkan bir topun hareketini incelemek istiyor. Topun hareketini, saniyede 10 fotoğraf çeken bir kamerayla kaydediyorlar. Fotoğraflardan topun harekete başladığı noktaya göre yatayda ve düşeyde aldığı yolları ölçüp tabloya yazıyorlar.</p>
<div class="sekil-orta">{fig_strobo(56, etiket=False)}</div>
{tablo8}
<p class="kok">Tabloya göre topun hareketinin yatay ve düşey bileşenleri hangi tür harekettir?</p>
{cozum(["Yatayda: Her 0,1 s'de alınan yol 20 cm'dir; eşit sürelerde eşit yollar alınıyor.", "Yatay bileşen sabit hızlı harekettir: <i>v</i> = 20 cm / 0,1 s = 2 m/s",
        "Düşeyde: Her 0,1 s'de alınan yollar 5 cm, 15 cm, 25 cm'dir.", "Yollar her aralıkta 10 cm artıyor; hız düzgün artıyor.",
        "Düşey bileşen sabit ivmeli harekettir (ilk hızı sıfır olan serbest düşme)."], "Yatayda sabit hızlı, düşeyde sabit ivmeli hareket")}
''') + '<div class="aktifnot"><div class="an-etiket">AKTİF NOT</div><p>• Hızın yatay bileşeni sabit olduğu için eşit sürelerde yatayda alınan yollar eşittir.</p><p>• İlk hızın düşey bileşeni sıfırsa eşit sürelerde düşeyde alınan yollar <b>1 : 3 : 5 : 7</b> oranında artar.</p></div>'
s8_sag = soru("9A", f'''
<p>Öğrenciler tablodaki verilerden yola çıkarak bir genelleme yapmak istiyor.</p>
<p class="kok">Bu verilerle yapılabilecek en uygun genelleme aşağıdakilerden hangisidir?</p>
{siklar_alt(["Yatay hızla harekete başlayan cisimlerin hızı hareket boyunca değişmez.",
             "Cisim yalnızca yer çekimi etkisindeyken hareketin yatay bileşeni sabit hızlı, düşey bileşeni sabit ivmelidir.",
             "Cismin yatayda aldığı yol, düşeyde aldığı yoldan her zaman büyüktür.",
             "Topun ivmesi hareket boyunca artar.",
             "Topun yatay hızı arttıkça düşeyde aldığı yollar da artar."])}
''') + soru("9B", f'''
<p>Top 0,4 s'de henüz yere çarpmamıştır.</p>
<p class="kok">Hareket aynı şekilde sürdüğüne göre top 0,4 s'de yatayda ve düşeyde kaçar cm yol almış olur?</p>
{sik_tablo(["Yatayda (cm)", "Düşeyde (cm)"], [["80", "60"], ["80", "80"], ["60", "80"], ["100", "80"], ["80", "65"]])}
<div class="cozumbosluk kisa"></div>
''') + soru("9C", f'''
<p>Öğrenciler deneyi aynı masada tekrarlıyor; bu kez top masanın kenarından iki katı büyüklükte yatay hızla çıkıyor.</p>
<p class="kok">Topun yere düşme süresi ve yere düştüğü noktanın masaya uzaklığı ilk denemeye göre nasıl değişir?</p>
{sik_tablo(["Yere düşme süresi", "Masaya uzaklık"], [["Değişmez", "İki katına çıkar"], ["İki katına çıkar", "İki katına çıkar"], ["Değişmez", "Değişmez"], ["Yarıya iner", "Değişmez"], ["İki katına çıkar", "Dört katına çıkar"]])}
''')

# ---------------- baglam 2: yangin sondurme helikopteri
s9_sol = ornek(10, f'''
<div class="baslik">Orman yangınına havadan müdahale</div>
<p>Orman yangınlarında yangın söndürme helikopterleri, altlarına asılı su kovalarındaki suyu yangının üzerine bırakır. Pilot suyu hedefin tam üzerinde değil, hedefe varmadan önce bırakmalıdır.</p>
<p>Bir helikopter yerden 45 m yükseklikte, yatay doğrultuda 40 m/s sabit hızla uçuyor. Hava direnci önemsenmiyor ve kovadan bırakılan su tek bir cisim gibi hareket ediyor.</p>
<div class="sekil-orta">{fig_helikopter(78)}</div>
<p class="kok">Pilot, suyun hedefe düşmesi için suyu hedefe yatayda kaç metre kala bırakmalıdır? <span class="nk">(<i>g</i> = 10 m/s²)</span></p>
{cozum(["Su, kovadan bırakıldığı anda helikopterin hızına sahiptir: yatayda 40 m/s.", "Düşeyde ilk hızı sıfır olan serbest düşme yapar:",
        "<i>h</i> = ½ · <i>g</i> · <i>t</i>²", "45 = 5 · <i>t</i>²  ise  <i>t</i> = 3 s", "Bu sürede su yatayda <i>x</i> = 40 · 3 = 120 m yol alır."], "120 m")}
''') + '<div class="aktifnot"><div class="an-etiket">AKTİF NOT</div><p>• Hareket eden bir araçtan bırakılan cisim, bırakıldığı anda aracın hızına sahiptir.</p><p>• Yerden yüksek bir noktadan yatay hızla harekete başlayan cismin havada kalma süresi yalnızca yüksekliğe bağlıdır; yatay hız, cismin yatayda aldığı yolu değiştirir.</p></div>'
s9_sag = soru("10A", f'''
<p>Rüzgâr nedeniyle pilot, aynı yatay hızla bu kez yerden 80 m yükseklikte uçuyor.</p>
<p class="kok">Suyun hedefe düşmesi için pilot suyu hedefe yatayda kaç metre kala bırakmalıdır? <span class="nk">(<i>g</i> = 10 m/s²)</span></p>
{siklar_tek(["100", "120", "140", "160", "180"])}
<div class="cozumbosluk"></div>
''') + soru("10B", f'''
<p>Helikopter yerden 45 m yükseklikte, yatay 40 m/s hızla uçarken suyu bırakıyor.</p>
<p class="kok">Su yere kaç m/s büyüklüğündeki hızla çarpar? <span class="nk">(<i>g</i> = 10 m/s²)</span></p>
{siklar_tek(["40", "50", "60", "70", "80"])}
<div class="cozumbosluk"></div>
''') + soru("10C", f'''
<p>Pilot, yangının dumanı nedeniyle aynı yükseklikte kalarak helikopterin hızını yarıya düşürüyor.</p>
<p class="kok">Suyun havada kalma süresi ve suyun bırakılması gereken noktanın hedefe yatay uzaklığı ilk duruma göre nasıl değişir?</p>
{sik_tablo(["Havada kalma süresi", "Hedefe yatay uzaklık"], [["Yarıya iner", "Yarıya iner"], ["Değişmez", "Değişmez"], ["Değişmez", "Yarıya iner"], ["İki katına çıkar", "Değişmez"], ["Yarıya iner", "Değişmez"]])}
''')

SAYFALAR = [
    sayfa_konu(1, konu1), sayfa_konu(2, konu2), sayfa_konu(3, konu3),
    sayfa_soru(4, s4_sol, s4_sag, [("Soru 1A", "C"), ("Soru 1B", "D"), ("Soru 2", "E")]),
    sayfa_soru(5, s5_sol, s5_sag, [("Soru 3A", "B"), ("Soru 3B", "D"), ("Soru 4", "E")]),
    sayfa_soru(6, s6_sol, s6_sag, [("Soru 5A", "B"), ("Soru 5B", "C"), ("Soru 6", "A")]),
    sayfa_soru(7, s7_sol, s7_sag, [("Soru 7A", "C"), ("Soru 7B", "D"), ("Soru 8", "C")]),
    sayfa_soru(8, s8_sol, s8_sag, [("Soru 9A", "B"), ("Soru 9B", "B"), ("Soru 9C", "A")]),
    sayfa_soru(9, s9_sol, s9_sag, [("Soru 10A", "D"), ("Soru 10B", "B"), ("Soru 10C", "C")]),
]

CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "stil_v1.css"), encoding="utf-8").read()
html = f'<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8"><title>İki Boyutta Sabit İvmeli Hareket</title><style>{CSS}</style></head><body>{"".join(SAYFALAR)}</body></html>'
# Alt indis karakterlerini (ₓ ᵧ ₀ ₁ ₂) gercek alt indise cevir: Liberation'da yoklar, Type3 yazi tipine dusuyorlar.
import re as _re
ALT = {"ₓ": "x", "ᵧ": "y", "₀": "0", "₁": "1", "₂": "2", "ₜ": "t"}
def _svg_alt(m):
    t = m.group(0)
    for k, v in ALT.items():
        t = t.replace(k, f'<tspan baseline-shift="sub" font-size="70%">{v}</tspan>')
    return t
html = _re.sub(r"<svg.*?</svg>", _svg_alt, html, flags=_re.S)
for k, v in ALT.items():
    html = html.replace(k, f"<sub>{v}</sub>")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "iki_boyutta_v1.html"), "w", encoding="utf-8").write(html)
print("HTML yazildi:", len(SAYFALAR), "sayfa")
