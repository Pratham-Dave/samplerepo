from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import random

cities = ['Mumbai', 'Rajkot', 'Junagadh', 'Dubai', 'NewYork']
data = [2343411, 4565466, 5565542, 3232344, 4535453]


def index(request):
    return render(request, 'Project1/map.html', {
        'cities': cities,
        'data': data
    })
# def index(request):
#     x_data = [i for i in range(50)]
#     y_data = [j for j in range(60)]

#     labels = [1,2,3,4]
#     values = [10,20,30,40]
#     ndata = 100
#     fig = {
#         'data': [{'labels': labels,
#             'values': values,
#             'type': 'pie',
#             'textposition':"none",
#             'textinfo':"percent",
#             'textfont':{'size':'12'},
#             'showlegend':'false'}],
#         'layout': {'title': 'Total:'+str(ndata),
#             'showlegend':'false',
#             'height':'200',
#             'width':'200',
#             'autosize':'false',
#             'margin':{'t':'50','l':'75','r':'0','b':'10'},
#             'separators':'.,'}
#     }
#     plotly_url = plot(fig, filename='map.html', auto_open=False)
#     pie_url = '<iframe width="200" height="200" frameborder="0" seamless="seamless" scrolling="no" src='+plotly_url+'.embed?width=200&height=200&link=false&showlegend=false></iframe>'
#     plot_div = plot([go.Scatter(x=x_data, y=y_data,
#                         mode='lines', name='test',
#                         opacity=1.0, marker_color='green')],
#                output_type='div')

#     return render(request, "Project1/map.html", {
#         'graph': plot_div,
#         'pie_chart': pie_url
#     })

