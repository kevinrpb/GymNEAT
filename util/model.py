from enum import Enum

import neat
from neat.config import Config

from util.enums import ModelKind, EnvKind
import util.run as run


FUNC_MAP = {
  ModelKind.NEAT: run.neat,
  ModelKind.HYPERNEAT: run.hyperneat,
  ModelKind.ES_HYPERNEAT: run.es_hyperneat
}

class Model(object):

  def __init__(self, model_kind: ModelKind):
    self._kind = model_kind

  def run(self,
    env_kind: EnvKind,
    params: run.RunParams,
    output: bool = True,
    config_file: str = None,
    animate: bool = False):
    if config_file is not None:
      _config_file = config_file
    else:
      _config_file = './config/environments/{}.{}.cfg'.format(env_kind.value, self._kind.value)

    config = Config(
      neat.genome.DefaultGenome,
      neat.reproduction.DefaultReproduction,
      neat.species.DefaultSpeciesSet,
      neat.stagnation.DefaultStagnation,
      _config_file
    )

    _func = FUNC_MAP[self._kind]

    return _func(
      config,
      env_kind,
      params,
      output,
      animate
    )
