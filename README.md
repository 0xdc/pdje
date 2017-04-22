pdje - (python) django email configuration app
===

Postfix, dovecot and opendkim support configuration lookups through SQL databases,
and Django models are a very simple configurator of SQL tables - with the built-in
admin features too!

This app is motivated in part by the Snowden revelations and the
["NSA"-proof email](http://sealedabstract.com/code/nsa-proof-your-e-mail-in-2-hours/)
[<sup>via</sup>](https://prism-break.org/en/categories/gnu-linux/#mail-servers)
blog post.

Quick-start
---
1. Add "pydje" to your INSTALLED_APPS setting
2. Run `./manage.py migrate` to update the databases
3. Access [the admin panel](http://127.0.0.1:8000/admin/)
4. Setup a user and add at least one alias for a domain