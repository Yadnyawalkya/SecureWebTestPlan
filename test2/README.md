# Reflected XSS

Reflected cross-site scripting (Reflected XSS) can also happen when a user is tricked into clicking on a link that contains malicious code. 

**How to test?** 

To test for this type of vulnerability, a tester can try creating a link with malicious code in it and see if it can be executed when clicked on.

One way to do this is to construct a URL with a malicious payload in the query parameter, such as `https://example.com/search?q=<script>alert('XSS')</script>`, then share it and observe if the payload is executed in the browser of the person that clicked on the link. With our example we used similar payload but done url encoding on it already.
