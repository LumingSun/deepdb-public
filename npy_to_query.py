import numpy as np
import pandas as pd
import csv


def construct_sql(line,new_line=True):
    if new_line:
        sql = "SELECT COUNT(*) FROM cover WHERE c0>={} AND c0<={} AND c1>={} AND c1<={} AND c2>={} AND c2<={} AND c3>={} AND c3<={} AND c4>={} AND c4<={} AND c5>={} AND c5<={} AND c6>={} AND c6<={} AND c7>={} AND c7<={} AND c8>={} AND c8<={} AND c9>={} AND c9<={};\n".format(*line)
    else:
        sql = "SELECT COUNT(*) FROM cover WHERE c0>={} AND c0<={} AND c1>={} AND c1<={} AND c2>={} AND c2<={} AND c3>={} AND c3<={} AND c4>={} AND c4<={} AND c5>={} AND c5<={} AND c6>={} AND c6<={} AND c7>={} AND c7<={} AND c8>={} AND c8<={} AND c9>={} AND c9<={};".format(*line)
    return sql


if __name__ == "__main__":
    np_query_path = './cover-benchmark/sql/cover_5000_attr_ten.npy'
    np_true_card_path = './cover-benchmark/sql/cover_5000_attr_ten_rows.npy'

    sql_query_path = './cover-benchmark/sql/cover_5000_attr_ten_queries.sql'
    sql_true_card_path = './cover-benchmark/sql/cover_5000_attr_ten_true_cardinalities.csv'

    np_query = np.load(np_query_path)
    true_card = np.load(np_true_card_path)

    sql = []
    for each in np_query:
        sql.append(construct_sql(each))

    with open(sql_query_path,'w') as f:
        f.writelines(sql)
    
    sql = []
    for each in np_query:
        sql.append(construct_sql(each,new_line=False))

    result = pd.DataFrame({"query_no":range(len(sql)),"query":sql,"cardinality_true":true_card})
    result.to_csv(sql_true_card_path,index=False,quoting=csv.QUOTE_NONNUMERIC)
    # with open(sql_true_card_path,'w') as f:
    #     for i, query, card in zip(range(len(sql)),sql,true_card):
    #         f.writelines(i)


