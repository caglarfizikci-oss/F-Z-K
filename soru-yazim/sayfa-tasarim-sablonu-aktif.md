# Sayfa Tasarım ve Dizgi Şablonu (Aktif Fizik AYT esas alınarak)

**Kullanıcı kararı (2026-11-22):** İstenen bütün konular bu tasarımla hazırlanır. Önce konu anlatımı, sonra soru sayfaları gelir. Soru sayfalarında solda **Kavrama Bölümü** (Örnek ve Çözüm), sağda **Uygulama Bölümü** (Soru) bulunur. Renkler ve tasarımın bütün öğeleri aşağıdaki ölçülere uyar.

Kaynak: `soru-yazim/kaynak/Aktif-1-17.pdf`, `Aktif-18-35.pdf`, `Aktif-36-50.pdf` (Aktif Fizik AYT 2024, s. 1-50).
Ölçüm yöntemi: Renk kodları, yazı tipleri, puntolar ve konumlar PDF'in içinden (çizim ve metin nesnelerinden) birebir okundu; tahmin değildir. Ölçüler mm cinsindendir; konumlar sayfanın sol üst köşesinden ölçülür.

Bu şablon `tymm-2026-fizik-programi-genel-kurallar.md` dosyasındaki görsel ve tablet kurallarıyla birlikte uygulanır. Çelişki olursa kullanıcı kuralları geçerlidir (bkz. bölüm 12).

---

## 1. Sayfa

- Boyut: **198 × 281 mm** (561,26 × 796,53 pt). MEB kitap ebadı 195 × 275 mm'dir; Aktif'in kesimli boyutu bu ölçüye yakındır.
- Tek ve çift sayfa kenar boşlukları aynalıdır (metin başlangıcı):
  - **Tek sayfa** (11, 13…): sol sütun 16,5-94,9 mm; sağ sütun 101,0-179,4 mm.
  - **Çift sayfa** (10, 12…): sol sütun 19,5-97,9 mm; sağ sütun 104,0-182,4 mm. Yani her şey 3 mm sağa kayar.
- Sütun genişliği yaklaşık **78,4 mm**. İki sütun arasında **dikey ayırıcı çizgi** vardır: renk `#F47920` (turuncu), kalınlık 0,5 pt; tek sayfada x = 97,6 mm, y 29-258 mm.
- Tam genişlik konu anlatımında metin 18,5-177,4 mm arasındadır.
- Üst bant y 19,0-23,9 mm; içerik y ≈ 28 mm'de başlar ve 258 mm'de biter.

## 2. Renk paleti (PDF'ten okunan kodlar)

| Kullanım | Renk | Kod |
|---|---|---|
| Ana metin | koyu siyah | `#231F20` |
| Vektörler, kuvvet okları, vurgulu kavram yazısı, tablo çizgileri | magenta | `#EC008C` |
| "Örnek :" etiketi | gül kırmızısı | `#DA5273` |
| "Çözüm" ve "Cevap:" yazısı; Kavrama bandı | pembe | `#F05A89` |
| "Soru :" etiketi; Uygulama bandı; formül kutusu çerçevesi | camgöbeği | `#00AEEF` |
| Orta bant (ünite adı) zemini | açık şeftali | `#FEE0C8` |
| Orta bant yazısı; konu kutusu başlık yazısı | koyu kahve | `#5C3716` |
| Sütun ayırıcı çizgisi | turuncu | `#F47920` |
| Konu kutusu başlık sekmesi | açık turuncu | `#FDC992` |
| Konu kutusu zemini | krem | `#FFF5E9` |
| Konu kutusu gölgesi; konu testi bandı | turuncu | `#F8992F` |
| AKTİF NOT etiketi zemini; ünite numarası "1." | kırmızı | `#D2232A` |
| Ünite başlık bandı | mavi | `#1678BE` |
| Konu testi soru numaraları (1., 2.) | parlak kırmızı | `#ED1C24` |
| Cevap anahtarı şeridi zemini | çok açık mavi | `#E1F4FD` |
| Kavrama bandı koyu kıvrımı / Uygulama bandı koyu kıvrımı | bordo / lacivert | `#A52C53` / `#24408F` |
| Tablo başlık satırı zemini | çok açık pembe | `#FDE9F1` |
| Eşit bölmeli çubuk (dönüşümlü) | mavi ve turuncu | `#1678BE` + `#F8992F` |
| Asılı yükler | magenta veya yeşil | `#EC008C` / `#8DC63F` |
| Tavan ve duvar taraması, destekler | gri | `#D1D3D4`, `#ACACAC` |
| Eğik düzlem | açık sarı ve krem tonları | `#F3B366`, `#F6C181` |
| Yeşil vurgu (bazı şekiller) | yeşil | `#39B54A`, `#69BD45` |

