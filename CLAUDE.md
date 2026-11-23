# F-Z-K: Lise Fizik Materyalleri (Çalışma Kuralları)

Kullanıcı lise fizik öğretmenidir. Kullanıcıyla **Türkçe** ve lise öğrencisinin anlayacağı **sade bir dille** konuşulur.

## Rehber dosyalar (hafif okuma kuralı, kullanıcı kararı, 2026-11-23)

Token tasarrufu için rehberlerin hepsi her işten önce okunmaz. Bu dosyadaki değişmez kurallar her zaman geçerlidir. Rehberler yalnız **kullanıcı söylediğinde** ya da iş o rehberin içeriğini **gerçekten gerektirdiğinde** açılır. Açılırken de **yalnız ilgili bölüm** okunur (grep ile başlık bulunup o kısım okunur, dosyanın tamamı okunmaz). Ne yapılacağı kullanıcı tarafından söylenir. Emin olunamazsa dosya okumak yerine kullanıcıya kısaca sorulur.

1. `soru-yazim/tymm-2026-fizik-programi-genel-kurallar.md`: **ANA ŞABLON.** TYMM 2026 programının genel esasları, öncelik sırası, çıktı fiili ile soru türü eşlemesi, ünite ünite kritik sınırlar ve kullanıcının bütün materyal kuralları burada. Yeni materyal yazılırken yalnız ilgili ünitenin kısmı okunur.
2. `soru-yazim/tymm-2026-fizik-ciktilar-tum-siniflar.md` (145 KB, büyük): 9-12. sınıfların 106 öğrenme çıktısı ve "kaçınılır" / "sınırlı kalınır" notları. **Asla tamamı okunmaz**; yalnız çalışılan sınıfın ilgili ünitesi okunur (başlıklar: "## 11. Sınıf 2. Ünite: ..." biçiminde).
3. `soru-yazim/tymm-baglam-temelli-soru-yazim-kurallari.md`: Bağlam temelli soru yazım kuralları. Yalnız bağlam (Örnek + 2-3 soru) yazılırken.
4. `soru-yazim/stil-rehberi-aktif-ayt.md`: Aktif Fizik AYT'nin sayfa düzeni, soru türleri ve TYMM ile çelişen noktaları. Yalnız gerektiğinde.
5. `soru-yazim/sayfa-tasarim-sablonu-aktif.md`: **Bütün sayfalar bu tasarımla yapılır** (kullanıcı kararı, 2026-11-22). Renk kodları, yazı tipleri, ölçüler burada. Yalnız sayfa (PDF) üretilirken ya da tasarım düzeltilirken okunur; aynı oturumda bir kez okunduysa yeniden okunmaz.

Ek tasarruf: Aynı dosya aynı oturumda tekrar okunmaz. Büyük PDF'ler ve görüntüler gerekmedikçe açılmaz; açılırsa yalnız gereken sayfalar okunur.

Kaynak belgeler `soru-yazim/kaynak/` klasöründedir: `Fizikprg.pdf` (program), bağlam kılavuzunun Ocak 2026 baskısı (`Tymm-1-50`, `Tymm-51-100`, `Tymm-101-138`) ve Mart 2026 web kopyası ile bunların metinleri. Kullanıcının Drive'ında bunlar da var: Tymm.pdf (kılavuzun tamamı, 24 MB; parçalı hali Tymm-1-50/51-100/101-138), 11meb kitap bölümleri (kuvvet, indüksiyon, transformatör), 11zengin.pdf, PISA örnek soruları, AYT çıkmış sorular, Fizikeskikazanımeski.pdf, Manyetik_Aki_v1.pdf.

## Öncelik sırası

Öğrenme çıktısı + süreç bileşeni > öğrenme-öğretme uygulamalarındaki sınırlar ("kaçınılır", "sınırlı kalınır", "matematiksel hesaplamalara girmeden") > içerik çerçevesi ve anahtar kavramlar > MEB kitabı > diğer kaynaklar.

## Değişmez kurallar (özet; ayrıntısı genel kurallar dosyasında)

