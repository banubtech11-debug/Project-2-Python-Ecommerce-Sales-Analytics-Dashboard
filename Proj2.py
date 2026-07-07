 # Task:Ecommerce Dirty Dataset:

import pandas as pd
import numpy as np
ecommerce=pd.read_csv(r'c:\Users\nasira\Downloads\ecommerce_dirty_dataset_375_rows.csv')
print(ecommerce.shape)
print(ecommerce.dtypes)
print(ecommerce.isnull().sum())
print(ecommerce.duplicated().sum())
ecommerce.drop_duplicates(inplace=True)
print(ecommerce.duplicated().sum())
print(ecommerce)

print(ecommerce.columns.tolist())

# order Date:
ecommerce['OrderDate']=pd.to_datetime(ecommerce['OrderDate'],format='mixed')
ecommerce['OrderDate']=ecommerce['OrderDate'].dt.strftime('%Y-%m-%d')
print(ecommerce['OrderDate'])

# OrderMonth:
ecommerce['OrderMonth']=pd.to_datetime(ecommerce['OrderDate']).dt.month
ecommerce['OrderYear']=pd.to_datetime(ecommerce['OrderDate']).dt.year
print(ecommerce[['OrderMonth','OrderYear']])

# Product Name Max Min Value:
print('Max:',ecommerce['ProductName'].max())
print('Min:',ecommerce['ProductName'].min())

# Product Id Max and Min Value:
print('Max:',ecommerce['ShippingCost'].max())
print('Min:',ecommerce['ShippingCost'].min())

# Is Null Values:Shipping Cost
ecommerce['ShippingCost']=ecommerce['ShippingCost'].fillna(ecommerce['ShippingCost'].mean().astype(int))
print(ecommerce['ShippingCost'])
print(ecommerce.isnull().sum())

# # ShippingCost MISING values:
ecommerce["ShippingCost"] = ecommerce["ShippingCost"].fillna(ecommerce.groupby(["CustomerID","ProductID", "OrderID"])["ShippingCost"].transform('mean'))
print(ecommerce[['ShippingCost']])
# print(ecommerce.to_string())

# ShippingCost Max and MIn Values:
print('Max:',ecommerce['ShippingCost'].max())
print('Min:',ecommerce['ShippingCost'].min())
print('Median:',ecommerce['ShippingCost'].median())
print('Mean:',ecommerce['ShippingCost'].mean())
print('Sum:',ecommerce['ShippingCost'].sum())
print('Count:',ecommerce['ShippingCost'].count())
print('Mode:',ecommerce['ShippingCost'].mode())
# print(ecommerce[['ShippingCost']])


# Is Null Values:
ecommerce['Rating']=ecommerce['Rating'].fillna(ecommerce['Rating'].mean().astype(int))
print(ecommerce['Rating'])
print(ecommerce.isnull().sum())


# RATING MISING values:
ecommerce["Rating"] = ecommerce["Rating"].fillna(ecommerce.groupby(["ProductName", "UserReview"])["Rating"].transform('mean'))
print(ecommerce[["Rating"]])
print(ecommerce.to_string())

# Max & MIn Vale:Rating:
print('Max:',ecommerce['Rating'].max())
print('Min:',ecommerce['Rating'].min())
print('Mean:',ecommerce['Rating'].mean())
print('Median:',ecommerce['Rating'].median())
print('Sum:',ecommerce['Rating'].sum())
print('Count:',ecommerce['Rating'].count())
print('Mode:',ecommerce['Rating'].mode())

 
# Is Null Values:User Reviews:
ecommerce['UserReview']=ecommerce['UserReview'].fillna(ecommerce['UserReview'].mode()[0])
print(ecommerce[['UserReview']])
print(ecommerce.to_string())
print(ecommerce.isnull().sum())
print(ecommerce['UserReview'])

# # UserReview :missing values()
ecommerce["UserReview"] = ecommerce["UserReview"].fillna(
    ecommerce.groupby(["ProductName", "Rating"])["UserReview"].transform(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan))
print(ecommerce[["UserReview"]])
# print(ecommerce.to_string())

print('Max:',ecommerce['UserReview'].max())
print('Min:',ecommerce['UserReview'].min())
print('Mode:',ecommerce['UserReview'].mode())
print('Count:',ecommerce['UserReview'].count())

# Is NUll Values:Quantity

ecommerce['Quantity']=ecommerce['Quantity'].fillna(ecommerce['Quantity'].mean().astype(int))
print(ecommerce[['Quantity']])
print(ecommerce.isnull().sum())
print(ecommerce)


# quantity fillna(missing values):Quantity

ecommerce['Quantity']=ecommerce['Quantity'].fillna(ecommerce.groupby(['ProductID','CustomerID'])['Quantity'].transform('mean').astype(int))
print(ecommerce['Quantity'])
# print(ecommerce.to_string())

# Quantity Max and MIn Values:
print('Max:',ecommerce['Quantity'].max())
print('Min:',ecommerce['Quantity'].min())
print('Median:',ecommerce['Quantity'].median())
print('Mean:',ecommerce['Quantity'].mean())
print('Sum:',ecommerce['Quantity'].sum())
print('Count:',ecommerce['Quantity'].count())
print('Mode:',ecommerce['Quantity'].mode())
# print(ecommerce[['Quantity']])

# # Is Null Values:Payment Method:
ecommerce['PaymentMethod']=ecommerce['PaymentMethod'].fillna(ecommerce['PaymentMethod'].mode()[0])
print(ecommerce['PaymentMethod'])
print(ecommerce.isnull().sum())
print(ecommerce)

# # payment Method: fillna(missing values)
ecommerce["PaymentMethod"]=ecommerce['PaymentMethod'].fillna(ecommerce['PaymentMethod'].mode()[0])
print(ecommerce['PaymentMethod'])
# print(ecommerce.to_string())



# # Is null Values:Discount Percent:
ecommerce['DiscountPercent']=ecommerce['DiscountPercent'].fillna(ecommerce['DiscountPercent'].mean())
print(ecommerce['DiscountPercent'])
print(ecommerce.isnull().sum())
print(ecommerce)


# # Missing Values:Discount Percent:
ecommerce['DiscountPercent']=ecommerce['DiscountPercent'].fillna(ecommerce.groupby(['ProductName','Price','Quantity'])['DiscountPercent'].transform('mean').round().astype(int))
print(ecommerce['DiscountPercent'])
# print(ecommerce.to_string())


print('Max:',ecommerce['DiscountPercent'].max())
print('Min:',ecommerce['DiscountPercent'].min())
print('Mean:',ecommerce['DiscountPercent'].mean())
print('Median:',ecommerce['DiscountPercent'].median())
print('Sum:',ecommerce['DiscountPercent'].sum())
print('Count:',ecommerce['DiscountPercent'].count())
print('Mode:',ecommerce['DiscountPercent'].mode())
print(ecommerce[['DiscountPercent']])

# # Region:Is NUll Values:
ecommerce['Region']=ecommerce['Region'].fillna(ecommerce['Region'].mode()[0])
print(ecommerce.isnull().sum())
print(ecommerce)

# # # Region Missing Value:

