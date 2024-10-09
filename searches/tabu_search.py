"""
Bu, Seyahat Satıcısı Problemi için Tabu arama algoritmasının saf Python uygulamasıdır. 
Şehirler arasındaki mesafeler simetriktir (şehir 'a' ile şehir 'b' arasındaki mesafe, 
şehir 'b' ile şehir 'a' arasındaki mesafeye eşittir). TSP, bir grafik olarak temsil edilebilir. 
Şehirler düğümlerle, aralarındaki mesafe ise düğümler arasındaki kenarın ağırlığı ile temsil edilir.

Grafi içeren .txt dosyası şu formata sahiptir:

Grafiği takma algoritması ile ilgili daha fazla bilgi için:
https://en.wikipedia.org/wiki/Travelling_salesman_problem

node1 node2 node1_ve_node2_arasındaki_mesafe
node1 node3 node1_ve_node3_arasındaki_mesafe
...

Organiser: K. Umut Araz

Dikkat: node1, node2 ve aralarındaki mesafe yalnızca bir kez bulunmalıdır. Bu, .txt dosyasında 
şunların bulunmaması gerektiği anlamına gelir:
node1 node2 node1_ve_node2_arasındaki_mesafe
node2 node1 node2_ve_node1_arasındaki_mesafe

Pytest'leri çalıştırmak için aşağıdaki komutu kullanın:
pytest

Manuel test için çalıştırın:
python tabu_search.py -f dosya_adınız.txt -i tabu_arama_iterasyon_sayısı \
    -s tabu_listesi_boyutu
örneğin: python tabu_search.py -f tabudata2.txt -i 4 -s 3
"""

import argparse
import copy


def generate_neighbours(path):
    """
    Bir grafi içeren bir dosya yoluna göre komşuların ve her komşunun maliyetinin 
    yer aldığı bir sözlük oluşturmanın saf uygulaması.

    :param path: Grafi içeren .txt dosyasının yolu (örneğin: tabudata2.txt)
    :return dict_of_neighbours: Anahtar olarak her düğüm ve değer olarak düğümün 
        komşuları ile her komşunun maliyetini (mesafe) içeren bir liste.
    
    dict_of_neighbours örneği:
    >>) dict_of_neighbours[a]
    [[b,20],[c,18],[d,22],[e,26]]

    Bu, 'a' düğümünün (şehir) komşularını gösterir; 'b' düğümü 20 mesafesiyle, 
    'c' düğümü 18 mesafesiyle, 'd' düğümü 22 mesafesiyle ve 'e' düğümü 26 mesafesiyle komşudur.
    """

    dict_of_neighbours = {}

    with open(path) as f:
        for line in f:
            if line.split()[0] not in dict_of_neighbours:
                _list = []
                _list.append([line.split()[1], line.split()[2]])
                dict_of_neighbours[line.split()[0]] = _list
            else:
                dict_of_neighbours[line.split()[0]].append(
                    [line.split()[1], line.split()[2]]
                )
            if line.split()[1] not in dict_of_neighbours:
                _list = []
                _list.append([line.split()[0], line.split()[2]])
                dict_of_neighbours[line.split()[1]] = _list
            else:
                dict_of_neighbours[line.split()[1]].append(
                    [line.split()[0], line.split()[2]]
                )

    return dict_of_neighbours


def generate_first_solution(path, dict_of_neighbours):
    """
    Tabu aramasına başlamak için ilk çözümü oluşturmanın saf uygulaması, 
    gereksiz çözümleme stratejisi ile. Bu, başlangıç düğümünden (örneğin: 'a' düğümü) 
    başlayarak, bu düğüme en yakın (en düşük mesafe) şehre (örneğin: 'c' düğümü) 
    gitmek anlamına gelir. Ardından 'c' düğümünün en yakın şehrine, vb. 
    giderek tüm şehirleri ziyaret edip başlangıç düğümüne geri döneriz.

    :param path: Grafi içeren .txt dosyasının yolu (örneğin: tabudata2.txt)
    :param dict_of_neighbours: Anahtar olarak her düğüm ve değer olarak düğümün 
        komşuları ile her komşunun maliyetini (mesafe) içeren bir liste.
    :return first_solution: Tabu aramasının ilk iterasyonu için çözüm.
    :return distance_of_first_solution: Seyahat Satıcısının, 
        first_solution'daki yolu takip ettiğinde kat edeceği toplam mesafe.
    """

    with open(path) as f:
        start_node = f.read(1)
    end_node = start_node

    first_solution = []

    visiting = start_node

    distance_of_first_solution = 0
    while visiting not in first_solution:
        minim = 10000
        for k in dict_of_neighbours[visiting]:
            if int(k[1]) < int(minim) and k[0] not in first_solution:
                minim = k[1]
                best_node = k[0]

        first_solution.append(visiting)
        distance_of_first_solution += int(minim)
        visiting = best_node

    first_solution.append(end_node)

    position = 0
    for k in dict_of_neighbours[first_solution[-2]]:
        if k[0] == start_node:
            break
        position += 1

    distance_of_first_solution += (
        int(dict_of_neighbours[first_solution[-2]][position][1]) - 10000
    )
    return first_solution, distance_of_first_solution


