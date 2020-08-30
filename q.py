import gym
import matplotlib as plt

enviroment = gym.make("MountainCar-v0")
enviroment.reset()

finished = False

while not finished:
	action = 2
	new_state, reward, done, _ = enviroment.step(action)
	enviroment.render()

enviroment.close()