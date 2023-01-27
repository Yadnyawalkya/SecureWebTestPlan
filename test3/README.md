# SQL injection

SQL injection is a type of security vulnerability that can be found in web applications that use a database. It occurs when user input (such as from a form or search bar) is not properly sanitized, and is then used in a SQL query. This can allow an attacker to manipulate the query and retrieve or modify sensitive information from the database.

**How to test?**

To test for SQL injection vulnerabilities, a tester can try entering special characters or SQL commands into various user inputs and see if they can manipulate the query or retrieve information from the database. For example, they can try entering `"'` OR `'1'='1"` into a search bar or parameter of url `(http://example.com/id=123')` and see if they can retrieve information they shouldn't have access to.

It's important to note that SQL injection testing can be dangerous if not done properly, as it can cause data loss or damage to the database. So it's recommended to test in a safe environment, such as a test database, and to inform the developers before starting testing.

Testing SQL injections also depends upto type of database offering team is using. If its a SQL database, process remains the same. OWASP has good guide for how to test [NoSQL Injections](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05.6-Testing_for_NoSQL_Injection).