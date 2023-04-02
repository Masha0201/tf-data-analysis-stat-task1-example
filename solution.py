import pandas as pd
import numpy as np


chat_id = 1289160674 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 96
    res = np.mean(2*x/t**2)
    return res # Ваш ответ
