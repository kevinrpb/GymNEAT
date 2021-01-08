from util.model import EnvKind, Model, ModelKind
from util.parser import create_parser
from util.run import RunParams

def main():
  # ----- Parse arguments -----
  parser = create_parser()
  args   = parser.parse_args()

  # ----- Create Model & env -----
  model_kind = ModelKind(args.model)
  model      = Model(model_kind)
  env_kind   = EnvKind(args.env)

  # ----- Options -----
  output       = args.output
  make_network = args.make_network
  config_file  = args.config_file

  # ----- Get params -----
  generations        = args.gens
  max_steps          = args.max_steps
  max_trials         = args.max_trials
  initial_depth      = args.initial_depth
  max_depth          = args.max_depth
  variance_threshold = args.variance_threshold
  band_threshold     = args.band_threshold
  iteration_level    = args.iteration_level
  division_threshold = args.division_threshold
  max_weight         = args.max_weight
  activation         = args.activation

  params = RunParams(
    generations        = generations,
    max_steps          = max_steps,
    max_trials         = max_trials,
    initial_depth      = initial_depth,
    max_depth          = max_depth,
    variance_threshold = variance_threshold,
    band_threshold     = band_threshold,
    iteration_level    = iteration_level,
    division_threshold = division_threshold,
    max_weight         = max_weight,
    activation         = activation
  )

  # ----- Run Experiments -----
  winner, stats, network = model.run(
    env_kind,
    params,
    output,
    make_network,
    config_file
  )

  stats_one, stats_ten, stats_hundred = stats

if __name__ == '__main__':
  main()