ecommerce['Region']=ecommerce['Region'].fillna(ecommerce.groupby(['CustomerID'])['Region'].transform(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan))
print(ecommerce['Region'])
# print(ecommerce.to_string())

print('Max:',ecommerce['Region'].max())
print('Min:',ecommerce['Region'].min())
print('Mode:',ecommerce['Region'].mode())
print('Count:',ecommerce['Region'].count())


# # Product Currency:

ecommerce['Product_currency']=ecommerce['Price'].str.extract(r'([$,â,₹,€])')
ecommerce['Price']=ecommerce['Price'].str.replace(r'[$,â,₹,€]','',regex=True)
ecommerce['Price']=pd.to_numeric(ecommerce['Price'])
exchange_rate={
    
    '$': 85,
    '€': 100,
    '₹': 1,
    'â': 1
}
ecommerce['Price']=ecommerce['Price']*ecommerce['Product_currency'].map(exchange_rate)
print(ecommerce['Price'])
# print(ecommerce)


print('Max:',ecommerce['Price'].max())
print('Min:',ecommerce['Price'].min())
print('Mean:',ecommerce['Price'].mean())
print('Median:',ecommerce['Price'].median())
print('Sum:',ecommerce['Price'].sum())
print('Count:',ecommerce['Price'].count())
print('Mode:',ecommerce['Price'].mode())
print(ecommerce[['Price']])
# print(ecommerce.to_string())

# Max & Min Value:Category:
print('Max:',ecommerce['Category'].max())
print('Min:',ecommerce['Category'].min())
print('Count:',ecommerce['Category'].count())
print('Mode:',ecommerce['Category'].mode())


# Count value Category:
max_val = ecommerce['Category'].max()
print('Max:',max_val)
print('Count:',(ecommerce['Category'] == max_val).sum())
min_val=ecommerce['Category'].min()
print('Min:', min_val)
print('Count:',(ecommerce['Category'] == min_val).sum())


# # Standardize payment Method('Credit Card,Debit Card,'):

ecommerce['PaymentMethod']=ecommerce['PaymentMethod'].astype(str)
ecommerce['PaymentMethod']=ecommerce['PaymentMethod'].str.title()
print(ecommerce['PaymentMethod'].unique())


# online or Cash change:
ecommerce['PaymentMethod']=ecommerce['PaymentMethod'].replace({

'Credit Card':'Online',
'Debit Card':'Online',
'Net Banking':'Online',
'Upi':'Online',
'Paypal':'Online',
'Cash':'Cash'
})
print(ecommerce['PaymentMethod'].unique())
# print(ecommerce.to_string())


# max and min value of payment method:

print('Max:',ecommerce['PaymentMethod'].max())
print('Min:',ecommerce['PaymentMethod'].min())

# order by payment Method:

Order_by_PaymentMethod=ecommerce.groupby(['OrderID'])['PaymentMethod'].count().sort_values(ascending=False)
print(Order_by_PaymentMethod)

# # Amount Calculation:Total Amount:Quantity* Price:

ecommerce['Total_amount']=ecommerce['Quantity']*ecommerce['Price']
print(ecommerce[['Quantity','Price','Total_amount']])

# Dsicount Price:Total amount*DiscountPerrcent/100:

ecommerce['Discount_amount']=ecommerce['Total_amount']*(ecommerce['DiscountPercent']/100)
print(ecommerce[['Price','DiscountPercent','Discount_amount']])

# Net Amount: Total amount-Discount Amount:
ecommerce['Net_amount']=ecommerce['Total_amount']-ecommerce['Discount_amount'].astype(int)
print(ecommerce[['Total_amount','Discount_amount','Net_amount']])

# Net Amount Highest Value:
print('Max:',ecommerce['Net_amount'].max())
print('Min:',ecommerce['Net_amount'].min())
print('Mean:',ecommerce['Net_amount'].mean())
print('Median:',ecommerce['Net_amount'].median())
print('Sum:',ecommerce['Net_amount'].sum())
print('Count:',ecommerce['Net_amount'].count())
print('Mode:',ecommerce['Net_amount'].mode())
print(ecommerce[['Net_amount']])
# print(ecommerce.to_string())


# Order Value Category:
def ordervalue_category(net_amount):
    if net_amount>=1199363.5:
        return('High')
    elif net_amount>=649681.75:
        return('Medium')
    else:
        return('Low')

ecommerce['Ordervaluecategory']=ecommerce['Net_amount'].apply(ordervalue_category)
print(ecommerce[['Net_amount','Ordervaluecategory']])

# Rating Category:
def rating_category(rating):
    if rating >=4:
        return('High')
    elif rating >=3:
        return('Medium')
    else:
        return('Low')

ecommerce['Rating_category']=ecommerce['Rating'].apply(rating_category)
print(ecommerce[['Rating_category','Rating']])
# print(ecommerce.to_string())

# Revenue amount:
total_revenue = (ecommerce['Price'] * ecommerce['Quantity']).sum()
print("Total Revenue =", total_revenue)
 
# # #  Average Order Value:

total_revenue = (ecommerce['Price'] * ecommerce['Quantity']).sum()
print("Total Revenue =", total_revenue)
 
# # TOTAL ORDERS
total_orders=(ecommerce['OrderID']).count()
total_orders = ecommerce['OrderID'].nunique()
 
# # AVERAGE  ORDER VALUE
 
av = total_revenue / total_orders
 
print("Total Revenue :", total_revenue)
print("Total Orders :", total_orders)
print("Average Order Value :",(av))


# top 10 selling product: 
top10_products=ecommerce.groupby(['ProductID'])['Quantity'].sum().sort_values(ascending=False).head(10)

print(top10_products)

# top 10 highest revenue product:ques:7
top10_revenueProduct = (
    (ecommerce['Price'] * ecommerce['Quantity']).groupby(ecommerce['ProductName']).sum().sort_values(ascending=False) .head(10)).astype(int)

print(top10_revenueProduct)

# Product with the lowest rating:ques:8
Product_lowestrate=ecommerce.groupby(['ProductName'])['Rating'].min().sort_values(ascending=True).tail().astype(int)
print(Product_lowestrate)


# category_wise_revenue:ques:9
category_wise_revenue=(ecommerce['Price'] * ecommerce['Quantity']).groupby(ecommerce['Category']).sum().sort_values(ascending=False).astype(int)

print(category_wise_revenue)

# Average category wise rating:ques:10
category_wise_rating=(ecommerce.groupby(['Category'])['Rating']).count().astype(int)

# print(category_wise_rating)


# Top customers by spending:Ques:11
top_customer_spending=(ecommerce['Price'] * ecommerce['Quantity']).groupby(ecommerce['CustomerID']).max().sort_values(ascending=False)

print(top_customer_spending)


# Top Customer by order count:ques:12
category_wise_rating=(ecommerce.groupby(['CustomerID'])['OrderID']).count().astype(int)

print(category_wise_rating)

# Average order value per customer:Ques:13
category_wise_rating=(ecommerce.groupby(['CustomerID'])['OrderID']).value_counts().astype(int)

print(category_wise_rating)

# 14. Most used payment method
Most_Used_PaymentMethod=ecommerce['PaymentMethod'].max()
print('Most Used PaymentMethod:',Most_Used_PaymentMethod)

