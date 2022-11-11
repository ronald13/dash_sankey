import plotly.graph_objects as go

def create_sankey(all_numerics, names, count_dict, source_list, target_list):
   # define two sets of color dictionaries one for the nodes and the #other for the links
   # Node color dict, RGBA means red,green,blue,alpha. Alpha sets the #opacity/transperancy
   color_dict = {'LOW VALUE CUSTOMER': ' rgba(252,65,94,0.7)', 'MEDIUM VALUE CUSTOMER': 'rgba(255,162,0,0.7)',
                 'HIGH VALUE CUSTOMER': 'rgba(55,178,255,0.7)'}
   # link color dict.The colors are the same but lower a value, lower #opacity. Gives a nice effect.
   color_dict_link = {'LOW VALUE CUSTOMER': ' rgba(252,65,94,0.4)', 'MEDIUM VALUE CUSTOMER': 'rgba(255,162,0,0.4)',
                      'HIGH VALUE CUSTOMER': 'rgba(55,178,255,0.4)'}
   # Plotting, everything is the same as last with added colors
   fig = go.Figure(data=[go.Sankey(
    node=dict(
     thickness=5,
     line=dict(color=None, width=0.05),
     # Adding node colors,have to split to remove the added suffix
     color=[color_dict[x.split('_')[0]] for x in names], ),
    link=dict(
     source=[all_numerics[x] for x in source_list],
     target=[all_numerics[x] for x in target_list],
     value=[count_dict[x, y] for x, y in zip(source_list, target_list)],
     # Adding link colors,have to split to remove the added suffix
     color=[color_dict_link[x.split('_')[0]] for x in target_list]
    ), )])
   # Adds 1st,2nd month on top,x_coordinate is 0 - 5 integers,column #name is specified by the list we passed
   for x_coordinate, column_name in enumerate(
           ["1st<br>Month", "2nd<br>Month", "3rd<br>Month", "4th<br>Month", '5th<br>Month', '6th<br>Month']):
    fig.add_annotation(
     x=x_coordinate,  # Plotly recognizes 0-5 to be the x range.

     y=1.175,  # y value above 1 means above all nodes
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

   fig.update_layout(font_size=15,  height=600,
                     margin=dict(t=150, l=0, b=20, r=0))
   # Adding y labels is harder because you don't precisely know the #location of every node.
   # You could however add annotations using the labels option while defining the figure but you cannot change the color for each #annotation individually
   return fig