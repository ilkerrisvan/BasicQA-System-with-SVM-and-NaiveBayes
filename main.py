import input_stemmer as ins
import naivebayesian_question_based as nb_qb
import naivebayesian_answer_based as nb_ab
import svm_question_based as svm_qb
import svm_answer_based as svm_ab
import time

input_mode = int(input("(0)NaiveBayes vs SVM Result\n(1)I want ask a question.\n"))

if input_mode == 0:
    print("Which result would you like to see?")
    time.sleep(2)
    ml_mode = int(input("(0)Question Based Naive Bayes\n(1)Answer Based Naive Bayes\n(2)Question Based SVM\n(3)Answer Based SVM\n(4)ALL\n"))


    if ml_mode == 0:
        data_path = input("Please enter data path(data.json).\n")
        train_path = input("Please enter train path(train_data.json)\n")
        test_path = input("Please enter test path(test_data.json)\n")
        nb_qb.run(data_path,train_path,test_path)

    if ml_mode == 1:
        data_path = input("Please enter data path(data.json).\n")
        train_path = input("Please enter train path(train_data.json)\n")
        test_path = input("Please enter test path(test_data.json)\n")
        nb_ab.run(data_path,train_path,test_path)

    if ml_mode == 2:
        svm_question_based_path = input("Please enter svm question based datas path path(svm_question_based.json)\n")
        test_path = input("Please enter test path(test_data.json)\n")
        svm_qb.run(svm_question_based_path,test_path)

    if ml_mode == 3 :
        svm_answer_based_path = input("Please enter svm answer based datas path path(svm_answer_based.json)\n")
        test_path = input("Please enter test path(test_data.json)\n")
        svm_ab.run(svm_answer_based_path, test_path)

    if ml_mode == 4:
        data_path = input("Please enter data path(data.json).\n")
        train_path = input("Please enter train path(train_data.json)\n")
        test_path = input("Please enter test path(test_data.json)\n")
        svm_question_based_path = input("Please enter svm question based datas path path(svm_question_based.json)\n")
        svm_answer_based_path = input("Please enter svm answer based datas path path(svm_answer_based.json)\n")
        nb_qb.run(data_path, train_path, test_path)
        nb_ab.run(data_path, train_path, test_path)
        svm_qb.run(svm_question_based_path, test_path)
        svm_ab.run(svm_answer_based_path, test_path)

