import math, sys
def limb(pts, widths, fill):
    """Uzuv: eklemlerden geçen, kalınlığı değişen yumuşak şekil."""
    out=[]
    for (a,b),(wa,wb) in zip(zip(pts,pts[1:]),zip(widths,widths[1:])):
        dx,dy=b[0]-a[0],b[1]-a[1]; L=math.hypot(dx,dy); nx,ny=-dy/L,dx/L
        p=[(a[0]+nx*wa/2,a[1]+ny*wa/2),(b[0]+nx*wb/2,b[1]+ny*wb/2),(b[0]-nx*wb/2,b[1]-ny*wb/2),(a[0]-nx*wa/2,a[1]-ny*wa/2)]
        out.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in p)}" fill="{fill}"/>')
    for (x,y),w in zip(pts,widths):
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{w/2:.1f}" fill="{fill}"/>')
    return "\n    ".join(out)

def smooth(pts):
    """Kapalı Catmull-Rom eğrisi -> SVG path."""
    n=len(pts); d=f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(n):
        p0,p1,p2,p3=pts[i-1],pts[i],pts[(i+1)%n],pts[(i+2)%n]
        c1=(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6)
        c2=(p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6)
        d+=f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d+" Z"

SKIN,SKIN_D="#e3b08a","#c48a63"
SHIRT,SHIRT_D="#3f74ad","#2c5785"
PANTS,PANTS_D="#3d4350","#2a2e37"
SHOE="#2b1e16"; HAIR="#3a281c"

hip=(348,236); sh=(412,183)
# Gövde (kalça -> omuz), sırt üst-solda, karın alt-sağda
ux,uy=(sh[0]-hip[0]),(sh[1]-hip[1]); L=math.hypot(ux,uy); ux,uy=ux/L,uy/L
nx,ny=-uy,ux  # karın yönü
prof=[(-.08,15,15),(0.0,17,17),(.3,14,16),(.6,17,20),(.85,17,17),(1.02,12,10),(1.1,5,6)]
back=[(hip[0]+ux*L*t-nx*b, hip[1]+uy*L*t-ny*b) for t,b,f in prof]
front=[(hip[0]+ux*L*t+nx*f, hip[1]+uy*L*t+ny*f) for t,b,f in prof]
torso=smooth(back+front[::-1])
belt_a=(hip[0]+ux*L*.04-nx*16,hip[1]+uy*L*.04-ny*16); belt_b=(hip[0]+ux*L*.04+nx*17,hip[1]+uy*L*.04+ny*17)

svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="40 110 720 290" width="720" height="290">
  <title>Yerdeki kutuyu iten adam ve uyguladığı F kuvveti</title>
  <defs>
    <marker id="ok" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#d62828"/>
    </marker>
    <marker id="okKucuk" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#d62828"/>
    </marker>
    <linearGradient id="tahta" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#e2b46a"/><stop offset="1" stop-color="#c8924a"/>
    </linearGradient>
    <linearGradient id="gomlek" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#4a82bd"/><stop offset="1" stop-color="#335f92"/>
    </linearGradient>
  </defs>

  <rect x="40" y="110" width="720" height="290" fill="#ffffff"/>

  <!-- Gölgeler -->
  <ellipse cx="335" cy="362" rx="105" ry="6" fill="#000" opacity="0.12"/>
  <ellipse cx="552" cy="362" rx="92" ry="6" fill="#000" opacity="0.12"/>

  <!-- Zemin -->
  <path d="{' '.join(f'M{x},382 L{x+18},362' for x in range(62,730,18))}" stroke="#7a6a58" stroke-width="2"/>
  <line x1="60" y1="360" x2="740" y2="360" stroke="#4a3f35" stroke-width="4"/>

  <!-- Kutu (tahta sandık) -->
  <rect x="470" y="200" width="160" height="160" fill="url(#tahta)" stroke="#7a5420" stroke-width="4" rx="2"/>
  <g stroke="#a8763a" stroke-width="2" opacity="0.7">
    <line x1="472" y1="253" x2="628" y2="253"/><line x1="472" y1="306" x2="628" y2="306"/>
  </g>
  <text x="602" y="228" font-family="Georgia, serif" font-size="24" font-style="italic" fill="#4d3410">m</text>

  <!-- Adam: arka (uzak) uzuvlar daha koyu -->
  <g>
    <!-- uzak bacak (geride, düz, topuk havada) -->
    {limb([(346,240),(303,290),(262,340)],[30,21,15],PANTS_D)}
    <path d="M250,334 C246,342 250,350 262,356 L286,361 C292,361 292,354 286,351 L268,338 Z" fill="{SHOE}"/>
    <!-- uzak kol -->
    {limb([(404,190),(424,231)],[20,16],SHIRT_D)}
    {limb([(424,231),(463,247)],[14,10],SKIN_D)}
    {limb([(461,247),(468,238),(471,224)],[11,13,9],SKIN_D)}
    <!-- yakın bacak (önde, dizden bükük) -->
    {limb([(350,234),(404,272),(390,342)],[32,22,16],PANTS)}
    <path d="M380,338 C376,346 376,356 380,360 L420,360 C424,358 422,352 414,349 L400,342 Z" fill="{SHOE}"/>
    <!-- boyun -->
    {limb([(412,182),(428,170)],[17,15],SKIN)}
    <!-- gövde (gömlek) -->
    <path d="{torso}" fill="url(#gomlek)"/>
    <line x1="{belt_a[0]:.1f}" y1="{belt_a[1]:.1f}" x2="{belt_b[0]:.1f}" y2="{belt_b[1]:.1f}" stroke="#3a2a1e" stroke-width="5" stroke-linecap="butt"/>
    <!-- yakın kol -->
    {limb([(414,184),(429,224)],[21,17],SHIRT)}
    {limb([(429,224),(465,234)],[15,11],SKIN)}
    {limb([(463,233),(469,222),(471,207)],[12,14,9],SKIN)}
    <path d="M466,216 L470,215 M466,224 L470,224" stroke="{SKIN_D}" stroke-width="1.2" stroke-linecap="round"/>
    <!-- kafa (profil, öne bakıyor) -->
    <g transform="translate(434,155) rotate(14)">
      <path d="M-5,24 C-18,15 -22,-5 -14,-16 C-6,-25 11,-24 16,-12 L17,-4 L22,3 C22,5 19,6 17,6 L18,10 L16,12 L17,15 C15,20 10,21 5,20 L3,25 Z" fill="{SKIN}"/>
      <path d="M-16,-12 C-9,-27 13,-27 17,-9 C11,-14 2,-15 -4,-9 C-8,-5 -12,0 -18,4 C-21,-2 -20,-8 -16,-12 Z" fill="{HAIR}"/>
      <ellipse cx="-2" cy="3" rx="3.5" ry="5.5" fill="{SKIN_D}"/>
      <path d="M8,-6 L14,-6" stroke="{HAIR}" stroke-width="2" stroke-linecap="round"/>
      <circle cx="12" cy="-2" r="1.6" fill="#2a1d14"/>
      <path d="M14,11 L17,10" stroke="#a5654a" stroke-width="1.5" stroke-linecap="round"/>
    </g>
  </g>

  <!-- Kuvvet vektörü F (ellerin kutuya değdiği yerden, itme yönünde) -->
  <line x1="478" y1="236" x2="588" y2="236" stroke="#d62828" stroke-width="6" marker-end="url(#ok)"/>
  <!-- F etiketi (vektör işaretli) -->
  <line x1="516" y1="256" x2="538" y2="256" stroke="#d62828" stroke-width="2" marker-end="url(#okKucuk)"/>
  <text x="516" y="285" font-family="Georgia, serif" font-size="30" font-style="italic" font-weight="bold" fill="#d62828">F</text>
</svg>
'''
open(sys.argv[1],'w').write(svg)
