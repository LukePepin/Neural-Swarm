# Neural-Swarm: Graduate-Level Catchup

Welcome back to the Neural-Swarm project! This document serves as a high-level overview of the architectural shift from your undergraduate work (2024) to the new graduate-level scope.

## The Old Project (Undergraduate Phase)
- **Tech Stack**: ROS 2 Foxy, Gazebo Classic, Python.
- **Hardware**: Generic simulated differential drive robots.
- **Goal**: Basic neural network implementation for swarm decision-making under communication and sensor constraints.
- *Note*: The old state has been preserved as a git tag (`v1.0.0-undergrad`). The old data, URDFs, and worlds have been wiped from the working directory to make room for the new architecture.

## The New Project (Graduate Phase)
- **Tech Stack**: ROS 2 Humble (Ubuntu 22.04), Micro-ROS, PyTorch, Gazebo.
- **Hardware**: Physical Arduino Alviks (ESP32-based) and their Digital Twins.
- **Goal**: Environment mapping with limited compute. The swarm navigates 2D walled environments using Multi-Agent Reinforcement Learning (MARL), returning to an entry point to offload data. The central host ingests this data to reconstruct the environment.

## Current Repository Structure
- `micro_ros/`: Scripts and nodes for the host to communicate with the physical Alviks over Wi-Fi.
- `host_node/`: The central intelligence running on the host machine (e.g., `environment_builder.py` for map reconstruction).
- `marl_training/`: PyTorch pipelines to train the tiny ML models that will run on the Alviks' ESP32 chips.
- `launch/`: Contains `graduate_swarm.launch.py` to bring up the host ecosystem.
- `task.md`: The active checklist tracking our progression through the 5 phases of development.

## Next Technical Milestones
1. **Digital Twin**: We need to define the Alvik in URDF/SDF and get it running in a modern Gazebo simulation.
2. **Firmware**: We need to write the C++ micro-ROS firmware for the physical Alviks.
3. **MARL**: Training the swarm to explore efficiently and return home.