if input_mode == 1:
    print("First choose method that generete the answer.")
    ml_mode = int(input("(0)Question Based Naive Bayes.\n(1)Answer Based Naive Bayes.\n(2)Question Based SVM.\n(3)Answer Based SVM.\n"))


    if ml_mode == 0:
       data_path = input("Please enter data path(data.json).\n")
       data = ins.run()
       train_path = input("Please enter train path(train_data.json)\n")
       a = nb_qb.nb(data_path,train_path,data)
       print(a[0])

    if ml_mode == 1:
       data_path = input("Please enter data path(data.json).\n")
       data = ins.run()
       train_path = input("Please enter train path(train_data.json)\n")
       a = nb_ab.nb(data_path,train_path,data)
       print(a[0])

    if ml_mode == 2:
       data = ins.run_for_svm()
       svm_question_based_path = input("Please enter svm question based datas path path(svm_question_based.json)\n")

       if svm_ab.svm(svm_question_based_path,data)[0][0] == 0:
           print("Bir öğrenci, kayıtlı olduğu programın müfredatında bulunan tüm dersleri başarıyla tamamladığında(Lisans için 240 AKTS) genel not ortalaması 2,00 veya daha yüksek ise ve tarafına tahakkuk ettirilmiş bulunan eğitim-öğretim ücretinin ve diğer ücretlerin tamamını ödemişse, mezun olmaya ve lisans veya ön lisans diploması almaya hak kazanır. Öğrencinin diplomasını alabilmesi için eğitim-öğretim ücretinin tamamını ödemiş olması şarttır. Genel not ortalaması 3,00 - 3,49 olanlar onur, 3,50 ve üstü olanlar yüksek onur öğrencisi olarak mezun olurlar.")
       if svm_ab.svm(svm_question_based_path,data)[0][0] == 1:
           print("Program müfredatında bulunan bir dersten bir yarıyılda F, FX, FZ veya U notlarından birini alan öğrenciler bu dersleri takip eden iki yarıyıl içerisinde tekrar almak zorundadır. Birinci sınıf İngilizce derslerinde başarılı olamayan öğrencilerin, ilgili dersi verildiği ilk yarıyılda almaları zorunludur.")
       if svm_ab.svm(svm_question_based_path,data)[0][0] == 2:
           print("Bir öğrencinin bir dönemde alabileceği azami ders yükü 42 AKTS'dir. Öğrenciler 36 AKTS’ye kadar ders seçebilir. 37-42 AKTS ders alabilmek için danışman onayı, 43 AKTS ve daha fazlası için fakülte yönetim kurulu kararı gerekir.")
       if svm_ab.svm(svm_question_based_path,data)[0][0] == 3:
           print("Öğrenciler, Yükseköğretim Kurulunun belirlediği esaslar doğrultusunda derslere %70, laboratuvar ve atölye gibi bağımsız uygulamalı dersler %80 ve İngilizce Hazırlık Programına %90 oranında devam etmek, yarıyıl/akademik yıl içinde her türlü sınava ve dersi veren öğretim elemanının öngördüğü diğer çalışmalara katılmakla yükümlüdürler.Öğrencilerin devamları ile ilgili kurallar öğretim elemanı tarafından ders öğretim planına konarak yarıyıl/akademik yıl başında ilan edilir ve öğrencilerin devamları bu kurallara göre izlenir. Sağlık raporuyla belgelenmiş sağlık sorunları ve disiplin cezasıyla uzaklaştırma dahil, hangi gerekçeyle olursa olsun, bir dersin devam yükümlülüğünü yerine getirmeyen öğrenci, o dersten başarısız sayılır. Bu öğrenciler yarıyıl/akademik yılsonu ve bütünleme sınavına giremezler ve yarıyıl/akademik yıl sonu notları FZ olarak değerlendirilir.Aynı kurallar yandal ve çift anadal programları için de geçerlidir.")
       if svm_ab.svm(svm_question_based_path,data)[0][0] == 4:
           print("Dersten çekilme tarihleri ilgili dönem akademik takviminde belirtilir.Öğrenciler akademik takvimde belirtilen son başvuru tarihine kadar kayıtlı bulundukları bir dersten akademik danışmanlarının bilgisi dâhilinde çekilebilirler.Öğrenciler, akademik öğrenimleri süresince en fazla 6 dersten ve bir dönemde en fazla 2 dersten çekilebilirler.")
       if svm_ab.svm(svm_question_based_path,data)[0][0] == 5:
           print("FZ: Final sınavına girme hakkı elde edemeyen öğrencilere final sınavları öncesinde akademik takvimde belirtilen tarihler içinde FZ notu verilir.FX: Final sınavına girme hakkı olduğu halde geçerli mazereti olmaksızın final sınavına gelmeyen öğrencilere ve bütünleme sınavı başvurusu olduğu halde bu sınava gelmeyen öğrencilere verilir.W: Öğrencinin dersten çekildiği durumlarda verilir. Alınan derse not çizelgesinde yer verilmekle birlikte, W notu ortalama hesaplarına katılmaz. Daha önceki bir yarıyılda almış olduğu bir dersi, tekrar alıp sonra bu dersten çekilen öğrencilerin genel not ortalaması hesaplanırken daha önce aldıkları not geçerli sayılır. I: Final sınavı bulunmayan bir derste, harf notu takdir edilebilmesi için gereken çalışmaları zorunlu nedenlerle tamamlayamamış öğrencilere eksiklerini gidermek için süre tanımak amacıyla I notu verilebilir. Bu durumdaki bir öğrencinin, hangisi daha yakın bir tarihteyse, harf notlarının ilan edildiği tarihten itibaren en geç 14 gün içinde veya bir sonraki yarıyılın ders kayıtları başlayana kadar, eksiklerini tamamlaması gereklidir. Dersi veren öğretim elemanının başvurusu ve bölüm başkanının onayıyla bir sonraki yarıyılın ders kayıtları başlayana kadar ek süre verilebilir. Verilen sürede eksiklerini tamamlayan öğrenciye ilgili öğretim elemanı tarafından bir harf notu takdir edilir. Verilen süre bittiğinde I’dan farklı bir harf notu verilmemiş öğrencilere FX notu işlenir.S: Belirtilmiş derslerde başarılı bulunan öğrencilere verilir. Bu not, ortalama hesaplarına katılmaz.U: Belirtilmiş derslerde başarısız öğrencilere verilir. Bu not, ortalama hesaplarına katılmaz.P: Bir yarıyıldan çok süren kredili ya da kredisiz derslerde, son yarıyıldan önceki yarıyıllar sonunda verilir. Bu not, ortalama hesaplarına katılmaz.EX: Öğrencinin önceden başarılı olduğu bir ders, öğrencinin transkriptine işlenirken, programındaki mezuniyet koşulu dersten muaf tutulmasını işaret eder. Bu not, ortalama hesaplarına katılmaz.")
       if svm_ab.svm(svm_question_based_path,data)[0][0] == 6:
           print("Ara sınav notlarına itirazı olan öğrenci, dersin bağlı bulunduğu dekanlık veya bölüm başkanlığına notların ilan edilmesini izleyen üç iş günü içinde yazılı olarak başvuruda bulunur. Öğrencinin itirazı üzerine ara sınav kağıdı dersin öğretim elemanı tarafından maddi hata açısından tekrar incelenir. Bu itiraz, bölüm başkanlığınca gerekli görüldüğü takdirde, biri dersin öğretim elemanı olmak üzere, oluşturulan üç kişilik bir komisyon tarafından, maddi bir hatanın olup olmadığı açısından incelenir. Sonuç, yazılı olarak bölüm başkanlığına rapor edilir. Bölüm başkanlığı, sonucu öğrenciye bildirir.Yarıyıl/yılsonu ve bütünleme sınavı sonunda ders başarı notlarına itirazı olan öğrenci, notların ilanını takip eden üç iş günü içinde dersin bağlı bulunduğu dekanlığa veya müdürlüğe yazılı olarak başvuruda bulunur. Öğrencinin başvurusu, biri dersin öğretim elemanı olmak üzere, fakülte yönetim kurulunca oluşturulan, üç kişilik bir komisyon tarafından maddi bir hatanın olup olmadığı açısından incelenir, sonuç yazılı olarak, dekanlığa veya müdürlüğe bildirilir. Dekanlık/müdürlük sonucu öğrenciye duyurur ve başarı notunda bir değişiklik varsa, sonuç Öğrenci İşleri Direktörlüğüne de bildirilir.Tüm itirazlara rağmen notu değişmeyen öğrenci, itirazının değerlendirilmesi için Rektörlüğe başvurabilir. Üniversite Yönetim Kurulu gerekli gördüğü takdirde, dersi veren öğretim elemanı dışında bir jüri kurarak öğrencinin itirazını değerlendirir.")
       if svm_ab.svm(svm_question_based_path,data)[0][0] == 7:
           print("Bir yarıyıl sonunda, genel not ortalaması 1,80’den düşük olan öğrenciler gözetim öğrencisi sayılırlar.Bir yarıyıl sonunda, genel not ortalaması 2,00 ve üzerindeki öğrenciler başarılı sayılırlar.Akademik danışmanı, gözetim durumundaki öğrencinin başarılı duruma geçmesi için gerekli tedbirleri alır.Gözetim durumundaki öğrenciler, önceki yarıyıllarda C-, D+ veya D notu aldıkları derslerden istediklerini tekrarlayabilirler.")
       if svm_ab.svm(svm_question_based_path,data)[0][0] == 8:
           print("İlan edilmiş çift anadal programına,anadal lisans programının en erken üçüncü, en geç beşinci yarıyılın başında başvurabilir.Başvuru sırasında genel not ortalaması en az 2.72/4.00 olan, ancak anadal lisans programının ilgili sınıfında başarı sıralaması itibariyle en üst % 20 de bulunmayan öğrenciler, çift anadal yapılacak programın ilgili yıldaki taban puanı ya da üstü bir puana sahip ise, çift anadal programına başvurabilirler.")
       if svm_ab.svm(svm_question_based_path,data)[0][0] == 9:
           print("Dr. İbrahim Arıkan üstün başarı bursu: Hazırlık Programı dışında; lisans bölümlerinde okuyan öğrenciler için geçerlidir. Üstün Başarı Bursları her yıl bahar yarıyılı bitiminde (Temmuz ayında) belirlenir ve Eylül ayından itibaren bir takvim yılı için geçerli olur.Bir öğrencinin üstün başarı bursu alabilmesi için 1. ve 2. lisans yarıyılları sonunda (Güz, Bahar) 60 AKTS’yi, 3. ve 4. lisans yarıyılları sonunda 120 AKTS’yi,5. ve 6. lisans yarıyılları sonunda 180 AKTS’yi tamamlamış olması gerekmektedir.Bir öğrencinin üstün başarı bursu alabilmesi için, ilgili yılın tüm derslerinden başarılı olması ve ilgili yılın Güz ve Bahar dönemi ders yükü toplamının 60 AKTS olması gerekmektedir. 60 AKTS’ nin tamamlanmasında sadece yaz staj kredileri eksik olabilir.Not ortalamalarına göre dağılım şöyledir:3.75 ve üzerinde olan öğrenciler, bir yıl sonraki eğitim öğretim ücretinin %50’sinden, 3.60-3.74 olan öğrenciler %40'ından, 3.50-3.59 olan ögrenciler ise %25'inden muaf olur.")

    if ml_mode == 3:
       data = ins.run_for_svm()
       svm_answer_based_path = input("Please enter svm answer based datas path path(svm_answer_based.json)\n")

       if svm_ab.svm(svm_answer_based_path, data)[0][0] == 0 :
           print("Bir öğrenci, kayıtlı olduğu programın müfredatında bulunan tüm dersleri başarıyla tamamladığında(Lisans için 240 AKTS) genel not ortalaması 2,00 veya daha yüksek ise ve tarafına tahakkuk ettirilmiş bulunan eğitim-öğretim ücretinin ve diğer ücretlerin tamamını ödemişse, mezun olmaya ve lisans veya ön lisans diploması almaya hak kazanır. Öğrencinin diplomasını alabilmesi için eğitim-öğretim ücretinin tamamını ödemiş olması şarttır. Genel not ortalaması 3,00 - 3,49 olanlar onur, 3,50 ve üstü olanlar yüksek onur öğrencisi olarak mezun olurlar.")
       if svm_ab.svm(svm_answer_based_path, data)[0][0] == 1 :
           print("Program müfredatında bulunan bir dersten bir yarıyılda F, FX, FZ veya U notlarından birini alan öğrenciler bu dersleri takip eden iki yarıyıl içerisinde tekrar almak zorundadır. Birinci sınıf İngilizce derslerinde başarılı olamayan öğrencilerin, ilgili dersi verildiği ilk yarıyılda almaları zorunludur.")
       if svm_ab.svm(svm_answer_based_path, data)[0][0] == 2 :
           print("Bir öğrencinin bir dönemde alabileceği azami ders yükü 42 AKTS'dir. Öğrenciler 36 AKTS’ye kadar ders seçebilir. 37-42 AKTS ders alabilmek için danışman onayı, 43 AKTS ve daha fazlası için fakülte yönetim kurulu kararı gerekir.")
       if svm_ab.svm(svm_answer_based_path, data)[0][0] == 3 :
           print("Öğrenciler, Yükseköğretim Kurulunun belirlediği esaslar doğrultusunda derslere %70, laboratuvar ve atölye gibi bağımsız uygulamalı dersler %80 ve İngilizce Hazırlık Programına %90 oranında devam etmek, yarıyıl/akademik yıl içinde her türlü sınava ve dersi veren öğretim elemanının öngördüğü diğer çalışmalara katılmakla yükümlüdürler.Öğrencilerin devamları ile ilgili kurallar öğretim elemanı tarafından ders öğretim planına konarak yarıyıl/akademik yıl başında ilan edilir ve öğrencilerin devamları bu kurallara göre izlenir. Sağlık raporuyla belgelenmiş sağlık sorunları ve disiplin cezasıyla uzaklaştırma dahil, hangi gerekçeyle olursa olsun, bir dersin devam yükümlülüğünü yerine getirmeyen öğrenci, o dersten başarısız sayılır. Bu öğrenciler yarıyıl/akademik yılsonu ve bütünleme sınavına giremezler ve yarıyıl/akademik yıl sonu notları FZ olarak değerlendirilir.Aynı kurallar yandal ve çift anadal programları için de geçerlidir.")
       if svm_ab.svm(svm_answer_based_path, data)[0][0] == 4 :
           print("Dersten çekilme tarihleri ilgili dönem akademik takviminde belirtilir.Öğrenciler akademik takvimde belirtilen son başvuru tarihine kadar kayıtlı bulundukları bir dersten akademik danışmanlarının bilgisi dâhilinde çekilebilirler.Öğrenciler, akademik öğrenimleri süresince en fazla 6 dersten ve bir dönemde en fazla 2 dersten çekilebilirler.")
       if svm_ab.svm(svm_answer_based_path, data)[0][0] == 5 :
           print("FZ: Final sınavına girme hakkı elde edemeyen öğrencilere final sınavları öncesinde akademik takvimde belirtilen tarihler içinde FZ notu verilir.FX: Final sınavına girme hakkı olduğu halde geçerli mazereti olmaksızın final sınavına gelmeyen öğrencilere ve bütünleme sınavı başvurusu olduğu halde bu sınava gelmeyen öğrencilere verilir.W: Öğrencinin dersten çekildiği durumlarda verilir. Alınan derse not çizelgesinde yer verilmekle birlikte, W notu ortalama hesaplarına katılmaz. Daha önceki bir yarıyılda almış olduğu bir dersi, tekrar alıp sonra bu dersten çekilen öğrencilerin genel not ortalaması hesaplanırken daha önce aldıkları not geçerli sayılır. I: Final sınavı bulunmayan bir derste, harf notu takdir edilebilmesi için gereken çalışmaları zorunlu nedenlerle tamamlayamamış öğrencilere eksiklerini gidermek için süre tanımak amacıyla I notu verilebilir. Bu durumdaki bir öğrencinin, hangisi daha yakın bir tarihteyse, harf notlarının ilan edildiği tarihten itibaren en geç 14 gün içinde veya bir sonraki yarıyılın ders kayıtları başlayana kadar, eksiklerini tamamlaması gereklidir. Dersi veren öğretim elemanının başvurusu ve bölüm başkanının onayıyla bir sonraki yarıyılın ders kayıtları başlayana kadar ek süre verilebilir. Verilen sürede eksiklerini tamamlayan öğrenciye ilgili öğretim elemanı tarafından bir harf notu takdir edilir. Verilen süre bittiğinde I’dan farklı bir harf notu verilmemiş öğrencilere FX notu işlenir.S: Belirtilmiş derslerde başarılı bulunan öğrencilere verilir. Bu not, ortalama hesaplarına katılmaz.U: Belirtilmiş derslerde başarısız öğrencilere verilir. Bu not, ortalama hesaplarına katılmaz.P: Bir yarıyıldan çok süren kredili ya da kredisiz derslerde, son yarıyıldan önceki yarıyıllar sonunda verilir. Bu not, ortalama hesaplarına katılmaz.EX: Öğrencinin önceden başarılı olduğu bir ders, öğrencinin transkriptine işlenirken, programındaki mezuniyet koşulu dersten muaf tutulmasını işaret eder. Bu not, ortalama hesaplarına katılmaz.")
       if svm_ab.svm(svm_answer_based_path, data)[0][0] == 6 :
           print("Ara sınav notlarına itirazı olan öğrenci, dersin bağlı bulunduğu dekanlık veya bölüm başkanlığına notların ilan edilmesini izleyen üç iş günü içinde yazılı olarak başvuruda bulunur. Öğrencinin itirazı üzerine ara sınav kağıdı dersin öğretim elemanı tarafından maddi hata açısından tekrar incelenir. Bu itiraz, bölüm başkanlığınca gerekli görüldüğü takdirde, biri dersin öğretim elemanı olmak üzere, oluşturulan üç kişilik bir komisyon tarafından, maddi bir hatanın olup olmadığı açısından incelenir. Sonuç, yazılı olarak bölüm başkanlığına rapor edilir. Bölüm başkanlığı, sonucu öğrenciye bildirir.Yarıyıl/yılsonu ve bütünleme sınavı sonunda ders başarı notlarına itirazı olan öğrenci, notların ilanını takip eden üç iş günü içinde dersin bağlı bulunduğu dekanlığa veya müdürlüğe yazılı olarak başvuruda bulunur. Öğrencinin başvurusu, biri dersin öğretim elemanı olmak üzere, fakülte yönetim kurulunca oluşturulan, üç kişilik bir komisyon tarafından maddi bir hatanın olup olmadığı açısından incelenir, sonuç yazılı olarak, dekanlığa veya müdürlüğe bildirilir. Dekanlık/müdürlük sonucu öğrenciye duyurur ve başarı notunda bir değişiklik varsa, sonuç Öğrenci İşleri Direktörlüğüne de bildirilir.Tüm itirazlara rağmen notu değişmeyen öğrenci, itirazının değerlendirilmesi için Rektörlüğe başvurabilir. Üniversite Yönetim Kurulu gerekli gördüğü takdirde, dersi veren öğretim elemanı dışında bir jüri kurarak öğrencinin itirazını değerlendirir.")
       if svm_ab.svm(svm_answer_based_path, data)[0][0] == 7 :
           print("Bir yarıyıl sonunda, genel not ortalaması 1,80’den düşük olan öğrenciler gözetim öğrencisi sayılırlar.Bir yarıyıl sonunda, genel not ortalaması 2,00 ve üzerindeki öğrenciler başarılı sayılırlar.Akademik danışmanı, gözetim durumundaki öğrencinin başarılı duruma geçmesi için gerekli tedbirleri alır.Gözetim durumundaki öğrenciler, önceki yarıyıllarda C-, D+ veya D notu aldıkları derslerden istediklerini tekrarlayabilirler.")
       if svm_ab.svm(svm_answer_based_path, data)[0][0] == 8 :
           print("İlan edilmiş çift anadal programına,anadal lisans programının en erken üçüncü, en geç beşinci yarıyılın başında başvurabilir.Başvuru sırasında genel not ortalaması en az 2.72/4.00 olan, ancak anadal lisans programının ilgili sınıfında başarı sıralaması itibariyle en üst % 20 de bulunmayan öğrenciler, çift anadal yapılacak programın ilgili yıldaki taban puanı ya da üstü bir puana sahip ise, çift anadal programına başvurabilirler.")
       if svm_ab.svm(svm_answer_based_path, data)[0][0] == 9 :
           print("Dr. İbrahim Arıkan üstün başarı bursu: Hazırlık Programı dışında; lisans bölümlerinde okuyan öğrenciler için geçerlidir. Üstün Başarı Bursları her yıl bahar yarıyılı bitiminde (Temmuz ayında) belirlenir ve Eylül ayından itibaren bir takvim yılı için geçerli olur.Bir öğrencinin üstün başarı bursu alabilmesi için 1. ve 2. lisans yarıyılları sonunda (Güz, Bahar) 60 AKTS’yi, 3. ve 4. lisans yarıyılları sonunda 120 AKTS’yi,5. ve 6. lisans yarıyılları sonunda 180 AKTS’yi tamamlamış olması gerekmektedir.Bir öğrencinin üstün başarı bursu alabilmesi için, ilgili yılın tüm derslerinden başarılı olması ve ilgili yılın Güz ve Bahar dönemi ders yükü toplamının 60 AKTS olması gerekmektedir. 60 AKTS’ nin tamamlanmasında sadece yaz staj kredileri eksik olabilir.Not ortalamalarına göre dağılım şöyledir:3.75 ve üzerinde olan öğrenciler, bir yıl sonraki eğitim öğretim ücretinin %50’sinden, 3.60-3.74 olan öğrenciler %40'ından, 3.50-3.59 olan ögrenciler ise %25'inden muaf olur.")
