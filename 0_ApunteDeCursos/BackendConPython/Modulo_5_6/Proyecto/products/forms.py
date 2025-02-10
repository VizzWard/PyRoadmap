from django.forms import ModelForm, Textarea

from .models import Comment


class CommentsForm(ModelForm):
    class Meta:
        model = Comment

        fields = ('text',)

        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'aria-label': 'Comentarios',
                'placeholder': 'Deja tu comentario',
                'id': 'formComment'
            }),
        }


# ¿Qué es y para qué sirve un formulario?
# Un formulario es una herramienta que permite al usuario interactuar con una aplicación web, enviando información
# a través de la web. Los formularios permiten al usuario ingresar información, seleccionar opciones, enviar archivos,
# entre otras cosas. Los formularios son una parte esencial de cualquier aplicación web y son utilizados para
# recopilar información de los usuarios.