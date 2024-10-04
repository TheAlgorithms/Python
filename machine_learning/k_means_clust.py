"""README, Author - Anurag Kumar(mailto:anuragkumarak95@gmail.com)
Gereksinimler:
  - sklearn
  - numpy
  - matplotlib
Python:
  - 3.5
Girdiler:
  - X , 2D numpy özellik dizisi.
  - k , oluşturulacak küme sayısı.
  - initial_centroids , yardımcı fonksiyon tarafından oluşturulan başlangıç merkez değerleri
    (kullanımda belirtilmiştir).
  - maxiter , işlenecek maksimum iterasyon sayısı.
  - heterogeneity , kmeans fonksiyonuna geçirilirse heterojenlik değerleriyle doldurulacak boş liste.
Kullanım:
  1. 'k' değeri, 'X' özellik dizisi ve 'heterogeneity' boş listesini tanımlayın
  2. initial_centroids oluşturun,
        initial_centroids = get_initial_centroids(
            X,
            k,
            seed=0 # başlangıç merkezi oluşturma için tohum değeri,
                   # rastgelelik için None (varsayılan=None)
            )
  3. kmeans fonksiyonunu kullanarak merkezleri ve kümeleri bulun.
        centroids, cluster_assignment = kmeans(
            X,
            k,
            initial_centroids,
            maxiter=400,
            record_heterogeneity=heterogeneity,
            verbose=True # konsolda logların yazdırılıp yazdırılmayacağı (varsayılan=False)
            )
  4. heterogeneity listesinde kaydedilen her iterasyon için kayıp fonksiyonunu ve heterojenlik değerlerini çizin.
        plot_heterogeneity(
            heterogeneity,
            k
        )
  5. Verileri excel formatına dönüştürün, içinde k means kümeleme numaraları olan 'Clust' adlı bir özellik olmalıdır.
"""

import warnings

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import pairwise_distances

warnings.filterwarnings("ignore")

TAG = "K-MEANS-CLUST/ "


def get_initial_centroids(data, k, seed=None):
    """Rastgele olarak k veri noktasını başlangıç merkezleri olarak seç"""
    # tutarlı sonuçlar elde etmek için yararlı
    rng = np.random.default_rng(seed)
    n = data.shape[0]  # veri noktalarının sayısı

    # [0, N) aralığından K indeks seçin.
    rand_indices = rng.integers(0, n, k)

    # Merkezleri yoğun formatta tutun, çünkü ortalama nedeniyle birçok giriş sıfır olmayacaktır.
    # Bir kümedeki en az bir belge bir kelime içerdiği sürece,
    # bu kelime, merkezin TF-IDF vektöründe sıfır olmayan bir ağırlık taşıyacaktır.
    centroids = data[rand_indices, :]

    return centroids


def centroid_pairwise_dist(x, centroids):
    return pairwise_distances(x, centroids, metric="euclidean")


def assign_clusters(data, centroids):
    # Her veri noktası ile merkezler kümesi arasındaki mesafeleri hesaplayın:
    # Boşluğu doldurun (sadece RHS)
    distances_from_centroids = centroid_pairwise_dist(data, centroids)

    # Her veri noktası için küme atamalarını hesaplayın:
    # Boşluğu doldurun (sadece RHS)
    cluster_assignment = np.argmin(distances_from_centroids, axis=1)

    return cluster_assignment


def revise_centroids(data, k, cluster_assignment):
    new_centroids = []
    for i in range(k):
        # Küme i'ye ait tüm veri noktalarını seçin. Boşluğu doldurun (sadece RHS)
        member_data_points = data[cluster_assignment == i]
        # Veri noktalarının ortalamasını hesaplayın. Boşluğu doldurun (sadece RHS)
        centroid = member_data_points.mean(axis=0)
        new_centroids.append(centroid)
    new_centroids = np.array(new_centroids)

    return new_centroids


def compute_heterogeneity(data, k, centroids, cluster_assignment):
    heterogeneity = 0.0
    for i in range(k):
        # Küme i'ye ait tüm veri noktalarını seçin. Boşluğu doldurun (sadece RHS)
        member_data_points = data[cluster_assignment == i, :]

        if member_data_points.shape[0] > 0:  # i. kümenin boş olup olmadığını kontrol edin
            # Merkezden veri noktalarına olan mesafeleri hesaplayın (sadece RHS)
            distances = pairwise_distances(
                member_data_points, [centroids[i]], metric="euclidean"
            )
            squared_distances = distances**2
            heterogeneity += np.sum(squared_distances)

    return heterogeneity


