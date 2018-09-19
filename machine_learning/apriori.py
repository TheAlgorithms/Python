"""
simple apriori algorithm

author: mongoose
url: https://github.com/mongoose64
"""
from __future__ import division
from __future__ import print_function
import copy
from functools import reduce

def _compute_support(datas, ck):
    """
    helper function, compute item-set's support without div length

    :param datas: list of list
    :param ck: list of frozenset
    :return: the ck's support (without div data length)
    """
    res = []
    for c in ck:
        count = 0
        for d in datas:
            if set(c).issubset(set(d)):
                count += 1
        res.append(count)
    return res

def apriori_generate_conditions(pre_l):
    """
    get the next ck

    :param pre_l: list of frozenset
    :return: {new_frozenset: support_int, ...,}
    """
    new_cks = []
    for i, ck in enumerate(pre_l[:-1]):
        ck_list = copy.copy(list(ck))
        for ck_after in pre_l[i+1:]:
            diff = frozenset(ck_after) - frozenset(ck)
            if len(diff) != 1:
                continue
            else:
                ele = list(diff)[0]
                already_in = True
                for i in range(len(ck_list)):
                    if not already_in:
                        break
                    bk = ck_list[i]
                    ck_list[i] = ele
                    already_in = (frozenset(ck_list) in pre_l)
                    ck_list[i] = bk
                if already_in and frozenset(ck_list + [ele]) not in new_cks:
                    new_cks.append(frozenset(ck_list + [ele]))
    return dict(zip(new_cks, _compute_support(datas, new_cks)))


def filter_by_support(ck_and_support, min_support):
    """
    filter by support

    :param ck_and_support: {ck_frozenset: support_int, ..., ..}
    :param min_support: float * length of datas
    :return:
    """
    lk = []
    lsupport = []
    for c, s in ck_and_support.items():
        if s >= min_support:
            lk.append(c)
            lsupport.append(s)
    return lk


def generate_lks(datas, min_support):
    """
    generate lks
    :param datas:
    :param min_support:
    :return:
    """
    length = len(datas)
    c1 = list(map(lambda x: frozenset([x]), set(reduce(lambda x,y: x+y, datas))))
    support1 = _compute_support(datas, c1)
    l1 = filter_by_support(dict(zip(c1, support1)), min_support*length)  # does we need filter when compute 1-item-set ?

    lks = [l1]
    ck_and_supports = dict(zip(c1, support1))
    while True:
        pre_l = lks[-1]
        dict_ck_and_support = apriori_generate_conditions(pre_l)
        ck_and_supports.update(dict_ck_and_support)
        new_lk = filter_by_support(dict_ck_and_support, min_support * length)
        if len(new_lk) == 0:
            break
        lks.append(new_lk)
        if len(new_lk) == 1:
            break
    return lks, ck_and_supports

def generate_rules(lks, ck_and_supports, min_conf):
    """
    generate rules
    :param lk: [l1, l2, l3, l4,...]
    :param ck_and_support:
    :param min_conf:
    :return:
    """
    sub_set_list = []
    rules = []
    for lk in lks:
        for l in lk:
            for sub_set in sub_set_list:
                if sub_set.issubset(l):
                    pre = l - sub_set
                    conf = ck_and_supports[l] / ck_and_supports[pre]
                    rule = (pre, sub_set, conf)
                    if conf > min_conf and rule not in rules :
                        rules.append(rule)
            sub_set_list.append(l)
    return rules

if __name__ == '__main__':
    datas = [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
    min_support = 0.5
    min_conf = 0.5
    lks, ck_and_supports = generate_lks(datas, min_support)
    print("lks are: ", lks)
    rules = generate_rules(lks, ck_and_supports, min_conf)
    print("rules are: ", rules)
    pass
