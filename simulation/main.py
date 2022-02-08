import simulation

if __name__ == '__main__':
    SIMULATION_RUN_TIME = 25 #8*60 todo
    seed = 1234

    sim = simulation.Simulation(SIMULATION_RUN_TIME, seed)

    sim.start()
