import pandas as pd
from dotenv import load_dotenv
from nixtlats import TimeGPT
load_dotenv()


def kaggle_data_src():
    USD_RUB_df = pd.read_csv("USD_RUB.csv", sep=",")
    timegpt = TimeGPT()
    timegpt_fcst_df = timegpt.forecast(
        df=USD_RUB_df,
        h=12,
        freq='B',
        time_col='Date',
        target_col='Price',
    )
    plt2 = timegpt.plot(USD_RUB_df, timegpt_fcst_df, time_col='Date', target_col='Price')
    plt2.show()


def wsj():
    timegpt = TimeGPT()
    USD_RUB_df = pd.read_csv(
        "HistoricalPrices.csv",
        sep=",",
        header=0,
        names=['Date', 'Open', 'High', 'Low', 'Close'],
    )
    USD_RUB_df['Date'] = pd.to_datetime(USD_RUB_df['Date'], format="%m/%d/%y")  # 01/18/24
    timegpt_fcst_df = timegpt.forecast(
        df=USD_RUB_df,
        h=12,
        freq='B',
        time_col='Date',
        target_col='Close',
    )
    plt = timegpt.plot(USD_RUB_df, timegpt_fcst_df, time_col='Date', target_col='Close', )
    plt.show()
    return


def main():
    kaggle_data_src()
    wsj()


if __name__ == '__main__':
    main()
