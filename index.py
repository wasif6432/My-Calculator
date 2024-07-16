# Import necessary modules from Flask
from flask import Flask, render_template, url_for, request


# Initialize a Flask application
app = Flask(__name__)


# Defined the main route that renders the index.html template
@app.route("/")
def main():
    return render_template("index.html")


# Define the simple route that renders the simple.html template
@app.route("/simple")
def simple():
    return render_template("simple.html")


# Define a route to handle the calculator logic, accepts Post requests
@app.route("/calculate", methods = ["post"])
def calculate():
    # Get the operation, first number and the second number
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    second_number = int(request.form["secondNumber"])
    
    # Perform the calculation based on the operation
    if operation == "plus":
        result = first_number + second_number
        return render_template("simple.html", result=result)
    elif operation == "minus":
        result = first_number - second_number
        return render_template("simple.html", result=result)
    elif operation == "multiply":
        result = first_number * second_number
        return render_template("simple.html", result=result)
    elif operation == "divide":
        result = first_number / second_number
        return render_template("simple.html", result=result)
    else:
        return "There is an Error!"
    

# Run the Flask application in the debug mode
if __name__ == "__main__":
    app.run(debug=True)