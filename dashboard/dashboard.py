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

    st.subheader("Pendahuluan")
    st.markdown("""
    Halaman ini dibuat sebagai proyek akhir dari kelas Belajar Analisis Data dengan Python
                
    Data yang digunakan pada proyek akhir ini adalah data terkait Kualitas Air (Air Quality) di Negara China dengan alat pengukur kualitas udara yang telah tersedia.
                
    Pada data tersebut, didapatkan rentang data dari awal tahun 2013 hingga awal tahun (bulan ke-2) tahun 2017. 
    Untuk penelitian kali ini akan menggunakan range data tahunan, sehingga data pada tahun 2017 akan dihapuskan karena tidak lengkap dan akan menimbulkan ketimpangan terhadap tahun-tahun sebelumnya.
    Setelah dilakukan *cleaning data* dengan cara melakukan interpolasi terhadap data kosong lalu menghapuskan data yang tidak dapat dilakukan interpolasi (seperti data pada awal data).
    Maka data yang benar benar diolah adalah sebanyak **377620** baris.            
    
                
    Berdasarkan data yang tersedia, maka beberapa pertanyaan yang dirancang adalah:
    1. Wilayah mana yang memiliki kualitas udara yang paling buruk?
    1. Bagaimana tren kualitas udara di China dari tahun 2013?
    1. Wilayah mana yang memiliki suhu udara paling tinggi?
    1. Bagaimana tren suhu udara di China dari tahun 2013?
                
    Dari pertanyaan tersebut, didapatkan hasil sebagai berikut:
    """)


    st.subheader("Perbandingan Kualitas Udara pada Setiap Wilayah")
    pm_comparison_fig = draw_pm_comparison(pm_df)
    st.pyplot(pm_comparison_fig)
    st.caption("Grafik kualitas udara setiap wilayah pada setiap tahun")

    st.markdown("""
    Berdasarkan grafik tersebut dapat terlihat bahwa tidak terdapat wilayah dengan kategori kualitas udara terburuk 
    karena setiap tahunnya wilayah dengan kualitas udara terburuk terus berubah. 
    
    Seperti pada tahun **2013** wilayah dengan kualitas udara terburuk adalah **Donsi dan Wanliu**.
    
    Sementara itu pada tahun **2014** adalah **Gucheng dan Wanliu**.
    
    Berubah pada tahun **2015** adalah **Nongzhanguan**. 
                
    Pada akhirnya **2016** kembali dipegang oleh **Gucheng**.
    ____
    """)


    st.subheader("Tren Kualitas Udara per Tahun")
    pm_linechart_fig = draw_pm_linechart(pm_df)
    st.pyplot(pm_linechart_fig)
    st.caption("Grafik tren kualitas udara setiap wilayah pada setiap tahun")
    st.markdown("""
    Berdasarkan grafik tersebut dapat terlihat bahwa terdapat penurunan jumlah particulate matter 2.5
    pada setiap wilayah hingga tahun 2015. Pada periode 2015 hingga 2016 pada beberapa wilayah terdapat penurunan PM2.5
    dan ada beberapa wilayah yang terdapat kenaikan jumlah PM2.5.
                
    ____
    """)

    st.subheader("Perbandingan Suhu Udara pada Setiap Wilayah")
    temp_comparison_fig = draw_temp_comparison(temp_df)
    st.pyplot(temp_comparison_fig)
    st.caption("Grafik perbandingan suhu udara pada setiap wilayah")
    st.markdown("""
   Berdasarkan grafik tersebut dapat terlihat bahwa tidak terdapat perbedaan signifikan antara suhu udara antar wilayah.
    ____
    """)

    st.subheader("Tren Suhu Udara per Tahun")
    temp_linechart_fig = draw_temp_linechart(temp_df)
    st.pyplot(temp_linechart_fig)
    st.caption("Grafik tren suhu udara setiap wilayah pada setiap tahun")
    st.markdown("""
    Berdasarkan grafik tersebut dapat terlihat bahwa terdapat tren penurunan suhu udara 
    pada setiap wilayah hingga tahun 2016. 
    
    Penurunan signifikan terjadi pada periode 2013-2014 dimana seluruh wilayah terdapat penurunan suhu udara sekitar 1 derajat.
    
    Penurunan signifikan lainnya terjadi pada periode 2015-2016, dimana nyaris seluruh wilayah terdapat penurunan suhu signifikan,
    namun terhadap pula penurunan yang tidak signifikan seperti wilayah **Guanyuan, Tiantan, dan Wanshouxigong**
    ____
    """)

    st.caption("Proyek ini dibuat oleh Ahmad Naufal Hilmy")
    st.caption("Email: hilmyahmadnaufal@gmail.com")