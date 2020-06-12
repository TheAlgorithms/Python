"""
    Implementation of entropy of information
    https://en.wikipedia.org/wiki/Entropy_(information_theory)
"""

import sys
import math
r = range


def create_alpha_array():
    """
    This method creates array of our alphabet to print probabilities later on.
    :return:
    """
    my_alphas = [" "]
    for x in r(ord("a"), ord("z") + 1):
        my_alphas += chr(x)
    return my_alphas


def calculate_prob(my_dic_fir, my_dic_sec, path_dest):
    """
    This method takes path and two dict as argument
    and than calculates entropy of them.
    :param my_dic_fir:
    :param my_dic_sec:
    :param path_dest:
    :return:
    """
    f = open(path_dest, mode="w+", encoding="utf-8")

    my_alphas = create_alpha_array()  # create our alpha
    # what is our total sum of probabilities.
    values = my_dic_fir.values()
    all_sum = sum(values)

    # one length string
    my_fir_sum = 0
    # for each alpha we go in our dict and if it is in it we calculate entropy
    for _ in my_alphas:
        if _ in my_dic_fir:
            my_str = my_dic_fir[_]
            prob = my_str / all_sum
            my_fir_sum += prob * math.log2(prob)  # entropy formula.

    # write entropy to file
    f.write("{0:.7f}".format(-1 * my_fir_sum))
    f.write("\n")

    # two len string
    values = my_dic_sec.values()
    all_sum = sum(values)  # time for two len probabilities sum
    my_sec_sum = 0
    # for each alpha (two in size) calculate entropy.
    for _ in my_alphas:
        for __ in my_alphas:
            sequence = _ + __
            if sequence in my_dic_sec:
                my_str = my_dic_sec[sequence]
                prob = int(my_str) / all_sum
                my_sec_sum += prob * math.log2(prob)
    # write second entropy to the file
    f.write("{0:.7f}".format(-1 * my_sec_sum))
    f.write("\n")

    # write the difference between them to the file
    f.write("{0:.7f}".format((-1 * my_sec_sum) - (-1 * my_fir_sum)))
    # f.write('\n')


# 0x
def open_file(path_src, path_dest):
    """
    This method take path and also two clear dict as argument
    And later on it open the file at this path and puts frequency on each dictionary
    in first dictionary it puts one len strings.
    in second dictionary it puts two len strings.
    :param path_src:
    :param path_dest:
    :return:
    """
    my_dic_fir = {}
    my_dic_sec = {}
    f = open(path_src, mode="r", encoding="utf-8")
    text = f.read()
    my_dic_fir[text[len(text) - 1]] = 1

    # first case when we have space at start.
    my_dic_sec[" " + text[0]] = 1
    for _ in r(0, len(text) - 1):
        sequence_fir = text[_]
        sequence_sec = text[_ : _ + 2]
        # continue
        if sequence_fir not in my_dic_fir:
            my_dic_fir[sequence_fir] = 1
        else:
            my_dic_fir[sequence_fir] += 1

        if sequence_sec not in my_dic_sec:
            my_dic_sec[sequence_sec] = 1
        else:
            my_dic_sec[sequence_sec] += 1

    return my_dic_fir, my_dic_sec


def main():
    path_src = sys.argv[1]
    path_dest = sys.argv[2]
    print("-" * 20)
    print(path_src, path_dest)

    my_dic_fir, my_dic_sec = open_file(path_src, path_dest)
    calculate_prob(my_dic_fir, my_dic_sec, path_dest)


if __name__ == "__main__":
    main()
