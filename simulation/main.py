import simulation
import sys

if __name__ == '__main__':
    SIMULATION_RUN_TIME = 8*60
    print("length: " + str(len(sys.argv)))
    print("argv: " + str(sys.argv))
    seed = sys.argv[1] if len(sys.argv) > 1 else 1234

    sim = simulation.Simulation(SIMULATION_RUN_TIME, seed)

    sim.start()
