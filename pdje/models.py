from __future__ import unicode_literals

from django.db import models

from passlib.hash import sha512_crypt

# Create your models here.
class Domain(models.Model):
    name = models.CharField(max_length=63, unique=True)
    relay = models.BooleanField()
    
    def __str__(self):
        return self.name

    def aliases(self):
        aliases = Alias.objects.filter(domain=self)
        return len(aliases)

    def selectors(self):
        selectors = DkimDomain.objects.filter(domain_name=self)
        return len(selectors)

class User(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not sha512_crypt.identify(self.password):
            self.password = sha512_crypt.hash(self.password)
        super(User, self).save(*args, **kwargs) # Call the "real" save() method.
    
class Alias(models.Model):
    domain = models.ForeignKey(Domain, models.CASCADE)
    source = models.CharField(max_length=128,blank=True)
    target = models.ForeignKey(User, models.CASCADE)
    
    def __str__(self):
        return "{}@{} -> {}".format(self.source,self.domain,self.target)

class Recipient(models.Model):
    address = models.CharField(max_length=192)
    ## http://www.postfix.org/access.5.html
    ## http://tanguy.ortolo.eu/blog/article126/disable-spammed-addresses-postfix
    action  = models.CharField(max_length=8, choices=[('REJECT', 'REJECT'), ('DEFER', 'DEFER'), ('421', '421'), ('521', '521')])
    message = models.CharField(max_length=512)

    def __str__(self):
        return "{} {}".format(self.action, self.address)

class DkimDomain(models.Model):
    domain_name = models.ForeignKey(Domain, models.CASCADE, to_field="name")
    selector = models.CharField(max_length=63)
    private_key = models.TextField()
    public_key = models.TextField()

    def __str__(self):
        return "{}".format(self.selector)

class SenderCredential(models.Model):
    domain_name = models.ForeignKey(Domain, models.CASCADE, to_field="name")
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=106)
    relayhost = models.CharField(max_length=192)