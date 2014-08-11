# coding:utf-8

# Create your views here.
from info.models import Info
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.cache import cache



PAGE_SIZE = 4
CACHE_PREFIX = 'local_'
CACHE_TIME = 60 * 60

@login_required
def index(request):
    return list(request, 1)

@login_required
def list(request, page_num):
    all_list = Info.objects.order_by('-pub_date')
    return render_with_list(request, all_list,
                            page_num=page_num,
                            url_name='info.list',)

@login_required
def query_by_area(request, area_id, page_num):
    all_list = Info.objects.filter(info_area__pk=area_id).order_by('-pub_date')
    return render_with_list(request, all_list,
                            page_num=page_num,
                            url_name='info.by_area',
                            query_id=area_id,)

@login_required
def query_by_class(request, class_id, page_num):
    all_list = Info.objects.filter(info_class__pk=class_id).order_by('-pub_date')
    return render_with_list(request, all_list,
                            page_num=page_num,
                            url_name='info.by_class',
                            query_id=class_id,)

'''
公用分页方法
'''
def render_with_list(request, all_list, **args):

    paginator = Paginator(all_list, PAGE_SIZE)

    page_num = args['page_num']
    page_num = int(page_num)

    try:
        info_list = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        info_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        info_list = paginator.page(paginator.num_pages)

    prev_page = page_num - 1 if page_num > 1 else page_num
    next_page = page_num + 1 if page_num < paginator.num_pages else page_num

    return render(request, 'info/list.html',
                  {'info_list' : info_list,
                   'page_range' : paginator.page_range,
                   'prev_page' : prev_page,
                   'next_page' : next_page,
                   'curr_page' : page_num,
                   'url_name' : args['url_name'],
                   'query_id' : args.get('query_id')
                   })

@login_required
def detail(request, id, from_url):
    info = Info.objects.get(pk=id);

    # update view times
    info.view_times += 1
    info.save()

    area_num, class_num = get_from_cache(info)

    return render(request, 'info/detail.html',
                  {'info' : info,
                   'from_url' : from_url,
                   'area_num' : area_num,
                   'class_num' : class_num,
                   })

def get_from_cache(info):
    key = CACHE_PREFIX + str(info.pk)
    tuple = cache.get(key)
    if not tuple:
        tuple = (info.info_area.info_set.count(),
                 info.info_class.info_set.count())
        cache.set(key, tuple, CACHE_TIME)
    return tuple

