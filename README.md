# Ex.05 Design a Website for Server Side Processing
# Date:
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
math.html
<!DOCTYPE html>
<html>
<head>
  <title>Power Calculator</title>
</head>
<style>
    h2{
        background-color: bisque;
    }
    h3{
        background-color: aquamarine;
    }
    label{
        background-color: aquamarine;
    }
    h3{
        background-color:grey;
    }
    body{
        background-color: cornflowerblue;
    }
</style>
<body>
  <h2>Incandescent Bulb Power Calculator</h2>

  <label>Intensity (I) in amperes:</label><br>
  <input type="number" id="intensity"><br><br>

  <label>Resistance (R) in ohms:</label><br>
  <input type="number" id="resistance"><br><br>

  <button onclick="calculatePower()">Calculate Power</button>

  <h3 id="result"></h3>

  <script>
    function calculatePower() {
      var I = parseFloat(document.getElementById("intensity").value);
      var R = parseFloat(document.getElementById("resistance").value);

      if (!isNaN(I) && !isNaN(R)) {
        var P = I * I * R;
        document.getElementById("result").innerText = "Power (P) = " + P.toFixed(2) + " watts";
      } else {
        document.getElementById("result").innerText = "Please enter both values.";
      }
    }
  </script>
</body>
</html>

urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator, name='calculator'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mathapp.urls')),  
]

views.py
from django.shortcuts import render

def calculator(request):
    power = None

    if request.method == 'POST':
        try:
            intensity = float(request.POST.get('intensity'))
            resistance = float(request.POST.get('resistance'))
            power = round(intensity ** 2 * resistance, 2)
        except (TypeError, ValueError):
            power = "Invalid input. Please enter numeric values."

    return render(request, 'math.html', {'power': power})

 ```   
# SERVER SIDE PROCESSING:

![alt text](<Screenshot (28).png>)




# HOMEPAGE:

![alt text](<Screenshot (26).png>)

![alt text](<Screenshot (27).png>)




# RESULT:
The program for performing server side processing is completed successfully.
