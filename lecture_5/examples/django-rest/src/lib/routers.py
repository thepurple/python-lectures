"""
Goods Root API library (swagger)
"""
from rest_framework.routers import DefaultRouter, APIRootView


class ShopRootApiTitleView(APIRootView):
    """
    Shop root API title (will be get from class name)
    """
    pass


class DefaultRouterExt(DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for extending url routes
    from another router.
    """
    APIRootView = ShopRootApiTitleView

    def extend(self, router):
        """
        Extend the routes with url routes of the passed in router.

        Args:
             router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(router.registry)

    def get_api_root_view(self, api_urls=None):
        root_view = super(DefaultRouterExt,
                          self).get_api_root_view(api_urls=api_urls)
        root_view.cls.__doc__ = "The default basic root view for Visir API"
        return root_view
