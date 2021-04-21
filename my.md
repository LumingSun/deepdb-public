```
python maqp.py --generate_hdf --csv_seperator , --csv_path ./cover-benchmark --hdf_path ./cover-benchmark/gen_single --max_rows_per_hdf_file 1000000 --dataset cover


python maqp.py --generate_ensemble --dataset cover --samples_per_spn 10000000 --ensemble_strategy single --hdf_path ./cover-benchmark/gen_single --ensemble_path ./cover-benchmark/spn_ensembles --rdc_threshold 0.3 --post_sampling_factor 10


<!-- python maqp.py --generate_ensemble --dataset cover --samples_per_spn 10000000 --ensemble_strategy rdc_based --hdf_path ./cover-benchmark/gen_single --samples_rdc_ensemble_tests 10000 --max_rows_per_hdf_file 100000000 --ensemble_budget_factor 5 --ensemble_path ./cover-benchmark/spn_ensembles --rdc_threshold 0.3 --post_sampling_factor 10 -->

python3 maqp.py --evaluate_cardinalities
    --rdc_spn_selection
    --max_variants 1
    --dataset cover
    --target_path ./baselines/cardinality_estimation/results/deepDB/cover_ten.csv
    --ensemble_location ./cover-benchmark/spn_ensembles/ensemble_single_cover_10000000.pkl
    --query_file_location ./cover-benchmark/sql/cover_5000_attr_ten_queries.sql
    --ground_truth_file_location ./cover-benchmark/sql/cover_5000_attr_ten_true_cardinalities.csv

    <!-- --pairwise_rdc_path ../imdb-benchmark/spn_ensembles/pairwise_rdc.pkl -->

```
## use python 3.7