from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import DecorationZone, Actions, Way, Terms


# def zones_index(request):
#     zones_list = DecorationZone.objects.all()
#     context = {'zones_list': zones_list}
#     return render(request, 'polls/zones_index.html', context)
#
#
# def actions_index(request):
#     actions_list = Actions.objects.all()
#     context = {'actions_list': actions_list}
#     return render(request, 'polls/actions_index.html', context)
#
#
# def next_step(request):
#     if request.method == 'POST':
#         return redirect('polls:next_model')
#     # else:
#     #     return HttpResponseRedirect(reverse("polls:zones_index"))
#     else:
#         return redirect('polls:zones_index')
#
#
# def action_detail(request, action_id):
#     return HttpResponse("You're looking at action %s." % action_id)
#
#
# def next_model(request):
#     return render(request, 'polls/next_model.html')

def start(request):
    return render(request, 'polls/start.html', {})


def zones_index(request):
    if request.method == 'POST':
        zones = request.POST.getlist('zones')
        quantities = {}
        total_cost = 0

        for zone_id in zones:
            zone = get_object_or_404(DecorationZone, pk=zone_id)
            quantity = int(request.POST.get(f'{zone.zone_name}_quantity', 0))
            quantities[zone_id] = quantity
            total_cost += zone.zone_cost * quantity

        request.session['zones'] = quantities
        request.session['total_cost'] = total_cost

        return HttpResponseRedirect(reverse('polls:actions_index'))

    zones_list = DecorationZone.objects.all()
    context = {'zones_list': zones_list}
    return render(request, 'polls/zones_index.html', context)

def actions_index(request):
    if request.method == 'POST':
        selected_action = request.POST.get('selected_action')
        request.session['selected_action'] = selected_action

        return HttpResponseRedirect(reverse('polls:way_index'))

    actions_list = Actions.objects.all()
    context = {'actions_list': actions_list}
    return render(request, 'polls/actions_index.html', context)

def way_index(request):
    if request.method == 'POST':
        selected_way = request.POST.get('selected_way')
        request.session['selected_way'] = selected_way

        return HttpResponseRedirect(reverse('polls:terms_index'))

        # if selected_way == '1':  # Assuming 'on-line' has ID=1, you can change it based on your actual data
        #     return HttpResponseRedirect(reverse('polls:selection_index'))
        # else:
        #     return HttpResponseRedirect(reverse('polls:terms_index'))

    way_list = Way.objects.all()
    context = {'way_list': way_list}
    return render(request, 'polls/way_index.html', context)



def selection_index(request):
    if request.method == 'POST':
        selected_action_multiplier = request.POST.get('selected_action_multiplier')
        request.session['selected_action_multiplier'] = selected_action_multiplier

        return HttpResponseRedirect(reverse('polls:terms_index'))

    return render(request, 'polls/selection_index.html')





def terms_index(request):
    if request.method == 'POST':
        selected_term = request.POST.get('selected_term')
        request.session['selected_term'] = selected_term

        return HttpResponseRedirect(reverse('polls:result'))

    terms_list = Terms.objects.all()
    context = {'terms_list': terms_list}
    return render(request, 'polls/terms_index.html', context)

# def terms_index(request):
#     selected_selection = request.POST.get('selected_selection')
#     if selected_selection == 'online':
#         return HttpResponseRedirect(reverse('polls:result'))
#
#     if request.method == 'POST':
#         selected_term = request.POST.get('selected_term')
#         request.session['selected_term'] = selected_term
#
#         return HttpResponseRedirect(reverse('polls:result'))
#
#     terms_list = Terms.objects.all()
#     context = {'terms_list': terms_list}
#     return render(request, 'polls/terms_index.html', context)


def result(request):
    zones = request.session.get('zones', {})
    zones_ = {}
    for zone_id, quantity in zones.items():
        zones_[DecorationZone.objects.get(id=zone_id).zone_name] = quantity
    selected_action = request.session.get('selected_action')
    selected_way = request.session.get('selected_way')
    selected_term = request.session.get('selected_term')
    total_cost = request.session.get('total_cost', 0)

    if not (zones and selected_action and selected_way and selected_term):
        return HttpResponseRedirect(reverse('polls:zones_index'))

    action = get_object_or_404(Actions, pk=selected_action)
    way = get_object_or_404(Way, pk=selected_way)
    term = get_object_or_404(Terms, pk=selected_term)

    way_multiplier = way.way_cost
    term_multiplier = term.term_cost

    total_cost *= action.action_cost  # Adjust total cost based on action cost
    total_cost *= way_multiplier  # Adjust total cost based on way multiplier
    total_cost *= term_multiplier  # Adjust total cost based on term multiplier

    context = {'zones': zones, 'zones_': zones_, 'action': action, 'way': way, 'term': term, 'total_cost': total_cost}
    return render(request, 'polls/result.html', context)


# def result(request):
#     zones = request.session.get('zones', {})
#     zones_ = {}
#     for zone_id, quantity in zones.items():
#         zones_[DecorationZone.objects.get(id=zone_id).zone_name] = quantity
#     selected_action = request.session.get('selected_action')
#     selected_way = request.session.get('selected_way')
#     selected_term = request.session.get('selected_term')
#     total_cost = request.session.get('total_cost', 0)
#     selected_action_multiplier = request.session.get('selected_action_multiplier', 1)
#
#     if not (zones and selected_action and selected_way and selected_term):
#         return HttpResponseRedirect(reverse('polls:zones_index'))
#
#     action = get_object_or_404(Actions, pk=selected_action)
#     way = get_object_or_404(Way, pk=selected_way)
#     term = get_object_or_404(Terms, pk=selected_term)
#
#     way_multiplier = way.way_cost
#     term_multiplier = term.term_cost
#
#     total_cost *= action.action_cost  # Adjust total cost based on action cost
#     total_cost *= way_multiplier  # Adjust total cost based on way multiplier
#     total_cost *= selected_action_multiplier
#     total_cost *= term_multiplier  # Adjust total cost based on term multiplier
#
#     context = {'zones': zones, 'zones_': zones_, 'action': action, 'way': way, 'term': term, 'total_cost': total_cost}
#     return render(request, 'polls/result.html', context)
