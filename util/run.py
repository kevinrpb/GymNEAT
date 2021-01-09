from neat.config import Config
from neat.nn import FeedForwardNetwork
from pureples.shared.gym_runner import run_es, run_hyper, run_neat

from util.enums import EnvKind, ModelKind
from util.substrate import get_substrate

_DEFAULT_PARAMS = {
  'generations': 500,
  'max_steps': 500,
  'max_trials': 100,
  'initial_depth': 0,
  'max_depth': 1,
  'variance_threshold': 0.03,
  'band_threshold': 0.3,
  'iteration_level': 1,
  'division_threshold': 0.5,
  'max_weight': 8.0,
  'activation': 'sigmoid'
}

class RunParams(object):

  def __init__(self,
    generations:          int   = _DEFAULT_PARAMS['generations'],
    max_steps:            int   = _DEFAULT_PARAMS['max_steps'],
    max_trials:           int   = _DEFAULT_PARAMS['max_trials'],
    initial_depth:        int   = _DEFAULT_PARAMS['initial_depth'],
    max_depth:            int   = _DEFAULT_PARAMS['max_depth'],
    variance_threshold:   float = _DEFAULT_PARAMS['variance_threshold'],
    band_threshold:       float = _DEFAULT_PARAMS['band_threshold'],
    iteration_level:      int   = _DEFAULT_PARAMS['iteration_level'],
    division_threshold:   float = _DEFAULT_PARAMS['division_threshold'],
    max_weight:           float = _DEFAULT_PARAMS['max_weight'],
    activation:           str   = _DEFAULT_PARAMS['activation']
  ):
    self._params = {}
    self._params['generations']        = generations
    self._params['max_steps']          = max_steps
    self._params['max_trials']         = max_trials
    self._params['initial_depth']      = initial_depth
    self._params['max_depth']          = max_depth
    self._params['variance_threshold'] = variance_threshold
    self._params['band_threshold']     = band_threshold
    self._params['iteration_level']    = iteration_level
    self._params['division_threshold'] = division_threshold
    self._params['max_weight']         = max_weight
    self._params['activation']         = activation

  @property
  def generations(self) -> int:
    return self._params['generations']

  @property
  def max_steps(self) -> int:
    return self._params['max_steps']

  @property
  def max_trials(self) -> int:
    return self._params['max_trials']

  @property
  def initial_depth(self) -> int:
    return self._params['initial_depth']

  @property
  def max_depth(self) -> int:
    return self._params['max_depth']

  @property
  def variance_threshold(self) -> float:
    return self._params['variance_threshold']

  @property
  def band_threshold(self) -> float:
    return self._params['band_threshold']

  @property
  def iteration_level(self) -> int:
    return self._params['iteration_level']

  @property
  def division_threshold(self) -> float:
    return self._params['division_threshold']

  @property
  def max_weight(self) -> float:
    return self._params['max_weight']

  @property
  def activation(self) -> str:
    return self._params['activation']

  @property
  def dict(self) -> dict:
    return self._params

def neat(
  config: Config,
  env_kind: EnvKind,
  params: RunParams,
  output: bool,
  animate: bool):
  env = env_kind.get_env()

  winner, stats = run_neat(params.generations, env, params.max_steps, config, params.max_trials, output, animate)

  network = FeedForwardNetwork.create(winner, config)

  return winner, stats, network

def hyperneat(
  config: Config,
  env_kind: EnvKind,
  params: RunParams,
  output: bool,
  animate: bool):
  env = env_kind.get_env()
  substrate = get_substrate(ModelKind.HYPERNEAT, env_kind)
  activations = len(substrate.hidden_coordinates) + 2

  winner, stats = run_hyper(params.generations, env, params.max_steps, config, substrate, activations, params.max_trials, params.activation, output, animate)

  network = FeedForwardNetwork.create(winner, config)

  return winner, stats, network

def es_hyperneat(
  config: Config,
  env_kind: EnvKind,
  params: RunParams,
  output: bool,
  animate: bool):
  env = env_kind.get_env()
  substrate = get_substrate(ModelKind.ES_HYPERNEAT, env_kind)
  _params = params.dict

  winner, stats = run_es(params.generations, env, params.max_steps, config, _params, substrate, params.max_trials, output, animate)

  network = FeedForwardNetwork.create(winner, config)

  return winner, stats, network
