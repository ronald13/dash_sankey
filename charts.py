import plotly.graph_objects as go

def create_sankey(all_numerics, names, count_dict, source_list, target_list ):
    color_dict = {'LOW VALUE CUSTOMER':' rgba(252,65,94,0.7)','MEDIUM VALUE CUSTOMER':'rgba(255,162,0,0.7)','HIGH VALUE CUSTOMER':'rgba(55,178,255,0.7)'}
    color_dict_link = {'LOW VALUE CUSTOMER':' rgba(252,65,94,0.4)','MEDIUM VALUE CUSTOMER':'rgba(255,162,0,0.4)','HIGH VALUE CUSTOMER':'rgba(55,178,255,0.4)'}

    fig = go.Figure(data=[go.Sankey(
        node = dict(
            thickness = 5,
            line = dict(color = None, width = 0.05),
            #Adding node colors,have to split to remove the added suffix
            color = [color_dict[x.split('_')[0]] for x in names],),
        link = dict(
            source = [all_numerics[x] for x in source_list],
            target = [all_numerics[x] for x in target_list],
            value = [count_dict[x, y] for x, y in zip(source_list,target_list)],
            #Adding link colors,have to split to remove the added suffix
            color = [color_dict_link[x.split('_')[0]] for x in target_list]
        ),)])
    #Adds 1st,2nd month on top,x_coordinate is 0 - 5 integers,column #name is specified by the list we passed
    for x_coordinate, column_name in enumerate(["<b>1st Month</b>","<b>2nd Month</b>","<b>3rd Month</b>","<b>4th Month</b>","<b>5th Month</b>","<b>6th Month</b>"]):
        fig.add_annotation(
            x=x_coordinate,#Plotly recognizes 0-5 to be the x range.

            y=1.05,#y value above 1 means above all nodes
            xref="x",
            yref="paper",
            text=column_name,
            showarrow=False,
            font=dict(
                size=12,
                color="black"
            ),
            align="left",
        )

    fig.update_layout(font_size=15, height=600, margin=dict(t=60,l=0,b=20,r=30, pad=20))

    return fig