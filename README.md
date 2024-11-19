Rocket Landing with Double DQN

Goal - To train an agent to control a rocket and land it safely on the ground. The rocket starts at a certain position with some initial velocity, and the agent learns to control the rocket's thrust and rotation to achieve a soft landing.

Custom environment using OpenAI's Gym interface and used PyTorch to implement the DDQN algorithm.

Repository Structure

environment/rocket_landing_env.py: This file contains the custom environment class RocketLandingEnv. It defines the rocket's physics, the action and observation spaces, and handles the rendering of the environment.

agent/dqn_agent.py: This file includes the implementation of the DDQN agent using PyTorch. Defines the neural network architecture, the agent's learning process, and how it interacts with the environment.

scripts/train.py: This is the main script to train the agent. It includes the training loop, saving the best episodes, and rendering to mp4.

requirements.txt: Lists all the Python dependencies needed to run the project.

scripts/: A folder where the videos of the best episodes are saved.

-------------------------

Code Explanation

rocket_landing_env.py ->
This file defines the RocketLandingEnv class, which is the custom environment for our rocket landing task.

State Representation: The state (observation) includes the rocket's position (x, y), velocity (vx, vy), and angle.

Action Space: The agent can choose from four discrete actions:

0: Do nothing
1: Apply thrust
2: Rotate left
3: Rotate right

Reward Function: The agent receives rewards or penalties based on its actions:
Positive reward for a safe landing.
Negative penalty proportional to the crash velocity if it crashes.
Continuous penalties for undesirable states like high velocity or large angles.

Rendering: The environment uses Pygame for rendering. It displays the rocket, the ground, and shows the rocket's velocity and angle on the screen.

dqn_agent.py ->
This file contains the implementation of the DDQN agent.

Neural Network Architecture: The Q-network is a simple feedforward neural network with two hidden layers.

Memory Buffer: The agent uses experience replay to store and sample past experiences.

Learning Process: The agent updates its Q-network by minimizing the difference between predicted and target Q-values.

Action Selection: Uses an epsilon-greedy policy to balance exploration and exploitation.


train.py ->
Training Loop: Runs multiple episodes where the agent interacts with the environment and learns from its experiences.

Saving Best Episodes: Keeps track of the top 3 episodes based on the total reward and saves their actions and seeds.

Rendering and Saving Videos: After training, it replays the best episodes, captures the frames, and saves them as video files using moviepy.

requirements.txt ->
Lists some of the required Python packages:

scripts/ ->
This folder will also contain the videos of the best episodes after training. The videos will be named best_episode_1.mp4, best_episode_2.mp4, and best_episode_3.mp4.

Customizations and Features ->
Dynamic Crash Penalty: The reward function has been modified so that the penalty for crashing is proportional to the crash velocity. This encourages the agent to attempt softer landings.

Display of Velocity and Angle: During rendering, the rocket's current velocity and angle are displayed on the screen, allowing for better visualization of the agent's performance.

How to Modify the Training Parameters ->
You can adjust the training parameters in train.py:

Number of Episodes: Change the n_episodes parameter in the train_agent function call.

Hyperparameters: Modify the agent's hyperparameters like learning rate, epsilon decay, etc., in the DoubleQAgent initialization.
