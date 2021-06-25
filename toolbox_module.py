import pandas as pd


def drop_values(df: pd.DataFrame, column, value):
    df.drop(df.index[df[column] == value], inplace=True)


def count_values(df: pd.DataFrame,value):
    for col in df.columns:
        if df[col].dtype == object:
            print(col, df[col][df[col] == value].count())


def count_value(df:pd.DataFrame, value):
    if df[col].dtype == object:
        print(col, df[col][df[col] == value].count())
