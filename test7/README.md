# Path traversal issues

Path traversal, also known as "directory traversal," is a type of vulnerability that allows an attacker to access files and directories on a server that should not be accessible. To test for this type of vulnerability, a tester can try to access files and directories on the server by using special characters or sequences in the file path.

One way to test for path traversal vulnerabilities is to try accessing files and directories by using `../` in the file path. This tells the server to go up one level in the directory hierarchy. For example, if a tester wants to access a file called `hidden.conf` that is located in the "private" directory, they might try accessing it by using the file path `http://example.com/../../private/hidden.conf`. and try if they can view the file.

Along with UI, for this vulenerability type, its worth also check API and Command-line interface.