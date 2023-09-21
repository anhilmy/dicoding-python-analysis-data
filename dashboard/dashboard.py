import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

def dataframe_temp(df: pd.DataFrame):
    res = df.groupby("station").resample(rule="Y", on="datetime").agg({
        "TEMP": ["mean"]
    })
    res = res.swaplevel(0,1, axis=0).sort_index(level=0, axis="rows").reset_index()
    res['datetime'] = res['datetime'].dt.year
    res["mean"] = res[("TEMP", "mean")]
    res.drop(columns=("TEMP", "mean"), inplace=True)
    res.reset_index(inplace=True)
    return res

def dataframe_pm(df: pd.DataFrame):
    res = df.groupby("station").resample(rule="Y", on="datetime").agg({
        "PM2.5": ["mean"]
    })
    res = res.swaplevel(0,1, axis=0).sort_index(level=0, axis="rows").reset_index()
    res['datetime'] = res['datetime'].dt.year
    res["mean"] = res[("PM2.5", "mean")]
    res.drop(columns=("PM2.5", "mean"), inplace=True)
    res.reset_index(inplace=True)
    return res

def draw_pm_comparison(df: pd.DataFrame):

    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(20, 9))
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    # print(a_df[a_df["datetime"] == 2013])

    sns.barplot(x="station", y="mean", data=(df[df["datetime"] == 2013]), ax=ax[0][0])
    ax[0][0].xaxis.set_tick_params(rotation=-30)
    ax[0][0].set_ylabel("PM2.5 (ug/m^3)")
    ax[0][0].set_xlabel(None)
    ax[0][0].set_title("2013", loc="center", fontsize=15)
    ax[0][0].tick_params(axis ='y', labelsize=12)

    sns.barplot(x="station", y="mean", data=(df[df["datetime"] == 2014]), ax=ax[0][1])
    ax[0][1].xaxis.set_tick_params(rotation=-30)
    ax[0][1].set_ylabel("PM2.5 (ug/m^3)")
    ax[0][1].set_xlabel(None)
    ax[0][1].set_title("2014", loc="center", fontsize=15)
    ax[0][1].tick_params(axis ='y', labelsize=12)

    sns.barplot(x="station", y="mean", data=(df[df["datetime"] == 2015]), ax=ax[1][0])
    ax[1][0].xaxis.set_tick_params(rotation=-30)
    ax[1][0].set_ylabel("PM2.5 (ug/m^3)")
    ax[1][0].set_xlabel(None)
    ax[1][0].set_title("2015", loc="center", fontsize=15)
    ax[1][0].tick_params(axis ='y', labelsize=12)

    sns.barplot(x="station", y="mean", data=(df[df["datetime"] == 2016]), ax=ax[1][1])
    ax[1][1].xaxis.set_tick_params(rotation=-30)
    ax[1][1].set_ylabel("PM2.5 (ug/m^3)")
    ax[1][1].set_xlabel(None)
    ax[1][1].set_title("2016", loc="center", fontsize=15)
    ax[1][1].tick_params(axis ='y', labelsize=12)

    return fig

def draw_pm_linechart(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(20, 9))
    ax.set_ylabel("PM2.5 (ug/m^3)")
    ax.set_xlabel("tahun.bulan")
    ax.set_title("Tren Kualitas udara per tahun")
    sns.lineplot(x="datetime", y='mean', hue="station",  data=df)
    return fig

def draw_temp_comparison(df: pd.DataFrame):
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(20, 9))
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    # print(a_df[a_df["datetime"] == 2013])

    sns.barplot(x="station", y="mean", data=(df[df["datetime"] == 2013]), ax=ax[0][0])
    ax[0][0].xaxis.set_tick_params(rotation=-30)
    ax[0][0].set_ylabel("temperature (in Celsius) ")
    ax[0][0].set_xlabel(None)
    ax[0][0].set_title("2013", loc="center", fontsize=15)
    ax[0][0].tick_params(axis ='y', labelsize=12)

    sns.barplot(x="station", y="mean", data=(df[df["datetime"] == 2014]), ax=ax[0][1])
    ax[0][1].xaxis.set_tick_params(rotation=-30)
    ax[0][1].set_ylabel("temperature (in Celsius) ")
    ax[0][1].set_xlabel(None)
    ax[0][1].set_title("2014", loc="center", fontsize=15)
    ax[0][1].tick_params(axis ='y', labelsize=12)

    sns.barplot(x="station", y="mean", data=(df[df["datetime"] == 2015]), ax=ax[1][0])
    ax[1][0].xaxis.set_tick_params(rotation=-30)
    ax[1][0].set_ylabel("temperature (in Celsius) ")
    ax[1][0].set_xlabel(None)
    ax[1][0].set_title("2015", loc="center", fontsize=15)
    ax[1][0].tick_params(axis ='y', labelsize=12)

    sns.barplot(x="station", y="mean", data=(df[df["datetime"] == 2016]), ax=ax[1][1])
    ax[1][1].xaxis.set_tick_params(rotation=-30)
    ax[1][1].set_ylabel("temperature (in Celsius) ")
    ax[1][1].set_xlabel(None)
    ax[1][1].set_title("2016", loc="center", fontsize=15)
    ax[1][1].tick_params(axis ='y', labelsize=12)

    return fig

def draw_temp_linechart(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(20, 9))
    ax.set_ylabel("temperature (in Celsius) ")
    ax.set_xlabel("tahun.bulan")
    ax.set_title("Trend suhu per tahun")
    sns.lineplot(x="datetime", y='mean', hue="station",  data=df)

    return fig


if __name__ == "__main__":
    sns.set(style='dark')
    all_df = pd.read_csv("dashboard/clean_data.csv")

    all_df["datetime"] = pd.to_datetime(all_df["datetime"])
    all_df.drop(all_df[all_df["datetime"] > '2017-01-01'].index, inplace=True)
    all_df.reset_index(inplace=True)

    pm_df = dataframe_pm(all_df)
    temp_df = dataframe_temp(all_df)

    st.header("Proyek Analisis Data")

    pm_comparison_fig = draw_pm_comparison(pm_df)
    st.pyplot(pm_comparison_fig)

    pm_linechart_fig = draw_pm_linechart(pm_df)
    st.pyplot(pm_linechart_fig)

    temp_comparison_fig = draw_temp_comparison(temp_df)
    st.pyplot(temp_comparison_fig)

    temp_linechart_fig = draw_temp_linechart(temp_df)
    st.pyplot(temp_linechart_fig)

