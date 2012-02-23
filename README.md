django-elin [UNDER CONSTRUCTION]
=============

PLEASE CHECk BACK SOON THIS SITE IS UNDER CONSTRUCTION. THE CODE IS BEING DIVORCED FROM THE ORIGINAL PROJECT FOR WHICH IT WAS DEVELOPED.

To see the current progress have a look on Trello : [https://trello.com/board/django-elin/4f4545a50b4f0def04c33b73]

This is a django application that allows for password-less login via email. 

The process works as follows: 
-----------------------------
1. A user browses to a django-elin protected site. 
2. The site detects that the user has not been authenticated yet.
3. The user is prompted to provide an email and pass a CAPTCHA.
4. django-elin sends the user an email with a URL containg the current valid token for the user.
5. The user clicks on the link and is allowd to interact with the site as an authenticated user.

Installing
----------
TBD

Usage
-----
TBD 

MIT License
===========

    Copyright (C) 2012 by whoatemydomain
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
