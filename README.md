# SYSC_4005_Project

Simulation of a factory in python for the sysc4005 class

## running the simulation

The code was developed using pipenv which allows python to have a virtual environment for each project. [The documentation of pipenv can be found here](https://pipenv.pypa.io/en/latest/), and is installed using

```shell
pip install --user pipenv
```

To use pipenv, navigate to the project root folder `SYSC_4005_Project`, then create a virtual environment and then activate it with the following

```shell
pipenv install
pipenv shell
```

Once this is done, the simulation can be run using

```shell
python simulation/main.py
```

additional arguments can be supplied to specify the seed, and the number of simulations to be performed. The default seed is `1234`, the default number of simulations is `1`. Sequential simulations use incremental seeds.

```shell
python simulation/main.py 1234 1
```

Simulation statistics are automatically saved to a `stats` folder in the root directory.
