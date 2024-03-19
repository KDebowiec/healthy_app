# from datetime import datetime
# from django.db import models
# from django.contrib.auth.models import User
#
#
# class HealthyAppUser(models.Model):
#     user = models.OneToOneField(User)
#     meal_plans = models.KLUCZ_OBCY
#
#
# class KCAL(models.Model)
#     kcal
#     protein
#     carbs
#     fat
#
#     class Meta:
#         abstract = True
#
#
# class MealPlan(KCAL):
#     datetime = models.DateTime(default=datetime.now)
#
#
# class MealDay(KCAL):
#     meal_plan = models.ForeignKey(related_name='meal_days')
#     day_number
#     meals = models.ManyToManyField(Meal,)
#
#
# class Meal(KCAL):
#     meal_url = models.URLField
#     image_url = models.URLField



# meal_plan = MealPlan.objects.last()
#
# meal_plan.mealday_set.all()



