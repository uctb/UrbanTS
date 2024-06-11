import pandas as pd
import matplotlib.pyplot as plt
def convert2UTC(dt:pd.Timestamp,city:str):
    return dt.tz_localize(city).tz_convert('UTC')
def convert2Local(dt:pd.Timestamp,city:str):
    return dt.tz_localize('UTC').tz_convert(city)
#改为数据路径
csv_path = 'path.csv'
df = pd.read_csv(csv_path)
df['datetime'] = pd.to_datetime(df['timestamp'],unit='s')
df['datetime'] = df['datetime'].apply(lambda x: convert2Local(x,'America/Chicago'))
#三个时间分别采样春夏秋，根据样本更改时间
datetime_1 = pd.Timestamp('2015-03-01 00:00:00', tz='America/Chicago')
#南半球地区把改成12月
datetime_2 = pd.Timestamp('2015-06-01 00:00:00', tz='America/Chicago')
datetime_3 = pd.Timestamp('2015-09-01 00:00:00', tz='America/Chicago')
max_datetime = df['datetime'].max()
min_datetime = df['datetime'].min()
print('Max DateTime',max_datetime.strftime('%Y-%m-%d %H:%M:%S'))
print('Min DateTime',min_datetime.strftime('%Y-%m-%d %H:%M:%S'))
# 时间跨度大于一周
assert df['datetime'].max() - df['datetime'].min() >= pd.Timedelta(days=7)
df_tmp = df.groupby(['item_id'])['target'].sum().reset_index()
# get max medium and lowerest target rows of df
max_target = df_tmp['target'].max()
min_target = df_tmp['target'].min()
median_target = df_tmp['target'].median()
item_id_max = df_tmp[df_tmp['target'] == max_target]['item_id'].mode()
item_id_min = df_tmp[df_tmp['target'] == min_target]['item_id'].mode()
item_id_median = df_tmp[df_tmp['target'] == median_target]['item_id'].mode()
item_id_max_v=item_id_max.values[0]
item_id_min_v=item_id_min.values[0]
item_id_median_v=item_id_median.values[0]
df_max_item_id = df[df['item_id'] == item_id_max_v]
df_min_item_id = df[df['item_id'] == item_id_min_v]
df_median_item_id = df[df['item_id'] == item_id_median_v]
df_max_item_id.to_csv('df_max_item_id.csv',index=False)
df_min_item_id.to_csv('df_min_item_id.csv',index=False)
df_median_item_id.to_csv('df_median_item_id.csv',index=False)

df_max_item_id_selected_a_week_1 = df_max_item_id.loc[(df_max_item_id['datetime']>=datetime_1)&(df_max_item_id['datetime']<datetime_1+pd.Timedelta(days=7))]
df_median_item_id_selected_a_week_1 = df_median_item_id.loc[(df_median_item_id['datetime']>=datetime_1)&(df_median_item_id['datetime']<datetime_1+pd.Timedelta(days=7))]
df_min_item_id_selected_a_week_1 = df_min_item_id.loc[(df_min_item_id['datetime']>=datetime_1)&(df_min_item_id['datetime']<datetime_1+pd.Timedelta(days=7))]

df_max_item_id_selected_a_week_2 = df_max_item_id.loc[(df_max_item_id['datetime']>=datetime_2)&(df_max_item_id['datetime']<datetime_2+pd.Timedelta(days=7))]
df_median_item_id_selected_a_week_2 = df_median_item_id.loc[(df_median_item_id['datetime']>=datetime_2)&(df_median_item_id['datetime']<datetime_2+pd.Timedelta(days=7))]
df_min_item_id_selected_a_week_2 = df_min_item_id.loc[(df_min_item_id['datetime']>=datetime_2)&(df_min_item_id['datetime']<datetime_2+pd.Timedelta(days=7))]

df_max_item_id_selected_a_week_3 = df_max_item_id.loc[(df_max_item_id['datetime']>=datetime_3)&(df_max_item_id['datetime']<datetime_3+pd.Timedelta(days=7))]
df_median_item_id_selected_a_week_3 = df_median_item_id.loc[(df_median_item_id['datetime']>=datetime_3)&(df_median_item_id['datetime']<datetime_3+pd.Timedelta(days=7))]
df_min_item_id_selected_a_week_3 = df_min_item_id.loc[(df_min_item_id['datetime']>=datetime_3)&(df_min_item_id['datetime']<datetime_3+pd.Timedelta(days=7))]

print('Number of item_id',len(df['item_id'].unique()))
print('Number of total records',df['target'].sum())
print('Max DateTime',max_datetime.strftime('%Y-%m-%d %H:%M:%S'))
print('Min DateTime',min_datetime.strftime('%Y-%m-%d %H:%M:%S'))

df_max_item_id_selected_a_week_1.plot(x='datetime',y='target',title='max volume item_id 03')
plt.show()
df_median_item_id_selected_a_week_1.plot(x='datetime',y='target',title='median volume item_id 03')
plt.show()
df_min_item_id_selected_a_week_1.plot(x='datetime',y='target',title='min volume item_id 03')
plt.show()

df_max_item_id_selected_a_week_2.plot(x='datetime',y='target',title='max volume item_id 06')
plt.show()
df_median_item_id_selected_a_week_2.plot(x='datetime',y='target',title='median volume item_id 06')
plt.show()
df_min_item_id_selected_a_week_2.plot(x='datetime',y='target',title='min volume item_id 06')
plt.show()

df_max_item_id_selected_a_week_3.plot(x='datetime',y='target',title='max volume item_id 09')
plt.show()
df_median_item_id_selected_a_week_3.plot(x='datetime',y='target',title='median volume item_id 09')
plt.show()
df_min_item_id_selected_a_week_2.plot(x='datetime',y='target',title='min volume item_id 09')
plt.show()

