# File upload vulnerability

File upload vulnerabilities can occur when a web application allows users to upload files, but doesn't properly validate the type or contents of those files. This can allow an attacker to upload a malicious file, such as a script, that can then be executed by the server or other users.

To test for file upload vulnerabilities, a tester can try uploading different types of files to see if they are accepted or rejected. They should also try uploading files with malicious content, such as a script or executable file, to see if they are executed by the server.

There are certain file formats that are commonly used to deliver malicious code or exploits, and are considered unsecure or high risk. These include:

* `.sh`: Shell files, which can run commands on a user's computer. These are often used to deliver malware or viruses.
* `.js`: JavaScript files, which can run scripts in a user's browser. These are often used to deliver client-side attacks such as XSS.
* `.html`: HTML files, which can contain scripts or links to other malicious files.
* `.xml`: XML files, which can contain scripts or links to other malicious files.
* `.pdf`: PDF files, which can contain embedded scripts or links to other malicious files.
* `.exe`: Executable files, which can run code on a user's computer. These are often used to deliver malware or viruses (mostly only for Windows).
* `.dll`: Dynamic Link Library files, which are similar to .exe files, but are intended to be used as shared libraries of code for other programs (mostly only for Windows).

Also, these filetype depends upon programming language offering using. In case of PHP, tester should check `.php`, for Ruby or Ruby on Rails applications it should be `.rb`