## 3. Yazı tipleri ve puntolar

| Öğe | Aktif'teki yazı tipi | Punto | Renk | Bizim ortamdaki karşılığı |
|---|---|---|---|---|
| Ana metin, soru metni, çözüm | Swiss 721 BT Roman | 9 | `#231F20` | Nimbus Sans (ya da Liberation Sans) |
| Soru kökü ("Buna göre, …"), vurgulu yazı | Swiss 721 BT Bold | 9 | `#231F20` | Nimbus Sans Bold |
| Şekil etiketleri, küçük notlar | Swiss | 8 | `#231F20` | Nimbus Sans 8 |
| "Örnek :" | Arial Bold | 11 | `#DA5273` | Liberation Sans Bold 11 |
| Örnek ve soru numarası ("2", "4a") | Arial Bold | 11 | `#231F20` | Liberation Sans Bold 11 |
| "Soru :" | Arial Bold | 11 | `#00AEEF` | Liberation Sans Bold 11 |
| "Çözüm", "Cevap:" | Swiss 721 BT Bold | 9 | `#F05A89` | Nimbus Sans Bold 9 |
| Bant yazısı "KAVRAMA BÖLÜMÜ" | Calibri Bold, küçük büyük harf (ilk harf 12, diğerleri 10) | 12/10 | beyaz | Carlito Bold |
| Orta bant (ünite adı) | Calibri Bold | 11 | `#5C3716` | Carlito Bold 11 |
| Sayfa numarası | Calibri Bold | 10 | `#231F20` | Carlito Bold 10 |
| Cevap anahtarı ("Soru 2/ E") | Swiss Roman 7; harf kalın | 7 | `#00AEEF`; harf siyah | Nimbus Sans 7 |
| Konu kutusu başlığı (BÜYÜK HARF) | Swiss 721 BT Bold | 10 | `#5C3716` | Nimbus Sans Bold 10 |
| "AKTİF NOT" etiketi | Helvetica Bold | 12 | beyaz | Nimbus Sans Bold 12 |
| Ünite başlığı | Aero (yuvarlak hatlı kalın, eğik) | 23 | beyaz | Carlito Bold Italic 23 (yaklaşık) |
| "ÜNİTE" ve "1." | Aero 20 `#F7DACE`; Calibri Bold 30 `#D2232A` | | | Carlito Bold |
| Konu testi başlığı | Calibri Bold 16 beyaz; "KONU TESTİ" Calibri Bold 14/11 beyaz; test no. Benguiat 20 `#F05A89` | | | Carlito Bold |
| Konu testi soru no. ("1.") | Swiss Bold | 10 | `#ED1C24` | Nimbus Sans Bold 10 |

- Satır aralığı: 9 punto metinde yaklaşık 11-13,5 pt. Paragraflar iki yana yaslıdır ve heceleme açıktır.
- Matematik ifadeleri metinle aynı puntoda yazılır; vektörlerin üstünde ok bulunur. Kesirler alt alta yazılır.

## 4. Konu anlatımı sayfası

### 4.1. Ünite giriş başlığı (ünitenin ilk sayfası)
- Mavi (`#1678BE`) yatay şerit: x 16-178 mm, y 19-37 mm, sağ ucu yuvarlatılmış. Arkasında 1 mm kaydırılmış siyah (`#231F20`) gölge vardır.
- Şeridin içinde ünite adı büyük harflerle, beyaz, kalın ve eğik (Aero 23).
- Sağda turuncu (`#F8992F`) eğik sekme (x 118-173 mm) var; içinde açık krem bir alan, kırmızı "1." ve altında "ÜNİTE" yazısı.

