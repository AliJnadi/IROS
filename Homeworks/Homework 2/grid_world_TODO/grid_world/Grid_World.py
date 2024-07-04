import numpy as np

from random import sample
import copy

class Grid_World:
    rows = []
    cols = []

    # Obstacles and thier locations
    obs = []
    obs_loc = None

    # Start and end positions
    start = []
    end = []

    # Player coordinates
    player = []
    score = None

    # State Matrix
    state = []

    # Block
    block_size = []
    block_boarders = []
    scale = []
    block = []

    # image 
    world = [] 
    image_boarder = []

    def __init__(self, rows = 4, cols = 5, obs = 3) -> None:
        self.rows = rows
        self.cols = cols
        
        self.obs = obs

        self.start = (0, 0)
        self.end = (rows - 1, cols - 1)

        self.player = self.start

        # Generate obstacles randomly
        if obs > 0:
            temp = [(i, j) for i in range(1, rows-1) for j in range(1, cols)]
            self.obs_loc = [temp[i] for i in sample(range(0, (rows - 2) * (cols - 1)), obs)]
        
        # initialize the World
        self.init_world()

    def init_world(self, scale = 4, block_size = 30, block_boarders = 2):
        self.block_size = block_size * scale
        self.block_boarders = block_boarders * scale

        # Define block
        block_size *= scale
        block_boarders *= scale   
        self.block = np.zeros(shape=(block_size, block_size, 3),dtype=np.uint8)
        block = self.block
        
        shift = int(np.floor(block_boarders/2))
        block[shift + 1 : block_size - shift, shift + 1: block_size - shift, :] = 255

        rows, cols = self.rows, self.cols 

        # Initialize state matrix
        self.state = np.zeros((rows, cols), dtype=int)

        self.img_boarders = (block_boarders + 1) * 2
        img_boarders = self.img_boarders

        self.world = np.zeros([rows * block_size + img_boarders, cols * block_size + img_boarders, 3], dtype=np.uint8)

        # Build the grid world
        for i in range(0, rows):
            if i == 0:
                r_idx = int(img_boarders / 2)
            else:
                r_idx += block_size 

            for j in range(0, cols):
                if j == 0:
                    c_idx = int(img_boarders / 2)
                else:
                    c_idx += block_size 
                
                # Represent the obstacles as red blocks, also assign -1 in state matrix
                if (i, j) in self.obs_loc:
                    self.state[i, j] = -1
                    self.world[r_idx : r_idx + block_size, c_idx : c_idx + block_size, 2] = block[:, :, 2]
                    continue
                # Represent the terminal state as green block also assign +2 in state matrix
                elif (i, j) == self.end:
                    self.state[i, j] = 2
                    self.world[r_idx : r_idx + block_size, c_idx : c_idx + block_size, 1] = block[:, :, 1]
                    continue
                
                self.world[r_idx : r_idx + block_size, c_idx : c_idx + block_size, :] = block[:]

        self.state[self.player] = 1
        self.score = 0


    def world_update(self):
        img = copy.deepcopy(self.world)

        assert self.player not in self.obs_loc, 'Error Player cannot stand in obstacles blocks'
            

        r_idx = int(self.img_boarders / 2) + self.player[0] * self.block_size
        shift = 40
        c_idx = int(self.img_boarders / 2) + self.player[1] * self.block_size

        img[r_idx + shift: r_idx + self.block_size - shift, c_idx + shift : c_idx + self.block_size - shift, 1:3] = self.block[0 : self.block_size - 2 * shift, 0 : self.block_size - 2 * shift, 1:3] * 0

        return img

def main():
    grid_world = Grid_World()

    print(grid_world.state)

if __name__ == '__main__':
    main()