from oscar.apps.promotions.app import PromotionsApplication as CorePromotionsApplication
# from oscar.apps.promotions.views import


class PromotionsApplication(CorePromotionsApplication):
    extra_view = 1


application = PromotionsApplication()