def plot_heterogeneity(heterogeneity, k):
    plt.figure(figsize=(7, 4))
    plt.plot(heterogeneity, linewidth=4)
    plt.xlabel("# Iterations")
    plt.ylabel("Heterogeneity")
    plt.title(f"Heterogeneity of clustering over time, K={k:d}")
    plt.rcParams.update({"font.size": 16})
    plt.show()


def kmeans(
    data, k, initial_centroids, maxiter=500, record_heterogeneity=None, verbose=False
):
    """Verilen veri ve başlangıç merkezleri kümesi üzerinde k-means çalıştırır.
    maxiter: çalıştırılacak maksimum iterasyon sayısı (varsayılan=500)
    record_heterogeneity: (isteğe bağlı) heterojenlik geçmişini
                          iterasyonların bir fonksiyonu olarak kaydetmek için bir liste
                          eğer None ise, geçmişi kaydetme.
    verbose: True ise, her iterasyonda kaç veri noktasının küme etiketlerini değiştirdiğini yazdırır"""
    centroids = initial_centroids[:]
    prev_cluster_assignment = None

    for itr in range(maxiter):
        if verbose:
            print(itr, end="")

        # 1. En yakın merkezleri kullanarak küme atamaları yapın
        cluster_assignment = assign_clusters(data, centroids)

        # 2. Her bir k kümesi için yeni bir merkez hesaplayın, bu kümeye atanan tüm veri noktalarının ortalamasını alın.
        centroids = revise_centroids(data, k, cluster_assignment)

        # Yakınsama kontrolü: eğer atamalardan hiçbiri değişmediyse, durdurun
        if (
            prev_cluster_assignment is not None
            and (prev_cluster_assignment == cluster_assignment).all()
        ):
            break

        # Yeni atamaların sayısını yazdır
        if prev_cluster_assignment is not None:
            num_changed = np.sum(prev_cluster_assignment != cluster_assignment)
            if verbose:
                print(
                    f"    {num_changed:5d} eleman küme atamasını değiştirdi."
                )

        # Heterojenlik yakınsama metriğini kaydedin
        if record_heterogeneity is not None:
            # KODUNUZ BURAYA
            score = compute_heterogeneity(data, k, centroids, cluster_assignment)
            record_heterogeneity.append(score)

        prev_cluster_assignment = cluster_assignment[:]

    return centroids, cluster_assignment


# Aşağıda sahte test
if False:  # bu test durumunu çalıştırmak için true olarak değiştirin.
    from sklearn import datasets as ds

    dataset = ds.load_iris()
    k = 3
    heterogeneity = []
    initial_centroids = get_initial_centroids(dataset["data"], k, seed=0)
    centroids, cluster_assignment = kmeans(
        dataset["data"],
        k,
        initial_centroids,
        maxiter=400,
        record_heterogeneity=heterogeneity,
        verbose=True,
    )
    plot_heterogeneity(heterogeneity, k)


