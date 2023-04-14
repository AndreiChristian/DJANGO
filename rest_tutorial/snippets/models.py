# Import the necessary modules for the Snippet model
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Get a list of all available lexers, filtering out those that don't have a language associated with them
LEXERS = [item for item in get_all_lexers() if item[1]]

# Create a sorted list of tuples containing the language name and the lexer name, based on the LEXERS list
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

# Get a list of all available styles and create a sorted list of tuples containing the style name (used as both the display name and the style class) repeated twice
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Define the Snippet model, which will be used to represent code snippets in the app


class Snippet(models.Model):
    # Define the fields for the Snippet model
    # Automatically set the 'created' field to the current date and time when a Snippet object is created
    created = models.DateTimeField(auto_now_add=True)
    # A short title for the snippet, which can be left blank
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()  # The code for the snippet, which can be of arbitrary length
    # Whether to display line numbers next to the code in the app
    linenos = models.BooleanField(default=False)
    # The language of the code, selected from a list of available languages
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # The style to use for syntax highlighting, selected from a list of available styles
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly', max_length=100)

    # Define any metadata for the Snippet model
    class Meta:
        # Set the default ordering for Snippet objects to be by their 'created' field, with the most recently created snippets appearing first
        ordering = ['created']
