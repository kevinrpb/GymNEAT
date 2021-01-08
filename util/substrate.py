from pureples.shared.substrate import Substrate

from util.model import EnvKind, ModelKind


def _acrobot_hyperneat():
  return None

def _acrobot_es_hyperneat():
  return None

def _cartpole_hyperneat():
  input_coordinates = []
  for i in range(0,4):
    input_coordinates.append((-1. + (2.*i/3.), -1.))

  hidden_coordinates = [[(-0.5, 0.5), (0.5, 0.5)], [(-0.5, -0.5), (0.5, -0.5)]]
  output_coordinates = [(-1., 1.), (1., 1.)]

  return Substrate(input_coordinates, output_coordinates, hidden_coordinates)

def _cartpole_es_hyperneat():
  input_coordinates = []
  for i in range(0,4):
    input_coordinates.append((-1. +(2.*i/3.), -1.))

  output_coordinates = [(-1., 1.), (1., 1.)]

  return Substrate(input_coordinates, output_coordinates)

SUB_MAPS = {
  'acrobot.hyperneat':     _acrobot_hyperneat(),
  'acrobot.es_hyperneat':  _acrobot_es_hyperneat(),
  'cartpole.hyperneat':    _cartpole_hyperneat(),
  'cartpole.es_hyperneat': _cartpole_es_hyperneat(),
}

def get_substrate(model: ModelKind, env: EnvKind):
  key = '{}.{}'.format(env.value, model.value)

  return SUB_MAPS[key]
