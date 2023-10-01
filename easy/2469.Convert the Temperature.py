# https://leetcode.com/problems/convert-the-temperature/description/

from typing import List

def convertTemperature(celsius: float) -> List[float]:
    return [celsius+273.15,celsius*1.8+32]


assert convertTemperature(36.50) == [309.65000,97.70000]
assert convertTemperature(122.11) == [395.26000,251.79800]
