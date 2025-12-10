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
    <title>Area of Rectangle</title>

    <style>
        body {
            background-color: rgba(183, 57, 151, 0.781);
            font-size: 20px;
        }

        .box {
            width: 500px;
            height: 300px;
            background-color: rgba(200, 70, 105, 0.977);
            margin: 150px auto;
            border: 7px dashed rgb(69, 10, 10);
        }

        h1 {
            color:rgb(69, 10, 10);
            text-align: center;
            padding-top: 20px;
        }

        .formelt {
            color:rgb(69, 10, 10);
            text-align: center;
            margin-top: 7px;
            margin-bottom: 6px;
        }
    </style>
</head>

<body>

<div class="edge">
    <div class="box">
        <h1>Area of a Rectangle</h1>

        <form method="POST">
            {% csrf_token %}
            
            <div class="formelt">
                Length :
                <input type="text" name="length" value="{{ l }}"> (in m) <br>
            </div>

            <div class="formelt">
                Breadth :
                <input type="text" name="breadth" value="{{ b }}"> (in m) <br>
            </div>

            <div class="formelt">
                <input type="submit" value="Calculate">
            </div>

            <div class="formelt">
                Area :
                <input type="text" name="area" value="{{ area }}"> m<sup>2</sup>
            </div>
        </form>

    </div>
</div>

</body>
</html>

views.py

from django.shortcuts import render

def rectanglearea(request):
    context = {}
    context['area'] = "0"
    context['l'] = "0"
    context['b'] = "0"

    if request.method == 'POST':
        print("POST method is used")
        l = request.POST.get('length', '0')
        b = request.POST.get('breadth', '0')

        print("length=", l)
        print("breadth=", b)

        area = int(l) * int(b)
        context['area'] = area
        context['l'] = l
        context['b'] = b

        print("Area=", area)

    return render(request, 'mathapp/math.html',context)

urls.py

    from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofrectangle/', views.rectanglearea, name="areaofrectangle"),
    path('', views.rectanglearea, name="areaofrectangleroot"),
]

~~~

## SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-12-10 214548.png>)

## HOMEPAGE:

![alt text](<Screenshot 2025-12-10 214329.png>)

## RESULT:
The program for performing server side processing is completed successfully.
