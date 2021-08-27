"""
PROBLEM 14 [MEDIUM]

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""
from multiprocessing import Manager, Pool, Process, Value
import math
from multiprocessing.pool import MapResult
import random
import time
from functools import reduce


class Point:
    def __init__(self) -> None:
        self.x = random.uniform(0, 1)
        self.y = random.uniform(0, 1)

    def get_hypotenuse(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    @classmethod
    def build_point_list(cls, size: int) -> list['Point']:
        points: list[Point] = list()
        for _ in range(size):
            points.append(Point())
        return points
    
    def is_in_circle(self) -> bool:
        return self.get_hypotenuse() <= 1


class SimpleSolver:

    @classmethod
    def estimate_pi(cls, points: list[Point]) -> float:
        in_circle: int = 0
        for p in points:
            in_circle += p.is_in_circle()
            
        return 4.0 * in_circle / len(points)


class AdvancedSolver:
    def __init__(self, processes: int, chunksize: int) -> None:
        self.processes = processes
        self.chunksize = chunksize
    
    def estimate_pi_sync(self, points: list[Point]) -> float:
        with Pool(processes=self.processes) as pool:
            outputs: list[int] = pool.map(Point.is_in_circle, points, chunksize=self.chunksize)
        
        return 4.0 * sum(outputs) / len(points)
    
    @classmethod
    def estimate_pi_map_reduce(cls, points: list[Point]) -> float:
        in_circle: int = reduce((lambda x, y: x + y), map(Point.is_in_circle, points))
        
        return 4.0 * in_circle / len(points)
    

if __name__ == "__main__":
    sizes: list[int] = [10000, 100000, 1000000, 10000000, 100000000]
    one_process_solver: AdvancedSolver = AdvancedSolver(processes=1, chunksize=10000)
    two_processes_solver: AdvancedSolver = AdvancedSolver(processes=2, chunksize=10000)
    four_processes_solver: AdvancedSolver = AdvancedSolver(processes=4, chunksize=10000)
    one_process_solver_bigger: AdvancedSolver = AdvancedSolver(processes=1, chunksize=1000000)
    two_processes_solver_bigger: AdvancedSolver = AdvancedSolver(processes=2, chunksize=1000000)
    four_processes_solver_bigger: AdvancedSolver = AdvancedSolver(processes=4, chunksize=1000000)
    
    for size in sizes:
        points: list[Point] = Point.build_point_list(size)

        start_time = time.time()
        print("Map-reduce approach - {} loops: {}".format(size, AdvancedSolver.estimate_pi_map_reduce(points)))
        print("\t--- {} seconds ---".format(time.time() - start_time))

        start_time = time.time()
        print("One process solver - sync approach - {} loops: {}".format(size, one_process_solver.estimate_pi_sync(points)))
        print("\t--- {} seconds ---".format(time.time() - start_time))

        start_time = time.time()
        print("Two processes solver - sync approach - {} loops: {}".format(size, two_processes_solver.estimate_pi_sync(points)))
        print("\t--- {} seconds ---".format(time.time() - start_time))

        start_time = time.time()
        print("Four processes solver - sync approach - {} loops: {}".format(size, four_processes_solver.estimate_pi_sync(points)))
        print("\t--- {} seconds ---".format(time.time() - start_time))

        start_time = time.time()
        print("One process solver bigger chunk size - sync approach - {} loops: {}".format(size, one_process_solver_bigger.estimate_pi_sync(points)))
        print("\t--- {} seconds ---".format(time.time() - start_time))

        start_time = time.time()
        print("Two processes solver bigger chunk size - sync approach - {} loops: {}".format(size, two_processes_solver_bigger.estimate_pi_sync(points)))
        print("\t--- {} seconds ---".format(time.time() - start_time))

        start_time = time.time()
        print("Four processes solver bigger chunk size - sync approach - {} loops: {}".format(size, four_processes_solver_bigger.estimate_pi_sync(points)))
        print("\t--- {} seconds ---".format(time.time() - start_time))

        """
        Map-reduce approach - 10000 loops: 3.1632
                --- 0.005001544952392578 seconds ---
        One process solver - sync approach - 10000 loops: 3.1632
                --- 0.13395929336547852 seconds ---
        Two processes solver - sync approach - 10000 loops: 3.1632
                --- 0.14804577827453613 seconds ---
        Four processes solver - sync approach - 10000 loops: 3.1632
                --- 0.1645064353942871 seconds ---
        One process solver bigger chunk size - sync approach - 10000 loops: 3.1632
                --- 0.12923359870910645 seconds ---
        Two processes solver bigger chunk size - sync approach - 10000 loops: 3.1632
                --- 0.1439955234527588 seconds ---
        Four processes solver bigger chunk size - sync approach - 10000 loops: 3.1632
                --- 0.17755746841430664 seconds ---
        Map-reduce approach - 100000 loops: 3.14896
                --- 0.041008949279785156 seconds ---
        One process solver - sync approach - 100000 loops: 3.14896
                --- 0.2259984016418457 seconds ---
        Two processes solver - sync approach - 100000 loops: 3.14896
                --- 0.23600363731384277 seconds ---
        Four processes solver - sync approach - 100000 loops: 3.14896
                --- 0.2765684127807617 seconds ---
        One process solver bigger chunk size - sync approach - 100000 loops: 3.14896
                --- 0.24117779731750488 seconds ---
        Two processes solver bigger chunk size - sync approach - 100000 loops: 3.14896
                --- 0.25800275802612305 seconds ---
        Four processes solver bigger chunk size - sync approach - 100000 loops: 3.14896
                --- 0.2840719223022461 seconds ---
        Map-reduce approach - 1000000 loops: 3.143312
                --- 0.43048810958862305 seconds ---
        One process solver - sync approach - 1000000 loops: 3.143312
                --- 1.4372994899749756 seconds ---
        Two processes solver - sync approach - 1000000 loops: 3.143312
                --- 1.1555604934692383 seconds ---
        Four processes solver - sync approach - 1000000 loops: 3.143312
                --- 1.1966102123260498 seconds ---
        One process solver bigger chunk size - sync approach - 1000000 loops: 3.143312
                --- 2.5235981941223145 seconds ---
        Two processes solver bigger chunk size - sync approach - 1000000 loops: 3.143312
                --- 2.538066864013672 seconds ---
        Four processes solver bigger chunk size - sync approach - 1000000 loops: 3.143312
                --- 2.5922837257385254 seconds ---
        Map-reduce approach - 10000000 loops: 3.142222
                --- 4.420398950576782 seconds ---
        One process solver - sync approach - 10000000 loops: 3.142222
                --- 12.132107496261597 seconds ---
        Two processes solver - sync approach - 10000000 loops: 3.142222
                --- 10.174471139907837 seconds ---
        Four processes solver - sync approach - 10000000 loops: 3.142222
                --- 10.868808507919312 seconds ---
        One process solver bigger chunk size - sync approach - 10000000 loops: 3.142222
                --- 17.735909461975098 seconds ---
        Two processes solver bigger chunk size - sync approach - 10000000 loops: 3.142222
                --- 17.031863927841187 seconds ---
        Four processes solver bigger chunk size - sync approach - 10000000 loops: 3.142222
                --- 16.382593154907227 seconds ---
        Map-reduce approach - 100000000 loops: 3.14189924
                --- 194.81965398788452 seconds ---
        One process solver - sync approach - 100000000 loops: 3.14189924
                --- 222.40667748451233 seconds ---
        Two processes solver - sync approach - 100000000 loops: 3.14189924
                --- 219.732342004776 seconds ---
        Four processes solver - sync approach - 100000000 loops: 3.14189924
                --- 220.32443809509277 seconds ---
        One process solver bigger chunk size - sync approach - 100000000 loops: 3.14189924
                --- 249.75499820709229 seconds ---
        Two processes solver bigger chunk size - sync approach - 100000000 loops: 3.14189924
                --- 250.55771803855896 seconds ---
        Four processes solver bigger chunk size - sync approach - 100000000 loops: 3.14189924
                --- 256.0891664028168 seconds ---
        """