python maqp.py --generate_hdf --csv_seperator , --csv_path ./cover-benchmark --hdf_path ./cover-benchmark/gen_single --max_rows_per_hdf_file 1000000 --dataset cover


python maqp.py --generate_ensemble --dataset cover --samples_per_spn 10000000 --ensemble_strategy single --hdf_path ./cover-benchmark/gen_single --ensemble_path ./cover-benchmark/spn_ensembles --rdc_threshold 0.3 --post_sampling_factor 10


python maqp.py --generate_ensemble --dataset cover --samples_per_spn 10000000 --ensemble_strategy rdc_based --hdf_path ./cover-benchmark/gen_single --samples_rdc_ensemble_tests 10000 --max_rows_per_hdf_file 100000000 --ensemble_budget_factor 5 --ensemble_path ./cover-benchmark/spn_ensembles --rdc_threshold 0.3 --post_sampling_factor 10


## use python 3.7