import numpy as np
import math

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    line = np.arange(seq_len, dtype = float)
    line = np.reshape(line,(seq_len,1))
    angle = np.arange(0, d_model, 2, dtype = float)
    angle = np.power(base, angle/d_model)
    angle = line/angle
    ans = np.zeros((seq_len, d_model), dtype = float)
    ans[:,0::2] = np.sin(angle)
    ans[:,1::2] = np.cos(angle[:,0:(d_model//2)])
    return ans
    pass