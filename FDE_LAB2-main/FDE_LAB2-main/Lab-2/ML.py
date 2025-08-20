# # Minimal ML pipeline for VIP customer classification

# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster._kmeans import KMeans  # Direct import to avoid extra modules

# # Load processed sales data
# df = pd.read_csv("data_warehouse/processed_sales_data.csv")

# # Feature engineering
# customer_df = df.groupby('customer_id').agg({
#     'total_revenue': 'sum',
#     'product_id': 'count'
# }).reset_index()
# customer_df.rename(columns={'product_id': 'purchase_frequency'}, inplace=True)

# # Scaling features
# scaler = StandardScaler()
# scaled_features = scaler.fit_transform(
#     customer_df[['total_revenue', 'purchase_frequency']]
# )

# # K-Means clustering
# kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
# customer_df['VIP_status'] = kmeans.fit_predict(scaled_features)

# # Map labels (decide which cluster is VIP based on total_revenue mean)
# vip_cluster = customer_df.groupby('VIP_status')['total_revenue'].mean().idxmax()
# customer_df['VIP_status'] = customer_df['VIP_status'].apply(
#     lambda x: 'VIP' if x == vip_cluster else 'Non-VIP'
# )

# # Reverse ETL – merge back into main dataset
# df = pd.merge(df, customer_df[['customer_id', 'VIP_status']], on='customer_id', how='left')

# # Save enriched data
# df.to_csv("data_warehouse/enriched_sales_data.csv", index=False)

# print("VIP classification complete. Output saved to enriched_sales_data.csv")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_warehouse/enriched_sales_data.csv")

vip_revenue = df.groupby('VIP_status')['total_revenue'].sum()

plt.bar(vip_revenue.index, vip_revenue.values)
plt.xlabel('Customer Type')
plt.ylabel('Total Revenue')
plt.title('VIP vs Non-VIP Revenue')
plt.show()
