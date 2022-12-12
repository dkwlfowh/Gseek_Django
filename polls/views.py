from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from .models import State
from datetime import datetime, date, timedelta
from django.template import loader



# # Create your views here.
# def index(request):
#
#     # latest_state = State.objects.filter(date__range=[date.today()-timedelta(days=1),date.today()]).values('state').annotate(
#     #     cnt_state=Count('state')
#     # ).order_by('-cnt_state')[0:10]
#
#     latest_state = State.objects.filter(date__range=["2022-12-01","2022-12-02"]).values('state').annotate(
#         cnt_state=Count('state')
#     ).order_by('-cnt_state')[1:20]
#
#     context = {"latest_state": latest_state}
#     # # lee=type(latest_state)
#     # # # output=', '.join([q.state for q in latest_state])
#     return render(request,"polls/index.html",context)
#     # return HttpResponse(latest_state)

def news(request):
   starttime = request.GET.get('starttime')
   endtime = request.GET.get('endtime')
   print("startime",starttime)
   print("endtime",endtime)

   latest_state = State.objects.filter(date__range=[starttime, endtime]).values('state').annotate(
           cnt_state=Count('state')
       ).order_by('-cnt_state')[1:20]

   context = {"latest_state": latest_state,
              "starttime":starttime,
              "endtime":endtime}
   # print(datetime.now())
   return render(request,"polls/home.html",context)
   # return HttpResponse(latest_state.query)


def detail(request):
    detail="detail"
    context={ "detail" : detail }
    return render(request, "polls/detail.html", context)