def find_neighborhood(solution, dict_of_neighbours):
    """
    Bir çözümün komşuluğunu (her çözümün toplam mesafesine göre en düşükten en yükseğe 
    sıralanmış) 1-1 değişim yöntemi ile oluşturmanın saf uygulaması. 
    Bu, bir çözümdeki her düğümü diğer düğümlerle değiştirerek bir dizi çözüm 
    oluşturmak anlamına gelir.

    :param solution: Komşuluğunu bulmak istediğimiz çözüm.
    :param dict_of_neighbours: Anahtar olarak her düğüm ve değer olarak düğümün 
        komşuları ile her komşunun maliyetini (mesafe) içeren bir liste.
    :return neighborhood_of_solution: 1-1 değişim ile üretilen çözümleri ve 
        her çözümün toplam mesafesini içeren bir liste.
    
    Örnek:
    >>> find_neighborhood(['a', 'c', 'b', 'd', 'e', 'a'],
    ...                   {'a': [['b', '20'], ['c', '18'], ['d', '22'], ['e', '26']],
    ...                    'c': [['a', '18'], ['b', '10'], ['d', '23'], ['e', '24']],
    ...                    'b': [['a', '20'], ['c', '10'], ['d', '11'], ['e', '12']],
    ...                    'e': [['a', '26'], ['b', '12'], ['c', '24'], ['d', '40']],
    ...                    'd': [['a', '22'], ['b', '11'], ['c', '23'], ['e', '40']]}
    ...                   )  # doctest: +NORMALIZE_WHITESPACE
    [['a', 'e', 'b', 'd', 'c', 'a', 90],
     ['a', 'c', 'd', 'b', 'e', 'a', 90],
     ['a', 'd', 'b', 'c', 'e', 'a', 93],
     ['a', 'c', 'b', 'e', 'd', 'a', 102],
     ['a', 'c', 'e', 'd', 'b', 'a', 113],
     ['a', 'b', 'c', 'd', 'e', 'a', 119]]
    """

    neighborhood_of_solution = []

    for n in solution[1:-1]:
        idx1 = solution.index(n)
        for kn in solution[1:-1]:
            idx2 = solution.index(kn)
            if n == kn:
                continue

            _tmp = copy.deepcopy(solution)
            _tmp[idx1] = kn
            _tmp[idx2] = n

            distance = 0

            for k in _tmp[:-1]:
                next_node = _tmp[_tmp.index(k) + 1]
                for i in dict_of_neighbours[k]:
                    if i[0] == next_node:
                        distance += int(i[1])
            _tmp.append(distance)

            if _tmp not in neighborhood_of_solution:
                neighborhood_of_solution.append(_tmp)

    index_of_last_item_in_the_list = len(neighborhood_of_solution[0]) - 1

    neighborhood_of_solution.sort(key=lambda x: x[index_of_last_item_in_the_list])
    return neighborhood_of_solution


def tabu_search(
    first_solution, distance_of_first_solution, dict_of_neighbours, iters, size
):
    """
    Seyahat Satıcısı Problemi için Tabu arama algoritmasının saf uygulaması.

    :param first_solution: Tabu aramasının ilk iterasyonu için çözüm.
    :param distance_of_first_solution: Seyahat Satıcısının, 
        first_solution'daki yolu takip ettiğinde kat edeceği toplam mesafe.
    :param dict_of_neighbours: Anahtar olarak her düğüm ve değer olarak düğümün 
        komşuları ile her komşunun maliyetini (mesafe) içeren bir liste.
    :param iters: Tabu aramasının gerçekleştireceği iterasyon sayısı.
    :param size: Tabu Listesi boyutu.
    :return best_solution_ever: Tabu araması sırasında elde edilen en düşük mesafeye 
        sahip çözüm.
    :return best_cost: En iyi çözümde Seyahat Satıcısının kat edeceği toplam mesafe.
    """
    count = 1
    solution = first_solution
    tabu_list = []
    best_cost = distance_of_first_solution
    best_solution_ever = solution

    while count <= iters:
        neighborhood = find_neighborhood(solution, dict_of_neighbours)
        index_of_best_solution = 0
        best_solution = neighborhood[index_of_best_solution]
        best_cost_index = len(best_solution) - 1

        found = False
        while not found:
            i = 0
            while i < len(best_solution):
                if best_solution[i] != solution[i]:
                    first_exchange_node = best_solution[i]
                    second_exchange_node = solution[i]
                    break
                i += 1

            if [first_exchange_node, second_exchange_node] not in tabu_list and [
                second_exchange_node,
                first_exchange_node,
            ] not in tabu_list:
                tabu_list.append([first_exchange_node, second_exchange_node])
                found = True
                solution = best_solution[:-1]
                cost = neighborhood[index_of_best_solution][best_cost_index]
                if cost < best_cost:
                    best_cost = cost
                    best_solution_ever = solution
            else:
                index_of_best_solution += 1
                best_solution = neighborhood[index_of_best_solution]

        if len(tabu_list) >= size:
            tabu_list.pop(0)

        count += 1

    return best_solution_ever, best_cost


def main(args=None):
    dict_of_neighbours = generate_neighbours(args.File)

    first_solution, distance_of_first_solution = generate_first_solution(
        args.File, dict_of_neighbours
    )

    best_sol, best_cost = tabu_search(
        first_solution,
        distance_of_first_solution,
        dict_of_neighbours,
        args.Iterations,
        args.Size,
    )

    print(f"En iyi çözüm: {best_sol}, toplam mesafe: {best_cost}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tabu Arama")
    parser.add_argument(
        "-f",
        "--File",
        type=str,
        help="Veri içeren dosyanın yolu",
        required=True,
    )
    parser.add_argument(
        "-i",
        "--Iterations",
        type=int,
        help="Algoritmanın gerçekleştireceği iterasyon sayısı",
        required=True,
    )
    parser.add_argument(
        "-s", "--Size", type=int, help="Tabu listesinin boyutu", required=True
    )

    # Argümanları ana metoda geçirin
    main(parser.parse_args())
