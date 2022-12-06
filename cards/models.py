from django import forms
from django.db import models

# Create your models here.
NUM_BOXES = 5
BOXES = range(1, NUM_BOXES+1)

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(
        choices= zip(BOXES, BOXES),
        default= BOXES[0]
    )
    date_created = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.question

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]
        # if self.box == 5 and solved: // those 2 ifs are specific but line 22 is more generic in case the borders or the boxes are more than 5 
        # if self.box == 1 and not solved:// solved == false:

        # Corner cases
        if new_box in BOXES:
            self.box = new_box
            self.save()
        return self

class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=True)