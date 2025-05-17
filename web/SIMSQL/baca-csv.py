import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

directory = './data'

dataframes = []

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        print('filename:',filename)

        filepath = os.path.join(directory, filename)
        print('filepath:',filepath)
        try:
            df = pd.read_csv(filepath)
            print(df)
            df['store'] = filename.replace('.csv', '')
            print('after:\n', df)
            dataframes.append(df)
            print(f"successfully read {filename}")
        except Exception as e:
            print(f"error reading {filename}: {e}")

for d in dataframes:
    print(d)

if len(dataframes) > 0:
    combined_df = pd.concat(dataframes, ignore_index=True)
    for store, store_data in combined_df.groupby('store'):
        store_data = store_data.sort_values(by=['tanggal'], ascending=True)
    print(store_data)
    # combined_df = combined_df.sort_values(by=['store','sales'], ascending=False)
    # print(combined_df)

    # print("all files combined into a single dataframes.")
    plt.figure(figsize=(12, 6))
    plt.title('Borma sales')
    plt.xlabel('tanggal')
    plt.ylabel('sales')
    plt.bar(store_data['tanggal'], store_data['sales'], color='violet')
    plt.savefig(store + '.png')