# revenue by Paymentmethod:ques:15
Revenue_by_paymentMethod=(ecommerce['Price']*ecommerce['Quantity']).groupby(ecommerce['PaymentMethod']).mean().astype(int)
print(Revenue_by_paymentMethod)


# 16. Revenue by month. 
Revenue_by_month=(ecommerce['Price']*ecommerce['Quantity']).groupby(ecommerce['OrderMonth']).sum().astype(int)
print(Revenue_by_month)

# 17. Orders by month. 
order_by_month=(ecommerce['Price']*ecommerce['Quantity']).groupby(ecommerce['OrderMonth']).count().astype(int)
print(order_by_month)



# 18. Highest sales month.
Highest_Sales_month=(ecommerce['Price']*ecommerce['Quantity']).groupby(ecommerce['OrderMonth']).max().sort_values(ascending=False).astype(int)
print(Highest_Sales_month)


                                                                # Matplot
# ==============================
# TOP 10 PRODUCTS BY REVENUE
# ==============================
 
# import matplotlib.pyplot as plt
# from matplotlib.patches import Patch
 
# top10_revenueProduct = (
#     ecommerce.groupby('ProductName')['Net_amount']
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )
 
# colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1',
#     '#76B7B2',
#     '#EDC948',
#     '#9C755F',
#     '#FF9DA7',
#     '#BAB0AC'
# ]
 
# plt.figure(figsize=(13,6))
 
# bars = plt.bar(
#     top10_revenueProduct.index,
#     top10_revenueProduct.values,
#     color=colors,
#     edgecolor='black',
#     linewidth=1
# )
 
# plt.title("Top 10 Products by Revenue",fontsize=16,fontweight='bold')
# plt.xlabel("ProductName",fontsize=12,fontweight='bold')
# plt.ylabel("Revenue",fontsize=12,fontweight='bold')
 
# plt.xticks(rotation=45,ha='right')
 
# plt.grid(axis='y',linestyle='--',alpha=0.4)
 
# # Value Labels
# for bar in bars:
#     plt.text(
#         bar.get_x()+bar.get_width()/2,
#         bar.get_height(),
#         f'{int(bar.get_height()):,}',
#         ha='center',
#         va='bottom',
#         fontsize=9,
#         fontweight='bold'
#     )
 
# # ===========================
# # Legend (Product + Revenue)
# # ===========================
 
# legend_elements = [
#     Patch(
#         facecolor=colors[i],
#         edgecolor='black',
#         label=f"{top10_revenueProduct.index[i]}   ₹{top10_revenueProduct.values[i]:,.0f}"
#     )
#     for i in range(len(top10_revenueProduct))
# ]
 
# # ==========================================
# # TABLE (Product Name + Revenue)
# # ==========================================
 
# table_data = []
 
# for i in range(len(top10_revenueProduct)):
#     table_data.append([
#         "■",
#         top10_revenueProduct.index[i],
#         f"₹{top10_revenueProduct.values[i]:,.0f}"
#     ])
 
# table = plt.table(
#     cellText=table_data,
#     colLabels=["", "Product", "Revenue"],
#     cellLoc='left',
#     colLoc='center',
#     bbox=[1.03, 0.05, 0.45, 0.90]
# )
 
# table.auto_set_font_size(False)
# table.set_fontsize(9)
# table.scale(1.1, 1.4)
 
# # Header Style
# for j in range(3):
#     table[(0, j)].set_facecolor('#2C3E50')
#     table[(0, j)].set_text_props(color='white', weight='bold')
 
# # Row Colors (Match Bar Colors)
# for i, color in enumerate(colors):
#     table[(i+1, 0)].get_text().set_color(color)
#     table[(i+1, 0)].set_text_props(fontsize=16, weight='bold')
 
#     table[(i+1, 1)].set_facecolor('#F8F9F9')
#     table[(i+1, 2)].set_facecolor('#F8F9F9')
 
# plt.tight_layout()
 
# plt.show()
 

#  -----------------------------------

 
# ==========================================
#2. REVENUE BY CATEGORY
# ==========================================
 
# import matplotlib.pyplot as plt
 
# category_revenue = (
#     ecommerce.groupby('Category')['Net_amount']
#     .sum()
#     .sort_values(ascending=False)
# )
 
# colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1',
#     '#76B7B2',
#     '#EDC948',
#     '#9C755F',
#     '#FF9DA7',
#     '#BAB0AC'
# ]
 
# plt.figure(figsize=(13,6))
 
# bars = plt.bar(
#     category_revenue.index,
#     category_revenue.values,
#     color=colors[:len(category_revenue)],
#     edgecolor='black',
#     linewidth=1.2
# )
 
# plt.title(
#     'Revenue by Category',
#     fontsize=16,
#     fontweight='bold'
# )
 
# plt.xlabel(
#     'Category',
#     fontsize=12,
#     fontweight='bold'
# )
 
# plt.ylabel(
#     'Revenue',
#     fontsize=12,
#     fontweight='bold'
# )
 
# plt.xticks(rotation=30, ha='right')
 
# plt.grid(axis='y', linestyle='--', alpha=0.4)
 
# # Revenue Labels
# for bar in bars:
#     plt.text(
#         bar.get_x()+bar.get_width()/2,
#         bar.get_height(),
#         f'₹{int(bar.get_height()):,}',
#         ha='center',
#         va='bottom',
#         fontsize=9,
#         fontweight='bold'
#     )
 
# # ==========================================
# # TABLE (Category + Revenue)
# # ==========================================
 
# table_data = []
 
# for i in range(len(category_revenue)):
#     table_data.append([
#         "■",
#         category_revenue.index[i],
#         f"₹{category_revenue.values[i]:,.0f}"
#     ])
 
# table = plt.table(
#     cellText=table_data,
#     colLabels=["", "Category", "Revenue"],
#     cellLoc='left',
#     colLoc='center',
#     bbox=[1.03, 0.05, 0.45, 0.90]
# )
 
# table.auto_set_font_size(False)
# table.set_fontsize(9)
# table.scale(1.1, 1.4)
 
# # Header Style
# for j in range(3):
#     table[(0, j)].set_facecolor('#2C3E50')
#     table[(0, j)].set_text_props(color='white', weight='bold')
 
# # Match Table Color with Bars
# for i, color in enumerate(colors[:len(category_revenue)]):
#     table[(i+1, 0)].get_text().set_color(color)
#     table[(i+1, 0)].set_text_props(fontsize=16, weight='bold')
 
#     table[(i+1, 1)].set_facecolor('#F8F9F9')
#     table[(i+1, 2)].set_facecolor('#F8F9F9')
 
# plt.tight_layout()
 
# plt.show()


# ----------------------------------

 
 
 
# ==========================================
#3. ORDERS BY PAYMENT METHOD
# ==========================================
 
# import matplotlib.pyplot as plt
 
# payment_orders = (
#     ecommerce.groupby('PaymentMethod')['OrderID']
#     .count()
#     .sort_values(ascending=False)
# )
 
# colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1',
#     '#76B7B2',
#     '#EDC948',
#     '#9C755F'
# ]
 
