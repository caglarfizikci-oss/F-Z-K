# Eğik Atış Animasyonu - Blender ile
# Kullanım (arka planda):  blender -b -P egik_atis.py
# Sadece tek bir kareyi denemek için:  TEK_KARE=60 blender -b -P egik_atis.py
#
# Değerler: v0 = 15 m/s, açı = 53°, g = 10 m/s²
#   vx = v0·cos53° = 15·0,6 = 9 m/s   (sabit)
#   vy = v0·sin53° = 15·0,8 = 12 m/s  (her saniye 10 m/s azalır)
#   Uçuş süresi = 2·vy/g = 2,4 s | Hmax = vy²/2g = 7,2 m | Menzil = vx·T = 21,6 m

import bpy, math, os
from mathutils import Vector

# ---------------- Fizik değerleri ----------------
V0, ACI, G = 15.0, 53.0, 10.0
VX, VY0 = 9.0, 12.0              # cos53=0,6  sin53=0,8 (ders kitabı değerleri)
T_UCUS = 2 * VY0 / G             # 2,4 s
H_MAX = VY0**2 / (2 * G)         # 7,2 m
MENZIL = VX * T_UCUS             # 21,6 m

FPS = 25
YAVAS = 2.0                      # 2 kat ağır çekim
KARE_UCUS = int(T_UCUS * YAVAS * FPS)   # 120 kare
KARE_BEKLE = 40                  # sonda bekleme
TOPLAM = KARE_UCUS + KARE_BEKLE
OK_OLCEK = 0.22                  # 1 m/s hız = 0,22 m ok uzunluğu
YARICAP = 0.35

CIKTI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kareler")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# ---------------- Sahneyi temizle ----------------
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
font = bpy.data.fonts.load(FONT) if os.path.exists(FONT) else None


def malzeme(ad, renk, isik=0.0):
    m = bpy.data.materials.new(ad)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*renk, 1)
    b.inputs["Roughness"].default_value = 0.6
    b.inputs["Specular IOR Level"].default_value = 0.1   # parlamayı azalt, renkler canlı kalsın
    if isik:
        b.inputs["Emission Color"].default_value = (*renk, 1)
        b.inputs["Emission Strength"].default_value = isik
    return m


def ata(obj, m):
    obj.data.materials.clear()
    obj.data.materials.append(m)


def yazi(metin, konum, boyut=0.7, m=None, hiza="LEFT"):
    bpy.ops.object.text_add(location=konum, rotation=(math.pi / 2, 0, 0))
    t = bpy.context.object
    t.data.body = metin
    t.data.size = boyut
    t.data.align_x = hiza
    if font:
        t.data.font = font
    t.visible_shadow = False      # yazıların gölgesi zemine düşmesin
    if m:
        ata(t, m)
    return t


M_ZEMIN = malzeme("zemin", (0.35, 0.6, 0.25))
M_TOP = malzeme("top", (0.95, 0.25, 0.1))
M_IZ = malzeme("iz", (0.95, 0.55, 0.2))
M_VX = malzeme("vx", (0.0, 0.2, 0.85))
M_VY = malzeme("vy", (0.0, 0.5, 0.1))
M_V = malzeme("v", (0.75, 0.0, 0.45))
M_YAZI = malzeme("yazi", (0.05, 0.05, 0.1))
M_CIZGI = malzeme("cizgi", (0.3, 0.3, 0.35))

# ---------------- Zemin ----------------
bpy.ops.mesh.primitive_cube_add(size=1, location=(MENZIL / 2, 2, -1.5))
z = bpy.context.object
z.scale = (60, 6, 3)          # üst yüzü z = 0'da olan kalın bir toprak bloğu
ata(z, M_ZEMIN)

# Metre işaretleri (her 3 m'de bir)
for x in range(0, 22, 3):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, -1.2, 0.0))
    c = bpy.context.object
    c.scale = (0.05, 0.05, 0.25)
    c.visible_shadow = False
    ata(c, M_CIZGI)
    yazi(f"{x}", (x, -1.3, -0.8), 0.5, M_YAZI, "CENTER")
