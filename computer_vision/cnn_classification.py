"""
Evrişimli Sinir Ağı

Amaç : Bir CNN modeli eğiterek Akciğer Röntgeninde Tüberküloz olup olmadığını tespit etmek.

Kaynaklar CNN Teorisi :
    https://en.wikipedia.org/wiki/Convolutional_neural_network
Kaynaklar Tensorflow : https://www.tensorflow.org/tutorials/images/cnn

Veri setini indirin :
https://lhncbc.nlm.nih.gov/LHC-publications/pubs/TuberculosisChestXrayImageDataSets.html

1. Veri seti klasörünü indirin ve ana veri seti klasöründe iki klasör oluşturun: eğitim seti ve test seti
2. Hem TB pozitif hem de TB negatif klasörlerinden 30-40 görüntüyü test seti klasörüne taşıyın
3. Görüntülerin etiketleri, görüntünün bulunduğu klasör adından çıkarılacaktır.

"""

# Bölüm 1 - CNN'i Oluşturma

import numpy as np

# Keras kütüphanelerini ve paketlerini içe aktarma
import tensorflow as tf
from keras import layers, models

if __name__ == "__main__":
    # CNN'i Başlatma
    # (Sıralı- Modeli katman katman oluşturma)
    sınıflandırıcı = models.Sequential()

    # Adım 1 - Evrişim
    # Burada 64,64 veri seti görüntülerinin uzunluğu ve genişliği ve 3 RGB kanalı içindir
    # (3,3) çekirdek boyutudur (filtre matrisi)
    sınıflandırıcı.add(
        layers.Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation="relu")
    )

    # Adım 2 - Havuzlama
    sınıflandırıcı.add(layers.MaxPooling2D(pool_size=(2, 2)))

    # İkinci bir evrişim katmanı ekleme
    sınıflandırıcı.add(layers.Conv2D(32, (3, 3), activation="relu"))
    sınıflandırıcı.add(layers.MaxPooling2D(pool_size=(2, 2)))

    # Adım 3 - Düzleştirme
    sınıflandırıcı.add(layers.Flatten())

    # Adım 4 - Tam bağlantı
    sınıflandırıcı.add(layers.Dense(units=128, activation="relu"))
    sınıflandırıcı.add(layers.Dense(units=1, activation="sigmoid"))

    # CNN'i Derleme
    sınıflandırıcı.compile(
        optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
    )

    # Bölüm 2 - CNN'i görüntülere uydurma

    # Eğitilmiş model ağırlıklarını yükle

    # from keras.models import load_model
    # regressor=load_model('cnn.h5')

    eğitim_veri_üretici = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1.0 / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True
    )

    test_veri_üretici = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0 / 255)

    eğitim_seti = eğitim_veri_üretici.flow_from_directory(
        "dataset/training_set", target_size=(64, 64), batch_size=32, class_mode="binary"
    )

    test_seti = test_veri_üretici.flow_from_directory(
        "dataset/test_set", target_size=(64, 64), batch_size=32, class_mode="binary"
    )

    sınıflandırıcı.fit_generator(
        eğitim_seti, steps_per_epoch=5, epochs=30, validation_data=test_seti
    )

    sınıflandırıcı.save("cnn.h5")

    # Bölüm 3 - Yeni tahminler yapma

    test_görüntü = tf.keras.preprocessing.image.load_img(
        "dataset/single_prediction/image.png", target_size=(64, 64)
    )
    test_görüntü = tf.keras.preprocessing.image.img_to_array(test_görüntü)
    test_görüntü = np.expand_dims(test_görüntü, axis=0)
    sonuç = sınıflandırıcı.predict(test_görüntü)
    # eğitim_seti.class_indices
    if sonuç[0][0] == 0:
        tahmin = "Normal"
    if sonuç[0][0] == 1:
        tahmin = "Anormallik tespit edildi"
