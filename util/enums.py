from enum import Enum

import gym

class ModelKind(Enum):
  NEAT         = 'neat'
  HYPERNEAT    = 'hyperneat'
  ES_HYPERNEAT = 'es_hyperneat'

  @staticmethod
  def all() -> list:
    return [ModelKind.NONE, ModelKind.NEAT, ModelKind.HYPERNEAT, ModelKind.ES_HYPERNEAT]

class EnvKind(Enum):
  ACROBOT      = 'acrobot'
  CARTPOLE     = 'cartpole'

  def get_env(self) -> gym.Env:
    return gym.make(ENV_MAP[self])

  @staticmethod
  def all() -> list:
    return [EnvKind.ACROBOT, EnvKind.CARTPOLE]

ENV_MAP = {
  EnvKind.ACROBOT: 'Acrobot-v1',
  EnvKind.CARTPOLE: 'CartPole-v1'
}
