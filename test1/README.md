# Stored cross-site scripting (Stored-XSS),

Stored cross-site scripting (Stored-XSS), is a type of security vulnerability that allows an attacker to inject malicious code into a website, which is then executed by other users who visit the site. 

**How to test**?

To test for this vulnerability, a tester would need to try to inject their own code into the website and see if it is executed by other users.

Here is a simple step by step process for testing stored XSS:
* Identify an input field on the website, such as a search bar or a comment section, where users can input their own data.
* Try injecting some code into that field, such as `<script>alert("XSS")</script>`.
* Check to see if the code is executed by other users who visit the website. For example, if the code is injected into a comment section, check to see if the code is executed when other users view the comments.
* If the code is executed (as a pop-up in our example), then the website is vulnerable to stored XSS. If it is not executed, then the website is likely not vulnerable. 

It's worth noting that this is a very basic example and real-world stored XSS attacks can be much more complex and harder to detect.
