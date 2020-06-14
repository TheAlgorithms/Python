"""
    Implementation of entropy of information
    https://en.wikipedia.org/wiki/Entropy_(information_theory)
"""

import math
from collections import Counter


def create_alpha_array():
    """
    This method creates array of our alphabet to print probabilities later on.
    :return:
    """
    my_alphas = [" "]
    for x in range(ord("a"), ord("z") + 1):
        my_alphas += chr(x)
    return my_alphas


def calculate_prob(text):
    """
    This method takes path and two dict as argument
    and than calculates entropy of them.
    :param dict:
    :param dict:
    :return: Prints
    1) Entropy of information based on 1 alphabet
    2) Entropy of information based on couples of 2 alphabet
    3) print Entropy of H(X n∣Xn−1)

    Text from random books. Also, random quotes.
    >>> text = ("Behind Winston’s back the voice"
    ...         "from the telescreen was still"
    ...         "babbling and the overfulfilment")
    >>> calculate_prob(text)
    4.0
    6.0
    2.0

    >>> text = ("The Ministry of Truth—Minitrue, in Newspeak [Newspeak was the official"
    ...         "face in elegant lettering, the three")
    >>> calculate_prob(text)
    4.0
    5.0
    1.0
    >>> text = ("Had repulsive dashwoods suspicion sincerity but advantage now him. Remark easily garret nor nay."
    ...         "Civil those mrs enjoy shy fat merry. You greatest jointure saw horrible. He private he on be "
    ...         "imagine suppose. Fertile beloved evident through no service elderly is. Blind there if every "
    ...         "no so at. Own neglected you preferred way sincerity delivered his attempted. To of message "
    ...         "cottage windows do besides against uncivil.  Delightful unreserved impossible few estimating "
    ...         "men favourable see entreaties. She propriety immediate was improving. He or entrance humoured "
    ...         "likewise moderate. Much nor game son say feel. Fat make met can must form into gate. Me we "
    ...         "offending prevailed discovery. ")
    >>> calculate_prob(text)
    4.0
    7.0
    3.0
    """
    my_dic_fir, my_dic_sec = open_file(text)
    my_alphas = create_alpha_array()  # create our alpha
    # what is our total sum of probabilities.
    values = my_dic_fir.values()
    all_sum = sum(my_dic_fir.values())

    # one length string
    my_fir_sum = 0
    # for each alpha we go in our dict and if it is in it we calculate entropy
    for ch in my_alphas:
        if ch in my_dic_fir:
            my_str = my_dic_fir[ch]
            prob = my_str / all_sum
            my_fir_sum += prob * math.log2(prob)  # entropy formula.

    # write entropy to file
    print("{0:.1f}".format(round(-1 * my_fir_sum)))

    # two len string
    values = my_dic_sec.values()
    all_sum = sum(values)  # time for two len probabilities sum
    my_sec_sum = 0
    # for each alpha (two in size) calculate entropy.
    for ch0 in my_alphas:
        for ch1 in my_alphas:
            sequence = ch0 + ch1
            if sequence in my_dic_sec:
                my_str = my_dic_sec[sequence]
                prob = int(my_str) / all_sum
                my_sec_sum += prob * math.log2(prob)

    # write second entropy to the file
    print("{0:.1f}".format(round(-1 * my_sec_sum)))

    # write the difference between them to the file
    print("{0:.1f}".format(round(((-1 * my_sec_sum) - (-1 * my_fir_sum)))))


def open_file(text):
    """
    This method take path and also two clear dict as argument
    And later on it open the file at this path and puts frequency on each dictionary
    in first dictionary it puts one len strings.
    in second dictionary it puts two len strings.
    :param text as string type:
    :return: dict, dict
    """
    my_dic_fir = {}
    my_dic_sec = {}
    my_dic_fir[text[len(text) - 1]] = 1

    # first case when we have space at start.
    my_dic_sec[" " + text[0]] = 1
    for _ in range(0, len(text) - 1):
        sequence_fir = text[_]
        sequence_sec = text[_ : _ + 2]
        # continue

        if not Counter(my_dic_fir)[sequence_fir]:
            my_dic_fir[sequence_fir] = 1
        else:
            my_dic_fir[sequence_fir] += 1

        if not Counter(my_dic_sec)[sequence_sec]:
            my_dic_sec[sequence_sec] = 1
        else:
            my_dic_sec[sequence_sec] += 1

    return my_dic_fir, my_dic_sec


def main():
    import doctest

    doctest.testmod()
    # text = (
    #     "Had repulsive dashwoods suspicion sincerity but advantage now him. Remark easily garret nor nay."
    #     "Civil those mrs enjoy shy fat merry. You greatest jointure saw horrible. He private he on be "
    #     "imagine suppose. Fertile beloved evident through no service elderly is. Blind there if every "
    #     "no so at. Own neglected you preferred way sincerity delivered his attempted. To of message "
    #     "cottage windows do besides against uncivil.  Delightful unreserved impossible few estimating "
    #     "men favourable see entreaties. She propriety immediate was improving. He or entrance humoured "
    #     "likewise moderate. Much nor game son say feel. Fat make met can must form into gate. Me we "
    #     "offending prevailed discovery. "
    # )

    # calculate_prob(text)


if __name__ == "__main__":
    main()
