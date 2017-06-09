import MalmoPython, json, logging, math, os, random, sys, time
import Tkinter as tk

class visualization:
    """
        The class introduced a GUI Displayed for Agent to 
        Visualize The Environment, including the size of the
        matrix we showed on Tkinter, entities and envrionments,
        and a smaller canvas to show a vertical view of 
        the game map. The default size of the game matrix
        is 11 x 11.
    """

    def __init__(self, x = 21, y = 21, debug=False):
        self._world_x = x
        self._world_y = y
        self._matrix = [['None' for x in range(self._world_x)] for y in range(self._world_y)]
        self.debug = debug
        if self.debug:
            self.init_canvas()


    def init_canvas(self, scale = 20):
        """
            Initialize the Canvas (the game map) to provide a
            more direct vertical view for the purpose of testing
        """
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
        """
            Update and Draw the Environment, with showing
            corresponding object in each position, including
            "clear", "blocked", and "enemy".
        """

        # Drawing the Grid and Enemies Position
        for x in range(self._world_x):
            for y in range(self._world_y):
                if self.debug:
                    self._canvas.create_rectangle((self._world_x - 1 - x) * self._scale,
                                                  (self._world_y - 1 - y) * self._scale,
                                                  (self._world_x - 1 - x + 1) * self._scale,
                                                  (self._world_y - 1 - y + 1) * self._scale,
                                                  outline="#fff", fill="#000")
                self._matrix[self._world_y - 1 - y][self._world_x - 1 - x] = "clear"

                if self._env[x][y] == "stone":
                    if self.debug:
                        self._canvas.create_rectangle((self._world_x - 1 - x) * self._scale,
                                                      (self._world_y - 1 - y) * self._scale,
                                                      (self._world_x - 1 - x + 1) * self._scale,
                                                      (self._world_y - 1 - y + 1) * self._scale,
                                                      outline="#fff", fill="#00f")
                    self._matrix[self._world_y - 1 - y][self._world_x - 1 - x] = "blocked"

                if self._ent[x][y] != "None":
                    if self.debug:
                        self._canvas.create_rectangle((self._world_x - 1 - x) * self._scale,
                                                      (self._world_y - 1 - y) * self._scale,
                                                      (self._world_x - 1 - x + 1) * self._scale,
                                                      (self._world_y - 1 - y + 1) * self._scale,
                                                      outline="#fff", fill="#f00")
                    self._matrix[self._world_y - 1 - y][self._world_x - 1 - x ]= "enemy"

        # Update the Agent Position
        x = self._world_x // 2
        y = self._world_y // 2

        if self.debug:
            self._canvas.create_oval((self._world_x-1-x)*self._scale,
                                          (self._world_y-1-y)*self._scale,
                                          (self._world_x-1-x+1)*self._scale,
                                          (self._world_y-1-y+1)*self._scale,
                                          outline="#fff", fill="#0f0")

            self._root.update()

    def quit(self):
        self._root.destroy()
