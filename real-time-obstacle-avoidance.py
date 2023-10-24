# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:08:28 2023

@author: Fadi Helal
"""

import numpy as np
import tkinter as tk
from tkinter import Canvas
obstacles = [
    (3,0), (4,0), (5,0), (6,0), (7,0), (8,0),
    (2,1), (3,1), (4,1), (5,1), (6,1), (7,1),
    (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2), (8,2), (9,2),
    (0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3), (8,3),
    (0,4), (1,4), (5,4), (6,4), (7,4), (8,4),
    (0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5), (11,5), (12,5),
    (0,6), (1,6), (2,6), (3,6), (4,6), (11,6), (12,6),
    (0,7), (1,7), (2,7), (3,7), (11,7), (12,7),
    (0,8), (1,8), (2,8), (3,8), (9,8), (10,8), (11,8), (12,8),
    (0,9), (1,9), (2,9), (9,9), (10,9), (11,9), (12,9),
    (0,10), (1,10), (8,10), (9,10),
    (8,11), (9,11), (10,11), (11,11), (12,11),
    (8,12), (9,12), (10,12),
    (6,13), (7,13), (8,13), (9,13),
    (6,14), (7,14)
]
# Grid dimensions
width = 21
height = 21
grid_size = 21
start = (0, 0)
end = (grid_size-1, grid_size-1)

import numpy as np
import random

def generate_obstacles(world, num_obstacles=50):
    for _ in range(num_obstacles):
        x = random.randint(0, world.shape[0]-1)
        y = random.randint(0, world.shape[1]-1)
        world[x, y] = 1
    return world


class ACO:
    def __init__(self, start, end, world):
        self.world = world
        self.start = start
        self.end = end
        self.pheromone = np.ones(world.shape) * 1e-5
        self.attractiveness = 1 / (world + 1e-5)
        self.num_ants = 10
        self.decay = 0.1
        self.alpha = 1
        self.beta = 5

    def choose_direction(self, ant_pos, visited):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        transition_probs = np.zeros(4, dtype=float)
    
        for idx, (dx, dy) in enumerate(neighbors):
            x, y = ant_pos[0] + dx, ant_pos[1] + dy
            if 0 <= x < grid_size and 0 <= y < grid_size and self.world[x, y] == 0:
                tau = self.pheromone[x, y] ** self.alpha
                eta = (1 / self.attractiveness[x, y]) ** self.beta
                heuristic = 1 / (abs(end[0] - x) + abs(end[1] - y) + 1e-5)
                transition_probs[idx] = tau * eta * heuristic
    

        for dx, dy in neighbors:
            x, y = ant_pos[0] + dx, ant_pos[1] + dy
            if (x, y) in visited:
                transition_probs[neighbors.index((dx, dy))] = 0
    

        if np.sum(transition_probs) == 0:
            return None  
    
        transition_probs /= np.sum(transition_probs)
        direction = np.random.choice(4, p=transition_probs)
        return neighbors[direction]


    def find_path(self):
        visited = set()
        path = [self.start]
        visited.add(self.start)
        ant_pos = self.start
        max_steps = grid_size * grid_size

        for _ in range(max_steps):
            if ant_pos == self.end:
                break
            direction = self.choose_direction(ant_pos, visited)
            if direction is None:
                if len(path) > 1:
                    ant_pos = path[-2]
                    path.pop()
                    continue
                else:
                    return path
            ant_pos = (ant_pos[0] + direction[0], ant_pos[1] + direction[1])
            path.append(ant_pos)
            visited.add(ant_pos)
        return path

    def simulate_ants(self, num_iterations=10):
        for iteration in range(num_iterations):
            all_paths = [self.find_path() for _ in range(self.num_ants)]
            all_lengths = [len(p) for p in all_paths]
            shortest_path_index = np.argmin(all_lengths)

            self.pheromone *= (1 - self.decay)
            for i, path in enumerate(all_paths):
                for x, y in path:
                    if i == shortest_path_index:
                        self.pheromone[x][y] += 1.0
                    else:
                        self.pheromone[x][y] += 0.5
        return all_paths[shortest_path_index]

    @staticmethod
    def draw_world(canvas, world, path=[]):
        canvas.delete("all")
        

        for i in range(grid_size):
            for j in range(grid_size):
                if world[i, j] == 1:
                    canvas.create_rectangle(j*10, i*10, j*10+10, i*10+10, fill="black")
        

        for i in range(len(path) - 1):
            x1, y1 = path[i][1]*10 + 5, path[i][0]*10 + 5  
            x2, y2 = path[i + 1][1]*10 + 5, path[i + 1][0]*10 + 5
            canvas.create_line(x1, y1, x2, y2, fill='green', width=2)


def generate_new_obstacles():
    global world
    world = generate_obstacles(np.zeros((grid_size, grid_size)))
    aco = ACO(start, end, world)
    path = aco.simulate_ants()

    if path[-1] != end:
        print("Path blocked. Please try again.")
        return


    ACO.draw_world(canvas, world, path)
root = tk.Tk()
canvas = Canvas(root, width=grid_size*10, height=grid_size*10)
canvas.pack()
button = tk.Button(root, text="Generate Obstacles", command=generate_new_obstacles)
button.pack()
root.mainloop()