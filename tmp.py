 if ((self.grid_data[Y+i][X+j] == self.turn*-1 for j in range(-1, 1)) for i in range(-1, 1)):
                        for i in range(-1, 1):
                            for j in range(-1, 1):
                                if self.grid_data[Y+i][X+j] == self.turn*-1:
                                    for n in range():
                                        if self.grid_data[Y+i*(n+1)][X+j*(n+1)] != self.turn*-1:
                                            break
                                        else:
                                            self.turn_pieces += 1