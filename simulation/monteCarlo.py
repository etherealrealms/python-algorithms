class MonteCarlo(object):
    def __init__(self, number_of_times_per_trial=1, number_of_trials=10000):
        self.number_of_times_per_trial = number_of_times_per_trial
        self.number_of_trials = number_of_trials

    @staticmethod
    def std_dev(trial_mean, trial_results):
        sum_of_squares_dev_from_mean = 0

        for x in trial_results:
            sum_of_squares_dev_from_mean += (x - trial_mean)**2

        return (sum_of_squares_dev_from_mean / len(trial_results))**0.5

    def simulate(self, object_to_simulate):
        trials = {
            'trials': [],
            'trial_run_means': [],
            'mean_over_all_runs': 0,
            'std_dev_of_means': 0,
            'number_of_trials': self.number_of_trials
        }

        sum_of_results_for_trial = 0

        for i in range(0, self.number_of_trials):
            sum_of_results_for_run = 0
            run_results = []

            for j in range(0, self.number_of_times_per_trial):
                result = object_to_simulate.simulate()
                sum_of_results_for_run += result
                run_results.append(result)

            sum_of_results_for_trial += sum_of_results_for_run
            run_mean = sum_of_results_for_run / self.number_of_times_per_trial
            trials['trial_run_means'].append(run_mean)
            trials['trials'].append({
                'mean': run_mean,
                'std_dev':  MonteCarlo.std_dev(run_mean, run_results),
                'results': run_results,
                'number_of_runs': self.number_of_times_per_trial, 'trial_count': i + 1
            })

        mean_over_all_runs = sum_of_results_for_trial / self.number_of_trials
        trials['mean_over_all_runs'] = mean_over_all_runs
        trials['std_dev_of_means'] = MonteCarlo.std_dev(mean_over_all_runs, trials['trial_run_means'])

        return trials
