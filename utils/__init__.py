# Модули профиля
from .profileInformations.profile_ import Profile__
from .profileInformations.awards_ import Awards__
from .profileInformations.friends_ import Friends
from .profileInformations.menu_ import ProfileMenu
#Модули магазина 
from .storeInformations.wishlist_ import wishlist
from .storeInformations.wishlistGameInfo import GameInfo
#Модули торговой площадки
# from .marketInformations.menu_ import Menu




__all__ = ["Profile__", "Awards__", "ProfileMenu", "wishlist", "GameInfo", "Friends"]