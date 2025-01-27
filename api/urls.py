from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import BlogViewSet, CommentViewSet, ReactionViewSet

urlpatterns = [
    # path('api/', include(router.urls)),
    path(
        'blog/', BlogViewSet.as_view({   
            'get': 'list',
            'post': 'create',
    })),
    path(
        'blog/<int:id>', BlogViewSet.as_view({   
            'get': 'retrieve',
            'put': 'partial_update',
            'delete': 'destroy',
    })),
    path(
        'comment', CommentViewSet.as_view({   
            'get': 'list',
            'post': 'create',
    })),
    path(
        'comment/<int:id>', CommentViewSet
        .as_view({   
            'get': 'retrieve',
            'put': 'partial_update',
            'delete': 'destroy',
    })),
    path(
        'reaction', ReactionViewSet.as_view({   
            'get': 'list',
            'post': 'create',
    })),
    path(
        'reaction/<int:id>', ReactionViewSet
        .as_view({   
            'get': 'retrieve',
            'put': 'partial_update',
            'delete': 'destroy',
    })),
]