from django.apps import AppConfig
import os
 
default_app_config = 'place.PlaceConfig'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]
 
class PlaceConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '景点模块'