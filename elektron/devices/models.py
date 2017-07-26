# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Device(models.Model):
    device_ip = models.CharField(max_length=100, blank=True, default='0.0.0.0')
    created = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=100, blank=True, default='Elektron')
    state = models.CharField(max_length=100, blank=True, default='Off')
    measure = models.CharField(max_length=100, blank=True, default='') #measure puede ser un objeto en sí mismo
    #owner = models.ForeignKey('auth.User', related_name='devices', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet FROM elektron EXAMPLE.

        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        """
        super(Device, self).save(*args, **kwargs)
