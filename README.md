# Ex.05 Design a Website for Server Side Processing
## Date: 10.12.2025
## Reference number: 25004692

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
~~~
math.html

<!DOCTYPE html>
<html>
<head>
<title>Power of a Lamp</title>
<style>
    body {
        background-color: powderblue;
        font-family: Arial;
    }
    .box {
        width: 380px;
        background-color: plum;
        color: black;
        padding: 20px;
        margin: auto;
        margin-top: 120px;
        border: 5px dotted black;
        text-align: left;
    }
    input {
        width: 150px;
        padding: 5px;
    }
    button {
        margin-top: 10px;
        padding: 5px 15px;
    }
</style>
</head>
<body>

<div class="box">
    <h2 style="text-align:center;">Power of a Lamp</h2>

    Current : 
    <input type="text" id="i"> (in A)
    <br><br>

    Resistance : 
    <input type="text" id="r"> (in Ω)
    <br><br>

    <button onclick="calc()">Calculate</button>
    <br><br>

    Power : 
    <input type="text" id="p" readonly> W
</div>

<script>
function calc() {
    let I = parseFloat(document.getElementById("i").value);
    let R = parseFloat(document.getElementById("r").value);
    
    if (!isNaN(I) && !isNaN(R)) {
        document.getElementById("p").value = (I * I * R).toFixed(0);
    } else {
        document.getElementById("p").value = "Error";
    }
}
</script>

</body>
</html>


views.py

from django.shortcuts import render

def calculate_power(request):
    power = None
    if request.method == "POST":
        current = float(request.POST.get("current"))   # I
        resistance = float(request.POST.get("resistance"))  # R
        power = (current ** 2) * resistance            # P = I² × R
        print(f"Current: {current} A, Resistance: {resistance} Ω, Power: {power:.2f} W")

    return render(request, 'mathapp/math.html', {'Power': power})


urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.calculate_power),
]

~~~

## SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-12-12 111806.png>)

## HOMEPAGE:

![alt text](<Screenshot 2025-12-12 111625.png>)

## RESULT:
The program for performing server side processing is completed successfully.
