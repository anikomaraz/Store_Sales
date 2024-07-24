# imports
import pandas as pd
from matplotlib import pyplot as plt

#################  DATA   ####################

# read data
data_path = '../data/'
data_holidays_events = pd.read_csv(data_path + 'holidays_events.csv')
#A holiday that is transferred officially falls on that calendar day, but was moved to another date by the government. A transferred day is more like a normal day than a holiday.

data_oil = pd.read_csv(data_path + 'oil.csv')
data_stores = pd.read_csv(data_path + 'stores.csv')  #cluster is a grouping of similar stores.
data_train = pd.read_csv(data_path + 'train.csv')
#onpromotion gives the total number of items in a product family that were being promoted at a store at a given date.
data_transactions = pd.read_csv(data_path + 'transactions.csv')

# read in test data
data_test = pd.read_csv(data_path + 'test.csv') # 15 days after train data

# Wages in the public sector are paid every two weeks on the 15 th and on the last day of the month. Supermarket sales could be affected by this.
# A magnitude 7.8 earthquake struck Ecuador on April 16, 2016. People rallied in relief efforts donating water and other first need products which greatly affected supermarket sales for several weeks after the earthquake.

print(data_holidays_events.head())

#################  DATA   ####################