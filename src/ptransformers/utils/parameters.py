new_trand_feature_list = [
    'machine_id',
    'quarter',
    'component_id',
    'bearing',
    'plane',
    'recorded_at',
    'algo_version',
    'cliff_status',
    'created_at',
    'is_servo',
    'machine_line_frequency__cliff_score',
    'machine_line_frequency__opmode_cliff_score',
    'machine_line_frequency__stats_1_0_mean',
    'machine_line_frequency__stats_30_1_mean',
    'machine_line_frequency__stats_8_1_mean',
    'machine_line_frequency__stats_90_1_mean',
    'magnetic_acc_rms__cliff_score',
    'magnetic_acc_rms__opmode_cliff_score',
    'magnetic_acc_rms__stats_1_0_mean',
    'magnetic_acc_rms__stats_30_1_mean',
    'magnetic_acc_rms__stats_8_1_mean',
    'magnetic_acc_rms__stats_90_1_mean',
    'magnetic_maglf__cliff_score',
    'magnetic_maglf__opmode_cliff_score',
    'magnetic_maglf__stats_1_0_mean',
    'magnetic_maglf__stats_30_1_mean',
    'magnetic_maglf__stats_8_1_mean',
    'magnetic_maglf__stats_90_1_mean',
    'magnetic_maglf_level__cliff_score',
    'magnetic_maglf_level__opmode_cliff_score',
    'magnetic_maglf_level__stats_1_0_mean',
    'magnetic_maglf_level__stats_30_1_mean',
    'magnetic_maglf_level__stats_8_1_mean',
    'magnetic_maglf_level__stats_90_1_mean',
    'magnetic_magtotalpeaks__cliff_score',
    'rapid_cliff_status',
    'sampled_at',
    'session_id',
    'temperature_difference__cliff_score',
    'temperature_eptemp__cliff_score',
    'temperature_eptemp__stats_1_0_mean',
    'temperature_eptemp__stats_30_1_mean',
    'temperature_eptemp__stats_8_1_mean',
    'temperature_eptemp__stats_90_1_mean',
    'trend_status',
    'vibration_acc_kurt__cliff_score',
    'vibration_acc_kurt__stats_1_0_mean',
    'vibration_acc_kurt__stats_30_1_mean',
    'vibration_acc_kurt__stats_8_1_mean',
    'vibration_acc_kurt__stats_90_1_mean',
    'vibration_acc_p2p__cliff_score',
    'vibration_acc_p2p__stats_1_0_mean',
    'vibration_acc_p2p__stats_30_1_mean',
    'vibration_acc_p2p__stats_8_1_mean',
    'vibration_acc_p2p__stats_90_1_mean',
    'vibration_acc_p2p_percentiles__14__r_squared',
    'vibration_acc_p2p_percentiles__14__slope',
    'vibration_acc_p2p_percentiles__30__r_squared',
    'vibration_acc_p2p_percentiles__30__slope',
    'vibration_acc_p2p_percentiles__45__r_squared',
    'vibration_acc_p2p_percentiles__45__slope',
    'vibration_acc_p2p_percentiles__60__r_squared',
    'vibration_acc_p2p_percentiles__60__slope',
    'vibration_acc_p2p_percentiles__cliff_score',
    'vibration_acc_p2p_percentiles__current_value',
    'vibration_acc_p2p_percentiles__r_squared',
    'vibration_acc_p2p_percentiles__rapid_cliff_score',
    'vibration_acc_rms_0k_1k__cliff_score',
    'vibration_acc_rms_0k_1k__stats_1_0_mean',
    'vibration_acc_rms_0k_1k__stats_30_1_mean',
    'vibration_acc_rms_0k_1k__stats_8_1_mean',
    'vibration_acc_rms_0k_1k__stats_90_1_mean',
    'vibration_acc_rms_1k_2k__cliff_score',
    'vibration_acc_rms_1k_2k__stats_1_0_mean',
    'vibration_acc_rms_1k_2k__stats_30_1_mean',
    'vibration_acc_rms_1k_2k__stats_8_1_mean',
    'vibration_acc_rms_1k_2k__stats_90_1_mean',
    'vibration_acc_rms_1khz_to_max__cliff_score',
    'vibration_acc_rms_1khz_to_max__stats_1_0_mean',
    'vibration_acc_rms_1khz_to_max__stats_30_1_mean',
    'vibration_acc_rms_1khz_to_max__stats_8_1_mean',
    'vibration_acc_rms_1khz_to_max__stats_90_1_mean',
    'vibration_acc_rms_2k_3k__cliff_score',
    'vibration_acc_rms_3k_4k__cliff_score',
    'vibration_acc_rms_4k_5k__cliff_score',
    'vibration_acc_rms_5k_6k__cliff_score',
    'vibration_acc_rms_6k_7k__cliff_score',
    'vibration_acc_rms_7k_8k__cliff_score',
    'vibration_acc_rms__14__r_squared',
    'vibration_acc_rms__14__slope',
    'vibration_acc_rms__30__r_squared',
    'vibration_acc_rms__30__slope',
    'vibration_acc_rms__45__r_squared',
    'vibration_acc_rms__45__slope',
    'vibration_acc_rms__60__r_squared',
    'vibration_acc_rms__60__slope',
    'vibration_acc_rms__cliff_score',
    'vibration_acc_rms__current_value',
    'vibration_acc_rms__prev_value',
    'vibration_acc_rms__r_squared',
    'vibration_acc_rms__rapid_cliff_score',
    'vibration_acc_rms__stats_1_0_mean',
    'vibration_acc_rms__stats_30_1_mean',
    'vibration_acc_rms__stats_8_1_mean',
    'vibration_acc_rms__stats_90_1_mean',
    'vibration_anomaly__0__cliff_score',
    'vibration_anomaly__1__cliff_score',
    'vibration_anomaly__1__rapid_cliff_score',
    'vibration_bpfi_uniform_vel_rms__cliff_score',
    'vibration_bpfi_uniform_vel_rms__rapid_cliff_score',
    'vibration_bpfo_uniform_vel_rms__cliff_score',
    'vibration_bpfo_uniform_vel_rms__rapid_cliff_score',
    'vibration_crest_factor__cliff_score',
    'vibration_env_rms__14__r_squared',
    'vibration_env_rms__14__slope',
    'vibration_env_rms__30__r_squared',
    'vibration_env_rms__30__slope',
    'vibration_env_rms__45__r_squared',
    'vibration_env_rms__45__slope',
    'vibration_env_rms__60__r_squared',
    'vibration_env_rms__60__slope',
    'vibration_env_rms__cliff_score',
    'vibration_env_rms__current_value',
    'vibration_env_rms__r_squared',
    'vibration_env_rms__rapid_cliff_score',
    'vibration_env_rms__stats_1_0_mean',
    'vibration_env_rms__stats_30_1_mean',
    'vibration_env_rms__stats_8_1_mean',
    'vibration_env_rms__stats_90_1_mean',
    'vibration_tlfpeakslevel__cliff_score',
    'vibration_vel_order__0__14__r_squared',
    'vibration_vel_order__0__14__slope',
    'vibration_vel_order__0__30__r_squared',
    'vibration_vel_order__0__30__slope',
    'vibration_vel_order__0__45__r_squared',
    'vibration_vel_order__0__45__slope',
    'vibration_vel_order__0__60__r_squared',
    'vibration_vel_order__0__60__slope',
    'vibration_vel_order__0__cliff_score',
    'vibration_vel_order__0__current_value',
    'vibration_vel_order__0__prev_value',
    'vibration_vel_order__0__r_squared',
    'vibration_vel_order__0__rapid_cliff_score',
    'vibration_vel_order__0__stats_1_0_mean',
    'vibration_vel_order__0__stats_30_1_mean',
    'vibration_vel_order__0__stats_8_1_mean',
    'vibration_vel_order__0__stats_90_1_mean',
    'vibration_vel_order__1__cliff_score',
    'vibration_vel_order__1__rapid_cliff_score',
    'vibration_vel_order__1__stats_1_0_mean',
    'vibration_vel_order__1__stats_30_1_mean',
    'vibration_vel_order__1__stats_8_1_mean',
    'vibration_vel_order__1__stats_90_1_mean',
    'vibration_vel_order__2__cliff_score',
    'vibration_vel_order__2__rapid_cliff_score',
    'vibration_vel_order__2__stats_1_0_mean',
    'vibration_vel_order__2__stats_30_1_mean',
    'vibration_vel_order__2__stats_8_1_mean',
    'vibration_vel_order__2__stats_90_1_mean',
    'vibration_vel_order__3__stats_1_0_mean',
    'vibration_vel_order__3__stats_30_1_mean',
    'vibration_vel_order__3__stats_8_1_mean',
    'vibration_vel_order__3__stats_90_1_mean',
    'vibration_vel_orders_4_10__cliff_score',
    'vibration_vel_orders_4_10__rapid_cliff_score',
    'vibration_vel_rms__14__r_squared',
    'vibration_vel_rms__14__slope',
    'vibration_vel_rms__30__r_squared',
    'vibration_vel_rms__30__slope',
    'vibration_vel_rms__45__r_squared',
    'vibration_vel_rms__45__slope',
    'vibration_vel_rms__60__r_squared',
    'vibration_vel_rms__60__slope',
    'vibration_vel_rms__cliff_score',
    'vibration_vel_rms__current_value',
    'vibration_vel_rms__prev_value',
    'vibration_vel_rms__r_squared',
    'vibration_vel_rms__rapid_cliff_score',
    'vibration_vel_rms__stats_1_0_mean',
    'vibration_vel_rms__stats_30_1_mean',
    'vibration_vel_rms__stats_8_1_mean',
    'vibration_vel_rms__stats_90_1_mean',
    'vibration_session_machine_on'
]
rapid_cliff_enhancements_features_list = [
    "timestamp",
    "vibration_session_machine_on",
    "motor_poles",
    "temperature_difference",
    "vibration_env_kurt",
    "vibration_env_kurt_4000_5500",
    "vibration_env_kurt_1000_2500",
    "vibration_anomaly__7",
    "stationary_score",
    "vibration_env_kurt_6250_7750",
    "vibration_env_skew_1000_2500",
    "vibration_anomaly__5",
    "vibration_env_rms_1000_2500",
    "vibration_env_std_1750_3250",
    "vibration_dis_rms",
    "vibration_env_rms_1750_3250",
    "vibration_acc_rms_3k_4k",
    "vibration_peak_prominence",
    "cepstrum_twice_line_freq_peak",
    "vibration_env_std_2500_4000",
    "vibration_anomaly__6",
    "vibration_acc_kurt",
    "vibration_vel_rms",
    "vibration_env_rms_5500_7000",
    "vibration_env_std_4750_6250",
    "vibration_acc_rms_1k_2k",
    "impact_rms_iqr",
    "vibration_window_var_percentile",
    "vibration_env_skew_2500_4000",
    "vibration_acc_skew",
    "vibration_acc_rms_0k_1k",
    "vibration_env_std_1000_2500",
    "vibration_env_std_3250_4750",
    "vibration_env_kurt_3250_4750",
    "vibration_acc_rms_4k_5k",
    "vibration_env_kurt_4750_6250",
    "vibration_acc_rms_1khz_to_max",
    "vibration_env_std_4000_5500",
    "impact_skew_median",
    "impact_frequency",
    "vibration_env_std_6250_7750",
    "impact_ringdown_time_iqr",
    "vibration_anomaly__1",
    "vibration_env_rms",
    "vibration_acc_rms_6k_7k",
    "vibration_env_rms_4000_5500",
    "vibration_env_std_5500_7000",
    "vibration_acc_rms",
    "is_valid_vibration",
    "vibration_window_p2p",
    "vibration_acc_p2p",
    "vibration_anomaly__0",
    "vibration_env_rms_6250_7750",
    "vibration_env_rms_3250_4750",
    "vibration_anomaly__2",
    "vibration_vel_kurt",
    "vibration_env_skew_4000_5500",
    "vibration_env_kurt_1750_3250",
    "vibration_env_skew_1750_3250",
    "vibration_acc_rms_2k_3k",
    "impact_rms_median",
    "vibration_env_skew_4750_6250",
    "vibration_acc_rms_7k_8k",
    "vibration_env_skew_3250_4750",
    "vibration_acc_rms_5k_6k",
    "vibration_anomaly__3",
    "vibration_env_rms_2500_4000",
    "vibration_env_rms_4750_6250",
    "vibration_env_kurt_5500_7000",
    "vibration_env_kurt_2500_4000",
    "vibration_env_skew_5500_7000",
    "cepstrum_line_freq_peak",
    "impact_p2p_median",
    "impact_ringdown_time_median",
    "vibration_dc_level",
    "vibration_acc_var",
    "vibration_anomaly__4",
    "vibration_acc_p2p_percentiles",
    "vibration_crest_factor",
    "impact_skew_iqr",
    "impact_p2p_iqr",
    "vibration_env_skew_6250_7750",
    "cepstrum_one_third_line_freq_peak",
    "is_valid",
    "old_is_on",
    "machine_is_on",
    "vibration_acc_kurt__stats_1_0_mean",
    "vibration_acc_rms__stats_1_0_mean",
    "vibration_acc_rms_0k_1k__stats_1_0_mean",
    "vibration_acc_rms_1k_2k__stats_1_0_mean",
    "vibration_acc_rms_1khz_to_max__stats_1_0_mean",
    "vibration_acc_p2p__stats_1_0_mean",
    "vibration_env_rms__stats_1_0_mean",
    "vibration_vel_rms__stats_1_0_mean",
    "vibration_vel_order__0__stats_1_0_mean",
    "vibration_vel_order__1__stats_1_0_mean",
    "vibration_vel_order__2__stats_1_0_mean",
    "vibration_vel_order__3__stats_1_0_mean",
    "machine_line_frequency__stats_1_0_mean",
    "vibration_acc_kurt__stats_8_1_mean",
    "vibration_acc_rms__stats_8_1_mean",
    "vibration_acc_rms_0k_1k__stats_8_1_mean",
    "vibration_acc_rms_1k_2k__stats_8_1_mean",
    "vibration_acc_rms_1khz_to_max__stats_8_1_mean",
    "vibration_acc_p2p__stats_8_1_mean",
    "vibration_env_rms__stats_8_1_mean",
    "vibration_vel_rms__stats_8_1_mean",
    "vibration_vel_order__0__stats_8_1_mean",
    "vibration_vel_order__1__stats_8_1_mean",
    "vibration_vel_order__2__stats_8_1_mean",
    "vibration_vel_order__3__stats_8_1_mean",
    "machine_line_frequency__stats_8_1_mean",
    "vibration_acc_kurt__stats_30_1_mean",
    "vibration_acc_rms__stats_30_1_mean",
    "vibration_acc_rms_0k_1k__stats_30_1_mean",
    "vibration_acc_rms_1k_2k__stats_30_1_mean",
    "vibration_acc_rms_1khz_to_max__stats_30_1_mean",
    "vibration_acc_p2p__stats_30_1_mean",
    "vibration_env_rms__stats_30_1_mean",
    "vibration_vel_rms__stats_30_1_mean",
    "vibration_vel_order__0__stats_30_1_mean",
    "vibration_vel_order__1__stats_30_1_mean",
    "vibration_vel_order__2__stats_30_1_mean",
    "vibration_vel_order__3__stats_30_1_mean",
    "machine_line_frequency__stats_30_1_mean",
    "vibration_acc_kurt__stats_90_1_mean",
    "vibration_acc_rms__stats_90_1_mean",
    "vibration_acc_rms_0k_1k__stats_90_1_mean",
    "vibration_acc_rms_1k_2k__stats_90_1_mean",
    "vibration_acc_rms_1khz_to_max__stats_90_1_mean",
    "vibration_acc_p2p__stats_90_1_mean",
    "vibration_env_rms__stats_90_1_mean",
    "vibration_vel_rms__stats_90_1_mean",
    "vibration_vel_order__0__stats_90_1_mean",
    "vibration_vel_order__1__stats_90_1_mean",
    "vibration_vel_order__2__stats_90_1_mean",
    "vibration_vel_order__3__stats_90_1_mean",
    "machine_line_frequency__stats_90_1_mean",
    "vibration_acc_kurt__stats_1_0_std",
    "vibration_acc_rms__stats_1_0_std",
    "vibration_acc_rms_0k_1k__stats_1_0_std",
    "vibration_acc_rms_1k_2k__stats_1_0_std",
    "vibration_acc_rms_1khz_to_max__stats_1_0_std",
    "vibration_acc_p2p__stats_1_0_std",
    "vibration_env_rms__stats_1_0_std",
    "vibration_vel_rms__stats_1_0_std",
    "vibration_vel_order__0__stats_1_0_std",
    "vibration_vel_order__1__stats_1_0_std",
    "vibration_vel_order__2__stats_1_0_std",
    "vibration_vel_order__3__stats_1_0_std",
    "machine_line_frequency__stats_1_0_std",
    "vibration_acc_kurt__stats_8_1_std",
    "vibration_acc_rms__stats_8_1_std",
    "vibration_acc_rms_0k_1k__stats_8_1_std",
    "vibration_acc_rms_1k_2k__stats_8_1_std",
    "vibration_acc_rms_1khz_to_max__stats_8_1_std",
    "vibration_acc_p2p__stats_8_1_std",
    "vibration_env_rms__stats_8_1_std",
    "vibration_vel_rms__stats_8_1_std",
    "vibration_vel_order__0__stats_8_1_std",
    "vibration_vel_order__1__stats_8_1_std",
    "vibration_vel_order__2__stats_8_1_std",
    "vibration_vel_order__3__stats_8_1_std",
    "machine_line_frequency__stats_8_1_std",
    "vibration_acc_kurt__stats_30_1_std",
    "vibration_acc_rms__stats_30_1_std",
    "vibration_acc_rms_0k_1k__stats_30_1_std",
    "vibration_acc_rms_1k_2k__stats_30_1_std",
    "vibration_acc_rms_1khz_to_max__stats_30_1_std",
    "vibration_acc_p2p__stats_30_1_std",
    "vibration_env_rms__stats_30_1_std",
    "vibration_vel_rms__stats_30_1_std",
    "vibration_vel_order__0__stats_30_1_std",
    "vibration_vel_order__1__stats_30_1_std",
    "vibration_vel_order__2__stats_30_1_std",
    "vibration_vel_order__3__stats_30_1_std",
    "machine_line_frequency__stats_30_1_std",
    "vibration_acc_kurt__stats_90_1_std",
    "vibration_acc_rms__stats_90_1_std",
    "vibration_acc_rms_0k_1k__stats_90_1_std",
    "vibration_acc_rms_1k_2k__stats_90_1_std",
    "vibration_acc_rms_1khz_to_max__stats_90_1_std",
    "vibration_acc_p2p__stats_90_1_std",
    "vibration_env_rms__stats_90_1_std",
    "vibration_vel_rms__stats_90_1_std",
    "vibration_vel_order__0__stats_90_1_std",
    "vibration_vel_order__1__stats_90_1_std",
    "vibration_vel_order__2__stats_90_1_std",
    "vibration_vel_order__3__stats_90_1_std",
    "machine_line_frequency__stats_90_1_std",
    "vibration_acc_kurt__stats_1_0_median",
    "vibration_acc_rms__stats_1_0_median",
    "vibration_acc_rms_0k_1k__stats_1_0_median",
    "vibration_acc_rms_1k_2k__stats_1_0_median",
    "vibration_acc_rms_1khz_to_max__stats_1_0_median",
    "vibration_acc_p2p__stats_1_0_median",
    "vibration_env_rms__stats_1_0_median",
    "vibration_vel_rms__stats_1_0_median",
    "vibration_vel_order__0__stats_1_0_median",
    "vibration_vel_order__1__stats_1_0_median",
    "vibration_vel_order__2__stats_1_0_median",
    "vibration_vel_order__3__stats_1_0_median",
    "machine_line_frequency__stats_1_0_median",
    "vibration_acc_kurt__stats_8_1_median",
    "vibration_acc_rms__stats_8_1_median",
    "vibration_acc_rms_0k_1k__stats_8_1_median",
    "vibration_acc_rms_1k_2k__stats_8_1_median",
    "vibration_acc_rms_1khz_to_max__stats_8_1_median",
    "vibration_acc_p2p__stats_8_1_median",
    "vibration_env_rms__stats_8_1_median",
    "vibration_vel_rms__stats_8_1_median",
    "vibration_vel_order__0__stats_8_1_median",
    "vibration_vel_order__1__stats_8_1_median",
    "vibration_vel_order__2__stats_8_1_median",
    "vibration_vel_order__3__stats_8_1_median",
    "machine_line_frequency__stats_8_1_median",
    "vibration_acc_kurt__stats_30_1_median",
    "vibration_acc_rms__stats_30_1_median",
    "vibration_acc_rms_0k_1k__stats_30_1_median",
    "vibration_acc_rms_1k_2k__stats_30_1_median",
    "vibration_acc_rms_1khz_to_max__stats_30_1_median",
    "vibration_acc_p2p__stats_30_1_median",
    "vibration_env_rms__stats_30_1_median",
    "vibration_vel_rms__stats_30_1_median",
    "vibration_vel_order__0__stats_30_1_median",
    "vibration_vel_order__1__stats_30_1_median",
    "vibration_vel_order__2__stats_30_1_median",
    "vibration_vel_order__3__stats_30_1_median",
    "machine_line_frequency__stats_30_1_median",
    "vibration_acc_kurt__stats_90_1_median",
    "vibration_acc_rms__stats_90_1_median",
    "vibration_acc_rms_0k_1k__stats_90_1_median",
    "vibration_acc_rms_1k_2k__stats_90_1_median",
    "vibration_acc_rms_1khz_to_max__stats_90_1_median",
    "vibration_acc_p2p__stats_90_1_median",
    "vibration_env_rms__stats_90_1_median",
    "vibration_vel_rms__stats_90_1_median",
    "vibration_vel_order__0__stats_90_1_median",
    "vibration_vel_order__1__stats_90_1_median",
    "vibration_vel_order__2__stats_90_1_median",
    "vibration_vel_order__3__stats_90_1_median",
    "machine_line_frequency__stats_90_1_median",
    "vibration_acc_kurt__stats_1_0_pctl_90",
    "vibration_acc_rms__stats_1_0_pctl_90",
    "vibration_acc_rms_0k_1k__stats_1_0_pctl_90",
    "vibration_acc_rms_1k_2k__stats_1_0_pctl_90",
    "vibration_acc_rms_1khz_to_max__stats_1_0_pctl_90",
    "vibration_acc_p2p__stats_1_0_pctl_90",
    "vibration_env_rms__stats_1_0_pctl_90",
    "vibration_vel_rms__stats_1_0_pctl_90",
    "vibration_vel_order__0__stats_1_0_pctl_90",
    "vibration_vel_order__1__stats_1_0_pctl_90",
    "vibration_vel_order__2__stats_1_0_pctl_90",
    "vibration_vel_order__3__stats_1_0_pctl_90",
    "machine_line_frequency__stats_1_0_pctl_90",
    "vibration_acc_kurt__stats_8_1_pctl_90",
    "vibration_acc_rms__stats_8_1_pctl_90",
    "vibration_acc_rms_0k_1k__stats_8_1_pctl_90",
    "vibration_acc_rms_1k_2k__stats_8_1_pctl_90",
    "vibration_acc_rms_1khz_to_max__stats_8_1_pctl_90",
    "vibration_acc_p2p__stats_8_1_pctl_90",
    "vibration_env_rms__stats_8_1_pctl_90",
    "vibration_vel_rms__stats_8_1_pctl_90",
    "vibration_vel_order__0__stats_8_1_pctl_90",
    "vibration_vel_order__1__stats_8_1_pctl_90",
    "vibration_vel_order__2__stats_8_1_pctl_90",
    "vibration_vel_order__3__stats_8_1_pctl_90",
    "machine_line_frequency__stats_8_1_pctl_90",
    "vibration_acc_kurt__stats_30_1_pctl_90",
    "vibration_acc_rms__stats_30_1_pctl_90",
    "vibration_acc_rms_0k_1k__stats_30_1_pctl_90",
    "vibration_acc_rms_1k_2k__stats_30_1_pctl_90",
    "vibration_acc_rms_1khz_to_max__stats_30_1_pctl_90",
    "vibration_acc_p2p__stats_30_1_pctl_90",
    "vibration_env_rms__stats_30_1_pctl_90",
    "vibration_vel_rms__stats_30_1_pctl_90",
    "vibration_vel_order__0__stats_30_1_pctl_90",
    "vibration_vel_order__1__stats_30_1_pctl_90",
    "vibration_vel_order__2__stats_30_1_pctl_90",
    "vibration_vel_order__3__stats_30_1_pctl_90",
    "machine_line_frequency__stats_30_1_pctl_90",
    "vibration_acc_kurt__stats_90_1_pctl_90",
    "vibration_acc_rms__stats_90_1_pctl_90",
    "vibration_acc_rms_0k_1k__stats_90_1_pctl_90",
    "vibration_acc_rms_1k_2k__stats_90_1_pctl_90",
    "vibration_acc_rms_1khz_to_max__stats_90_1_pctl_90",
    "vibration_acc_p2p__stats_90_1_pctl_90",
    "vibration_env_rms__stats_90_1_pctl_90",
    "vibration_vel_rms__stats_90_1_pctl_90",
    "vibration_vel_order__0__stats_90_1_pctl_90",
    "vibration_vel_order__1__stats_90_1_pctl_90",
    "vibration_vel_order__2__stats_90_1_pctl_90",
    "vibration_vel_order__3__stats_90_1_pctl_90",
    "machine_line_frequency__stats_90_1_pctl_90",
    "cliff_status",
    "rapid_cliff_status",
    "trend_status",
    "magnetic_mag_var",
    "magnetic_zero_crossings_percentile_density",
    "magnetic_mag_rmsHF",
    "magnetic_window_var_percentile",
    "magnetic_acc_rms",
    "magnetic_mag_p2p_percentiles",
    "magnetic_mag_rmsLF",
    "magnetic_zero_crossings_std",
    "magnetic_magTotalPeaks",
    "magnetic_mag_p2p",
    "is_valid_magnetic",
    "magnetic_zero_crossings_pvalue",
    "magnetic_magLF",
    "magnetic_window_p2p",
    "magnetic_zero_crossings_percentile",
    "magnetic_magLF_level",
    "temperature_EpTemp",
    "is_valid_temperature",
    "magnetic_acc_rms__stats_1_0_mean",
    "magnetic_maglf__stats_1_0_mean",
    "magnetic_maglf_level__stats_1_0_mean",
    "magnetic_acc_rms__stats_8_1_mean",
    "magnetic_maglf__stats_8_1_mean",
    "magnetic_maglf_level__stats_8_1_mean",
    "magnetic_acc_rms__stats_30_1_mean",
    "magnetic_maglf__stats_30_1_mean",
    "magnetic_maglf_level__stats_30_1_mean",
    "magnetic_acc_rms__stats_90_1_mean",
    "magnetic_maglf__stats_90_1_mean",
    "magnetic_maglf_level__stats_90_1_mean",
    "magnetic_acc_rms__stats_1_0_std",
    "magnetic_maglf__stats_1_0_std",
    "magnetic_maglf_level__stats_1_0_std",
    "magnetic_acc_rms__stats_8_1_std",
    "magnetic_maglf__stats_8_1_std",
    "magnetic_maglf_level__stats_8_1_std",
    "magnetic_acc_rms__stats_30_1_std",
    "magnetic_maglf__stats_30_1_std",
    "magnetic_maglf_level__stats_30_1_std",
    "magnetic_acc_rms__stats_90_1_std",
    "magnetic_maglf__stats_90_1_std",
    "magnetic_maglf_level__stats_90_1_std",
    "magnetic_acc_rms__stats_1_0_median",
    "magnetic_maglf__stats_1_0_median",
    "magnetic_maglf_level__stats_1_0_median",
    "magnetic_acc_rms__stats_8_1_median",
    "magnetic_maglf__stats_8_1_median",
    "magnetic_maglf_level__stats_8_1_median",
    "magnetic_acc_rms__stats_30_1_median",
    "magnetic_maglf__stats_30_1_median",
    "magnetic_maglf_level__stats_30_1_median",
    "magnetic_acc_rms__stats_90_1_median",
    "magnetic_maglf__stats_90_1_median",
    "magnetic_maglf_level__stats_90_1_median",
    "magnetic_acc_rms__stats_1_0_pctl_90",
    "magnetic_maglf__stats_1_0_pctl_90",
    "magnetic_maglf_level__stats_1_0_pctl_90",
    "magnetic_acc_rms__stats_8_1_pctl_90",
    "magnetic_maglf__stats_8_1_pctl_90",
    "magnetic_maglf_level__stats_8_1_pctl_90",
    "magnetic_acc_rms__stats_30_1_pctl_90",
    "magnetic_maglf__stats_30_1_pctl_90",
    "magnetic_maglf_level__stats_30_1_pctl_90",
    "magnetic_acc_rms__stats_90_1_pctl_90",
    "magnetic_maglf__stats_90_1_pctl_90",
    "magnetic_maglf_level__stats_90_1_pctl_90",
    "temperature_eptemp__stats_1_0_mean",
    "temperature_eptemp__stats_8_1_mean",
    "temperature_eptemp__stats_30_1_mean",
    "temperature_eptemp__stats_90_1_mean",
    "temperature_eptemp__stats_1_0_std",
    "temperature_eptemp__stats_8_1_std",
    "temperature_eptemp__stats_30_1_std",
    "temperature_eptemp__stats_90_1_std",
    "temperature_eptemp__stats_1_0_median",
    "temperature_eptemp__stats_8_1_median",
    "temperature_eptemp__stats_30_1_median",
    "temperature_eptemp__stats_90_1_median",
    "temperature_eptemp__stats_1_0_pctl_90",
    "temperature_eptemp__stats_8_1_pctl_90",
    "temperature_eptemp__stats_30_1_pctl_90",
    "temperature_eptemp__stats_90_1_pctl_90"
]