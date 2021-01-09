from argparse import ArgumentParser

from util.run import _DEFAULT_PARAMS


def create_parser():

  # ----- Program -----
  parser = ArgumentParser(
    prog        = 'GymNEAT',
    description = '''Run OpenAI Gym experiments using NEAT, HyperNEAT, and ES-HyperNEAT'''
  )

  # ----- Model and Env -----
  parser.add_argument(
    choices  = ['neat', 'hyperneat', 'es_hyperneat'],
    dest     = 'model',
    help     = 'The model to use in the experiment'
  )

  parser.add_argument(
    choices  = ['acrobot', 'cartpole'],
    dest     = 'env',
    help     = 'The Gym environment to use in the experiment'
  )

  # ----- Output Params -----
  parser.add_argument('-v', '--verbose',
    action = 'store_true',
    default = False,
    dest = 'output',
    help = 'Print output to stdout'
  )

  parser.add_argument('-c', '--config',
    default = None,
    dest = 'config_file',
    help = 'Path to custon config file'
  )

  parser.add_argument('-p', '--pickle',
    action = 'store_true',
    default = False,
    dest = 'save_network',
    help = 'Save winner network\'s pickle file'
  )

  parser.add_argument('-a', '--animate',
    action = 'store_true',
    default = False,
    dest = 'animate',
    help = 'Animate experiment running'
  )

  parser.add_argument('-d', '--draw',
    action = 'store_true',
    default = False,
    dest = 'draw_network',
    help = 'Draw network to file'
  )

  parser.add_argument('-s', '--save',
    action = 'store_true',
    default = False,
    dest = 'save_results',
    help = 'Save experiment results to files'
  )

  # ----- Shared Run Params -----
  default_generations = _DEFAULT_PARAMS['generations']
  parser.add_argument('--generations',
    default = default_generations,
    type = int,
    dest = 'gens',
    help = 'Number of generations to run (default {})'.format(default_generations)
  )

  default_max_steps = _DEFAULT_PARAMS['max_steps']
  parser.add_argument('--max-steps',
    default = default_max_steps,
    type = int,
    dest = 'max_steps',
    help = 'Max steps to run (default {})'.format(default_max_steps)
  )

  default_max_trials = _DEFAULT_PARAMS['max_trials']
  parser.add_argument('--max-trials',
    default = default_max_trials,
    type = int,
    dest = 'max_trials',
    help = 'Max trials to run (default {})'.format(default_max_trials)
  )

  # ----- NEAT Run Params -----

  # ----- HYPERNEAT Run Params -----
  default_activation = _DEFAULT_PARAMS['activation']
  parser.add_argument('--activation',
    default = default_activation,
    type = str,
    dest = 'activation',
    help = 'Activation function to use (default {}, ignored in neat model)'.format(default_activation)
  )

  # ----- ES_HYPERNEAT Run Params -----
  default_initial_depth = _DEFAULT_PARAMS['initial_depth']
  parser.add_argument('--initial_depth',
    default = default_initial_depth,
    type = int,
    dest = 'initial_depth',
    help = 'Network initial depth (default {}, es_hyperneat model only)'.format(default_initial_depth)
  )

  default_max_depth = _DEFAULT_PARAMS['max_depth']
  parser.add_argument('--max_depth',
    default = default_max_depth,
    type = int,
    dest = 'max_depth',
    help = 'Network max depth (default {}, es_hyperneat model only)'.format(default_max_depth)
  )

  default_variance_threshold = _DEFAULT_PARAMS['variance_threshold']
  parser.add_argument('--variance_threshold',
    default = default_variance_threshold,
    type = float,
    dest = 'variance_threshold',
    help = ' (default {}, es_hyperneat model only)'.format(default_variance_threshold)
  )

  default_band_threshold = _DEFAULT_PARAMS['band_threshold']
  parser.add_argument('--band_threshold',
    default = default_band_threshold,
    type = float,
    dest = 'band_threshold',
    help = ' (default {}, es_hyperneat model only)'.format(default_band_threshold)
  )

  default_iteration_level = _DEFAULT_PARAMS['iteration_level']
  parser.add_argument('--iteration_level',
    default = default_iteration_level,
    type = int,
    dest = 'iteration_level',
    help = ' (default {}, es_hyperneat model only)'.format(default_iteration_level)
  )

  default_division_threshold = _DEFAULT_PARAMS['division_threshold']
  parser.add_argument('--division_threshold',
    default = default_division_threshold,
    type = float,
    dest = 'division_threshold',
    help = ' (default {}, es_hyperneat model only)'.format(default_division_threshold)
  )

  default_max_weight = _DEFAULT_PARAMS['max_weight']
  parser.add_argument('--max_weight',
    default = default_max_weight,
    type = float,
    dest = 'max_weight',
    help = ' (default {}, es_hyperneat model only)'.format(default_max_weight)
  )

  return parser
