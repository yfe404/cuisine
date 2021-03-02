

<p align="center">
<a href="https://github.com/yfe404/cuisine/"><img alt="Kuisine Logo" src="./logos/kuisine-logo-regular.png" width="75%"></a>
</p>


<h2 align="center">Be Healthy</h2>

<p align="center">
<a href="https://github.com/yfe4040/cuisine/actions"><img alt="Actions Status" src="https://github.com/yfe404/cuisine/workflows/CI/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>


# What is it ? 

#+BEGIN_QUOTE
Let =R= be a recipe composed of =n= ingredients. Each ingredient is denoted by its amount of calories =c=. The recipe =R= has a quantity =q= of each
ingredient composing it. The goal is to find the right quantity =q= for each ingredient such that \sum_{i=0}^{n} c_i * q_i = T.
T behing the target number of calories that you want for your recipe. Exemple: I want to make a recipe composed of oats, milk, eggs, flakseeds and peanut butter 
such that the total number of calories for the recipe is 600 kcal; how much of each ingredient should I take? This is the purpose of this repository. 
#+END_QUOTE


** How it works 

[[file:img/tuto.png]]
** Roadmap
- [X] Add ingredients
- [X] Remove ingredients
- [ ] Enable users to quickly find and select from a pre-populated list of values as they type an ingredient name 
- [ ] Handle more units (currently only grams, next: liters, units, etc.)
- [ ] Can choose the range for proteins, carbohydrates and fats (eg. I want a 600kcal recipe with at least 30g of proteins)
- [ ] Optimize the PRAL index (how acid the recipe is)
- [ ] Error handling
- ... Don't hesitate to add issues including the features you'd like to see



