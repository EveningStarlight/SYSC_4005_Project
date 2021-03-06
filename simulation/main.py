import simulation
import sys

if __name__ == '__main__':
    SIMULATION_RUN_TIME = 30*60
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1234
    numberOfSims = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    for i in range(numberOfSims):
        sim = simulation.Simulation(SIMULATION_RUN_TIME, seed+i)
        sim.run()