- Her soru ya da etkinlik hazırlanırken bir çıktıya ve bileşene göre planlanır (ör. FİZ.11.1.5.b). Soru türü çıktının fiiline uyar.
- **Çıktı kodları (FİZ.x.y.z, FBAB, SB vb.) materyallerde hiçbir zaman yazılmaz** (kullanıcı kararı, 2026-11-22): sayfada, şıklarda, cevap anahtarında ve öğretmen notunda yer almaz. Çıktıya bağlama yalnızca hazırlık sırasında, içeride yapılır.
- **Şıklı sorular 5 seçeneklidir (A, B, C, D, E)** (kullanıcı kararı, 2026-11-22). Öncüllü ve tablo şıklı sorular da buna dahildir.
- **YASAK:** boşluk doldurma; doğru-yanlış (D/Y, Evet/Hayır tabloları dahil); öğrencinin cevabı kendisinin yazdığı açık uçlu ya da kısa cevaplı soru (bunlar şıklı türe dönüştürülür, hesap sonucu da şıklardan seçilir); pekiştirme sayfası ya da çalışma yaprağı; konu anlatımı içine başlıklı alıştırma kutusu ("Kendimizi deneyelim" gibi).
- **Boş kalan yer** (konu anlatımı sayfası dahil) konuya uygun **kısa, 5 şıklı bir soruyla** doldurulur; sayfanın altı boş kalmaz. Bu soru alıştırma kutusu değildir: kutusuz, "Soru" etiketiyle (`#00AEEF`), şekilli yazılır ve cevabı sayfa altındaki açık mavi cevap şeridinde verilir (kullanıcı kararı, 2026-11-22). **Kısa bir soru sığmayacak kadar az yer kalırsa** soru yerine konuyla ilgili bir **AKTİF NOT** kutusu konur (kırmızı "AKTİF NOT" etiketi, krem zemin, turuncu gölge; bkz. tasarım şablonu 4.3) (kullanıcı kararı, 2026-11-22).
- **Bağlam düzeni:** Bağlam ayrı sayfa olmaz. Sol sütunda Örnek olarak verilir ve çözümü adım adım yapılır; sağ sütunda aynı bağlamla 2-3 soru sorulur. Konunun başında bağlam olmaz, konu anlatımından sonra doğrudan Örnek 1 başlar. Bölüm sonunda 2 bağlam olur (önce kolay ve hesapsız olan, sonra son bağlam).
- Konu anlatımı tam genişliktedir (iki sütun yok). KONU ANLATIMI / KAVRAMA BÖLÜMÜ / UYGULAMA BÖLÜMÜ bantları kullanılır.
- Temel seviye: Sayılar basit ve tam sayıdır, kolaydan zora gidilir, zor soru yoktur, örnek çözümleri ayrıntılıdır (her işlem ayrı satırda). Destekleme sadeleştirmeleri varsayılandır; zenginleştirme ana metne girmez.
- MEB 11'de olmayan konular yazılmaz: elektriksel potansiyel, potansiyel enerji, W=qV, dokunmayla yük paylaşımı. Manyetizmada yalnızca oran ("kaç B") soruları sorulur; sağ el kuralı MEB tutuşuyla verilir.
- Programdaki terimler kullanılır: "eğik atış", "yatay atış", "düşey atış" **kullanılmaz** ("serbest düşme", "iki boyutta sabit ivmeli hareket" kullanılır).
- Kavram yanılgısı doğuracak içerikten kaçınılır. Türk-İslam bilim insanları ve yerli projeler programdaki gibi kullanılır; biyografi ezberletilmez.
- Aktif Fizik kullanıcının kendi kitabıdır (kullanıcı yazarlarından biri), MEB programıyla uyumlu her şeyi aynen ya da değiştirilerek kullanılabilir. **MEB ders kitabından aynen alınmaz:** soru değiştirilir (bağlam, sayılar, kurgu) ya da benzeri özgün yazılır (kullanıcı kararı, 2026-11-22). Diğer yayınevlerinden yalnız kalıp alınır.
- Her sayısal cevap ve her yön cevabı kodla (assert) kontrol edilir.

## Çalışma şekli

- Kullanıcı istemeden yeni bölüm ya da materyal yazılmaz. Kaynak yükleme aşamasında yalnız inceleme yapılır.
- Düzeltmelerde kullanıcının söylemediği kısma ya da sütuna dokunulmaz.
- Silinen kısımlar ve eski sürümler silinmez, depoda saklanır. Her yeni sürüm yeni dosya adıyla kaydedilir (v2, v3…).
- Teslimde yalnız PDF ve sayfaların JPG görüntüleri gönderilir; düzeltmelerde yalnız değişen sayfalar. Mesaj başına en çok 6 ek.
- Tablet uyumu: Metinde ←, →, ⇒, ⇔ gibi özel işaretler kullanılmaz. Saydam PNG, SVG opaklığı, kesikli kenarlık ile yuvarlak köşe ve konturlu SVG metin kullanılmaz (beyaz zeminli JPG). Göndermeden önce PDF'te /SMask, /Group ve Type3 font olmadığı kontrol edilir.
- **Canva iş akışı (2026-11-22):** Claude görseli Canva'da çizer (Canva bağlantısı çalışıyor) ve kullanıcıya Canva bağlantısını verir; kullanıcı indirip sohbete ya da Drive'a yükler; Claude sayfaya yerleştirir. Ortamın ağı `export-download.canva.com` ve `design.canva.ai` adreslerine kapalıdır ve kullanıcı açılmasını istemedi; bu yüzden Claude Canva dosyasını kendisi indirmeye çalışmaz. Kullanıcıdan görsel beyaz zeminli JPG olarak istenir.
- Gerçekçi insan ve fotoğraf benzeri sahneler Canva'da; şekil, grafik, düzenek, araç ve kuvvet okları kodla (SVG) çizilir.
- **Kodla (SVG) insan figürü çizilmesi gerekirse** öğretmenin onayladığı tarz kullanılır (2026-10-22): çöp adam ya da çizgi film tarzı yok; gerçekçi vücut oranları, eklemlerden bükülen kol ve bacaklar, harekete uygun doğal duruş, kıyafet ve profil yüz. Kuvvetler kalın kırmızı (#d62828) oklarla temas noktasından çizilir; etiketler italik serif. Örnek: `gorseller/kutu_iten_adam.svg` (üreten betik: `gorseller/kutu_iten_adam.py`).

## Eksik rehberler (kullanıcının talimatında adı geçiyor, depoda yok)

`aktif-elektrik-sablon-analizi.md`, `meb11-elektrik-inceleme.md`, `meb11-elektrik-sekil-rehberi.md`, `meb11-destekleme-kilavuzu-analizi.md`, `meb11-zenginlestirme-kilavuzu-analizi.md`, `pisa-fen-ornek-analizi.md`, `mof-11-coulomb-analizi.md`, `orijinal-ayt-elektrostatik-analizi.md`, `345-ayt-elektrostatik-analizi.md`. Bunlar önceki oturumlarda üretilmiş ve kaybolmuş inceleme dosyalarıdır. Kaynakları (MEB 11 bölümleri, 11zengin, PISA) Drive'da duruyor; kullanıcı isterse yeniden üretilir. Aktif Fizik AYT'nin yalnız 1-50. sayfaları Drive'da (2026-11-22); elektrik bölümü yok. Diğer yayınevi kitapları Drive'da bulunamadı.
