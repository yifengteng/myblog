#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import template
from django.db.models.aggregates import Count

from ..models import Post, Category, Tag

register = template.Library()


# 将函数 get_recent_posts 装饰为 register.simple_tag
@register.simple_tag
def get_recent_posts(num=8):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # return Category.objects.all()
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.all()
