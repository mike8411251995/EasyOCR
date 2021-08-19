import os

data_dir = './all_data/cn_cpoe_val_real/'
csv_path = os.path.join(data_dir, 'labels.csv')

all_files = []

with open(csv_path, 'w', encoding='utf-8') as f:
    f.write('filename,words\n')
    for filename in os.listdir(data_dir):
        if filename.endswith('.jpg'): 
            word = filename.split('_')[0]
            f.write(f'{filename},{word}\n')