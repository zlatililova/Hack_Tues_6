{% if post %}
	<center><h1>Search Result Found</h1></center>
	<br>
{%for i in post%}
<center><h2><a href="/home/{{i.neigh}}">{{i.str}}</a></h2></center>
{%endfor%}
	{%else%}
	<center><h1>nothing found</h1></center>
{%endif%}
