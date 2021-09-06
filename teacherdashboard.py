import csv
import pandas as pd
import numpy as np


def get_feedback_counts():
    path = 'dataset/teacherdb.csv'
    df = pd.read_csv(path)
    index = df.index
    no_of_feedbacks = len(index)
    total_feedbacks = len(index)*6

    df1 = df.groupby('teacher1score').count()[['teacher1']]
    teacher1_negative_count = df1['teacher1'][-1]
    teacher1_neutral_count = df1['teacher1'][0]
    teacher1_positive_count = df1['teacher1'][1]

    df1 = df.groupby('teacher2score').count()[['teacher2']]
    teacher2_negative_count = df1['teacher2'][-1]
    teacher2_neutral_count = df1['teacher2'][0]
    teacher2_positive_count = df1['teacher2'][1]

    df1 = df.groupby('teacher3score').count()[['teacher3']]
    teacher3_negative_count = df1['teacher3'][-1]
    teacher3_neutral_count = df1['teacher3'][0]
    teacher3_positive_count = df1['teacher3'][1]

    df1 = df.groupby('teacher4score').count()[['teacher4']]
    teacher4_negative_count = df1['teacher4'][-1]
    teacher4_neutral_count = df1['teacher4'][0]
    teacher4_positive_count = df1['teacher4'][1]

    df1 = df.groupby('teacher5score').count()[['teacher5']]
    teacher5_negative_count = df1['teacher5'][-1]
    teacher5_neutral_count = df1['teacher5'][0]
    teacher5_positive_count = df1['teacher5'][1]

    df1 = df.groupby('teacher6score').count()[['teacher6']]
    teacher6_negative_count = df1['teacher6'][-1]
    teacher6_neutral_count = df1['teacher6'][0]
    teacher6_positive_count = df1['teacher6'][1]

    total_positive_feedbacks = teacher1_positive_count + teacher2_positive_count + teacher3_positive_count + teacher4_positive_count + teacher5_positive_count + teacher6_positive_count
    total_neutral_feedbacks = teacher1_neutral_count + teacher2_neutral_count + teacher3_neutral_count + teacher4_neutral_count + teacher5_neutral_count + teacher6_neutral_count
    total_negative_feedbacks = teacher1_negative_count + teacher2_negative_count + teacher3_negative_count +teacher4_negative_count + teacher5_negative_count + teacher6_negative_count

    li = [teacher1_positive_count,teacher1_negative_count,teacher1_neutral_count,
          teacher2_positive_count,teacher2_negative_count,teacher2_neutral_count,
          teacher3_positive_count,teacher3_negative_count,teacher3_neutral_count,
          teacher4_positive_count,teacher4_negative_count,teacher4_neutral_count,
          teacher5_positive_count,teacher5_negative_count,teacher5_neutral_count,
          teacher6_positive_count,teacher6_negative_count,teacher6_neutral_count]


    return no_of_feedbacks,\
           int(round(total_positive_feedbacks / total_feedbacks * 100)),\
           int(round(total_negative_feedbacks / total_feedbacks * 100)),\
           int(round(total_neutral_feedbacks / total_feedbacks * 100)),\
            li


