import MalmoPython
import json
import logging
import math
import os
import random
import sys
import time
import Tkinter as tk

class visualization:
    """GUI Display for Agent to Visualize The Environment"""

    def __init__(self, x = 21, y = 21):
        self._world_x = x
        self._world_y = y
        self.init_canvas()
        self._matrix = [['None' for x in range(self._world_x)] for y in range(self._world_y)]


    def init_canvas(self, scale = 20):
        """Set-up the Canvas"""
        self._scale = scale
        root = tk.Tk()
        root.wm_title("Environment")
        canvas = tk.Canvas(root, width=self._world_x*scale, height=self._world_y*scale, borderwidth=0, highlightthickness=0, bg="black")
        canvas.grid()
        root.update()
        self._root = root
        self._canvas = canvas

    def get_entities(self, ent):
        self._ent = ent

    def get_environment(self, env):
        self._env = env

    def get_matrix(self):
        return self._matrix

    def draw(self):
        """Update and Draw the Environment"""

        # Drawing the Grid and Enemies Position
        for x in range(self._world_x):
            for y in range(self._world_y):
                self._canvas.create_rectangle((self._world_x - 1 - x) * self._scale,
                                              (self._world_y - 1 - y) * self._scale,
                                              (self._world_x - 1 - x + 1) * self._scale,
                                              (self._world_y - 1 - y + 1) * self._scale,
                                              outline="#fff", fill="#000")
                self._matrix[x][y] = "clear"
                if self._env[x][y] == "stone":
                    self._canvas.create_rectangle((self._world_x - 1 - x) * self._scale,
                                                  (self._world_y - 1 - y) * self._scale,
                                                  (self._world_x - 1 - x + 1) * self._scale,
                                                  (self._world_y - 1 - y + 1) * self._scale,
                                                  outline="#fff", fill="#00f")
                    self._matrix[x][y] = "blocked"

                if self._ent[x][y] != "None":
                    self._canvas.create_rectangle((self._world_x - 1 - x) * self._scale,
                                                  (self._world_y - 1 - y) * self._scale,
                                                  (self._world_x - 1 - x + 1) * self._scale,
                                                  (self._world_y - 1 - y + 1) * self._scale,
                                                  outline="#fff", fill="#f00")
                    self._matrix[x][y] = "enemy"



        # Agent Position
        x = self._world_x // 2
        y = self._world_y // 2
        self._canvas.create_oval((self._world_x-1-x)*self._scale,
                                      (self._world_y-1-y)*self._scale,
                                      (self._world_x-1-x+1)*self._scale,
                                      (self._world_y-1-y+1)*self._scale,
                                      outline="#fff", fill="#0f0")

        self._root.update()