# plt.figure(figsize=(13,6))
 
# bars = plt.bar(
#     payment_orders.index,
#     payment_orders.values,
#     color=colors[:len(payment_orders)],
#     edgecolor='black',
#     linewidth=1.2
# )
 
# plt.title(
#     'Orders by Payment Method',
#     fontsize=16,
#     fontweight='bold'
# )
 
# plt.xlabel(
#     'Payment Method',
#     fontsize=12,
#     fontweight='bold'
# )
 
# plt.ylabel(
#     'Number of Orders',
#     fontsize=12,
#     fontweight='bold'
# )
 
# plt.xticks(rotation=20)
 
# plt.grid(axis='y', linestyle='--', alpha=0.4)
 
# # Order Count Labels
# for bar in bars:
#     plt.text(
#         bar.get_x() + bar.get_width()/2,
#         bar.get_height(),
#         f'{int(bar.get_height())}',
#         ha='center',
#         va='bottom',
#         fontsize=10,
#         fontweight='bold'
#     )
 
# # ==========================================
# # TABLE (Payment Method + Orders)
# # ==========================================
 
# table_data = []
 
# for i in range(len(payment_orders)):
#     table_data.append([
#         "■",
#         payment_orders.index[i],
#         int(payment_orders.values[i])
#     ])
 
# table = plt.table(
#     cellText=table_data,
#     colLabels=["", "PaymentMethod", "Orders"],
#     cellLoc='left',
#     colLoc='center',
#     bbox=[1.03, 0.03, 0.45, 0.65]
# )
 
# table.auto_set_font_size(False)
# table.set_fontsize(9)
# table.scale(1,1)
 
# # Header Style
# for j in range(3):
#     table[(0, j)].set_facecolor('#2C3E50')
#     table[(0, j)].set_text_props(color='white', weight='bold')
 
# # Match Table Color with Bar Color
# for i, color in enumerate(colors[:len(payment_orders)]):
#     table[(i+1, 0)].get_text().set_color(color)
#     table[(i+1, 0)].set_text_props(fontsize=16, weight='bold')
 
#     table[(i+1, 1)].set_facecolor('#F8F9F9')
#     table[(i+1, 2)].set_facecolor('#F8F9F9')
 
# plt.tight_layout()
 
# plt.show()
 
 # ==========================================
# 4.CATEGORY DISTRIBUTION (DONUT CHART)
# ==========================================
 
# import matplotlib.pyplot as plt
 
# category_revenue = (
#     ecommerce.groupby('Category')['Net_amount']
#     .sum()
#     .sort_values(ascending=False)
# )
 
# colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1',
#     '#76B7B2',
#     '#EDC948',
#     '#9C755F',
#     '#FF9DA7',
#     '#BAB0AC'
# ]
 
# fig, ax = plt.subplots(figsize=(13,7))
 
# # Donut Chart
# wedges, texts, autotexts = ax.pie(
#     category_revenue.values,
#     labels=category_revenue.index,
#     colors=colors[:len(category_revenue)],
#     autopct='%1.1f%%',
#     startangle=90,
#     pctdistance=0.80,
#     wedgeprops=dict(
#         width=0.45,
#         edgecolor='white'
#     )
# )
 
# # Center KPI
# total_revenue = category_revenue.sum()
 
# ax.text(
#     0,
#     0,
#     f'Total Revenue\n₹{total_revenue:,.0f}',
#     ha='center',
#     va='center',
#     fontsize=12,
#     fontweight='bold'
# )
 
# plt.title(
#     'Category Distribution by Revenue',
#     fontsize=16,
#     fontweight='bold'
# )
 
# # ==========================================
# # TABLE (Category + Revenue)
# # ==========================================
 
# table_data = []
 
# for i in range(len(category_revenue)):
#     table_data.append([
#         "■",
#         category_revenue.index[i],
#         f"₹{category_revenue.values[i]:,.0f}"
#     ])
 
# table = plt.table(
#     cellText=table_data,
#     colLabels=["", "Category", "Revenue"],
#     cellLoc='left',
#     colLoc='center',
#     bbox=[1.15, 0.05, 0.50, 0.90]
# )
 
# table.auto_set_font_size(False)
# table.set_fontsize(9)
# table.scale(1.1, 1.4)
 
# # Header Style
# for j in range(3):
#     table[(0, j)].set_facecolor('#2C3E50')
#     table[(0, j)].set_text_props(
#         color='white',
#         weight='bold'
#     )
 
# # Match Color with Donut
# for i, color in enumerate(colors[:len(category_revenue)]):
 
#     table[(i+1, 0)].get_text().set_color(color)
#     table[(i+1, 0)].set_text_props(
#         fontsize=16,
#         weight='bold'
#     )
 
#     table[(i+1, 1)].set_facecolor('#F8F9F9')
#     table[(i+1, 2)].set_facecolor('#F8F9F9')
 
# plt.tight_layout()
 
# plt.show()
 

#  --------------------------------------


# ==========================================
# 5.PAYMENT METHOD DISTRIBUTION (DONUT CHART)
# ==========================================
 
# import matplotlib.pyplot as plt
 
# payment_orders = (
#     ecommerce.groupby('PaymentMethod')['OrderID']
#     .count()
#     .sort_values(ascending=False)
# )
 
# colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1',
#     '#76B7B2',
#     '#EDC948',
#     '#9C755F'
# ]
 
# fig, ax = plt.subplots(figsize=(13,7))
 
# # Donut Chart
# wedges, texts, autotexts = ax.pie(
#     payment_orders.values,
#     labels=payment_orders.index,
#     colors=colors[:len(payment_orders)],
#     autopct='%1.1f%%',
#     startangle=90,
#     pctdistance=0.80,
#     wedgeprops=dict(
#         width=0.45,
#         edgecolor='white',
#         linewidth=2
#     )
# )
 
# # Improve Text Style
# for text in texts:
#     text.set_fontsize(10)
#     text.set_fontweight('bold')
 
# for autotext in autotexts:
#     autotext.set_fontsize(10)
#     autotext.set_fontweight('bold')
#     autotext.set_color('white')
 
# # ==========================================
# # CENTER KPI
# # ==========================================
 
# total_orders = payment_orders.sum()
# top_method = payment_orders.idxmax()
# top_orders = payment_orders.max()
 
# ax.text(
#     0,
#     0,
#     f"Total Orders\n{total_orders:,}",
#     ha='center',
#     va='center',
#     fontsize=14,
#     fontweight='bold'
# )
 
# plt.title(
#     "Payment Method Distribution",
#     fontsize=16,
#     fontweight='bold'
# )
 
# # ==========================================
# # KPI BOX
# # ==========================================
 
# kpi_text = (
#     f"Total Orders : {total_orders:,}\n\n"
#     f"Top Method : {top_method}\n\n"
#     f"Top Orders : {top_orders:,}"
# )
 
# plt.text(
#     1.22,
#     0.92,
#     kpi_text,
#     transform=ax.transAxes,
#     fontsize=10,
#     fontweight='bold',
#     color='white',
#     bbox=dict(
#         facecolor='#2C3E50',
#         edgecolor='black',
#         boxstyle='round,pad=0.6'
#     )
# )
 
