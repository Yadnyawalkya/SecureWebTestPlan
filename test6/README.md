# Permission issues

Security permission issues on servers can occur when the server is configured in a way that allows unauthorized access to sensitive files or directories. To test for these types of vulnerabilities, a tester can try accessing different files and directories on the server to see if they are able to view or modify them.

There are several types of files that are commonly exposed to permission issues, including:

**Configuration files**: These files contain sensitive information such as passwords, database credentials, and other settings that are used by the server and applications. They should be protected from unauthorized access.

**Log files**: These files contain a record of the server's activity, including login attempts, system errors, and other events. They should be protected from unauthorized access or modification.

**Backup files**: These files contain a copy of the server's data and should be protected from unauthorized access or modification.

**Script files**: These files contain code, such as JavaScript, PHP, or Python, that can be executed by the server or a user's browser. They should be protected from unauthorized access or modification.

**Data files**: These files contain sensitive data such as user information, financial data and should be protected from unauthorized access or modification.

**Executable files**: These files contain code that can be run on the server or the user's device, such as .exe and .dll files. They should be protected from unauthorized access or execution.

Testers can also create new user on server with lesser persmisison and check if they can access sensetive files. Here is such [reference](https://theforeman.org/security.html#CVE-2020-14335:WorldreadabledhcpOMAPIsecretcouldexposedhcpAPIaccess).

