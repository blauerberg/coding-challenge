# coding: utf-8

'''その他ユーティリティ関数を提供する
'''

import os

from flask import render_template


GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']


def render(template, **kargs):
    '''テンプレートを使ってレスポンスを返す

    Google API Key を自動で追加する
    '''
    kargs['GOOGLE_API_KEY'] = GOOGLE_API_KEY
    return render_template(template, **kargs)


def location_to_dict(location):
    '''Location オブジェクトを辞書に変換する
    '''
    return {
      'id': location.id,
      'title': location.title,
      'year': location.year,
      'locations': location.locations,
      'geo_lng': location.geo_lng,
      'geo_lat': location.geo_lat,
    }