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