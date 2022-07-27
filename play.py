import os
import tensorflow as tf
from agent import *

def play_with_agent(params):
    
    if not os.path.exists(params.gif_path):
        os.makedirs(params.gif_path)
    
    configs = tf.compat.v1.ConfigProto()
    configs.gpu_options.allow_growth = True
    
    tf.compat.v1.reset_default_graph()

    with tf.compat.v1.Session(config = configs) as sess:
        print("what is state_size", state_size)
        Agent = Worker(0, state_size, action_size, player_mode=True)

        print('Loading Model...')
        saver = tf.compat.v1.train.Saver()
        ckpt = tf.compat.v1.train.get_checkpoint_state(params.model_path)
        print("what uis the path ", params.model_path)
        saver.restore(sess, ckpt.model_checkpoint_path)
        print('Successfully loaded!')

        Agent.play_game(sess, params.play_episodes)