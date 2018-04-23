from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from works.models import Catalog, Category, Filter, Work


class IndexView(TemplateView):
    template_name = 'works/works.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['catalogs'] = Catalog.objects.all()[:12]
        return context


class WorksListView(ListView):
    template_name = 'works/works_by_category.html'
    model = Work
    context_object_name = 'works'
    paginate_by = 6

    def get_queryset(self):
        if self.request.is_ajax():
            self.template_name = 'works/object.html'
        return self.model.objects.filter(filter__slug=self.kwargs['filter_slug'],
                                         category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super(WorksListView, self).get_context_data(**kwargs)
        pagination = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')
        try:
            works = pagination.page(page)
        except PageNotAnInteger:
            works = pagination.page(1)
        except EmptyPage:
            raise Http404("That page contains no results")
        context['filter'] = get_object_or_404(Filter, slug=self.kwargs['filter_slug'])
        context['category'] = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        context['categories'] = Category.objects.all()[:6]
        context['works'] = works.object_list
        context['is_paginated'] = works.has_next()

        return context


class AllWorksView(TemplateView):
    template_name = 'works/all_works_by_category.html'

    def get_context_data(self, **kwargs):
        context = super(AllWorksView, self).get_context_data(**kwargs)
        _filter = get_object_or_404(Filter, slug=self.kwargs['filter_slug'])
        category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        works = Work.objects.filter(filter=_filter, category=category)
        context['filter'] = _filter
        context['category'] = category
        context['categories'] = Category.objects.all()
        context['works'] = works
        return context
