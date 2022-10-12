# Curiosity-exploration-in-Vizdoom
This project allows to train the agent playing two particular Vizdoom scenarios "Health Gathering Supreme" and "Deathmatch" using curiosity-based exploration strategies RND (Random Network Distillation) and ICM (Intrinsic Curiosity Motivation). The project is written on **Python 3** and uses **TensorFlow 2** framework. Exploration techniques are combined with Asynchronuos Advantage Actor Critic Reinforcement learning algorithm. The implementation is based on the project ["Deep-Reinforcement-Learning-applied-to-DOOM"](https://github.com/boubnanm/Deep-Reinforcement-Learning-applied-to-DOOM). You can visit it for the additional information on A3C architecture and other details.

## Installation
You can find all the information on getting Vizdoom to your machine on the [Vizdoom repository](https://github.com/mwydmuch/ViZDoom).

To run the project you should have these modules installed:
* tensorboard 
* tensorboardX
* moviepy
* tf_slim

## Running code
Use the command `python main.py` to start the training process. You can manage the training settings using special parameters (detailes are in utils/args.py file).
For instance, to train the agent to play "Deathmatch" scenario with RND exploration method:
```
python main.py --scenario deathmatch --use_curiosity --RND --total_episodes 100  
```
In order to test the trained model add `--play` parameter.

