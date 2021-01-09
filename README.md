# GymNEAT

## Requirements

- **Python 3.8** (3.9 conflicts with some packages!)
- **pip 20** (installed with python)
- **pipenv** (optional)

## Install Dependencies

- With pip: `pip install -r requirements.txt`
- With pipenv: `pipenv install`

> NOTE: In MacOS Big Sur, numpy packages have trouble installing. Setting env variable `SYSTEM_VERSION_COMPAT=1` when running pip or pipenv helps.

## Gym Support

Currently, only **CartPole-v1** and **Acrobot-v1** environments are supported. Support for arbitrary environments is planned, current limitation is the included configuration files, as well as network substrates.

## Running Experiments

All configuration options can be found by running with the `--help` flag:

```
usage: GymNEAT [-h] [-v] [-c CONFIG_FILE] [-p] [-a] [-d] [-s] [--generations GENS] [--max-steps MAX_STEPS] [--max-trials MAX_TRIALS] [--activation ACTIVATION] [--initial_depth INITIAL_DEPTH]
               [--max_depth MAX_DEPTH] [--variance_threshold VARIANCE_THRESHOLD] [--band_threshold BAND_THRESHOLD] [--iteration_level ITERATION_LEVEL] [--division_threshold DIVISION_THRESHOLD]
               [--max_weight MAX_WEIGHT]
               {neat,hyperneat,es_hyperneat} {acrobot,cartpole}

Run OpenAI Gym experiments using NEAT, HyperNEAT, and ES-HyperNEAT

positional arguments:
  {neat,hyperneat,es_hyperneat}
                        The model to use in the experiment
  {acrobot,cartpole}
                        The Gym environment to use in the experiment

optional arguments:
  -h, --help
                        show this help message and exit
  -v, --verbose
                        Print output to stdout
  -c CONFIG_FILE, --config CONFIG_FILE
                        Path to custon config file
  -p, --pickle
                        Save winner network's pickle file
  -a, --animate
                        Animate experiment running
  -d, --draw
                        Draw network to file
  -s, --save
                        Save experiment results to files
  --generations GENS
                        Number of generations to run (default 500)
  --max-steps MAX_STEPS
                        Max steps to run (default 500)
  --max-trials MAX_TRIALS
                        Max trials to run (default 100)
  --activation ACTIVATION
                        Activation function to use (default sigmoid, ignored in neat model)
  --initial_depth INITIAL_DEPTH
                        Network initial depth (default 0, es_hyperneat model only)
  --max_depth MAX_DEPTH
                        Network max depth (default 1, es_hyperneat model only)
  --variance_threshold VARIANCE_THRESHOLD
                        (default 0.03, es_hyperneat model only)
  --band_threshold BAND_THRESHOLD
                        (default 0.3, es_hyperneat model only)
  --iteration_level ITERATION_LEVEL
                        (default 1, es_hyperneat model only)
  --division_threshold DIVISION_THRESHOLD
                        (default 0.5, es_hyperneat model only)
  --max_weight MAX_WEIGHT
                        (default 8.0, es_hyperneat model only)
```

> NOTE: On recent MacOS distributions, OpenGL is not available. Therefore, piglet is not available and animating the experiment might fail.

## Credits

GymNEAT uses the followin OSS:

- [OpenAI Gym](https://github.com/openai/gym) for experiment environments. MIT License.
- [neat-python](https://github.com/CodeReclaimers/neat-python) for the NEAT alg implementation. BSD 3-Clause License.
- [pureples](https://github.com/ukuleleplayer/pureples) for HyperNEAT, ES-HyperNEAT, and Gym runner. MIT License.

## License

GymNEAT is published under the MIT License.
