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

## Creating simulation visualizations

After running simulations, data will have been saved to the `/stats/` directory. The data can be visualized using:

```shell
python visualization/main.py
```