### 4.2. Konu kutusu ("konu anlatım kutusu")
- **Başlık sekmesi:** `#FDC992` zeminli, yaklaşık 8 mm yüksek, kutu genişliğinden kısa bir şerit. Solda turuncu üçgen ya da ok ucu işareti, içinde BÜYÜK HARFLE başlık (Swiss Bold 10, `#5C3716`).
- **Kutu:** `#FFF5E9` krem zemin. Arkasında sağa ve aşağı 1 mm kaydırılmış **düz turuncu gölge** (`#F8992F`) vardır; saydamlık kullanılmaz.
- Kutunun içinde metin solda, şekil sağda ya da altta durur (metin ve şekil yan yana).
- Yeni kavram ilk geçtiğinde **magenta** (`#EC008C`) yazılır ("vektörel büyüklük"); tanım terimleri kalın yazılabilir ("**tork**").
- **Formül kutusu:** Beyaz zemin, ince camgöbeği (`#00AEEF`) çerçeve; formül ortada (örneğin τ₀ = F · d). Bazen açık mavi zeminli.

### 4.3. AKTİF NOT kutusu
- Üstte solda turuncu aşağı bakan üçgen; yanında **kırmızı (`#D2232A`) hap biçimli etiket**, içinde beyaz "AKTİF NOT" (Helvetica Bold 12).
- Kutu `#FFF5EA` zeminli, `#F99F3D` turuncu gölgeli (konu kutusuyla aynı yapı).
- İçerikte kesinlikle bilinmesi gereken kısa bir kural ya da püf noktası bulunur.
- **Boşluk doldurma işlevi:** Bir sayfada kısa bir sorunun sığmayacağı kadar az yer kalırsa o boşluğa konuyla ilgili bir AKTİF NOT konur. Yer yeterliyse önce kısa, 5 şıklı soru tercih edilir.

### 4.4. Yerleşim
- Vektör ünitesinin 7-9. sayfalarında konu kutuları **iki sütunlu** dizilmiştir. Tork ünitesinin 33. sayfasında kutular **tam genişliktedir**.
- **Bizim kuralımız:** Konu anlatımı **tam genişlikte** yapılır (33. sayfa modeli). Kutuların biçimi, yani sekme, krem zemin, turuncu gölge ve AKTİF NOT, aynen kullanılır.
- Sayfa numarası altta ortadadır (bkz. bölüm 7).

## 5. Kavrama ve Uygulama (soru) sayfası

### 5.1. Üst bant (y 19,0-23,9 mm)
Üç parçadan oluşur:
- **Sol:** "KAVRAMA BÖLÜMÜ" pembe (`#F05A89`) şerit, x 7,6-49,6 mm. Sol ucu sayfa kenarına taşar, sağ ucu ok gibi sivri. Altında bordo (`#A52C53`) küçük bir kıvrım (kurdele gölgesi) var. Yazı beyaz, küçük büyük harf (Calibri Bold).
- **Orta:** `#FEE0C8` açık şeftali şerit, x 50,3-144,7 mm, iki ucu çentikli. Ortasında ünite adı ("Vektör Kuvvet - Denge") Calibri Bold 11, `#5C3716`.
- **Sağ:** "UYGULAMA BÖLÜMÜ" camgöbeği (`#00AEEF`) şerit, x 145,6-187,4 mm. Sağ ucu sayfa kenarına doğru, altında lacivert (`#24408F`) kıvrım var. Yazı beyaz, küçük büyük harf.

### 5.2. Sol sütun: Kavrama Bölümü
- **"Örnek : 2"** etiketi: "Örnek :" `#DA5273` Arial Bold 11 ile, numara siyah aynı puntoda. Etiketten sonra 1-2 mm boşluk bırakılır.
- Örnek metni Swiss 9. Şekil metnin sağında ya da altında durur; şekil küçükse metin yanına sarılır.
- Soru kökü **kalın**: "**Buna göre, K + L vektörünün bitiş ucunun koordinatı nedir?**"
- Örneklerin çoğu **şıksızdır**. Şıklı örnek de olabilir (öncüllü ya da tablo şıklı).
- **"Çözüm"** başlığı `#F05A89` Swiss Bold 9 ile, kendi satırında yazılır. Çözüm metni siyah 9 punto; her işlem ayrı satırdadır. Çözüm şekli (genellikle magenta oklarla) metnin yanında durur.
- **"Cevap: (3, 4)"**: Çözümün sonunda, sağa yaslı; "Cevap:" pembe kalın, değer siyah.
- Gerekirse "I. yol / II. yol" ya da "Pratik Çözüm" başlıkları kullanılır. Pratik çözüm, camgöbeği çerçeveli bir kutuda verilir.