# # ==========================================
# # TABLE
# # ==========================================
 
# table_data = []
 
# for i in range(len(payment_orders)):
#     table_data.append([
#         "■",
#         payment_orders.index[i],
#         f"{payment_orders.values[i]:,}"
#     ])
 
# table = plt.table(
#     cellText=table_data,
#     colLabels=["", "PaymentMethod", "Orders"],
#     cellLoc='left',
#     colLoc='center',
#     bbox=[1.18, 0.05, 0.55, 0.72]
# )
 
# table.auto_set_font_size(False)
# table.set_fontsize(9)
# table.scale(1.15, 1.5)
 
# # Header
# for j in range(3):
#     table[(0, j)].set_facecolor('#2C3E50')
#     table[(0, j)].set_text_props(
#         color='white',
#         weight='bold'
#     )
 
# # Match Table Colors
# for i, color in enumerate(colors[:len(payment_orders)]):
 
#     table[(i+1,0)].get_text().set_color(color)
#     table[(i+1,0)].set_text_props(
#         fontsize=16,
#         weight='bold'
#     )
 
#     table[(i+1,1)].set_facecolor('#F8F9F9')
#     table[(i+1,2)].set_facecolor('#F8F9F9')
 
# plt.tight_layout()
 
# plt.show()


# ---------------------------------------------


 
# 6: Monthly Revenue Trend ( Line Chart)
 
 
# ==========================================
#6. MONTHLY REVENUE TREND
# ==========================================
 
# import matplotlib.pyplot as plt
 
# monthly_revenue = (
#     ecommerce.groupby('OrderMonth')['Net_amount']
#     .sum()
#     .sort_index()
# )
 
# months = [
#     'Jan','Feb','Mar','Apr','May','Jun',
#     'Jul','Aug','Sep','Oct','Nov','Dec'
# ]
 
# month_labels = [months[m-1] for m in monthly_revenue.index]
 
# fig, ax = plt.subplots(figsize=(20,8))
 
# # ==========================================
# # LINE CHART
# # ==========================================
 
# ax.plot(
#     month_labels,
#     monthly_revenue.values,
#     marker='o',
#     markersize=8,
#     linewidth=1,
#     color='#4E79A7'
# )
 
# ax.fill_between(
#     month_labels,
#     monthly_revenue.values,
#     color='#4E79A7',
#     alpha=0.15
# )
 