yazi("x (m)", (22.6, -1.3, -0.8), 0.5, M_YAZI, "LEFT")

# ---------------- Top ----------------
bpy.ops.mesh.primitive_uv_sphere_add(radius=YARICAP, segments=40, ring_count=20)
top = bpy.context.object
bpy.ops.object.shade_smooth()
ata(top, M_TOP)


# ---------------- Ok (silindir gövde + koni uç) ----------------
def ok_yap(m):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.07, depth=1, vertices=16)
    govde = bpy.context.object
    ata(govde, m)
    bpy.ops.mesh.primitive_cone_add(radius1=0.18, depth=0.35, vertices=16)
    uc = bpy.context.object
    ata(uc, m)
    return govde, uc


def ok_ayarla(ok, bas, vektor):
    govde, uc = ok
    uzunluk = vektor.length
    if uzunluk < 0.05:                      # çok kısaysa gizle
        govde.hide_render = uc.hide_render = True
        return
    govde.hide_render = uc.hide_render = False
    yon = vektor.normalized()
    rot = yon.to_track_quat("Z", "Y")       # Z eksenini ok yönüne çevir
    govde_boy = max(uzunluk - 0.35, 0.01)
    govde.rotation_mode = uc.rotation_mode = "QUATERNION"
    govde.rotation_quaternion = uc.rotation_quaternion = rot
    govde.scale = (1, 1, govde_boy)
    govde.location = bas + yon * (govde_boy / 2)
    uc.location = bas + yon * (govde_boy + 0.175)


ok_vx = ok_yap(M_VX)
ok_vy = ok_yap(M_VY)
ok_v = ok_yap(M_V)

# ---------------- Yazılar ----------------
yazi("Eğik Atış", (-1.5, 0, 11.3), 1.0, M_YAZI)
yazi("v₀ = 15 m/s   θ = 53°   g = 10 m/s²", (-1.5, 0, 10.3), 0.55, M_YAZI)
t_yazi = yazi("", (14.5, 0, 11.3), 0.6, M_YAZI)
vx_yazi = yazi("", (14.5, 0, 10.4), 0.6, M_VX)
vy_yazi = yazi("", (14.5, 0, 9.5), 0.6, M_VY)
v_yazi = yazi("", (14.5, 0, 8.6), 0.6, M_V)
sonuc_yazi = yazi("", (-1.5, 0, 9.0), 0.6, M_YAZI)

# Maksimum yükseklik kesikli çizgisi (top tepeye ulaşınca görünür)
hmax_parcalar = []
for i in range(0, 22):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(i * 0.5 + 0.15, 0.3, H_MAX))
    p = bpy.context.object
    p.scale = (0.25, 0.03, 0.03)
    ata(p, M_CIZGI)
    p.hide_render = True
    hmax_parcalar.append(p)
hmax_yazi = yazi("Hmax = 7,2 m", (0.2, 0, H_MAX + 0.3), 0.5, M_YAZI)
hmax_yazi.hide_render = True

# ---------------- Işık, kamera, gökyüzü ----------------
bpy.ops.object.light_add(type="SUN", rotation=(0.9, 0.25, 0))   # kameranın arkasından, önden aydınlatır
bpy.context.object.data.energy = 3.0

bpy.ops.object.camera_add(location=(MENZIL / 2 + 0.5, -30, 4.8), rotation=(math.pi / 2, 0, 0))
kam = bpy.context.object
kam.data.type = "ORTHO"            # yandan, perspektifsiz görünüm (grafik gibi)
kam.data.ortho_scale = 27.5
sc.camera = kam

