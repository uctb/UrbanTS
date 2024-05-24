import pandas as pd
from .utils import convert2Local
import matplotlib.pyplot as plt
csv_path = 'bike_chicago.csv'
df = pd.read_csv(csv_path)
df['datetime'] = pd.to_datetime(df['timestamp'],unit='s')

df['datetime'] = df['datetime'].apply(lambda x: convert2Local(x,'America/Chicago'))

max_datetime = df['datetime'].max()
min_datetime = df['datetime'].min()
# 时间跨度大于一周
assert df['datetime'].max() - df['datetime'].min() >= pd.Timedelta(days=7)

df_tmp = df.groupby(['item_id']).sum()

# get max medium and lowerest target rows of df
max_target = df_tmp['target'].max()
min_target = df_tmp['target'].min()
median_target = df_tmp['target'].median()

item_id_max = df_tmp[df_tmp['target'] == max_target,'item_id'].mode()
item_id_min = df_tmp[df_tmp['target'] == min_target,'item_id'].mode()
item_id_median = df_tmp[df_tmp['target'] == median_target,'item_id'].mode()

df_max_item_id = df[df['item_id'] == item_id_max]
df_min_item_id = df[df['item_id'] == item_id_min]
df_median_item_id = df[df['item_id'] == item_id_median]

df_max_item_id_selected_a_week = df_max_item_id.loc[(df_max_item_id['datetime']>=min_datetime)&(df_max_item_id['datetime']<min_datetime+pd.Timedelta(days=7))]
df_median_item_id_selected_a_week = df_median_item_id.loc[(df_median_item_id['datetime']>=min_datetime)&(df_median_item_id['datetime']<min_datetime+pd.Timedelta(days=7))]
df_min_item_id_selected_a_week = df_min_item_id.loc[(df_min_item_id['datetime']>=min_datetime)&(df_min_item_id['datetime']<min_datetime+pd.Timedelta(days=7))]

print('Number of item_id',len(df['item_id'].unique()))
print('Number of total records',df['target'].sum())
print('Max DateTime',max_datetime.strftime('%Y-%m-%d %H:%M:%S'))
print('Min DateTime',min_datetime.strftime('%Y-%m-%d %H:%M:%S'))


df_max_item_id_selected_a_week.plot(x='datetime',y='target',title='max volume item_id')
plt.show()
df_median_item_id_selected_a_week.plot(x='datetime',y='target',title='median volume item_id')
plt.show()
df_min_item_id_selected_a_week.plot(x='datetime',y='target',title='median volume item_id')
plt.show()


