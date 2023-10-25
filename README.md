# 🐜 Ant Colony Optimization Pathfinding
![Real-time Obstacle Avoidance_test#2](https://github.com/SAIPRONE/Real-Time-Obstacle-Avoidance/assets/95390348/e1c0239b-c3f7-4d99-9826-3ab650e1fffe)
![Real-time Obstacle Avoidance_test#4](https://github.com/SAIPRONE/Real-Time-Obstacle-Avoidance/assets/95390348/97386eaf-f880-4bb1-8f22-880506a53f26)
![Real-time Obstacle Avoidance_test#6](https://github.com/SAIPRONE/Real-Time-Obstacle-Avoidance/assets/95390348/fd3b5fcd-ee3a-4157-912c-71562f293c7d)

This repository implements the Ant Colony Optimization (ACO) algorithm for pathfinding in a grid world with obstacles. The graphical representation of the grid world and the path is achieved using the `tkinter` library.

## 🌟 Features
- 🔀 Random generation of obstacles in the grid.
- 📊 Visualization of the pathfinding process using ACO.
- 🔄 A button to generate new obstacles and re-run the ACO pathfinding.

## 🛠️ Prerequisites
To run the code, you need to have Python installed on your machine along with the `numpy` and `tkinter` libraries.

## 🚀 Usage
1. Clone the repository.
2. Run the script.
3. A window will pop up showing the grid world. Click on the "Generate Obstacles" button to randomly generate obstacles and visualize the pathfinding using ACO.
4. If a path from the start to the end is not found due to the obstacles, a message "Path blocked. Please try again." will be displayed in the console.

## 📖 Code Structure

- `generate_obstacles(world, num_obstacles)`: Generates random obstacles in the grid.
- `ACO`: A class implementing the ACO algorithm.
    - `choose_direction(ant_pos, visited)`: Determines the direction an ant should move based on the pheromone levels and the heuristic.
    - `find_path()`: Allows an ant to find a path from the start to the end.
    - `simulate_ants(num_iterations)`: Simulates the movement of multiple ants and updates the pheromone levels.
    - `draw_world(canvas, world, path)`: Draws the grid world, obstacles, and the path on the canvas.
- `generate_new_obstacles()`: Generates new obstacles, runs the ACO algorithm, and updates the visual representation.

## 👤 Author
Fadi Helal

## 🔖 License
This project is open-source and available under the BSD3 License.

## 📚 Sources
For more information about the Ant Colony Optimization algorithm:
- [Ant Colony Optimization](https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms) - Wikipedia
- [Intelligent Optimization Algorithm-Based Path Planning for a Mobile Robot]([https://www.scholarpedia.org/article/Ant_colony_optimization](https://www.hindawi.com/journals/cin/2021/8025730/)https://www.hindawi.com/journals/cin/2021/8025730/) 

