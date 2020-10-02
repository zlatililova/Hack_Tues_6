<html> 
<body>
<center>
<form action= "{% url 'searchbar' %}" method = "get">
<input type = "text" name="search"/>
<button type = "submit">Search</button>
</form>

</center>



	{%for item in all%}

	{{item.neigh}} <br/>
	{{item.str}} {{item.num}}<br/>
	Phone{{item.phone}}<br/><br/>
	<hr>
	<!--{{item.img}}-->
	{% endfor %}
</body>
</html>
