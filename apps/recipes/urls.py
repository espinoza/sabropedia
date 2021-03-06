from django.urls import path
from . import views

urlpatterns = [

    path(
        route='new/source/',
        view=views.UpdateRecipeDatabase.as_view(),
        name='update_recipe_database'
    ),

    path(
        route='go/',
        view=views.go_to_source,
        name='go_to_source'
    ),

    path(
        route='source_not_found/',
        view=views.source_not_found,
        name='source_not_found'
    ),

    path(
        route='',
        view=views.add_recipe_from_source
    ),

]