# ax.set_title(
#     "Monthly Revenue Trend",
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.set_xlabel(
#     "Month",
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.set_ylabel(
#     "Revenue",
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.grid(
#     linestyle='--',
#     alpha=0.4
# )
 
# # ==========================================
# # VALUE LABELS
# # ==========================================
 
# for x, y in zip(month_labels, monthly_revenue.values):
#     ax.text(
#         x,
#         y,
#         f'₹{int(y):,}',
#         ha='center',
#         va='bottom',
#         fontsize=9,
#         fontweight='bold'
 
#     )
 
# # ==========================================
# # KPI BOX
# # ==========================================
 
# total_revenue = monthly_revenue.sum()
# best_month = month_labels[monthly_revenue.argmax()]
# highest_revenue = monthly_revenue.max()
 
# kpi_text = (
#     f"Total Revenue : ₹{total_revenue:,.0f}\n\n"
#     f"Best Month : {best_month}\n\n"
#     f"Highest Revenue : ₹{highest_revenue:,.0f}"
# )
 
# plt.text(
#     1.20,
#     0.92,
#     kpi_text,
#     transform=ax.transAxes,
#     fontsize=10,
#     fontweight='bold',
#     color='white',
#     bbox=dict(
#         facecolor='#4E79A7',
#         edgecolor='black',
#         boxstyle='round,pad=0.6'
#     )
# )
 
# # ==========================================
# # TABLE
# # ==========================================
 
# table_data = []
 
# for month, revenue in zip(month_labels, monthly_revenue.values):
#     table_data.append([
#         "■",
#         month,
#         f"₹{revenue:,.0f}"
#     ])
 
# table = plt.table(
#     cellText=table_data,
#     colLabels=["","Month","Revenue"],
#     cellLoc='left',
#     colLoc='center',
#     bbox=[1.18,0.05,0.52,0.72]
# )
 
# table.auto_set_font_size(False)
# table.set_fontsize(9)
# table.scale(1.15,1.5)
 
# # Header
 
# for j in range(3):
#     table[(0,j)].set_facecolor('#2C3E50')
#     table[(0,j)].set_text_props(
#         color='white',
#         weight='bold'
#     )
 
# # Row Style
 
# for i in range(len(table_data)):
#     table[(i+1,0)].get_text().set_color('#4E79A7')
#     table[(i+1,0)].set_text_props(
#         fontsize=16,
#         weight='bold'
#     )
 
#     table[(i+1,1)].set_facecolor('#F8F9F9')
#     table[(i+1,2)].set_facecolor('#F8F9F9')
 
# plt.tight_layout()
 
# plt.show()
 

#  -----------------------------------------

    # ==========================================
# 7.MONTHLY ORDER TREND
# ==========================================
 
# import matplotlib.pyplot as plt
 
# monthly_orders = (
#     ecommerce.groupby('OrderMonth')['OrderID']
#     .count()
#     .sort_index()
# )
 
# months = [
#     'Jan','Feb','Mar','Apr','May','Jun',
#     'Jul','Aug','Sep','Oct','Nov','Dec'
# ]
 
# month_labels = [months[m-1] for m in monthly_orders.index]
 
# fig, ax = plt.subplots(figsize=(17,4.8))
 
# # ==========================================
# # LINE CHART
# # ==========================================
 
# ax.plot(
#     month_labels,
#     monthly_orders.values,
#     color='#F28E2B',
#     linewidth=3,
#     marker='o',
#     markersize=8
# )
 
# ax.fill_between(
#     month_labels,
#     monthly_orders.values,
#     color='#F28E2B',
#     alpha=0.15
# )
 
# ax.set_title(
#     "Monthly Order Trend",
#     fontsize=16,
#     fontweight='bold'
# )
 
# ax.set_xlabel(
#     "Month",
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.set_ylabel(
#     "Number of Orders",
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.grid(
#     linestyle='--',
#     alpha=0.4
# )
 
# # ==========================================
# # VALUE LABELS
# # ==========================================
 
# for x, y in zip(month_labels, monthly_orders.values):
#     ax.text(
#         x,
#         y,
#         f'{int(y)}',
#         ha='center',
#         va='bottom',
#         fontsize=9,
#         fontweight='bold'
#     )
 
# # ==========================================
# # KPI BOX
# # ==========================================
 
# total_orders = monthly_orders.sum()
# best_month = month_labels[monthly_orders.argmax()]
# highest_orders = monthly_orders.max()
 
# kpi_text = (
#     f"Total Orders : {total_orders:,}\n\n"
#     f"Best Month : {best_month}\n\n"
#     f"Highest Orders : {highest_orders:,}"
# )
 
# plt.text(
#     1.20,
#     0.92,
#     kpi_text,
#     transform=ax.transAxes,
#     fontsize=10,
#     fontweight='bold',
#     color='white',
#     bbox=dict(
#         facecolor='#F28E2B',
#         edgecolor='black',
#         boxstyle='round,pad=0.6'
#     )
# )
 
# # ==========================================
# # TABLE
# # ==========================================
 
# table_data = []
 
# for month, orders in zip(month_labels, monthly_orders.values):
#     table_data.append([
#         "■",
#         month,
#         f"{orders:,}"
#     ])
 
# table = plt.table(
#     cellText=table_data,
#     colLabels=["", "Month", "Orders"],
#     cellLoc='left',
#     colLoc='center',
#     bbox=[1.18,0.05,0.52,0.72]
# )
 
# table.auto_set_font_size(False)
# table.set_fontsize(9)
# table.scale(1.15,1.5)
 
# # Header Style
# for j in range(3):
#     table[(0,j)].set_facecolor('#2C3E50')
#     table[(0,j)].set_text_props(
#         color='white',
#         weight='bold'
#     )
 
# # Match Table Color with Line Color
# for i in range(len(table_data)):
#     table[(i+1,0)].get_text().set_color('#F28E2B')
#     table[(i+1,0)].set_text_props(
#         fontsize=16,
#         weight='bold'
#     )
 
#     table[(i+1,1)].set_facecolor('#F8F9F9')
#     table[(i+1,2)].set_facecolor('#F8F9F9')
 
# plt.tight_layout()
 
# plt.show()

# ---------------------------------------
# ==========================================
# 8.PRICE DISTRIBUTION (HISTOGRAM)
# ==========================================
 
# import matplotlib.pyplot as plt
# import numpy as np
 
# fig, ax = plt.subplots(figsize=(17,4.8))
 
# # Histogram
# counts, bins, patches = ax.hist(
#     ecommerce['Price'],
#     bins=10,
#     edgecolor='black',
#     linewidth=1.2
# )
 
# # Colors for each bin
# colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1',
#     '#76B7B2',
#     '#EDC948',
#     '#9C755F',
#     '#FF9DA7',
#     '#BAB0AC'
# ]
 
# for patch, color in zip(patches, colors):
#     patch.set_facecolor(color)
 
# # Titles
# ax.set_title(
#     'Price Distribution',
#     fontsize=16,
#     fontweight='bold'
# )
 
# ax.set_xlabel(
#     'Price',
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.set_ylabel(
#     'Frequency',
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.grid(
#     linestyle='--',
#     alpha=0.4
# )
 
# # Value Labels
# for count, patch, color in zip(counts, patches, colors):
 
#     if count > 0:
 
#         ax.text(
#             patch.get_x() + patch.get_width()/2,
#             count,
#             f'{int(count)}',
#             ha='center',
#             va='bottom',
#             fontsize=9,
#             fontweight='bold',
#             color=color
#         )
 
# # ==========================================
# # KPI BOX
# # ==========================================
 
# kpi_text = (
#     f"Maximum Price : ₹{ecommerce['Price'].max():,.0f}\n\n"
#     f"Minimum Price : ₹{ecommerce['Price'].min():,.0f}\n\n"
#     f"Average Price : ₹{ecommerce['Price'].mean():,.0f}"
# )
 
# plt.text(
#     1.20,
#     0.92,
#     kpi_text,
#     transform=ax.transAxes,
#     fontsize=10,
#     fontweight='bold',
#     color='white',
#     bbox=dict(
#         facecolor='#4E79A7',
#         edgecolor='black',
#         boxstyle='round,pad=0.6'
#     )
# )
 
# # ==========================================
# # TABLE
# # ==========================================
 
# table_data = []
 
# for i in range(len(counts)):
#     table_data.append([
#         "■",
#         f"{bins[i]:,.0f} - {bins[i+1]:,.0f}",
#         int(counts[i])
#     ])
 
# table = plt.table(
#     cellText=table_data,
#     colLabels=["","Price Range","Frequency"],
#     cellLoc='left',
#     colLoc='center',
#     bbox=[1.18,0.05,0.52,0.72]
# )
 
# table.auto_set_font_size(False)
# table.set_fontsize(9)
# table.scale(1.15,1.5)
 
# # Header
# for j in range(3):
#     table[(0,j)].set_facecolor('#2C3E50')
#     table[(0,j)].set_text_props(
#         color='white',
#         weight='bold'
#     )
 
# # Table Color Match
# for i in range(len(counts)):
 
#     table[(i+1,0)].get_text().set_color(colors[i])
 
#     table[(i+1,0)].set_text_props(
#         fontsize=16,
#         weight='bold'
#     )
 
#     table[(i+1,1)].set_facecolor('#F8F9F9')
#     table[(i+1,2)].set_facecolor('#F8F9F9')
 
# plt.tight_layout()
 
# plt.show()


# ------------------------------------------------



 
# ==========================================
# 9.RATING DISTRIBUTION (HISTOGRAM)
# ==========================================
 
# import matplotlib.pyplot as plt
# import numpy as np
 
# fig, ax = plt.subplots(figsize=(17,4.8))
 
# # Histogram
# counts, bins, patches = ax.hist(
#     ecommerce['Rating'],
#     bins=5,
#     edgecolor='black',
#     linewidth=1.2
# )
 
# # Colors
# colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1'
# ]
 
# # Apply Colors
# for patch, color in zip(patches, colors):
#     patch.set_facecolor(color)
 
# # Title
# ax.set_title(
#     'Rating Distribution',
#     fontsize=16,
#     fontweight='bold'
# )
 
# ax.set_xlabel(
#     'Rating',
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.set_ylabel(
#     'Frequency',
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.grid(
#     linestyle='--',
#     alpha=0.4
# )
 
# # Value Labels
# for count, patch, color in zip(counts, patches, colors):
 
#     if count > 0:
 
#         ax.text(
#             patch.get_x()+patch.get_width()/2,
#             count,
#             f'{int(count)}',
#             ha='center',
#             va='bottom',
#             fontsize=9,
#             fontweight='bold',
#             color=color
#         )
 
# # ==========================================
# # KPI BOX
# # ==========================================
 
# kpi_text = (
#     f"Highest Rating : {ecommerce['Rating'].max():.1f}\n\n"
#     f"Lowest Rating : {ecommerce['Rating'].min():.1f}\n\n"
#     f"Average Rating : {ecommerce['Rating'].mean():.2f}"
# )
 
# plt.text(
#     1.20,
#     0.92,
#     kpi_text,
#     transform=ax.transAxes,
#     fontsize=10,
#     fontweight='bold',
#     color='white',
#     bbox=dict(
#         facecolor='#4E79A7',
#         edgecolor='black',
#         boxstyle='round,pad=0.6'
#     )
# )
 
# # ==========================================
# # TABLE
# # ==========================================
 
# table_data = []
 
# for i in range(len(counts)):
#     table_data.append([
#         "■",
#         f"{bins[i]:.1f} - {bins[i+1]:.1f}",
#         int(counts[i])
#     ])
 
# table = plt.table(
#     cellText=table_data,
#     colLabels=["", "Rating Range", "Frequency"],
#     cellLoc='left',
#     colLoc='center',
#     bbox=[1.18,0.05,0.52,0.72]
# )
 
# table.auto_set_font_size(False)
# table.set_fontsize(9)
# table.scale(1.15,1.5)
 
# # Header Style
# for j in range(3):
 
#     table[(0,j)].set_facecolor('#2C3E50')
 
#     table[(0,j)].set_text_props(
#         color='white',
#         weight='bold'
#     )
 
# # Match Table Colors
# for i in range(len(counts)):
 
#     table[(i+1,0)].get_text().set_color(colors[i])
 
#     table[(i+1,0)].set_text_props(
#         fontsize=16,
#         weight='bold'
#     )
 
#     table[(i+1,1)].set_facecolor('#F8F9F9')
#     table[(i+1,2)].set_facecolor('#F8F9F9')
 
# plt.tight_layout()
 
# plt.show()
 
#  -------------------------------------------


 
# ==========================================
# 10.PRICE DISTRIBUTION BY CATEGORY (BOX PLOT)
# ==========================================
 
# import matplotlib.pyplot as plt
 
# fig, ax = plt.subplots(figsize=(17,4.8))

# # Categories
# categories = sorted(ecommerce['Category'].unique())
 
# # Data for Box Plot
# box_data = [
#     ecommerce[ecommerce['Category'] == cat]['Price']
#     for cat in categories
# ]
 
# # Colors
# colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1',
#     '#76B7B2',
#     '#EDC948',
#     '#9C755F',
#     '#FF9DA7',
#     '#BAB0AC'
# ]
 
# # Box Plot
# box = ax.boxplot(
#     box_data,
#     patch_artist=True,
#     tick_labels=categories,
#     widths=0.5

# )
 
# # Apply Colors
# for patch, color in zip(box['boxes'], colors):
#     patch.set_facecolor(color)
#     patch.set_edgecolor('black')
#     patch.set_linewidth(1.2)
 
# for whisker in box['whiskers']:
#     whisker.set(color='black')
 
# for cap in box['caps']:
#     cap.set(color='black')
 
# for median in box['medians']:
#     median.set(color='red', linewidth=2)
 
# # Title
# ax.set_title(
#     'Price Distribution by Category',
#     fontsize=16,
#     fontweight='bold'
# )
 
# ax.set_xlabel(
#     'Category',
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.set_ylabel(
#     'Price',
#     fontsize=12,
#     fontweight='bold'
# )
 
# plt.xticks(rotation=20)
 
# ax.grid(
#     linestyle='--',
#     alpha=0.4
# )
 
# # ==========================================
# # KPI BOX
# # ==========================================
 
# kpi_text = (
#     f"Highest Price : ₹{ecommerce['Price'].max():,.0f}\n\n"
#     f"Lowest Price : ₹{ecommerce['Price'].min():,.0f}\n\n"
#     f"Median Price : ₹{ecommerce['Price'].median():,.0f}"
# )
 
# plt.text(
#     1.20,
#     0.92,
#     kpi_text,
#     transform=ax.transAxes,
#     fontsize=10,
#     fontweight='bold',
#     color='white',
#     bbox=dict(
#         facecolor='#4E79A7',
#         edgecolor='black',
#         boxstyle='round,pad=0.6'
#     )
# )
 
# # ==========================================
# # TABLE
# # ==========================================
 
# table_data = []
 
# for cat in categories:
 
#     median_price = ecommerce.loc[
#         ecommerce['Category'] == cat,
#         'Price'
#     ].median()
 
#     table_data.append([
#         "■",
#         cat,
#         f"₹{median_price:,.0f}"
#     ])
 
# table = plt.table(
#     cellText=table_data,
#     colLabels=["", "Category", "Median Price"],
#     cellLoc='left',
#     colLoc='center',
#     bbox=[1.18,0.05,0.52,0.72]
# )
 
# table.auto_set_font_size(False)
# table.set_fontsize(9)
# table.scale(1.15,1.5)
 
# # Header
# for j in range(3):
 
#     table[(0,j)].set_facecolor('#2C3E50')
 
#     table[(0,j)].set_text_props(
#         color='white',
#         weight='bold'
#     )
 
# # Match Table Colors
# for i in range(len(categories)):
 
#     table[(i+1,0)].get_text().set_color(colors[i])
 
#     table[(i+1,0)].set_text_props(
#         fontsize=16,
#         weight='bold'
#     )
 
#     table[(i+1,1)].set_facecolor('#F8F9F9')
#     table[(i+1,2)].set_facecolor('#F8F9F9')
 
# plt.tight_layout()
 
# plt.show()
 

#  --------------------------------------------
 
# # ==========================================
# # 11.RATING VS REVENUE (SCATTER PLOT)
# # ==========================================
 
# import matplotlib.pyplot as plt
 
# fig, ax = plt.subplots(figsize=(17,4.8))
 
# colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1',
#     '#76B7B2',
#     '#EDC948',
#     '#9C755F',
#     '#FF9DA7',
#     '#BAB0AC'
# ]
 
# # Scatter Plot
# for i in range(len(ecommerce)):
#     ax.scatter(
#         ecommerce['Rating'].iloc[i],
#         ecommerce['Net_amount'].iloc[i],
#         color=colors[i % len(colors)],
#         edgecolors='black',
#         s=70,
#         alpha=0.8
#     )
 
# ax.set_title(
#     'Rating vs Revenue',
#     fontsize=16,
#     fontweight='bold'
# )
 
# ax.set_xlabel(
#     'Rating',
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.set_ylabel(
#     'Revenue',
#     fontsize=12,
#     fontweight='bold'
# )
 
# ax.grid(
#     linestyle='--',
#     alpha=0.4
# )
 
# # ==========================================
# # KPI BOX
# # ==========================================
 
# kpi_text = (
#     f"Highest Rating : {ecommerce['Rating'].max():.1f}\n\n"
#     f"Highest Revenue : ₹{ecommerce['Net_amount'].max():,.0f}\n\n"
#     f"Average Revenue : ₹{ecommerce['Net_amount'].mean():,.0f}"
# )
 
# plt.text(
#     1.20,
#     0.92,
#     kpi_text,
#     transform=ax.transAxes,
#     fontsize=10,
#     fontweight='bold',
#     color='white',
#     bbox=dict(
#         facecolor='#4E79A7',
#         edgecolor='black',
#         boxstyle='round,pad=0.6'
#     )
# )
 
# plt.tight_layout()
 
# plt.show()
 
#  --------------------------------------------

# 
 
# # ==========================================
# #12. DISCOUNT VS REVENUE (SCATTER PLOT)
# # ==========================================
 
 
# import matplotlib.pyplot as plt
# import numpy as np
 
# # ==========================================
# # FIGURE
# # ==========================================
 
# fig, ax = plt.subplots(figsize=(17,4.8))
 
# # ==========================================
# # COLOR PALETTE
# # ==========================================
 
# colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1',
#     '#76B7B2',
#     '#EDC948',
#     '#9C755F',
#     '#FF9DA7',
#     '#BAB0AC'
# ]
 
# # ==========================================
# # SCATTER PLOT
# # ==========================================
 
# scatter = ax.scatter(
#     ecommerce['DiscountPercent'],
#     ecommerce['Net_amount'],
#     c=ecommerce['DiscountPercent'],
#     cmap='plasma',
#     s=75,
#     edgecolors='black',
#     linewidth=0.8,
#     alpha=0.85
# )
 
# # ==========================================
# # TREND LINE
# # ==========================================
 
# x = ecommerce['DiscountPercent']
# y = ecommerce['Net_amount']
 
# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)
 
# ax.plot(
#     x,
#     p(x),
#     color='#2C3E50',
#     linewidth=2.8,
#     linestyle='--',
#     label='Trend Line'
# )
 
# # ==========================================
# # TITLE
# # ==========================================
 
# ax.set_title(
#     'Discount vs Revenue',
#     fontsize=16,
#     fontweight='bold'
# )
 
# # ==========================================
# # X LABEL
# # ==========================================
 
# ax.set_xlabel(
#     'Discount Percentage (%)',
#     fontsize=12,
#     fontweight='bold'
# )
 
# # ==========================================
# # Y LABEL
# # ==========================================
 
# ax.set_ylabel(
#     'Revenue',
#     fontsize=12,
#     fontweight='bold'
# )
 
# # ==========================================
# # GRID
# # ==========================================
 
# ax.grid(
#     linestyle='--',
#     linewidth=0.6,
#     alpha=0.4
# )
 
# # ==========================================
# # KPI VALUES
# # ==========================================
 
# highest_discount = ecommerce['DiscountPercent'].max()
# average_discount = ecommerce['DiscountPercent'].mean()
# highest_revenue = ecommerce['Net_amount'].max()
 
# correlation = ecommerce['DiscountPercent'].corr(
#     ecommerce['Net_amount']
# )
 
# # ==========================================
# # KPI BOX
# # ==========================================
 
# kpi_text = (
#     f"Highest Discount : {highest_discount:.0f}%\n\n"
#     f"Average Discount : {average_discount:.2f}%\n\n"
#     f"Highest Revenue : ₹{highest_revenue:,.0f}\n\n"
#     f"Correlation : {correlation:.2f}"
# )
 
# plt.text(
#     1.20,
#     0.92,
#     kpi_text,
#     transform=ax.transAxes,
#     fontsize=10,
#     fontweight='bold',
#     color='white',
#     bbox=dict(
#         facecolor='#4E79A7',
#         edgecolor='black',
#         boxstyle='round,pad=0.6'
#     )
# )
# # ==========================================
# # TABLE
# # ==========================================
 
# discount_summary = (
#     ecommerce.groupby('DiscountPercent')['Net_amount']
#     .mean()
#     .reset_index()
#     .sort_values(by='DiscountPercent')
# )
 
# table_data = []
 
# for i in range(len(discount_summary)):
 
#     table_data.append([
#         "■",
#         f"{discount_summary.iloc[i]['DiscountPercent']:.0f}%",
#         f"₹{discount_summary.iloc[i]['Net_amount']:,.0f}"
#     ])
 
# table = plt.table(
#     cellText=table_data,
#     colLabels=["","Discount","Average Revenue"],
#     cellLoc='left',
#     colLoc='center',
#     bbox=[1.18,0.05,0.55,0.72]
# )
 
# table.auto_set_font_size(False)
# table.set_fontsize(9)
# table.scale(1.15,1.50)
 
# # ==========================================
# # HEADER STYLE
# # ==========================================
 
# for j in range(3):
 
#     table[(0,j)].set_facecolor('#2C3E50')
 
#     table[(0,j)].set_text_props(
#         color='white',
#         weight='bold'
#     )
 
# # ==========================================
# # ROW COLORS
# # ==========================================
 
# row_colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1',
#     '#76B7B2',
#     '#EDC948',
#     '#9C755F',
#     '#FF9DA7',
#     '#BAB0AC'
# ]
 
# for i in range(len(table_data)):
 
#     table[(i+1,0)].get_text().set_color(
#         row_colors[i % len(row_colors)]
#     )
 
#     table[(i+1,0)].set_text_props(
#         fontsize=16,
#         weight='bold'
#     )
 
#     table[(i+1,1)].set_facecolor('#F8F9F9')
#     table[(i+1,2)].set_facecolor('#F8F9F9')
 
# # ==========================================
# # COLOR BAR
# # ==========================================
 
# cbar = plt.colorbar(
#     scatter,
#     ax=ax,
#     pad=0.02
# )
 
# cbar.set_label(
#     'Discount %',
#     fontsize=10,
#     fontweight='bold'
# )
 
# # ==========================================
# # LEGEND
# # ==========================================
 
# ax.legend(
#     loc='upper left',
#     frameon=True
# )
 
# # ==========================================
# # REMOVE TOP & RIGHT BORDER
# # ==========================================
 
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
 
# # ==========================================
# # LAYOUT
# # ==========================================
 
# plt.tight_layout()
 
# plt.show()



# ------------------------------------

 
# ==========================================
# CORRELATION MATRIX (HEATMAP)
# ==========================================
 
import matplotlib.pyplot as plt
import numpy as np
 
# ==========================================
# NUMERICAL COLUMNS
# ==========================================
 
corr_columns = [
    'Price',
    'Rating',
    'Quantity',
    'DiscountPercent',
    'ShippingCost',
    'Total_amount',
    'Discount_amount',
    'Net_amount'
]
 
corr_matrix = ecommerce[corr_columns].corr()
 
# ==========================================
# FIGURE
# ==========================================
 
fig, ax = plt.subplots(figsize=(12,8))
 
# ==========================================
# HEATMAP
# ==========================================
 
heatmap = ax.imshow(
    corr_matrix,
    cmap='RdYlBu_r',
    vmin=-1,
    vmax=1,
    aspect='auto'
)
 
# ==========================================
# AXIS LABELS
# ==========================================
 
ax.set_xticks(np.arange(len(corr_columns)))
ax.set_yticks(np.arange(len(corr_columns)))
 
ax.set_xticklabels(
    corr_columns,
    rotation=45,
    ha='right',
    fontsize=10,
    fontweight='bold'
)
 
ax.set_yticklabels(
    corr_columns,
    fontsize=10,
    fontweight='bold'
)
 
# ==========================================
# CORRELATION VALUES
# ==========================================
 
for i in range(len(corr_columns)):
    for j in range(len(corr_columns)):
 
        value = corr_matrix.iloc[i, j]
 
        text_color = 'white' if abs(value) > 0.55 else 'black'
 
        ax.text(
            j,
            i,
            f'{value:.2f}',
            ha='center',
            va='center',
            fontsize=9,
            fontweight='bold',
            color=text_color
        )
 
# ==========================================
# TITLE
# ==========================================
 
ax.set_title(
    'Correlation Matrix',
    fontsize=18,
    fontweight='bold',
    pad=20
)
 
# ==========================================
# COLOR BAR
# ==========================================
 
cbar = plt.colorbar(
    heatmap,
    ax=ax,
    shrink=0.9
)
 
cbar.set_label(
    'Correlation Coefficient',
    fontsize=11,
    fontweight='bold'
)
 
# ==========================================
# REMOVE BORDER
# ==========================================
 
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
 
plt.tight_layout()
 
plt.show()
  
 
 
 
 
 
 
 
 
 