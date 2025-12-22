"""
Author: IchBinJade
Date  : 2025-12-19
AoC 2025 Day 8 - https://adventofcode.com/2025/day/8
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import combinations


class Node:
    """
    Represents a single junction box with XYZ coords
    """
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.coords = (x, y, z)
        
    def __repr__(self):
        return f"Box {self.id}: {self.coords}"
    
    def calc_distance_to(self, next_box):
        """
        Calculate the Euclidean distance to next box
        d^2(P_1, P_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2
        """
        nx = self.x - next_box.x
        ny = self.y - next_box.y
        nz = self.z - next_box.z
        
        return nx**2 + ny**2 + nz**2


class Graph:
    """
    Represents collections of junction boxes and their coords
    """
    def __init__(self):
        self.boxes = {}
        self.edges = []
        self.next_id = 1
        self.parent = {}
        self.size = {}
        
    def __repr__(self):
        boxes = len(self.boxes)
        edges = len(self.edges)
        circuits = len(self.size)
        return f"Graph has {boxes} boxes/nodes & {edges} edges & {circuits} circuits"
    
    def add_box(self, x, y, z):
        new_box = Node(self.next_id, x, y, z)
        self.boxes[self.next_id] = new_box
        
        # Init DSU state
        self.parent[self.next_id] = self.next_id
        self.size[self.next_id] = 1
        
        self.next_id += 1
        return new_box
    
    def create_and_sort_edges(self):
        all_nodes = list(self.boxes.values())
        
        for node_a, node_b in combinations(all_nodes, 2):
            dist = node_a.calc_distance_to(node_b)
            self.edges.append((dist, node_a.id, node_b.id))
            
        self.edges.sort()
        
    def find(self, id):
        if self.parent[id] == id:
            return id
        
        self.parent[id] = self.find(self.parent[id])
        return self.parent[id]
    
    def union(self, id1, id2):
        root1, root2 = self.find(id1), self.find(id2)
        if root1 != root2:
            if self.size[root1] < self.size[root2]:
                root1, root2 = root2, root1
                
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
            del self.size[root2]
            return True
        
        return False
        
    def make_connections(self, limit):
        connections = 0
        for _, id1, id2 in self.edges:
            if connections == limit:
                break
            self.union(id1, id2)
            connections += 1


def part_one(data_input):
    graph = Graph()
    box_list = [tuple(int(coord) for coord in item.split(",")) for item in data_input]
    
    # populate the graph
    for x, y, z in box_list:
        graph.add_box(x, y, z)
    
    graph.create_and_sort_edges()
    graph.make_connections(1000)
    
    sizes = list(graph.size.values())
    sizes.sort(reverse=True)
    
    return sizes[0] * sizes[1] * sizes[2]


def part_two(data_input):
    graph = Graph()
    box_list = [tuple(int(coord) for coord in item.split(",")) for item in data_input]
    
    # populate the graph
    for x, y, z in box_list:
        graph.add_box(x, y, z)
    
    graph.create_and_sort_edges()
    
    for _, id1, id2 in graph.edges:
        if graph.union(id1, id2):
            if len(graph.size) == 1:
                box1, box2 = graph.boxes[id1], graph.boxes[id2]
                return box1.x * box2.x



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(8, 2025)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
