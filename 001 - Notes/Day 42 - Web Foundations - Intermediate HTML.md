2026-02-20 01:18

Status: Incomplete 

Tags: [[Day 41 - Web Foundation - Intro to HTML]]


# **HTML Boilerplate**
> This is the structure every html file should follow.
> - Doc-type declaration - tells the browser which version of html the file was written in.
> for html5, the declaration looks like
> 	`<!DOCTYPE html>`
>- HTML Tag - everything that will be displayed on the site is written here.
>	`<html lang="en">
>	
>	</html>`
>- Head tag - includes important meta data that the browser needs to render the webpage.
>	`<head>
>		<meta charset="UTF-8">
>		<title>My website</title>
>		<meta name="viewport" content="width=device-width, initial-scale=1.0">	
>	</head>`
>- Body tag - This is where all the content of the website goes
>	`<body>
>		<h1>hello world!</h1>
>		 
>	</body>`

###### The html boilerplate looks like this
![[html boilerplate.png]]

### The list element
> - Undordered list
> 	`<ul>
> 		<li>Milk</li>
> 		<li>Eggs</li>
> 		<li>Flour</li>
> 	</ul>`
> - Ordered list
> 	`<ol>
> 		<li>Milk</li>
> 		<li>Eggs</li>
> 		<li>Flour</li>
> 	</ol>` 

### Nesting and Indentation

![[Nested_indented code.png]]

### Understanding Attributes
> An attribute goes into the opening tag, just after the name of the tag before the end `>` of the opening tag, attributes add additional functionality to a tag.
> ![[HTML attributes.png]]
> You can use multiple attributes by separating them with whitespace.
>  
> ![[HTML attributes 1.png]]
> Some attributes are specific to certain elements like the `href` attribute to the anchor element.
> But some are Global attributes like `draggable` which works on all elements.

#### Images
> We use the `<img src="">` tag to render images. The `src` attributes takes the path to the image. This tag has no closing tag (void element). It's also important to add the `alt` attribute, this is important for screen readers (for people with visual impairment).
## References
