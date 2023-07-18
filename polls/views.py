from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.http import HttpResponse
from .models import DecorationZone, Actions


def zones_index(request):
    zones_list = DecorationZone.objects.all()
    context = {'zones_list': zones_list}
    return render(request, 'polls/zones_index.html', context)


# def zone_detail(request, zone_id):
#     return HttpResponse("You're looking at zone %s." % zone_id)


# def zone_detail(request, zone_id):
#     zone = get_object_or_404(DecorationZone, pk=zone_id)
#     return render(request, 'polls/detail.html', {'zone': zone})


def actions_index(request):
    actions_list = Actions.objects.all()
    context = {'actions_list': actions_list}
    return render(request, 'polls/actions_index.html', context)


def next_step(request):
    if request.method == 'POST':
        return redirect('polls:next_model')
    else:
        return redirect('polls:zones_index')

    # else:
    #     return HttpResponseRedirect(reverse("polls:zones_index"))

def action_detail(request, action_id):
    return HttpResponse("You're looking at action %s." % action_id)


def next_model(request):
    # Логика и шаблон для следующей модели
    return render(request, 'polls/next_model.html')

