import simulation

def main():
    SIMULATION_TIME = 60*8
    seed = 1234

    sim = simulation.Simulation(SIMULATION_TIME, seed)

    sim.start()
