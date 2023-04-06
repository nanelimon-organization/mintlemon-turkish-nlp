<h1 align = 'Center'>Mintlemon Türkçe Doğal Dil İşleme Kütüphanesi</h1>

|    | 
|----|
|![1](https://user-images.githubusercontent.com/83168207/229226994-d6023420-c88b-48c8-abaf-8429ce050c1f.jpg)|Türkçe Doğal Dil İşleme Kütüphanesi.|


### Gelecek Planlar

Mint & Lemon Türkçe Doğal Dil İşleme Kütüphanesi aktif olarak geliştirilmekte olup gelecek için birkaç planımız bulunmaktadır. Ana hedefimiz kütüphanenin işlevselliğini ve kullanılabilirliğini geliştirmeye devam ederken, yeni NLP İşlevleri ve uygulamalarını kapsayacak şekilde kütüphaneyi genişletmektir. Şu anda üzerinde çalıştığımız veya yakın gelecekte uygulamayı planladığımız bazı temel özellikler ve geliştirmeler şunlardır:

- **Derin öğrenme ve sinir ağı desteği:** Gelecekte kütüphaneye derin öğrenme ve sinir ağı desteği eklemeyi planlıyoruz.
- **Performans ve ölçeklenebilirlikte gelişmeler:** Özellikle büyük veri kümeleri ve yüksek hacimli kullanım durumları için kütüphanenin performans ve ölçeklenebilirliğini geliştirmek için çalışıyoruz. 
- **Dökümantasyon/Örnekler:** Yeni özellikleri ve kullanım durumlarını kapsayan dökümanları ve öğreticileri/örnekleri genişleteceğiz ve ayrıntılı açıklamalar sağlayacağız.
- **Değerlendirme ve karşılaştırma:** Gelecekte kütüphanenin performansını ve doğruluğunu ölçmek ve diğer popüler NLP kütüphaneleriyle karşılaştırmak için daha ayrıntılı değerlendirmeler ve karşılaştırmalar yapacağız.

---

### Kütüphanemiz literatürde açıklanan aşağıdaki yöntemleri içermektedir:

No | Modül | Fonksiyon | Açıklama |
| --- | --- | --- | --- |
| 0 | Sentence Splitter | `split_sentences(text: str) -> List[str]` |Türkçe metinlerde Türkçe olmayan cümle başlangıç öneklerini dikkate alarak  (Örneğin: "Dr.", "Prof." gibi kısaltmalar), bu önekler cümlelerin başında yer aldıklarında ayrı bir cümle olarak algılanmamalıdır.  Bunları dikkate alarak metni cümlelere ayırmak için kullanılır. Türkçe metinlerin doğru bir şekilde işlenmesine ve anlaşılmasına yardımcı olur. |
| 1 | Text Root DTM Vectorizer | `TextRootDTMVectorizer(dataframe: pd.DataFrame, column_name: str)` |TextRootDTMVectorizer, bir DataFrame içindeki metin verilerini belirtilen sütun ismiyle alır. Daha sonra, Zeyrek morfolojik analizörünü kullanarak Türkçe kelimelerin köklerini çıkarır ve belge-terim matrisine dönüştürür. Bu matris, her kelimenin belgedeki frekansını içerir ve makine öğrenimi algoritmalarında sıklıkla kullanılır. Örneğin, bir metin veri kümesindeki belirli bir kelimenin farklı belgelerdeki kullanım sıklığını analiz etmek istiyorsanız, bu matrisi kullanabilirsiniz. Sonuç olarak, TextRootDTMVectorizer verilen DataFrame içindeki metinleri daha uygun hale getirmek ve daha verimli bir şekilde analiz etmek için kullanılabilir. |
| 2 | Normalizer | `lower_case(text: str) -> str` | Türkçe metinleri küçük harfe dönüştürmek için kullanılır. `İ`, `I`, `Ğ`, `Ü`, `Ö`, `Ş`, `Ç` karakterlerini de doğru şekilde işler. |
| 3 | Normalizer | `remove_punctuations(text: str) -> str` | Verilen metinden noktalama işaretlerini (`!"#$%&'()*+,}{~-./:;<=>?@[\]^_` ) gibi ifadeleri kaldırır. |
| 4 | Normalizer | `remove_accent_marks(text: str) -> str` | Verilen metinden Türkçe karakterlerdeki aksan işaretlerini (`â, ô, î, ê, û, Â, Ô, Î, Ê, Û`) kaldırır. |
| 5 | Normalizer | `convert_text_numbers(text: str) -> str` | Verilen metindeki sayıları Türkçe yazıya çevirir. |
| 6 | Normalizer | `deasciify(input: List[str]) -> List[str]` | Deasciify, metindeki `ASCII` karakterlerini Türkçe karakterlere dönüştürür. Bu işlem, Türkçe metinlerin doğru bir şekilde işlenmesine ve anlaşılmasına yardımcı olur. |
| 7 | Normalizer | `normalize_turkish_chars(text: str) -> str` | Verilen metindeki Türkçe karakterleri `ASCII` karakterlere dönüştürür. |
| 8 | Normalizer | `remove_numbers(text: str) -> str` | Verilen metinden sayısal ifadeleri (tam sayılar, ondalık sayılar ve işaretli sayılar) kaldırır. |
| 9 | Normalizer | `remove_more_space(text: str) -> str` | Verilen metindeki ekstra boşlukları kaldırır. |
| 10 | Normalizer | `drop_empty_values(df, column_text) -> pd.DataFrame` | Verilen veri çerçevesinde, belirtilen sütun adı boş olan satırları kaldırır. |
| 11 | Normalizer | `remove_stopwords(text: str, stop_words_file: str = ST_WR_PATH) -> str` | Fonksiyon, verilen metindeki durak kelimelerini kaldırarak daha net ve anlamlı bir metin elde etmeyi amaçlar. Durak kelimeleri, dilbilgisi açısından önemsiz veya bir metnin anlamını etkilemeyen kelimelerdir. Örneğin, "bir", "ve", "ama", "ise", "ki" gibi sözcükler durak kelimeleridir. Bu kelimeler, bir metnin analizi veya işlenmesi sırasında genellikle göz ardı edilebilir. |



--- 

## Mint-Lemon-Turkish NLP Kütüphanesine'e Katkı Sağlama

Bu projeye doğrudan katkıda bulunmak istiyorsanız, lütfen [CONTRIBUTING](CONTRIBUTING.rst) dosyasına bir göz atın.


## Dökümantasyon & Örnekler

* [Mint & Lemon Turkish NLP Library Dökümantasyon.](https://mintlemon-turkish-nlp.readthedocs.io/en/latest/)
* Ek olarak, [ilgili klasöre](examples/) bakarak örneklerden yararlanabilirsiniz.




|    | 
|----|
|<img width="1792" alt="Ekran Resmi 2023-04-06 13 00 48" src="https://user-images.githubusercontent.com/83168207/230344345-4dfe39a3-46f4-4147-bd47-61ee9548c948.png">|



### Lisans

Bu proje [LİSANS](LICENSE) altında açık kaynaklıdır.

-   Lütfen dikkat edin, bu proje "olduğu gibi" sunulmaktadır ve hiçbir garanti verilmez. (Bu yazılımın kullanımı lisans sözleşmesinin şartlarına tabidir.) Bu yazılım Apache 2.0 lisansı altında lisanslanmıştır. [LİSANS](LICENSE) sayfasına bakın.

### Referanslar

* [Koehn, P. ve Schroeder, J. (n.d.)](https://github.com/mediacloud/sentence-splitter). 
* ["Türkçe Deasciification Yöntemleri Üzerine Karşılaştırmalı Bir Çalışma"](https://www.sciencedirect.com/science/article/pii/S221509862200101X), Türkçe Deasciification için çeşitli yöntemlerin karşılaştırmasını sunan bir bilimsel makale.
* [Python ile örnek Türkçe Deasciifier Uygulaması.](https://github.com/aysnrgenc/TurkishDeasciifier)
* [Bu dizinde bir istatistiksel modele dayalı Python'da bir Türkçe Deasciifier uygulaması bulunmaktadır.](https://github.com/emres/turkish-deasciifier)
* [Turkish Language Repository ~ TDD.](https://tdd.ai)