### 5.3. Sağ sütun: Uygulama Bölümü
- **"Soru : 2"** etiketi: "Soru :" `#00AEEF` Arial Bold 11, numara siyah. Kısa sorular "Soru : 4a", "Soru : 4b" diye bölünür.
- Soru metni Swiss 9; şekil ortalanmış; soru kökü kalın.
- **Şıklar:**
  - Kısa şıklar **tek satırda beş tane**: `A) 5   B) 4   C) 3   D) 2   E) 1`
  - Orta uzunlukta şıklar **iki sütunda**: A ile B, C ile D yan yana, E ortada ya da tek başına.
  - Uzun şıklar her biri ayrı satırda.
  - **Tablo şıklar:** Harfler tablonun solunda dışarıda yazılır. Tablo çizgileri ince magenta (`#EC008C`, 0,5 pt), başlık satırı kalın, siyah yazı ve açık pembe zemin; hücreler ortalı.
  - Öncüllü sorularda öncüller I., II., III. diye alt alta yazılır; şıklar `A) Yalnız I  B) I ve II …`.
- Soru ile ilgili şekil, metnin altında ve ortalı durur. Soru metni bazen şeklin yanına sarılır.

### 5.4. Hizalama
- Örnek 1 ile Soru 1'in etiketleri **aynı yükseklikten** başlar (y ≈ 27,9 mm).
- Sayfanın ikinci örneği ile ikinci soru da çoğu zaman aynı hizadadır (11. sayfada y 151,6 mm). Gerekirse soru a/b olarak bölünür.
- Sağ sütunda boşluk kalmaz; sorular sayfaya dağıtılır.

## 6. Konu testi sayfası (bilgi için; biz ayrı test sayfası yapmıyoruz)
- Üst bant: Solda turuncu (`#F8992F`) şerit, x 7-91 mm. Sol ucunda koyu kırmızımsı (`#C46853`) kare bir köşe ve beyaz ünite adı (Calibri Bold 16). Ortada açık camgöbeği (`#6DCFF6`) geçiş, sağda pembe (`#F05A89`) şerit ve "KONU TESTİ" yazısı. En sağda beyaz daire içinde pembe test numarası.
- İki sütunlu düzen, ortada turuncu ayırıcı; soru numaraları kırmızı ve kalın ("1.").
- Ayırıcı çizginin ortasında dikey olarak "aktif öğrenme yayınları" yazar (MyriadPro Cond 11, `#1D5B6F`).
- Cevap anahtarı altta iki şeritte bulunur: sol sütunun soruları solda, sağ sütununkiler sağda.
- **Bizim kuralımız:** Ayrı konu testi ya da pekiştirme sayfası yapılmaz.

## 7. Sayfa altı
- **Sayfa numarası:** Altta ortada (x ≈ 96 mm, y ≈ 265 mm). Numara, solda pembe, sağda camgöbeği renkte iki yarım yuvarlak öğenin oluşturduğu hap biçimli bir şeklin ortasındaki beyaz alanda yazar (Calibri Bold 10).
- **Cevap anahtarı şeridi:** `#E1F4FD` açık mavi zemin, sağda x 110,6-198 mm, y 264,1-281 mm (sayfa kenarına kadar). İçinde "Soru 2/ **E**   Soru 3/ **B**" yazar: "Soru 2/" camgöbeği 7 punto, harf siyah ve kalın.
- Konu anlatımı sayfalarında cevap şeridi yoktur, yalnızca sayfa numarası bulunur.

## 8. Şekil çizim stili
- **Vektör ve kuvvet okları:** Magenta `#EC008C`, kalınlık 1 pt, dolu küçük ok ucu. Kuvvet etiketi okun ucunun yanında yazılır (F₁, ok işaretli).
- **Kareli düzlem:** İnce siyah (`#231F20`) **noktalı** çizgiler (0,5 pt, çizgi deseni 1-1). Dış çerçeve de noktalıdır. Eksenler düz siyah 0,7 pt; eksen okları ve sayılar 8 puntodur.
- **Yardımcı çizgiler:** Bileşenler ve izdüşümler için ince kesikli magenta ya da siyah çizgiler.
- **Tavan ve duvar:** Gri tarama (eğik çizgili şerit) ve altında kalın siyah çizgi.
- **Cisimler:** Kutular açık şeftali (`#F8B77F` / `#F6C181`) ya da magenta dolgulu; yükler kare biçiminde magenta veya yeşil. "G" ve "P" etiketleri cismin içinde yazılır.
- **Eşit bölmeli çubuk:** Bölmeler sırayla mavi ve turuncu renklidir. Destek noktaları sarı üçgenle gösterilir. Kesikli "yatay" çizgisi ve "yatay" etiketi bulunur.
- **Küre ve eğik düzlem:** Küre açık mavi ve gri tonlu, merkezinde O noktası var. Eğik düzlem sarı ve krem dolgulu dik üçgendir.
- **Açılar:** İnce yay ile gösterilir; derece etiketi siyah 8 punto (30°, 53°).
- **Gerçek nesneler** (anahtar, makas, direksiyon, merdiven): Renkli ve gerçekçi illüstrasyonlardır (gri metal ve turuncu sap gibi).
- **İnsan figürleri:** Aktif'te çizgi film tarzındadır (barfiks çeken çocuk). **Bizim kuralımız:** İnsanlar gerçekçi çizilir ve kıyafetleri MEB kılık kıyafet yönetmeliğine uyar.
- Bir sayfadaki şekillerin ölçeği tutarlıdır; kareli düzlemde bir birim kare yaklaşık 4,4-5 mm'dir.

