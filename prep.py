import pandas as pd
import plotly.graph_objects as go

def prepare_sahkey_data(data):
    df = pd.read_csv(data)

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
    list_= [first_month,second_month,third_month,fourth_month,fifth_month]

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

    return all_numerics, names, count_dict, source_list, target_list
