import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv('data/Simulated_Customer_Data_Sankey.csv')

#groups has all the combinations of 6 months
groups = df.groupby(['First Month','Second Month','Third Month','Fourth Month','Fifth Month','Sixth Month']).agg({'Customer_id':'count'}).reset_index()
#first_month has all the combinations of 1st Month with 2nd Month
first_month = groups.groupby(['First Month','Second Month']).agg({'Customer_id':'sum'}).rename({'Customer_id':'counts'}).reset_index()
#second_month has all the combinations of 2nd Month with 3rd Month
second_month = groups.groupby(['Second Month','Third Month']).agg({'Customer_id':'sum'}).rename({'Customer_id':'counts'}).reset_index()
#third_month has all the combinations of 3rd Month with 4th Month
third_month = groups.groupby(['Third Month','Fourth Month']).agg({'Customer_id':'sum'}).rename({'Customer_id':'counts'}).reset_index()
#fourth_month has all the combinations of 4th Month with 5th Month
fourth_month = groups.groupby(['Fourth Month','Fifth Month']).agg({'Customer_id':'sum'}).rename({'Customer_id':'counts'}).reset_index()
#fifth_month has all the combinations of 5th Month with 6th Month
fifth_month = groups.groupby(['Fifth Month','Sixth Month']).agg({'Customer_id':'sum'}).rename({'Customer_id':'counts'}).reset_index()
#list_ contains all these dataframes
list_=[first_month,second_month,third_month,fourth_month,fifth_month]
print(list)
# names contains all the labels of our nodes. We will add suffix #'_M1,_M2,_M3....' to our segmentation to differntiate one months #segement with other months,i.e LOW VALUE CUSTOMER_M3 tells Low #value customer in 3rd month.
names = []
count_dict = {}  # will contain all info of value list
source_list = []  # will contain all info of source
target_list = []  # will contain all info of target
for i in range(0, len(list_)):
    cols = list_[i].columns  # contains columns for our dataframe
    # (list_[i])
    # This for loop is inside the outer loop
for x, y, z in zip(list_[i][cols[0]], list_[i][cols[1]],
                   list_[i][cols[2]]):  # Iterates over x(source),y(target),z(counts)

    if (x + '_M' + str(i + 1) not in names):
        names.append(x + '_M' + str(i + 1))  # appends in names
    # the next line is outside the if but inside the second loop
    count_dict[x + '_M' + str(i + 1), y + '_M' + str(i + 2)] = z
    source_list.append(x + '_M' + str(i + 1))
    target_list.append(y + '_M' + str(i + 2))
# Now we add labels into name for the last month targets
for v in target_list:
    if v not in names:
        names.append(v)

# all_numerics contains the index for every label
all_numerics = {}
for i in range(0, len(names)):
    all_numerics[names[i]] = i

#define two sets of color dictionaries one for the nodes and the #other for the links
#Node color dict, RGBA means red,green,blue,alpha. Alpha sets the #opacity/transperancy
color_dict = {'LOW VALUE CUSTOMER':' rgba(252,65,94,0.7)','MEDIUM VALUE CUSTOMER':'rgba(255,162,0,0.7)','HIGH VALUE CUSTOMER':'rgba(55,178,255,0.7)'}
#link color dict.The colors are the same but lower a value, lower #opacity. Gives a nice effect.
color_dict_link = {'LOW VALUE CUSTOMER':' rgba(252,65,94,0.4)','MEDIUM VALUE CUSTOMER':'rgba(255,162,0,0.4)','HIGH VALUE CUSTOMER':'rgba(55,178,255,0.4)'}
#Plotting, everything is the same as last with added colors
fig = go.Figure(data=[go.Sankey(
    node = dict(
      thickness = 5,
      line = dict(color = None, width = 0.01),
     #Adding node colors,have to split to remove the added suffix
      color = [color_dict[x.split('_')[0]] for x in names],),
    link = dict(
      source = [all_numerics[x] for x in source_list],
      target = [all_numerics[x] for x in target_list],
      value = [count_dict[x,y] for x,y in      zip(source_list,target_list)],
      #Adding link colors,have to split to remove the added suffix
      color = [color_dict_link[x.split('_')[0]] for x in target_list]
  ),)])

# Adds 1st,2nd month on top,x_coordinate is 0 - 5 integers,column #name is specified by the list we passed
for x_coordinate, column_name in enumerate(
        ["1st<br>Month", "2nd<br>Month", "3rd<br>Month", "4th<br>Month", '5th<br>Month', '6th<br>Month']):
    fig.add_annotation(
        x=x_coordinate,  # Plotly recognizes 0-5 to be the x range.

        y=1.075,  # y value above 1 means above all nodes
        xref="x",
        yref="paper",
        text=column_name,  # Text
        showarrow=False,
        font=dict(
            family="Tahoma",
            size=16,
            color="black"
        ),
        align="left",
    )
# Adding y labels is harder because you don't precisely know the #location of every node.
# You could however add annotations using the labels option while defining the figure but you cannot change the color for each #annotation individually

fig.show()