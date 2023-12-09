from django.shortcuts import render, get_object_or_404
from .models import Objective  # Import the Objective model

def all_objectives(request):
    objectives = Objective.objects.all()  # Retrieve all objectives from the database
    return render(request, 'objective/all_objectives.html', {'objectives': objectives})


def objective_details(request, objective_id):
    objective = get_object_or_404(Objective, pk=objective_id)  # Retrieve the objective based on the objective_id
    return render(request, 'objective/objective_details.html', {'objective': objective})

