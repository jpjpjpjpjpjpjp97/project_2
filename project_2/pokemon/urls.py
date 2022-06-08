from rest_framework import routers

from .views import PokemonViewset

router = routers.SimpleRouter()
router.register(r'pokemon', PokemonViewset)
urlpatterns = router.urls