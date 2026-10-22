# Proje notları

Bu depo bir lise fizik öğretmeninin ders materyallerini içerir (animasyonlar, görseller).
Açıklamaları lise öğrencilerinin anlayacağı sade bir Türkçeyle yaz.

## Görsel / çizim tarzı (öğretmenin onayladığı tarz)

Fizik görsellerinde insan figürü çizilecekse **çöp adam veya çizgi film tarzı kullanma**.
Referans: `gorseller/kutu_iten_adam.svg` (üreten betik: `gorseller/kutu_iten_adam.py`).

- **İnsan figürü:** Gerçekçi vücut oranları, eklemlerden bükülen kol ve bacaklar, harekete uygun
  doğal duruş (ör. iterken öne eğilme). Kıyafet (gömlek, pantolon, ayakkabı), profil yüz
  (saç, kulak, göz, burun). Uzaktaki uzuvlar daha koyu renkte (derinlik için).
- **Nesneler:** Gerçekçi görünüm (ör. tahta sandık), hafif renk geçişi, yerde hafif gölge.
- **Zemin:** Kalın çizgi ve altında eğik tarama.
- **Fizik gösterimi:** Kuvvetler kalın kırmızı (#d62828) oklarla, temas noktasından ve doğru yönde.
  Etiketler italik serif yazı tipinde, vektörlerin üstünde küçük ok (F⃗). Kütle gibi
  büyüklükler italik (m).
- **Çıktı:** Düzenlenebilir SVG ve 2x çözünürlüklü PNG, `gorseller/` klasörüne.
  PNG için: `/opt/pw-browsers/chromium_headless_shell-*/.../headless_shell --screenshot`
  (SVG'yi kenar boşluğu olmayan bir HTML içine koyarak).
