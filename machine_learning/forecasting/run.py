"""
this is code for forecasting
but i modified it and used it for safety checker of data
for ex: you have a online shop and for some reason some data are
missing (the amount of data that u expected are not supposed to be)
        then we can use it
*ps : 1. ofc we can use normal statistic method but in this case
         the data is quite absurd and only a little^^
      2. ofc u can use this and modified it for forecasting purpose
         for the next 3 months sales or something,
         u can just adjust it for ur own purpose
"""

import pandas as pd
from sklearn.preprocessing import Normalizer

from methods import lin_reg_pred, sarimax_predictor, support_machine_regressor


def data_safety_checker(list_vote, actual_result):
    safe = 0
    not_safe = 0
    for i in list_vote:
        if i > actual_result:
            safe = not_safe + 1
        else:
            if abs(abs(i) - abs(actual_result[0])) <= 0.1:
                safe = safe + 1
            else:
                not_safe = not_safe + 1
    if safe > not_safe:
        print("today's data is safe")
    else:
        print("today's data is not safe")


data_input_df = pd.read_csv("ex_data.csv")
"""
data column = total user in a day, how much online event held in one day,
what day is that(sunday-saturday)
"""

# start normalization
normalize_df = Normalizer().fit_transform(data_input_df.values)
# split data
total_date = normalize_df[:, 2].tolist()
total_user = normalize_df[:, 0].tolist()
total_match = normalize_df[:, 1].tolist()

# for svr (input variable = total date and total match)
x = normalize_df[:, [1, 2]].tolist()
x_train = x[: len(x) - 1]
x_test = x[len(x) - 1 :]

# for linear reression & sarimax
trn_date = total_date[: len(total_date) - 1]
trn_user = total_user[: len(total_user) - 1]
trn_match = total_match[: len(total_match) - 1]

tst_date = total_date[len(total_date) - 1 :]
tst_user = total_user[len(total_user) - 1 :]
tst_match = total_match[len(total_match) - 1 :]


# voting system with forecasting
res_vote = []
res_vote.append(lin_reg_pred(trn_date, trn_user, trn_match, tst_date, tst_match))
res_vote.append(sarimax_predictor(trn_user, trn_match, tst_match))
res_vote.append(support_machine_regressor(x_train, x_test, trn_user))

# check the safety of todays'data^^
data_safety_checker(res_vote, tst_user)
