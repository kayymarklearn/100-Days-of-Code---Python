2026-02-20 21:44

Status: Incomplete

Tags: [[Day 41 - Web Foundation - Intro to HTML]]
[[Day 42 - Web Foundations - Intermediate HTML]]

# **What is CSS**
> CSS - Cascading Style Sheets. There are other style sheet languages like Sass and Less. Basically just a language for styling web pages.

#### How to add CSS
> There is 3 ways of adding CSS to an html website
> 1. Inline - `<tag style="css" />`
> 2. Internal - `<style>css</style>`
> 3. External - `<link href="style.css"/>`

##### Inline CSS
![[Inline css.png]]

##### Internal CSS
![[Internal CSS.png]]

##### External CSS
![[External CSS.png]]


### CSS Selectors
> These help us target where to apply CSS. So they basically selects the part of the html to apply the css rules to.
> for exampel; 
> `h1 {
> 	color: blue;
> 	}`
> Here h1 is the selector.
> Types:
> - Element selectors - Using the name of the tag as a selector, like in the example above. When this selector is used, it affects all elements of that tag.
> 
> - Class Selector - A class is a special attribute to any html element, they're basically used to group html elements that allows for common styling. Example below;
> ```
> <h2 class="red-text"> Heading 2 </h2>
> <p class="red-text"> Paragraph </p>
> <!---------------- in style.css.............................>
> .red-text {
> 	color: red; # the dot before tine selector shows that it's a class
> }
> ```
> This type of selector is really useful on large sites with lots of elements.
> 
> - ID selector - This selects all elements with a particular ID, it's similar to the class selector. The difference between a class and id selector is that ID selectors should only be used for a single element in an html document while a class selector can be used for multiple elements (essentially a class of elements with similar styling). IDs are unique, Classes are for groups.
> ```
> <h2 id="main"> Red</h2>
> <h2>Green</h2>
> <!............................. in style.css...................................>
> #main {
> 	color: red; # the pound sign (#), is what denotes it as an ID selector
> }
> ```
> 
> - Attribute Selector - We can select elements that have particular attributes for styling using this kind of selector. Example;
> ```
> p[draggable] {
> 	color: red; # Basically means apply the styling to all p elements with the draggable attribute.
> }
> # We can even select the attribute with a specific value.
> p[draggable="false"] {
> 	color: red; # Apply to p elements with a 'draggable attrib' that have been set to 'false.'
> }
> ```
> 
> - Universal Selector - Basically means select all, it simply applies a style to everything where the style sheet is active.
> ```
> 	* {
> 		 color: red;
> 	}
> ```
## References
