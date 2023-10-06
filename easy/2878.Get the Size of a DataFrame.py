# https://leetcode.com/problems/get-the-size-of-a-dataframe/description/

from typing import List
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
