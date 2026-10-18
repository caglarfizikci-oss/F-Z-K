# Eğik atış animasyonu (Manim Community)
# Çalıştırma:  manim -pqm egik_atis.py EgikAtis
from manim import *
import numpy as np

V0 = 20      # ilk hız (m/s)
ACI = 50     # atış açısı (derece)
G = 10       # yer çekimi ivmesi (m/s²)

VX = V0 * np.cos(np.radians(ACI))
VY0 = V0 * np.sin(np.radians(ACI))
T_UCUS = 2 * VY0 / G
MENZIL = VX * T_UCUS
H_MAX = VY0**2 / (2 * G)

OK_OLCEK = 0.07  # 1 m/s hız kaç birim ok uzunluğu olsun


class EgikAtis(Scene):
    def construct(self):
        eksen = Axes(
            x_range=[0, 45, 5], y_range=[0, 14, 2],
            x_length=11, y_length=4.6,
            tips=False,
        ).to_edge(DOWN, buff=1.3)
        # Sayıları LaTeX gerektirmeden Text ile yaz
        sayilar = VGroup(
            *[Text(str(x), font_size=18).next_to(eksen.c2p(x, 0), DOWN, buff=0.15)
              for x in range(5, 46, 5)],
            *[Text(str(y), font_size=18).next_to(eksen.c2p(0, y), LEFT, buff=0.15)
              for y in range(2, 15, 2)],
        )
        x_et = Text("x (m)", font_size=22).next_to(eksen.x_axis, RIGHT, buff=0.15)
        y_et = Text("y (m)", font_size=22).next_to(eksen.y_axis, UP, buff=0.15)

        baslik = Text("Eğik Atış", font_size=40, weight=BOLD).to_corner(UL)
        bilgi = Text(
            f"v₀ = {V0} m/s    α = {ACI}°    g = {G} m/s²",
            font_size=20,
        ).next_to(baslik, RIGHT, buff=0.4)

        self.play(Write(baslik), FadeIn(bilgi))
        self.play(Create(eksen), FadeIn(sayilar), Write(x_et), Write(y_et))

        def konum(t):
            return eksen.c2p(VX * t, VY0 * t - 0.5 * G * t**2)

        t = ValueTracker(0)
        top = always_redraw(lambda: Dot(konum(t.get_value()), radius=0.11, color=YELLOW))
        iz = TracedPath(top.get_center, stroke_color=YELLOW, stroke_width=3,
                        dissipating_time=None)

        def oklar(tt, opak=1.0):
            p = konum(tt)
            vy = VY0 - G * tt
            vx_ok = Arrow(p, p + RIGHT * VX * OK_OLCEK, buff=0, color=BLUE,
                          stroke_width=5, max_tip_length_to_length_ratio=0.25)
            vy_ok = Arrow(p, p + UP * vy * OK_OLCEK, buff=0, color=RED,
                          stroke_width=5, max_tip_length_to_length_ratio=0.25)
            v_ok = Arrow(p, p + (RIGHT * VX + UP * vy) * OK_OLCEK, buff=0,
                         color=GREEN, stroke_width=6,
                         max_tip_length_to_length_ratio=0.2)
            g = VGroup(vx_ok, vy_ok, v_ok) if abs(vy) > 0.3 else VGroup(vx_ok, v_ok)
            return g.set_opacity(opak)

        canli_oklar = always_redraw(lambda: oklar(t.get_value()))

        aciklama = VGroup(
            MarkupText("v<sub>x</sub>  (yatay hız: hep sabit)", font_size=22, color=BLUE),
            MarkupText("v<sub>y</sub>  (düşey hız: değişir)", font_size=22, color=RED),
            MarkupText("v    (bileşke hız)", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR)

        self.add(iz)
        self.play(FadeIn(top), FadeIn(canli_oklar), FadeIn(aciklama))

        # Uçuşu 5 durakta göster, her durakta okların "hayaletini" bırak
        duraklar = np.linspace(0, T_UCUS, 5)[1:]
        for d in duraklar:
            self.add(oklar(t.get_value(), opak=0.3))
            self.play(t.animate.set_value(d), run_time=1.6, rate_func=linear)

            if np.isclose(d, T_UCUS / 2):
                p = konum(d)
                not_ = MarkupText("Tepe noktası: v<sub>y</sub> = 0", font_size=24, color=RED)
                not_.next_to(p, UP, buff=0.5)
                h_cizgi = DashedLine(eksen.c2p(VX * d, 0), p, color=GREY)
                h_et = MarkupText(f"h<sub>max</sub> ≈ {H_MAX:.1f} m", font_size=22).next_to(h_cizgi, LEFT)
                self.play(Write(not_), Create(h_cizgi), FadeIn(h_et))
                self.wait(1.2)
                self.play(FadeOut(not_))

        self.add(oklar(T_UCUS, opak=0.3))
        menzil_ok = DoubleArrow(eksen.c2p(0, -1.6), eksen.c2p(MENZIL, -1.6),
                                buff=0, color=WHITE, stroke_width=3)
        menzil_et = Text(f"Menzil ≈ {MENZIL:.1f} m   |   Uçuş süresi ≈ {T_UCUS:.1f} s",
                         font_size=22).next_to(menzil_ok, DOWN, buff=0.1)
        self.play(GrowFromCenter(menzil_ok), Write(menzil_et))
        self.wait(2)
