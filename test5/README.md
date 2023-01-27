# Authorization tests

The tester should attempt to access various resources on the website, both those they are authorized to access and those they are not authorized to access. They should observe whether they are only able to access the resources they are authorized for, and whether trying to access restricted resources returns an error or redirects to a login page without any vulnerabilities or weaknesses in the authorization system.
    
This type of vulnerability should also be particularly checked for APIs, as they are often susceptible to this issue. Offering which implements Role-Based Access Control (RBAC) are prone to authorization issues.