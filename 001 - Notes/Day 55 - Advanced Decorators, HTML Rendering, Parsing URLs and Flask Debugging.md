2026-03-06 11:50

Status: incomplete

Tags: [[Day 54 - Intro to web dev with Flask]]
[[Day 56 - Rendering HTML static files Using website Templates]]
[[Day 57 - Templating with Jinja in Flask apps]]
### **Working with Flask URL Paths and the Flask Debugger**
> - Parsing a  URL:
> 	- Routing:
> 		Modern web applications use meaningful URLs to help users\. Users are more likely to like a page and come back if the page uses a meaningful URL they can remember and use to directly visit the page. Use the route()  decorator to bind a function to a URL.
> 		```
> 			@app.route('/')
> 			def index():
> 				return 'Index page'
>
>			@app.route('/hello/')
>			def hello():
>				return 'Hello, world'
>		- Variable Rules
>			You can add variable sections to a URL by marking sections with <variable_name>. You function then receives the <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of argument like <converter:variable_name>
>			@app.route("/<name>")
			def gree(name):
			    return f"Hello {name}"
			if __name__ == "__main__":
			    app.run(debug=True) # enables the flask debugger
> 		```

### Rending HTML elements with Flask

## References
