import numpy as np
import pandas as pd


def drop_values(df: pd.DataFrame, column, value):
    df.drop(df.index[df[column] == value], inplace=True)


# def count_values(df: pd.DataFrame,value):
#     for col in df.columns:
#         if df[col].dtype == object:
#             print(col, df[col][df[col] == value].count())

def count_values(df: pd.DataFrame,value):
    for col in df.columns:
        count_value(df,value , col)


def count_value(df:pd.DataFrame, value, col):
    if df[col].dtype == object:
        print(col, df[col][df[col] == value].count())




def convert_idc_disease_class(value):
    #  this is a dict with the possible return codes
    classes = {'circulatory': 1, 'respiratory': 2, 'digestive': 3, 'diabetes': 4, 'injury': 5, 'musculoskeletal': 6,
               'genitourinary': 7, 'neoplasm': 8, 'other': 9}
    idc = 0

    # if its a non numeric character then ist either a diabetes code eg 250.6 or an injury code with a V or E suffix
    if not value.isnumeric():
        # if its a decimal we will get a lst longer tha 1 if we split on the '.'
        if len(value.split('.')) > 1:
            idc = int(value.split('.')[0])  # in which case store the diabetes code of 250
            if idc != 250:   # if it has another number then its 'other'
                disease_class="other"
                return classes.get(disease_class)  # in which case, we're done, nothing else to see here

    else:  # if it's another code
        idc = int(value) # make it an int

    #  assign a disease type
    if (idc in range(390, 460)) or idc == 785:
        disease_class='circulatory'
    elif (idc in range(460, 520)) or idc == 786:
        disease_class = 'respiratory'
    elif (idc in range(520, 580)) or idc == 787:
        disease_class = 'digestive'
    elif np.floor(idc) == 250:
        disease_class = 'diabetes'
    elif idc in range(800, 1000):
        disease_class = 'injury'
    elif idc in range(710, 740):
        disease_class = 'musculoskeletal'
    elif (idc in range(580, 660)) or idc == 788:
        disease_class = 'genitourinary'
    elif idc in range(140, 240):
        disease_class = 'neoplasm'
    else:
        disease_class = 'other'

    #  look up the dict for the code and return it
    return classes.get(disease_class)



