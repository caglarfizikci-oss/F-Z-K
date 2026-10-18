# Menzil formülünün adım adım çıkarılışı (Manim + LaTeX)
# Çalıştırma:  manim -pqh menzil_formulu.py MenzilFormulu
from manim import *

VX_RENK = BLUE
VY_RENK = RED
T_RENK = YELLOW


class MenzilFormulu(Scene):
    def construct(self):
        baslik = Text("Menzil Formülü Nereden Gelir?", font_size=40, weight=BOLD)
        baslik.to_edge(UP)
        self.play(Write(baslik))

        def adim(aciklama, *formul):
            yazi = Text(aciklama, font_size=24, color=GREY_A)
            tex = MathTex(*formul, font_size=44)
            return VGroup(yazi, tex).arrange(RIGHT, buff=0.5)

        # 1. adım: ilk hızı bileşenlerine ayır
        a1 = adim("1) Hızı bileşenlere ayır:",
                  r"v_x = v_0\cos\alpha", r"\qquad", r"v_{0y} = v_0\sin\alpha")
        a1[1][0].set_color(VX_RENK)
        a1[1][2].set_color(VY_RENK)

        # 2. adım: tepe noktasında düşey hız sıfır
        a2 = adim("2) Tepe noktasında", r"v_y = 0", r"\;\Rightarrow\;",
                  r"t_{\text{çıkış}} = \frac{v_0\sin\alpha}{g}")
        a2[1][0].set_color(VY_RENK)
        a2[1][2].set_color(T_RENK)

        # 3. adım: uçuş süresi çıkışın iki katı
        a3 = adim("3) İnmek de aynı süreyi alır:",
                  r"t_{\text{uçuş}} = \frac{2\,v_0\sin\alpha}{g}")
        a3[1].set_color(T_RENK)

        # 4. adım: yatayda sabit hızlı hareket
        a4 = adim("4) Yatayda hız sabit:",
                  r"R = v_x \cdot t_{\text{uçuş}}", r"=",
                  r"v_0\cos\alpha", r"\cdot", r"\frac{2\,v_0\sin\alpha}{g}")
        a4[1][2].set_color(VX_RENK)
        a4[1][4].set_color(T_RENK)

        adimlar = VGroup(a1, a2, a3, a4).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        adimlar.next_to(baslik, DOWN, buff=0.6).to_edge(LEFT, buff=0.6)

        for a in adimlar:
            self.play(FadeIn(a[0], shift=RIGHT * 0.3), run_time=0.7)
            self.play(Write(a[1]), run_time=1.6)
            self.wait(1.2)

        # 5. adım: trigonometri ile sadeleştir
        self.play(FadeOut(VGroup(a1, a2, a3)), a4.animate.next_to(baslik, DOWN, buff=0.6))

        ara = MathTex(r"R = \frac{v_0^2 \,(", r"2\sin\alpha\cos\alpha", r")}{g}", font_size=52)
        ozdes = MathTex(r"2\sin\alpha\cos\alpha", r"=", r"\sin 2\alpha", font_size=40)
        ozdes_yazi = Text("Trigonometri özdeşliği:", font_size=24, color=GREY_A)
        ozdes_grup = VGroup(ozdes_yazi, ozdes).arrange(RIGHT, buff=0.4)
        ara.next_to(a4, DOWN, buff=0.7)
        ozdes_grup.next_to(ara, DOWN, buff=0.6)

        self.play(Write(ara))
        self.play(Indicate(ara[1], color=ORANGE))
        self.play(FadeIn(ozdes_grup, shift=UP * 0.3))
        self.wait(1)

        sonuc = MathTex(r"R = \frac{v_0^2 \,", r"\sin 2\alpha", r"}{g}", font_size=64)
        sonuc.move_to(ara)
        self.play(TransformMatchingTex(ara, sonuc), FadeOut(ozdes_grup))
        kutu = SurroundingRectangle(sonuc, color=GREEN, buff=0.25, corner_radius=0.1)
        self.play(Create(kutu))
        self.wait(1)

        # 6. adım: önceki videodaki değerlerle kontrol
        kontrol_yazi = Text("Önceki videodaki değerlerle kontrol:", font_size=24, color=GREY_A)
        kontrol = MathTex(
            r"R = \frac{(20\ \text{m/s})^2 \cdot \sin 100^\circ}{10\ \text{m/s}^2}",
            r"\approx", r"39{,}4\ \text{m}", font_size=40,
        )
        kontrol[2].set_color(GREEN)
        kontrol_grup = VGroup(kontrol_yazi, kontrol).arrange(DOWN, buff=0.3)
        kontrol_grup.next_to(kutu, DOWN, buff=0.6)
        self.play(FadeIn(kontrol_yazi))
        self.play(Write(kontrol))
        self.wait(1.5)

        # Bonus: en uzak atış açısı
        bonus = MathTex(r"\sin 2\alpha = 1 \;\Rightarrow\; \alpha = 45^\circ",
                        font_size=40, color=YELLOW)
        bonus_yazi = Text("En uzağa atış:", font_size=24, color=YELLOW)
        bonus_grup = VGroup(bonus_yazi, bonus).arrange(DOWN, buff=0.3)
        bonus_grup.next_to(kutu, RIGHT, buff=0.6)
        self.play(FadeIn(bonus_grup, shift=UP * 0.3))
        self.wait(3)
