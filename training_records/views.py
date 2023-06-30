from django.shortcuts import render, get_object_or_404, redirect
from .models import Training
from .forms import RecordTraining
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def index(request):
    latest_training_list = Training.objects.order_by('-training_date')
    context = {
        'latest_training_list': latest_training_list,
    }

    form = RecordTraining(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form

    return render(request, 'training_records/index.html', context)


@require_POST
def delete(request, pk):
    training = get_object_or_404(Training, pk=pk)
    training.delete()
    return JsonResponse({'success': True})


def update(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == "POST":
        form = RecordTraining(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('training_records:index')
    else:
        form = RecordTraining(instance=training)
    return render(request, 'training_records/update.html', {'form': form})
