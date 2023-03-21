import json
from flask import Flask, render_template, url_for, request, jsonify


import json
import numpy as np
from scipy.optimize import minimize

app = Flask(__name__)



def get_price(ingredients, quantities):
    """Return the price of a recipe given the ingredients and the 
       associated quantities.
    """
    return sum([ingredients[i]["price"]*quantities[i] for i in range(len(ingredients))])

def get_macros(quantities, target, ingredients):
    """Return the macros of a recipe given the ingredients and 
       the associated quantities.
    """
    macros = dict()
    for attribute in target.keys():
        macros[attribute] = 0.0
        for idx, ingredient in enumerate(ingredients):
             macros[attribute] += ingredient[attribute] * quantities[idx]
        macros[attribute] = int(macros[attribute])
    return macros
    

def evaluate(quantities, ingredients):
    """Objective function to minimize"""
    price = get_price(ingredients, quantities)
    price = np.round(price, 2)
    return price




@app.route('/')
def index():
    return render_template('index.jinja2')

@app.route('/search')
def search():
    search = request.args.get('term')

    fd = open("ingredients.json")
    ingredients = json.load(fd)

    results = []
    for ingredient in ingredients:
        if search.lower() in ingredient["name"].lower():
            results.append(
                {
                    "label":ingredient["name"],
                    "value": ingredient,
                }
            )
    return jsonify(results)



@app.route('/', methods=['POST'])
def handle_post():
    # Get the data from the request body
    data = request.get_json()

    with open("data.json", "w") as f:
        json.dump(data, f)

    target = data["target"]
    ingredients = data["ingredients"]

    ## Linear Solver Settings
    ### tolerance of the constraints: C +/- epsilon
    epsilon = 25/2 

    ### initial solution
    x0 = [1 for _ in range(len(ingredients))]
    
    ### quantities must be positive or zero
    bounds = [(0, None) for _ in range(len(ingredients))]

    ### Constraints on the target profile (only considering
    ### calories and proteins for now
    cons = [
        {'type': 'ineq', 'fun':
         lambda x: sum([x[i]*ingredients[i]["calories"] for i in range(len(ingredients))]) - epsilon - target["calories"]},
        {'type': 'ineq', 'fun': lambda x: -sum([x[i]*ingredients[i]["calories"] for i in range(len(ingredients))]) - epsilon + target["calories"]},

    ]

    
    # Try to get AT LEAST target["proteins"] grams of proteins
    if target["proteins"] is not None and target["proteins"] >= 0 :
        cons.append(
            {'type': 'ineq', 'fun': lambda x: np.random.random() \
             if -sum([x[i]*ingredients[i]["proteins"] \
                      for i in range(len(ingredients))]) + target["proteins"] < 0 \
             else -sum([x[i]*ingredients[i]["proteins"] \
                    for i in range(len(ingredients))]) + target["proteins"]  }
        )

    cons = tuple(cons)
    
    ### Constraints on the quantities for each ingredients
    for idx, ingredient in enumerate(ingredients):
        qty_min = ingredient.get("quantity_min", None)
        qty_max = ingredient.get("quantity_max", None)

        if qty_min:
            qty_min = float(qty_min)
            bounds[idx] = (max(qty_min, 0), None)
        if qty_max:
            qty_max = float(qty_max)
            bounds[idx] = (bounds[idx][0], max(0, qty_max))


    res = minimize(
        evaluate,
        x0=x0,
        args=(ingredients),
        method='SLSQP',
        constraints=cons,
        bounds=bounds,
        options={'disp':False, "maxiter": 10000}
    )

    quantities = [np.round(x, 2) for x in res.x]
    price = res.fun
    macros = get_macros(quantities, target, ingredients)
    
    body = {
        "quantities": quantities,
        "macros": macros,
        "price": price
    }


    response = {
        "statusCode": 200,
        "headers": {
	    "Access-Control-Allow-Origin": "*",
	    "Access-Control-Allow-Credentials": True,
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }
    
            
    return body
    


if __name__ == '__main__':
    app.run()
