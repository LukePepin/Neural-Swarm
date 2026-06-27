# Graduate-Level Upgrade Task List

## Phase 1: Environment & Project Restructuring
- `[x]` Update `package.xml` and `CMakeLists.txt` for ROS 2 Humble compatibility.
- `[ ]` Clean up obsolete ROS 2 Foxy / old robot dependencies.
- `[x]` Set up the directory structure for Micro-ROS integration, ML training, and Digital Twin bridging.

## Phase 2: Micro-ROS & Hardware Integration
- `[x]` Create launch files to spin up the Micro-ROS agent on the host computer.
- `[ ]` Draft the firmware interface structure for the Arduino Alvik (ESP32) to communicate over Micro-ROS (subscriptions for cmd_vel, publishers for ToF/sensors).
- `[x]` Create a data ingestion node on the host computer that listens for the Alviks returning to the "entry point" and aggregating their sensor data.

## Phase 3: Digital Twin Simulation (Gazebo)
- `[ ]` Define a URDF/SDF for the Arduino Alvik with accurate kinematics and the forward-facing camera plugin for ROS 2 Humble.
- `[ ]` Create 2D Gazebo worlds representing simple walled environments.
- `[ ]` Implement a Python script to procedurally generate random 10x10 ft bounding box `.world` files with clustered obstacles.
- `[ ]` Implement the "Digital Twin Bridge Node" to allow real-time synchronization between physical and simulated Alviks.

## Phase 4: Multi-Agent Reinforcement Learning (MARL)
- `[ ]` Set up a PyTorch training pipeline for MARL (e.g., PPO or SAC) in the simulated environment.
- `[ ]` Define the reward function (exploring unmapped areas, returning to the entry point, collision avoidance).
- `[ ]` Implement model export scripts (e.g., converting the trained PyTorch model to TensorFlow Lite for Microcontrollers or a raw C array for the ESP32).

## Phase 5: Host Environment Reconstruction
- `[x]` Develop a Python node on the host to ingest the aggregated swarm data.
- `[ ]` Implement an algorithm (e.g., occupancy grid mapping or pose graph optimization) to reconstruct the 2D environment from the scattered Alvik scans.
- `[ ]` Create a visualization tool (e.g., using RViz2) to display the reconstructed map versus the ground truth.
