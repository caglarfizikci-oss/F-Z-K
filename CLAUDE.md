# F-Z-K: Lise Fizik Materyalleri (Çalışma Kuralları)

Kullanıcı lise fizik öğretmenidir. Kullanıcıyla **Türkçe** ve lise öğrencisinin anlayacağı **sade bir dille** konuşulur.

## Her soru, konu anlatımı ya da materyal hazırlığından ÖNCE okunacak dosyalar

1. `soru-yazim/tymm-2026-fizik-programi-genel-kurallar.md`: **ANA ŞABLON.** TYMM 2026 programının genel esasları, öncelik sırası, çıktı fiili ile soru türü eşlemesi, ünite ünite kritik sınırlar ve kullanıcının bütün materyal kuralları burada.
2. `soru-yazim/tymm-2026-fizik-ciktilar-tum-siniflar.md`: 9-12. sınıfların 106 öğrenme çıktısı, süreç bileşenleri ve çıktı bazındaki "kaçınılır" / "sınırlı kalınır" notları (programdan birebir).
3. `soru-yazim/tymm-baglam-temelli-soru-yazim-kurallari.md`: MEB bağlam temelli soru yazım kılavuzunun kuralları ve bizim sayfa düzenimize uyarlanışı.

Kaynak belgeler `soru-yazim/kaynak/` klasöründedir: `Fizikprg.pdf` (program), bağlam kılavuzunun Ocak 2026 baskısı (`Tymm-1-50`, `Tymm-51-100`, `Tymm-101-138`) ve Mart 2026 web kopyası ile bunların metinleri. Kullanıcının Drive'ında bunlar da var: Tymm.pdf (kılavuzun tamamı, 24 MB; parçalı hali Tymm-1-50/51-100/101-138), 11meb kitap bölümleri (kuvvet, indüksiyon, transformatör), 11zengin.pdf, PISA örnek soruları, AYT çıkmış sorular, Fizikeskikazanımeski.pdf, Manyetik_Aki_v1.pdf.

## Öncelik sırası

Öğrenme çıktısı + süreç bileşeni > öğrenme-öğretme uygulamalarındaki sınırlar ("kaçınılır", "sınırlı kalınır", "matematiksel hesaplamalara girmeden") > içerik çerçevesi ve anahtar kavramlar > MEB kitabı > diğer kaynaklar.

## Değişmez kurallar (özet; ayrıntısı genel kurallar dosyasında)

- Her soru ya da etkinlik bir çıktı koduna ve bileşene bağlanır (ör. FİZ.11.1.5.b). Soru türü çıktının fiiline uyar.
- **Şıklı sorular 5 seçeneklidir (A, B, C, D, E)** (kullanıcı kararı, 2026-11-22). Öncüllü ve tablo şıklı sorular da buna dahildir.
- **YASAK:** boşluk doldurma; doğru-yanlış (D/Y, Evet/Hayır tabloları dahil); öğrencinin cevabı kendisinin yazdığı açık uçlu ya da kısa cevaplı soru (bunlar şıklı türe dönüştürülür, hesap sonucu da şıklardan seçilir); pekiştirme sayfası ya da çalışma yaprağı.
- **Bağlam düzeni:** Bağlam ayrı sayfa olmaz. Sol sütunda Örnek olarak verilir ve çözümü adım adım yapılır; sağ sütunda aynı bağlamla 2-3 soru sorulur. Konunun başında bağlam olmaz, konu anlatımından sonra doğrudan Örnek 1 başlar. Bölüm sonunda 2 bağlam olur (önce kolay ve hesapsız olan, sonra son bağlam).
- Konu anlatımı tam genişliktedir (iki sütun yok). KONU ANLATIMI / KAVRAMA BÖLÜMÜ / UYGULAMA BÖLÜMÜ bantları kullanılır.
- Temel seviye: Sayılar basit ve tam sayıdır, kolaydan zora gidilir, zor soru yoktur, örnek çözümleri ayrıntılıdır (her işlem ayrı satırda). Destekleme sadeleştirmeleri varsayılandır; zenginleştirme ana metne girmez.
- MEB 11'de olmayan konular yazılmaz: elektriksel potansiyel, potansiyel enerji, W=qV, dokunmayla yük paylaşımı. Manyetizmada yalnızca oran ("kaç B") soruları sorulur; sağ el kuralı MEB tutuşuyla verilir.
- Programdaki terimler kullanılır: "eğik atış", "yatay atış", "düşey atış" **kullanılmaz** ("serbest düşme", "iki boyutta sabit ivmeli hareket" kullanılır).
- Kavram yanılgısı doğuracak içerikten kaçınılır. Türk-İslam bilim insanları ve yerli projeler programdaki gibi kullanılır; biyografi ezberletilmez.
- Aktif Fizik kullanıcının kendi kitabıdır, doğrudan kullanılabilir. Diğer yayınevlerinden yalnız kalıp alınır.
- Her sayısal cevap ve her yön cevabı kodla (assert) kontrol edilir.

## Çalışma şekli

- Kullanıcı istemeden yeni bölüm ya da materyal yazılmaz. Kaynak yükleme aşamasında yalnız inceleme yapılır.
- Düzeltmelerde kullanıcının söylemediği kısma ya da sütuna dokunulmaz.
- Silinen kısımlar ve eski sürümler silinmez, depoda saklanır. Her yeni sürüm yeni dosya adıyla kaydedilir (v2, v3…).
- Teslimde yalnız PDF ve sayfaların JPG görüntüleri gönderilir; düzeltmelerde yalnız değişen sayfalar. Mesaj başına en çok 6 ek.
- Tablet uyumu: Metinde ←, →, ⇒, ⇔ gibi özel işaretler kullanılmaz. Saydam PNG, SVG opaklığı, kesikli kenarlık ile yuvarlak köşe ve konturlu SVG metin kullanılmaz (beyaz zeminli JPG). Göndermeden önce PDF'te /SMask, /Group ve Type3 font olmadığı kontrol edilir.
- Canva görselleri ortamdan indirilemez: kullanıcı Canva'da üretip yükler, Claude yerleştirir.

## Eksik rehberler (kullanıcının talimatında adı geçiyor, depoda yok)

`stil-rehberi-aktif-ayt.md`, `aktif-elektrik-sablon-analizi.md`, `meb11-elektrik-inceleme.md`, `meb11-elektrik-sekil-rehberi.md`, `meb11-destekleme-kilavuzu-analizi.md`, `meb11-zenginlestirme-kilavuzu-analizi.md`, `pisa-fen-ornek-analizi.md`, `mof-11-coulomb-analizi.md`, `orijinal-ayt-elektrostatik-analizi.md`, `345-ayt-elektrostatik-analizi.md`. Bunlar önceki oturumlarda üretilmiş ve kaybolmuş inceleme dosyalarıdır. Kaynakları (MEB 11 bölümleri, 11zengin, PISA) Drive'da duruyor; kullanıcı isterse yeniden üretilir. Aktif Fizik ve yayınevi kitapları Drive'da bulunamadı.
