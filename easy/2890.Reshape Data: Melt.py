# https://leetcode.com/problems/reshape-data-melt/description/

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
    id_vars=["product"],
    value_vars=[f"quarter_{i}" for i in range(1, 5)],
    var_name="quarter",
    value_name="sales"
  )
