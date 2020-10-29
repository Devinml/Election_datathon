import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def read_pkl_df(file_path):
    df = pd.read_pickle(file_path)
    return df

def mod_df(df):
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['day_of_year'] = pd.DatetimeIndex(df['created_at']).dayofyear
    df['hour'] = pd.DatetimeIndex(df['created_at']).hour
    df['minute'] = pd.DatetimeIndex(df['created_at']).minute
    return df

def count_plot(df):
    fig, ax = plt.subplots()
    sns.countplot(x='minute', data=df)


def main():
    fp = 'data/pkl_df/df.pkl'
    df = read_pkl_df(fp)
    df = mod_df(df)
    count_plot(df)
    # print(df.head())


if __name__ == '__main__':
    main()
    plt.show()