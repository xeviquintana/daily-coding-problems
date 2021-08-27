"""
PROBLEM 14 [MEDIUM]

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""
from multiprocessing import Pool
import math
from multiprocessing.pool import MapResult
import random
import time


class Point:
    def __init__(self):
        self.x = random.uniform(0, 1)
        self.y = random.uniform(0, 1)

    def get_hypotenuse(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def build_point_list(size: int) -> list['Point']:
        points: list[Point] = list()
        for _ in range(size):
            points.append(Point())
        return points


class SimpleSolver:

    def is_in_circle(p: Point) -> bool:
        return p.get_hypotenuse() <= 1

    def estimate_pi(points: list[Point]) -> float:
        in_circle: int = 0
        for p in points:
            in_circle += SimpleSolver.is_in_circle(p)
            
        return 4.0 * in_circle / len(points)


class AdvancedSolver:    

    def estimate_pi_async(points: list[Point]) -> float:
        with Pool(processes=16) as pool:
            r: MapResult = pool.map_async(SimpleSolver.is_in_circle, points)
            r.wait()
            outputs: list[bool] = r.get()
            return 4.0 * sum(outputs) / len(points)
    
    def estimate_pi_sync(points: list[Point]) -> float:
        with Pool(processes=16) as pool:
            outputs: list[int] = pool.map(SimpleSolver.is_in_circle, points)
            return 4.0 * sum(outputs) / len(points)


if __name__ == "__main__":
    sizes: list[int] = [100, 1000, 10000, 100000, 1000000, 10000000]

    for size in sizes:
        points: list[Point] = Point.build_point_list(size)

        start_time = time.time()
        print("Simple approach - {} loops: {}".format(size, SimpleSolver.estimate_pi(points)))
        print("\t--- {} seconds ---".format(time.time() - start_time))

        start_time = time.time()
        print("Pool map sync approach - {} loops: {}".format(size, AdvancedSolver.estimate_pi_sync(points)))
        print("\t--- {} seconds ---".format(time.time() - start_time))

        start_time = time.time()
        print("Pool map async approach - {} loops: {}".format(size, AdvancedSolver.estimate_pi_async(points)))
        print("\t--- {} seconds ---".format(time.time() - start_time))