def report_generator(
    predicted: pd.DataFrame, clustering_variables: np.ndarray, fill_missing_report=None
) -> pd.DataFrame:
    """
    Bu iki argüman verilerek bir kümeleme raporu oluşturun:
        predicted - tahmin edilen küme sütunu ile veri çerçevesi
        fill_missing_report - nihai oluşturulan rapor için eksik değerleri nasıl dolduracağımıza dair kuralların sözlüğü
        (modellemeye dahil edilmemiş);
    >>> predicted = pd.DataFrame()
    >>> predicted['numbers'] = [1, 2, 3]
    >>> predicted['col1'] = [0.5, 2.5, 4.5]
    >>> predicted['col2'] = [100, 200, 300]
    >>> predicted['col3'] = [10, 20, 30]
    >>> predicted['Cluster'] = [1, 1, 2]
    >>> report_generator(predicted, ['col1', 'col2'], 0)
               Features               Type   Mark           1           2
    0    # of Customers        ClusterSize  False    2.000000    1.000000
    1    % of Customers  ClusterProportion  False    0.666667    0.333333
    2              col1    mean_with_zeros   True    1.500000    4.500000
    3              col2    mean_with_zeros   True  150.000000  300.000000
    4           numbers    mean_with_zeros  False    1.500000    3.000000
    ..              ...                ...    ...         ...         ...
    99            dummy                 5%  False    1.000000    1.000000
    100           dummy                95%  False    1.000000    1.000000
    101           dummy              stdev  False    0.000000         NaN
    102           dummy               mode  False    1.000000    1.000000
    103           dummy             median  False    1.000000    1.000000
    <BLANKLINE>
    [104 rows x 5 columns]
    """
    # Eksik değerleri verilen kurallarla doldurun
    if fill_missing_report:
        predicted = predicted.fillna(value=fill_missing_report)
    predicted["dummy"] = 1
    numeric_cols = predicted.select_dtypes(np.number).columns
    report = (
        predicted.groupby(["Cluster"])[  # rapor veri çerçevesi oluştur
            numeric_cols
        ]  # küme numarasına göre grupla
        .agg(
            [
                ("sum", "sum"),
                ("mean_with_zeros", lambda x: np.mean(np.nan_to_num(x))),
                ("mean_without_zeros", lambda x: x.replace(0, np.nan).mean()),
                (
                    "mean_25-75",
                    lambda x: np.mean(
                        np.nan_to_num(
                            sorted(x)[
                                round(len(x) * 25 / 100) : round(len(x) * 75 / 100)
                            ]
                        )
                    ),
                ),
                ("mean_with_na", "mean"),
                ("min", lambda x: x.min()),
                ("5%", lambda x: x.quantile(0.05)),
                ("25%", lambda x: x.quantile(0.25)),
                ("50%", lambda x: x.quantile(0.50)),
                ("75%", lambda x: x.quantile(0.75)),
                ("95%", lambda x: x.quantile(0.95)),
                ("max", lambda x: x.max()),
                ("count", lambda x: x.count()),
                ("stdev", lambda x: x.std()),
                ("mode", lambda x: x.mode()[0]),
                ("median", lambda x: x.median()),
                ("# > 0", lambda x: (x > 0).sum()),
            ]
        )
        .T.reset_index()
        .rename(index=str, columns={"level_0": "Features", "level_1": "Type"})
    )  # sütunları yeniden adlandır
    # küme boyutunu hesapla (clientID'lerin sayısı)
    # SettingWithCopyWarning'dan kaçının
    clustersize = report[
        (report["Features"] == "dummy") & (report["Type"] == "count")
    ].copy()
    # oluşturulan tahmin edilen kümeyi rapor sütun adlarıyla eşleşecek şekilde yeniden adlandırın
    clustersize.Type = "ClusterSize"
    clustersize.Features = "# of Customers"
    # küme oranını hesaplama
    clusterproportion = pd.DataFrame(
        clustersize.iloc[:, 2:].to_numpy() / clustersize.iloc[:, 2:].to_numpy().sum()
    )
    # oluşturulan tahmin edilen kümeyi rapor sütun adlarıyla eşleşecek şekilde yeniden adlandırın
    clusterproportion["Type"] = "% of Customers"
    clusterproportion["Features"] = "ClusterProportion"
    cols = clusterproportion.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    clusterproportion = clusterproportion[cols]  # sütunları raporla eşleşecek şekilde yeniden düzenleyin
    clusterproportion.columns = report.columns
    # nan değerlerinin sayısını içeren veri çerçevesi oluşturma
    a = pd.DataFrame(
        abs(
            report[report["Type"] == "count"].iloc[:, 2:].to_numpy()
            - clustersize.iloc[:, 2:].to_numpy()
        )
    )
    a["Features"] = 0
    a["Type"] = "# of nan"
    # raporla eşleşecek şekilde değerleri doldurma
    a.Features = report[report["Type"] == "count"].Features.tolist()
    cols = a.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    a = a[cols]  # sütunları raporla eşleşecek şekilde yeniden düzenleyin
    a.columns = report.columns  # sütunları raporla eşleşecek şekilde yeniden adlandırın
    # küme boyutu dışında sayım değerlerini düşür
    report = report.drop(report[report.Type == "count"].index)
    # raporu küme boyutu ve nan değerleri ile birleştirin
    report = pd.concat([report, a, clustersize, clusterproportion], axis=0)
    report["Mark"] = report["Features"].isin(clustering_variables)
    cols = report.columns.tolist()
    cols = cols[0:2] + cols[-1:] + cols[2:-1]
    report = report[cols]
    sorter1 = {
        "ClusterSize": 9,
        "ClusterProportion": 8,
        "mean_with_zeros": 7,
        "mean_with_na": 6,
        "max": 5,
        "50%": 4,
        "min": 3,
        "25%": 2,
        "75%": 1,
        "# of nan": 0,
        "# > 0": -1,
        "sum_with_na": -2,
    }
    report = (
        report.assign(
            Sorter1=lambda x: x.Type.map(sorter1),
            Sorter2=lambda x: list(reversed(range(len(x)))),
        )
        .sort_values(["Sorter1", "Mark", "Sorter2"], ascending=False)
        .drop(["Sorter1", "Sorter2"], axis=1)
    )
    report.columns.name = ""
    report = report.reset_index()
    report = report.drop(columns=["index"])
    return report


if __name__ == "__main__":
    import doctest

    doctest.testmod()
