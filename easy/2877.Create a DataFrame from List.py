# https://leetcode.com/problems/create-a-dataframe-from-list/description/

from typing import List
import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data,columns=['student_id','age'])
