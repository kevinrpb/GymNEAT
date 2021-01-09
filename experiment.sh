#! /bin/sh

# --------------------
# DEFAULT VARIABLES
# --------------------

GENERATIONS="100"
MAX_STEPS="100"
MAX_TRIALS="100"
ACTIVATION="sigmoid"
INITIAL_DEPTH="0"
MAX_DEPTH="1"
VARIANCE_THRESHOLD="0.03"
BAND_THRESHOLD="0.3"
ITERATION_LEVEL="1"
DIVISION_THRESHOLD="0.5"
MAX_WEIGHT="8.0"

# --------------------
# HELPER FUNCTION
# --------------------

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
    --max_weight          $MAX_WEIGHT \
    > $FILE_OUT

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

# --------------------
# CARTPOLE
# --------------------

##
EXP="Experiment 01 - Cartpole - NEAT - Default Settings"
##
run "neat" "cartpole" "./out/01.cartpole.neat" "$EXP"

##
EXP="Experiment 02 - Cartpole - HyperNEAT - Default Settings"
##
run "hyperneat" "cartpole" "./out/02.cartpole.hyperneat" "$EXP"

##
EXP="Experiment 03 - Cartpole - ES-HyperNEAT - Default Settings"
##
run "es_hyperneat" "cartpole" "./out/03.cartpole.es_hyperneat" "$EXP"
