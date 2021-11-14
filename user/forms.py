from django.forms import ModelForm, fields

from user.models import Post, user



class PostView(ModelForm):

    """Form definition for MODELNAME."""
    

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Post
        fields = [
            'user',
            'text',
            'created_at',
            'updated_at',                                                                   
            
        ]
        
        
class UserView(ModelForm):
    
    class Meta:
        model=user     
        fields=('first_name','last_name','email','username','password')   

