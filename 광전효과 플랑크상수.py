import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 실험 데이터 입력
voltage = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
current = np.array([0.0011, 0.0022, 0.0033, 0.0044, 0.0055])
freq = 5e14

# 함수 정의
def current_fit(v, I0, b):
    return I0 * (np.exp(b*v)-1)

# 초기값 설정
I0_init = current[0]
b_init = freq / (1.6e-19)

# 커브 피팅
popt, pcov = curve_fit(current_fit, voltage, current, p0=[I0_init, b_init])

# 결과 출력
print("플랑크 상수 h = {:.3e} J*s".format(popt[1]*1.6e-19))