dunya = bpy.data.worlds.new("gok")
sc.world = dunya
dunya.use_nodes = True
# Kamera açık mavi gökyüzü görsün, ama sahneyi aydınlatan ortam ışığı daha zayıf olsun
nt = dunya.node_tree
arka = nt.nodes["Background"]
arka.inputs[0].default_value = (0.55, 0.65, 0.8, 1)
arka.inputs[1].default_value = 0.6
gok = nt.nodes.new("ShaderNodeBackground")
gok.inputs[0].default_value = (0.62, 0.8, 1.0, 1)
gok.inputs[1].default_value = 1.0
yol = nt.nodes.new("ShaderNodeLightPath")
karis = nt.nodes.new("ShaderNodeMixShader")
nt.links.new(yol.outputs["Is Camera Ray"], karis.inputs[0])
nt.links.new(arka.outputs[0], karis.inputs[1])
nt.links.new(gok.outputs[0], karis.inputs[2])
nt.links.new(karis.outputs[0], nt.nodes["World Output"].inputs["Surface"])

# ---------------- Görüntü ayarları ----------------
sc.view_settings.view_transform = "Standard"
sc.render.engine = "CYCLES"
sc.cycles.device = "CPU"
sc.cycles.samples = 16
sc.cycles.use_denoising = False
sc.cycles.max_bounces = 3
sc.render.resolution_x = 1280
sc.render.resolution_y = 720
sc.render.fps = FPS
os.makedirs(CIKTI, exist_ok=True)


def sayi(x, basamak=1):
    return f"{x:.{basamak}f}".replace(".", ",")   # Türkçe ondalık virgül


# ---------------- Kare kare çizim ----------------
iz_zamanlari = [i * 0.2 for i in range(0, 13)]   # her 0,2 s'de bir iz bırak
izler = []

tek = os.environ.get("TEK_KARE")
kareler = [int(tek)] if tek else range(TOPLAM)

for kare in kareler:
    t = min(kare / (YAVAS * FPS), T_UCUS)
    x = VX * t
    y = VY0 * t - 0.5 * G * t * t
    vy = VY0 - G * t
    konum = Vector((x, 0, y + YARICAP))
    top.location = konum

    # Stroboskop izleri: geçmiş konumlarda küçük toplar
    while len(izler) < len([s for s in iz_zamanlari if s <= t + 1e-6]):
        s = iz_zamanlari[len(izler)]
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=0.12, segments=16, ring_count=8,
            location=(VX * s, 0.2, VY0 * s - 0.5 * G * s * s + YARICAP))
        ata(bpy.context.object, M_IZ)
        izler.append(bpy.context.object)

    # Hız okları (topun önünde dursun diye y = -0.6)
    bas = konum + Vector((0, -0.6, 0))
    ucuyor = t < T_UCUS
    if ucuyor:
        ok_ayarla(ok_vx, bas, Vector((VX, 0, 0)) * OK_OLCEK)
        ok_ayarla(ok_vy, bas, Vector((0, 0, vy)) * OK_OLCEK)
        ok_ayarla(ok_v, bas, Vector((VX, 0, vy)) * OK_OLCEK)
    else:
        for ok in (ok_vx, ok_vy, ok_v):
            ok_ayarla(ok, bas, Vector((0, 0, 0)))

    v = math.hypot(VX, vy)
    t_yazi.data.body = f"t = {sayi(t, 2)} s"
    vx_yazi.data.body = f"vx = 9 m/s (sabit)"
    vy_yazi.data.body = f"vy = {sayi(vy)} m/s"
    v_yazi.data.body = f"v = {sayi(v)} m/s"

    tepe = t >= VY0 / G - 1e-6
    for p in hmax_parcalar:
        p.hide_render = not tepe
    hmax_yazi.hide_render = not tepe

    if not ucuyor:
        sonuc_yazi.data.body = "Uçuş süresi = 2,4 s\nMenzil = 21,6 m"
        vy_yazi.data.body = "vy = -12 m/s (yere çarptı)"
        v_yazi.data.body = "v = 15 m/s"

    sc.render.filepath = os.path.join(CIKTI, f"kare_{kare:04d}.png")
    bpy.ops.render.render(write_still=True)
    print(f"Kare {kare + 1}/{TOPLAM} bitti")
