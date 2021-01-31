import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import datetime
import matplotlib.dates

book1 =pd.read_excel('Book1.xlsx')
book2 = pd.read_excel('Book2.xlsx')
data = pd.read_excel('RELEVES_MR DOE JOHN_20170119.xlsx')


def total_exp_acc_vs_date(dataframe):                                      # CORRECT
    fig =plt.figure(figsize=(10,5))
    sns.lineplot(y='Value', x='Date', data=dataframe, marker='o')
 #   plt.plot(dataframe.loc[:, "Date"], dataframe.loc[:, "Value"], color="blue", label='prices', marker='o')
    plt.xlabel("Dates")
    plt.ylabel("Total Amount ")
    plt.title("total_exp_acc_to_date")
   # plt.legend(loc='best')
    plt.xticks(rotation=40)
    plt.show()


def withdrawl_and_credit_vs_date(data_frame):                          # CORRECT
    sns.lineplot(y='Amount', x='Date', data=data_frame, hue='Debit/Credit', marker='o')
    plt.xlabel("Category")
    plt.ylabel("Total Amount ")
    plt.title("withdrawl_and_credit_vs_date")
    plt.xticks(rotation=40)
   # plt.legend(loc='best')
    plt.tight_layout()
    plt.show()



def total_exp_vs_category(data_frame):
    df1 = data_frame.groupby('Category')['Value'].sum()
    list1 = []
    list2 = []
    for i, j in df1.items():
        list1.append(i)
        list2.append(j)
    print(list1, "\n", list2)

    plt.bar(list1, list2)
    plt.grid()
    plt.xlabel("Category")
    plt.ylabel("turnover ")
    plt.title("turnover vs category")
    plt.xticks(rotation=40)
    plt.show()


def credit_acc_vs_category(data_frame):
    sns.barplot(y='Credit', x='Category', data=data_frame)
    plt.xlabel("Category")
    plt.ylabel("Credit Amount ")
    plt.title("Credit_amount_vs_category")
    plt.xticks(rotation=40)
    plt.tight_layout()
    plt.legend(loc='best')
    plt.show()


def debit_acc_vs_date(dataframe):
    fig =plt.figure(figsize=(10,5))
    sns.lineplot(y='Debit', x='Date', data=dataframe, marker='o')

    plt.xlabel("Dates")
    plt.ylabel("Debit Amount ")
    plt.title("total_exp_acc_to_date")
    plt.legend(loc='best')
    plt.xticks(rotation=40)
    plt.show()


if __name__ == '__main__':
    total_exp_acc_vs_date(data)
    withdrawl_and_credit_vs_date(book2)
    total_exp_vs_category(data)

   # credit_acc_vs_category(book1)

   # debit_acc_vs_date(book1)
  #  debit_acc_vs_date(book2)

