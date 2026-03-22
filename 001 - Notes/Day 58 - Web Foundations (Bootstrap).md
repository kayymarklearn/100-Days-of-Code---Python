2026-03-07 17:29

Status: Incomplete

Tags: [[Day 41 - Web Foundation - Intro to HTML]]
[[Day 42 - Web Foundations - Intermediate HTML]]

# **Bootstrap Framework**
> This is one of many external css layout systems (probably the most popular).
> It's a css framework created in 2010, it became popular because,
> it contained pre-made css files which could be simply included in project by simply adding classes to your html to make it easy to create components and responsive websites.
> ```
> <button>Home</button> # plain button
> <button class="nav-link active rounded-5">Home </button> # Prestyled button
> ```
> What are CSS Frameworks?
> They are pre-made CSS files which you can include into your project, they allow us to create sites with pre-built components to develop websites quickly and efficiently.
> How to include Bootstrap in your project:
> - Include the CDN (content delivery network) : only include Bootstrap's complited CSS or JS by simply including a link in the head section (css) and body (the js) in the the end of our section.
>Example of a card in bootstrap
>```
>      <div class="card" style="width: 18rem">
        <img src="./flower.jpg" class="card-img-top" alt="..." />
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            Some quick example text to build on the card title and make up the
            bulk of the card’s content.
          </p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>

>```

#### Bootstrap layout.
Bootstrap uses a 12 column layout which is outlined as;
![[Pasted image 20260307175910.png|697]]
> In code this looks like
> ```
> <div class="container">
> 	<div class="row"> 
> 		<div class="col">Hello</div>
> 	</div>
> </div>
> ```
#### Bootstrap Components
- buttons - They can be created by giving the button element a btn class.


## References
[Bootstrap Github](https://github.com/twbs/bootstrap)
[Bootstrap components (free)](https://graygrids.com/components)

