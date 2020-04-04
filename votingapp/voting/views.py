from django.shortcuts import render,redirect,get_object_or_404,reverse,HttpResponseRedirect
from .models import Poll
from .forms import PollForm
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PollSerializer
# Create your views here.



def poll_list(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls,
    }
    return render(request,'voting/poll_lists.html',context)

def poll_create(request):
    form = PollForm()
    if request.method == 'POST':
        form = PollForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('poll-list')
    context = {'form':form}
    return render(request,'voting/poll_creates.html',context)

def poll_vote(request,poll_id):
    poll = get_object_or_404(Poll,id = poll_id)
    if request.method == 'POST':
        selected_option = request.POST.get('poll')
        if selected_option == 'option1':
            poll.option1_count += 1
        elif selected_option == 'option2':
            poll.option2_count += 1
        elif selected_option == 'option3':
            poll.option3_count += 1
        else:
            return HttpResponseRedirect(reverse('poll-vote',kwargs={'poll_id':poll.id}))
        poll.save()
        return HttpResponseRedirect(reverse('poll-results',kwargs={'poll_id':poll.id}))
    context = {'poll':poll}
    return render(request,'voting/poll_votes.html',context)

def poll_results(request,poll_id):
    poll = get_object_or_404(Poll,id = poll_id)
    context = {'poll':poll}
    return render(request,'voting/poll_results.html',context)


"""
def get_resultsData(request,obj_id):
    poll = get_object_or_404(Poll,id = obj_id)
    data = {
        poll.option1:poll.option1_count,
        poll.option2:poll.option2_count,
        poll.option3:poll.option3_count,
    }
    return JsonResponse(data)
"""

@api_view(['GET'])
def get_api_data(reuqest,obj_id):
    poll = get_object_or_404(Poll,id=obj_id)
    serializer = PollSerializer(poll,many=False)
    return Response(serializer.data)

