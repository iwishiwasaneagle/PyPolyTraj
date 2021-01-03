import numpy as np
from typing import TypeVar

T = TypeVar('T', bound='QuinticPolynomialTrajectory')

def _type_check(var, expected, length):
    if not isinstance(var, expected):
        raise TypeError(f"Type {expected} expected. {type(var)} received")
    if len(var) != length:
        raise TypeError(f"Input {var} is not of length {length} (actual:{len(var)}).")

class QuinticPolynomialTrajectory:
    def __init__(self, start_pos: np.ndarray, dest_pos: np.ndarray, start_vel: np.ndarray, dest_vel: np.ndarray, start_acc: np.ndarray, dest_acc: np.ndarray, T: float) -> T:

        _type_check(start_pos, (list, tuple, np.ndarray), 2)
        _type_check(dest_pos,  (list, tuple, np.ndarray), 2) 
        _type_check(start_vel, (list, tuple, np.ndarray), 2) 
        _type_check(dest_vel,  (list, tuple, np.ndarray), 2) 
        _type_check(start_acc, (list, tuple, np.ndarray), 2) 
        _type_check(dest_acc,  (list, tuple, np.ndarray), 2) 

        assert(isinstance(T, float))

        self.start_pos = start_pos
        self.dest_pos = dest_pos

        self.start_vel = start_vel
        self.dest_vel = dest_vel

        self.start_acc = start_acc
        self.dest_acc = dest_acc

        self.T = T

        self.solve()

    def solve(self) -> None:
        A = np.array(
            [[0, 0, 0, 0, 0, 1],  # f(t=0)
             [self.T**5, self.T**4, self.T**3, self.T**2, self.T, 1],  # f(t=T)
             [0, 0, 0, 0, 1, 0],  # f'(t=0)
             [5*self.T**4, 4*self.T**3, 3*self.T **
                 2, 2*self.T, 1, 0],  # f'(t=T)
             [0, 0, 0, 2, 0, 0],  # f''(t=0)
             [20*self.T**3, 12*self.T**2, 6*self.T, 2, 0, 0]  # f''(t=T)
             ])

        b_x = np.array(
            [[self.start_pos[0]],
             [self.dest_pos[0]],
             [self.start_vel[0]],
             [self.dest_vel[0]],
             [self.start_acc[0]],
             [self.dest_acc[0]]
             ])

        b_y = np.array(
            [[self.start_pos[1]],
             [self.dest_pos[1]],
             [self.start_vel[1]],
             [self.dest_vel[1]],
             [self.start_acc[1]],
             [self.dest_acc[1]]
             ])

        self.coeffs = {'x': np.linalg.solve(A, b_x), 
                       'y': np.linalg.solve(A, b_y)}

    def acceleration(self, t: float) -> np.ndarray:
        def calc(c, t): return 20 * c[0] * t**3 + \
            12 * c[1] * t**2 + 6 * c[2] * t + 2 * c[3]
        xdd = calc(self.coeffs['x'], t)
        ydd = calc(self.coeffs['y'], t)
        return np.array([xdd,ydd]).flatten()

    def velocity(self, t: float) -> np.ndarray:
        def calc(c, t): return 5 * c[0] * t**4 + 4 * c[1] * \
            t**3 + 3 * c[2] * t**2 + 2 * c[3] * t + c[4]
        xd = calc(self.coeffs['x'], t)
        yd = calc(self.coeffs['y'], t)
        return np.array([xd,yd]).flatten()

    def position(self, t: float) -> np.ndarray:
        def calc(c, t): return c[0] * t**5 + c[1] * t**4 + \
            c[2] * t**3 + c[3] * t**2 + c[4] * t + c[5]
        x = calc(self.coeffs['x'], t)
        y = calc(self.coeffs['y'], t)
        return np.array([x,y]).flatten()
