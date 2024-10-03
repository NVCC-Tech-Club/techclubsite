from .col import (
    reformat_col_lst,
    resid_col,
    order_col_lst,
    interf_path_col,
    pocket_path_col,
    core_path_col,
    pdb_id_col,
    pdb_code_col,
    modelid_col,
    chainid_col,
    interf_col,
    cf_col,
    index_col,
    total_col,
    prot_col,
    count_col_dict,
    data_col_lst,
)

from .lst import (
    format_val,
    str_to_lst,
    type_lst,
    sort_lst,
    move_end_lst,
    lst_nums,
    lst_unique,
    lst_to_str,
    lst_inter,
)

def fix_query(query):

    return [fix_val(x) for x in type_lst(query)]


def fix_col(df, col):

    for index in list(df.index.values):

        df.at[index, col] = fix_val(df.at[index, col])

    return df


def mask_equal(df, col, query, reset_index=True):

    temp_df = df.copy(deep=True)

    query = fix_query(query)

    temp_df = fix_col(temp_df, col)

    temp_df = temp_df[temp_df[col].isin(query)]

    if reset_index:
        temp_df = temp_df.reset_index(drop=True)

    return temp_df


def order_cols(df, col_lst):

    df = df.reindex(columns=col_lst)

    return df


def order_rows(df, col_lst=None, reset_index=False):

    df_col_lst = list(df.columns)

    if col_lst is None:
        col_lst = list()

        if interf_path_col in df_col_lst:
            col_lst.append(interf_path_col)
        elif pocket_path_col in df_col_lst:
            col_lst.append(pocket_path_col)
        elif core_path_col in df_col_lst:
            col_lst.append(core_path_col)

        if pdb_id_col in df_col_lst:
            col_lst.append(pdb_id_col)
        if pdb_code_col in df_col_lst:
            col_lst.append(pdb_code_col)
        if modelid_col in df_col_lst:
            col_lst.append(modelid_col)
        if chainid_col in df_col_lst:
            col_lst.append(chainid_col)
        if interf_col in df_col_lst:
            col_lst.append(interf_col)

    if len(col_lst) > 0:
        df = df.sort_values(by=col_lst)

    if reset_index:
        df = df.reset_index(drop=True)

    return df


def get_col_order(df):

    df_col_lst = list(df.columns)

    col_lst = list()
    for order_col in order_col_lst:
        if order_col in df_col_lst:
            col_lst.append(order_col)
        if order_col in data_col_lst:
            for col in get_val_col_lst(df, order_col):
                if col not in col_lst:
                    col_lst.append(col)

    for col in df_col_lst:
        if col not in col_lst:
            col_lst.append(col)

    return col_lst