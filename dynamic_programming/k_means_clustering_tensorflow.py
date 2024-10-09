from random import shuffle

import tensorflow as tf
from numpy import array


def tf_k_means_cluster(vectors, noofclusters):
    """
    TensorFlow kullanarak K-Means Kümeleme.
    'vectors' n*k boyutunda bir 2-D NumPy dizisi olmalıdır, burada n,
    k boyutundaki vektörlerin sayısıdır.
    'noofclusters' bir tamsayı olmalıdır.
    """

    noofclusters = int(noofclusters)
    assert noofclusters < len(vectors)

    # Boyutu öğren
    dim = len(vectors[0])

    # Mevcut vektörlerden rastgele merkezler seçmeye yardımcı olacak
    vector_indices = list(range(len(vectors)))
    shuffle(vector_indices)

    # HESAPLAMA GRAFI
    # Bu algoritmanın her çalıştırılmasında yeni bir grafik başlatır ve
    # varsayılan olarak ayarlar. Bu, bu fonksiyonun birden çok kez çağrılması
    # durumunda, varsayılan grafiğin önceki fonksiyon çağrılarından kullanılmayan
    # işlemler ve Değişkenlerle dolup taşmamasını sağlar.

    graph = tf.Graph()

    with graph.as_default():
        # HESAPLAMA OTURUMU

        sess = tf.Session()

        ##HESAPLAMA ELEMANLARININ OLUŞTURULMASI

        ##Öncelikle, her merkez için bir Değişken vektörümüz olduğundan emin olalım,
        ##mevcut veri noktalarından birine başlatılmış
        centroids = [
            tf.Variable(vectors[vector_indices[i]]) for i in range(noofclusters)
        ]
        ##Bu düğümler, merkez Değişkenlerine uygun değerleri atayacak
        centroid_value = tf.placeholder("float64", [dim])
        cent_assigns = []
        for centroid in centroids:
            cent_assigns.append(tf.assign(centroid, centroid_value))

        ##Bireysel vektörlerin küme atamaları için değişkenler (ilk başta 0'a
        ##başlatılmış)
        assignments = [tf.Variable(0) for i in range(len(vectors))]
        ##Bu düğümler, bir atama Değişkenine uygun değeri atayacak
        assignment_value = tf.placeholder("int32")
        cluster_assigns = []
        for assignment in assignments:
            cluster_assigns.append(tf.assign(assignment, assignment_value))

        ##Şimdi ortalamayı hesaplayacak düğümü oluşturalım
        # Giriş için yer tutucu
        mean_input = tf.placeholder("float", [None, dim])
        # Düğüm/op girişi alır ve 0. boyut boyunca bir ortalama hesaplar,
        # yani giriş vektörlerinin listesi
        mean_op = tf.reduce_mean(mean_input, 0)

        ##Öklid mesafelerini hesaplama düğümü
        # Giriş için yer tutucular
        v1 = tf.placeholder("float", [dim])
        v2 = tf.placeholder("float", [dim])
        euclid_dist = tf.sqrt(tf.reduce_sum(tf.pow(tf.subtract(v1, v2), 2)))

        ##Bu düğüm, bir vektörü hangi kümeye atayacağını, vektörün merkezlerden
        ##Öklid mesafelerine dayanarak belirleyecek.
        # Giriş için yer tutucu
        centroid_distances = tf.placeholder("float", [noofclusters])
        cluster_assignment = tf.argmin(centroid_distances, 0)

        ##DURUM DEĞİŞKENLERİNİN BAŞLATILMASI

        ##Bu, grafiğe göre tanımlanan tüm Değişkenlerin başlatılmasına yardımcı
        ##olacaktır. Değişken başlatıcı, tüm Değişkenler oluşturulduktan sonra
        ##tanımlanmalıdır, böylece her biri başlatmaya dahil edilir.
        init_op = tf.initialize_all_variables()

        # Tüm değişkenleri başlat
        sess.run(init_op)

        ##KÜMELEME İTERASYONLARI

        # Şimdi K-Means kümeleme iterasyonlarının Beklenti-Maksimizasyon adımlarını
        # gerçekleştirin. İşleri basit tutmak için, bir Durdurma Kriteri kullanmak
        # yerine yalnızca belirli sayıda iterasyon yapacağız.
        noofiterations = 100
        for _ in range(noofiterations):
            ##BEKLENTİ ADIMI
            ##Son iterasyona kadar olan merkez konumlarına dayanarak, beklenen
            ##merkez atamalarını hesaplayın.
            # Her vektör üzerinde yineleme yap
            for vector_n in range(len(vectors)):
                vect = vectors[vector_n]
                # Bu vektör ile her merkez arasındaki Öklid mesafesini hesapla.
                # Bu listenin 'centroid_distances' olarak adlandırılamayacağını
                # unutmayın, çünkü bu, küme atama düğümüne giriştir.
                distances = [
                    sess.run(euclid_dist, feed_dict={v1: vect, v2: sess.run(centroid)})
                    for centroid in centroids
                ]
                # Şimdi küme atama düğümünü, mesafeleri girdi olarak kullanarak
                # çalıştır
                assignment = sess.run(
                    cluster_assignment, feed_dict={centroid_distances: distances}
                )
                # Şimdi değeri uygun durum değişkenine ata
                sess.run(
                    cluster_assigns[vector_n], feed_dict={assignment_value: assignment}
                )

            ##MAKSİMİZASYON ADIMI
            # Beklenti Adımından hesaplanan beklenen duruma dayanarak, merkezlerin
            # konumlarını, küme içi Kareler Toplamını en aza indirme genel amacını
            # en üst düzeye çıkarmak için hesaplayın
            for cluster_n in range(noofclusters):
                # Bu kümeye atanan tüm vektörleri topla
                assigned_vects = [
                    vectors[i]
                    for i in range(len(vectors))
                    if sess.run(assignments[i]) == cluster_n
                ]
                # Yeni merkez konumunu hesapla
                new_location = sess.run(
                    mean_op, feed_dict={mean_input: array(assigned_vects)}
                )
                # Uygun değişkene değeri ata
                sess.run(
                    cent_assigns[cluster_n], feed_dict={centroid_value: new_location}
                )

        # Merkezleri ve atamaları döndür
        centroids = sess.run(centroids)
        assignments = sess.run(assignments)
        return centroids, assignments
