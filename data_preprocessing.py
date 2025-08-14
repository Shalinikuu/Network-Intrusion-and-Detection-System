import os
import pandas as pd
import numpy as np

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

np.random.seed(42)
num_normal = 1000
num_attack = 1000
features = ['duration','src_bytes','dst_bytes','wrong_fragment','urgent',
            'hot','num_failed_logins','logged_in','count','srv_count']

normal_data = {
    'duration': np.random.randint(0, 1000, num_normal),
    'src_bytes': np.random.randint(0, 5000, num_normal),
    'dst_bytes': np.random.randint(0, 5000, num_normal),
    'wrong_fragment': np.zeros(num_normal, dtype=int),
    'urgent': np.zeros(num_normal, dtype=int),
    'hot': np.random.randint(0, 2, num_normal),
    'num_failed_logins': np.zeros(num_normal, dtype=int),
    'logged_in': np.ones(num_normal, dtype=int),
    'count': np.random.randint(1, 100, num_normal),
    'srv_count': np.random.randint(1, 50, num_normal),
    'label': np.zeros(num_normal, dtype=int)
}

attack_data = {
    'duration': np.random.randint(1000, 10000, num_attack),
    'src_bytes': np.random.randint(5000, 100000, num_attack),
    'dst_bytes': np.random.randint(5000, 100000, num_attack),
    'wrong_fragment': np.random.randint(1, 5, num_attack),
    'urgent': np.random.randint(0, 2, num_attack),
    'hot': np.random.randint(2, 10, num_attack),
    'num_failed_logins': np.random.randint(1, 5, num_attack),
    'logged_in': np.zeros(num_attack, dtype=int),
    'count': np.random.randint(50, 200, num_attack),
    'srv_count': np.random.randint(20, 100, num_attack),
    'label': np.ones(num_attack, dtype=int)
}

normal_df = pd.DataFrame(normal_data)
attack_df = pd.DataFrame(attack_data)

custom_dataset = pd.concat([normal_df, attack_df]).sample(frac=1, random_state=42).reset_index(drop=True)
custom_dataset.to_csv('data/custom_nids_dataset.csv', index=False)