## 9. Sayı ve dizgi alışkanlıkları
- Ondalık ayırıcı virgüldür (0,6). Birimler sayıdan bir boşlukla ayrılır (15 N, 90 cm).
- Trigonometri değerleri soru içinde parantezle verilir: "(sin37° = 0,6 , cos37° = 0,8)".
- Çarpma için nokta kullanılır ("F . d", "2AB . cos120°").
- Kesirler alt alta yazılır (1/2 değil, ½ biçiminde dikey kesir).
- Vektör adları italik değildir; üstlerinde ok vardır.

## 10. Uygulamada dosya hazırlama (bizim üretim notlarımız)
- Sayfaları HTML/CSS ile tasarlayıp PDF'e çeviriyoruz. Yazı tipleri TrueType ya da OpenType olarak gömülür; **Type3 font olmaz.**
- Gölgeler saydamlıkla değil, **ayrı ve düz renkli bir dikdörtgenle** verilir; /SMask ve /Group oluşmaz.
- Görseller beyaz zeminli JPG'dir; saydam PNG kullanılmaz.
- Metinde ←, →, ⇒ gibi işaretler kullanılmaz (Aktif çözümlerinde "⇒" geçiyor; biz kullanmıyoruz).
- Kesikli kenarlık ile yuvarlak köşe aynı öğede birlikte kullanılmaz (tablet kuralı). Kareli düzlemin noktalı çizgileri köşesiz düz çizgi olduğu için kullanılabilir.
- Her sayfanın JPG görüntüsü üretilir ve gönderilmeden önce kontrol edilir.

## 11. Kontrol listesi (her sayfa için)
1. Üst bant doğru mu? Soru sayfasında Kavrama / ünite adı / Uygulama; konu anlatımında ünite başlığı ya da konu kutusu.
2. Örnek ve Soru etiketlerinin renkleri doğru mu (`#DA5273` / `#00AEEF`), numaraları siyah mı?
3. Çözüm ve Cevap pembe (`#F05A89`) mi, Cevap sağa yaslı mı?
4. Sütun ayırıcı turuncu çizgi var mı, sütunlar 78 mm mi, tek ve çift sayfa boşlukları doğru mu?
5. Şıklar 5 tane mi (A-E), yerleşimi uzunluğa uygun mu?
6. Vektör ve kuvvet okları magenta mı, kareli düzlem noktalı mı?
7. Sayfa numarası hapı ve cevap anahtarı şeridi var mı?
8. Tablet kontrolü: Type3, /SMask ve /Group yok mu?

## 12. Kullanıcı kurallarıyla uyum (çelişki olursa kullanıcı kuralı geçerlidir)
| Aktif Fizik'te | Bizde |
|---|---|
| Konu anlatımı bazen iki sütun (s. 7-9) | Her zaman tam genişlik (s. 33 modeli) |
| Ayrı konu testi sayfaları | Yapılmaz |
| Çizgi film insan figürleri | Gerçekçi insan, MEB kıyafet kuralı |
| "⇒" işareti | Kullanılmaz |
| Kavrama örneklerinin çoğu şıksız | Sol sütun örneği şıksız olabilir; sağ sütundaki her soru 5 şıklı |
| Bağlam az | TYMM gereği sağ sütunda bağlam soruları; bölüm sonunda 2 bağlam |
| Lami teoremi, "atış" terimleri | Kullanılmaz (TYMM) |
| Akım oku ile i harfi, mıknatıs renkleri (Aktif'in bu sayfalarında yok) | Akım oku ile i harfi farklı renkte; N kırmızı, S mavi |
