2026-03-07 07:41

Status: Incomplete

Tags:[[Day 54 - Intro to web dev with Flask]]
[[Day 55 - Advanced Decorators, HTML Rendering, Parsing URLs and Flask Debugging]]
[[Day 56 - Rendering HTML static files Using website Templates]]

# **Jinja**
> A templating language is a specialized syntax used within a template engine to combine static text/markup (like HTML) with dynamic data.
> Jinja is a templating language used for python development, modelled after django's templates.
> It comes preinstalled with flask.
> Jinja allows us to run python code in our html files using the double curly bracket notation {{}}
> ```
> <h1>{{5 * 5}}</h1> # This h1 will display 30 in our webpage.
> In order to use variables in our html file, we can pass in kwargs in our in our render_template call with the keyword arguments and variables.
> render_template("index.html", number=3)
> <h2>{{number}} </h2> our h2 will then display the number 3
> ```
> Double curly brackets {{}} are typically used to render single line data, but what if we want to render multiline data like blog posts?
> For each line in the block of quote we start and end with {%  %}
> ```
> 		# FOR LOOP
>     {% for post in posts %}
      <h2>{{post["title"]}}</h2>
      <h4>{{post["subtitle"]}}</h4>
      <p>{{post["body"]}}</p>
    {% endfor %}
>   # IF CONDITiONAL
>       {% for post in posts %}
      {% if post["id"] == 2 %}
>
      <h2>{{post["title"]}}</h2>
      <h4>{{post["subtitle"]}}</h4>
      <p>{{post["body"]}}</p>
      {% endif %}
    {% endfor %}
  >
> ```
>![[Pasted image 20260307093029.png]]

#### URL BUILDING
> This is a way that allows us to direct the user to a specific page on the website or webapp
> To do this we use the url_for() method which is available in every jinja template, which takes the name of a function in our server.
> ```
>   <a href="{{url_for('get_blog')}}">Go to Blog</a>
>   This also takes arguments just like render_template and we can catch those parameters inside our app route.
>     <a href="{{url_for('get_blog', num='mark')}}" target="_blank">Go to Blog</a>
>	Then we change the function definition to take kwargs
>	@app.route("/blog/<num>")
		def get_blog(num):

> ```

## References
[Jinja Docs](https://jinja.palletsprojects.com/en/stable/intro/)
