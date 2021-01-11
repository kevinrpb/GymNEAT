#! /bin/sh

# --------------------
# DEFAULT VARIABLES
# --------------------

GENERATIONS="100"
MAX_STEPS="100"
MAX_TRIALS="50"
ACTIVATION="sigmoid"
INITIAL_DEPTH="0"
MAX_DEPTH="1"
VARIANCE_THRESHOLD="0.03"
BAND_THRESHOLD="0.3"
ITERATION_LEVEL="1"
DIVISION_THRESHOLD="0.5"

# --------------------
# HELPER FUNCTION
# --------------------

reset() {
  GENERATIONS="2"
  MAX_STEPS="2"
  MAX_TRIALS="2"
  ACTIVATION="sigmoid"
  INITIAL_DEPTH="0"
  MAX_DEPTH="1"
  VARIANCE_THRESHOLD="0.03"
  BAND_THRESHOLD="0.3"
  ITERATION_LEVEL="1"
  DIVISION_THRESHOLD="0.5"
}

# $1: model
# $2: env
# $3: stdout file
run() {
  MODEL=$1
  ENV=$2
  NAME=$4

  STR="[$ENV] [$MODEL] $NAME"

  FILE_OUT="$3.out.txt"

  FILE_FIT="$3.fitness_history.csv"
  FILE_SPE="$3.speciation.csv"
  FILE_SFI="$3.species_fitness.csv"
  FILE_PDF="$3.graph.pdf"

  echo $STR
  echo $STR > $FILE_OUT
  echo "" >> $FILE_OUT

  start=$(gdate +%s.%N)

  python3 ./main.py $MODEL $ENV -v --draw --save \
    --generations         $GENERATIONS \
    --max-steps           $MAX_STEPS \
    --max-trials          $MAX_TRIALS \
    --activation          $ACTIVATION \
    --initial_depth       $INITIAL_DEPTH \
    --max_depth           $MAX_DEPTH \
    --variance_threshold  $VARIANCE_THRESHOLD \
    --band_threshold      $BAND_THRESHOLD \
    --iteration_level     $ITERATION_LEVEL \
    --division_threshold  $DIVISION_THRESHOLD \
    > $FILE_OUT 2>&1

  end=$(gdate +%s.%N)
  duration=$(echo "$end - $start" | bc)
  execution_time=`printf "%.2f seconds" $duration`
  echo "  > $execution_time"

  if [[ -f "fitness_history.csv" ]]; then
    mv "fitness_history.csv" $FILE_FIT
  fi

  if [[ -f "speciation.csv" ]]; then
    mv "speciation.csv"      $FILE_SPE
  fi

  if [[ -f "species_fitness.csv" ]]; then
    mv "species_fitness.csv" $FILE_SFI
  fi

  if [[ -f "network.pdf" ]]; then
    mv "network.pdf"         $FILE_PDF
  fi

  if [[ -f "network" ]]; then
    rm "network"
  fi
}

# --------------------
# ACROBOT
# --------------------

if [[ "Acrobot01" == $1 ]]; then
  ##
  EXP="Acrobot - Experiment 01 - NEAT - Default Settings"
  ##
  run "neat" "acrobot" "./out/acrobot.01" "$EXP"
fi

if [[ "Acrobot02" == $1 ]]; then
##
EXP="Acrobot - Experiment 02 - HyperNEAT - Default Settings"
##
run "hyperneat" "acrobot" "./out/acrobot.02" "$EXP"
fi

if [[ "Acrobot03" == $1 ]]; then
##
EXP="Acrobot - Experiment 03 - ES-HyperNEAT - Default Settings"
##
run "es_hyperneat" "acrobot" "./out/acrobot.03" "$EXP"
fi

if [[ "Acrobot04" == $1 ]]; then
MAX_DEPTH="3"
VARIANCE_THRESHOLD="0.01"
##
EXP="Acrobot - Experiment 04 - ES-HyperNEAT - Less Variance, More Depth"
##
run "es_hyperneat" "acrobot" "./out/acrobot.04" "$EXP"
reset
fi

# --------------------
# CARTPOLE
# --------------------

if [[ "Cartpole01" == $1 ]]; then
##
EXP="Cartpole - Experiment 01 - NEAT - Default Settings"
##
run "neat" "cartpole" "./out/cartpole.01" "$EXP"
fi

if [[ "Cartpole02" == $1 ]]; then
##
EXP="Cartpole - Experiment 02 - HyperNEAT - Default Settings"
##
run "hyperneat" "cartpole" "./out/cartpole.02" "$EXP"
fi

if [[ "Cartpole03" == $1 ]]; then
##
EXP="Cartpole - Experiment 03 - ES-HyperNEAT - Default Settings"
##
run "es_hyperneat" "cartpole" "./out/cartpole.03" "$EXP"
fi

if [[ "Cartpole04" == $1 ]]; then
# MAX_DEPTH="3"
# VARIANCE_THRESHOLD="0.01"
##
EXP="Cartpole - Experiment 04 - ES-HyperNEAT - Less Variance, More Depth"
##
run "es_hyperneat" "cartpole" "./out/cartpole.04" "$EXP"
reset
fi
