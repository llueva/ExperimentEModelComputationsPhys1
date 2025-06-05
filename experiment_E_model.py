
# experiment_E_model.py
"""
a simple calculator for Experiment E physics 1 project motion graphs 2:
- fits a cubic polynomial a(t) to the given data points.
- integrates to produce v(t) and x(t).
- allows user to input a time t and outputs a(t), v(t), x(t).

how to use:
  1. make sure you have numpy installed: pip install numpy
  2. run: python experiment_E_model.py
  3. at the prompt, enter a time (in seconds between 0 and 0.5) to see a(t), v(t), x(t).
"""

import numpy as np


t_data = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
a_data = np.array([2.704, 2.755, 2.646, 1.721, 0.640, 0.379])


coeffs = np.polyfit(t_data, a_data, 3)


C3, C2, C1, C0 = coeffs


def a_t(t):
    return C3*t**3 + C2*t**2 + C1*t + C0


V4 = C3 / 4
V3 = C2 / 3
V2 = C1 / 2
V1 = C0

def v_t(t):
    return V4*t**4 + V3*t**3 + V2*t**2 + V1*t


X5 = V4 / 5
X4 = V3 / 4
X3 = V2 / 3
X2 = V1 / 2

def x_t(t):
    return X5*t**5 + X4*t**4 + X3*t**3 + X2*t**2


print("the fitted acceleration coefficients (a(t) = C3*t^3 + C2*t^2 + C1*t + C0):")
print(f"  C3 = {C3:.5f}")
print(f"  C2 = {C2:.5f}")
print(f"  C1 = {C1:.5f}")
print(f"  C0 = {C0:.5f}\n")

print("the derived velocity polynomial v(t) (with v(0)=0):")
print(f"  v(t) = {V4:.5f}*t^4 + {V3:.5f}*t^3 + {V2:.5f}*t^2 + {V1:.5f}*t\n")

print("the derived position polynomial x(t) (with x(0)=0):")
print(f"  x(t) = {X5:.5f}*t^5 + {X4:.5f}*t^4 + {X3:.5f}*t^3 + {X2:.5f}*t^2\n")


while True:
    try:
        s = input("enter a time t (s) between 0 and 0.5, or 'q' to quit: ").strip().lower()
        if s == 'q':
            print("see ya!")
            break
        t_val = float(s)
        if not (0 <= t_val <= 0.5):
            print("  please enter a value between 0 and 0.5.")
            continue
        a_val = a_t(t_val)
        v_val = v_t(t_val)
        x_val = x_t(t_val)
        print(f"  a({t_val:.3f}) = {a_val:.5f} m/s^2")
        print(f"  v({t_val:.3f}) = {v_val:.5f} m/s")
        print(f"  x({t_val:.3f}) = {x_val:.5f} m\n")
    except ValueError:
        print("  -- this is an invalid input. type a number (e.g. 0.12) or just 'q' to quit this calculator ;).")
