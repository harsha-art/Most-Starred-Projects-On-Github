# Request to get Data 
import requests 
from plotly.graph_objs import Bar
from plotly import offline

url = "https://api.github.com/search/repositories?q=language:python&sort=stars" 
# Change The Language to get any language you want
headers = {'Accept': 'application/vnd.github.v3+json'} #Github API version 3 
r = requests.get(url,headers = headers)

#Status code should be 200 if it is done properly 
print(f"{r.status_code}")

#Converts the JSON to a python dictionary 
requested_dict = r.json()

#We get a dictionary of the repos returned 
repo_dicts = requested_dict['items']

repo_heads,stars,labels_on_bar = [],[],[]
for repo_dict in repo_dicts:
	repo_name = repo_dict['name']
	repo_url = repo_dict['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
	repo_heads.append(repo_link)
	stars.append(repo_dict['stargazers_count'])
	owner = repo_dict['owner']['login']
	description = repo_dict['description']
	label = f"{owner} <br /> {description} <br /> {stars}"
	labels_on_bar.append(label)

data = [{
	'type':'bar',
	'x':repo_heads,
	'y':stars,
	'hovertext': labels_on_bar,
	'marker':{
	'color':'rgb(60, 100, 150)',
	'line':{'width':1.5,'color':'rgb(25, 25, 25)'}
	},
	'opacity':0.6,
}]

layout={
'titlefont':{'size':30},
'title':'Most-Starred Python Projects in github',
'xaxis':{'title':'Repo Names','tickfont':{'size':14},'titlefont':{'size':24}},
'yaxis':{'title':'Stars','tickfont':{'size':14},'titlefont':{'size':24}}}

fig = {'data':data,'layout':layout}
offline.plot(fig,filename="API.html")
