t_sim=1000
seed=67890
for needed in 0.0 0.25 0.5 0.75 1.0
do
    for chosen in 0.0 0.25 0.5 0.75 1.0
    do
	python sim.py nolog=1 t_sim=${t_sim} p_rework_needed=${needed} p_rework_chosen=${chosen} rng_seed=${seed} > needed=${needed}_chosen=${chosen}.json
	seed=$(expr ${seed} + 1)
    done
done
