
# What is testing?

Testing is executing a program with intention of finding errors.

Three levels of tests:
* system
* integration
* unit

System testing is the most complex and also the most vulnerable since it relies on all of the system's components. Uni tests are the smallest and fastest tests.

## Unit tests

Unit tests are used to test a single component of an application. This component is generally associated with a single function. TDD is a programming appproah in which unit tests are written before the actual code.

We might list the following JavaScript testing frameworks:

1. MochaJS
2. Jest
3. Jasmine
4. Karma
5. Puppeteer
6. NightwatchJS
7. Cypress

## E2E

End-to-end tests (also known as system tests) are used to ensure that the entire application functions properly. On our website, we may simulate situations of normal user behavior. For example, we may begin by creating an account, then login, then perform whatever activities are enabled for logged-in users, and lastly delete the account.

## Ui tests

Ui tests allow us to use code to replicate real-world scenarios. Frameworks exist that allow us to use code to perform certain tasks and then compare the results to our expectations. For example, suppose we wish to do a right click on a button with a specific id, and we expect a popup window to open. Selenium is an example of a framework that would allow us to perform such tests.

Another technique for conducting such tests is to record the tests themselves rather than coding the desired behavior. We then compare a set of screenshots taken at the time of recording to new screenshots taken whenever the tests are run. Recorded tests typically break for any minor change you make to your code.

## Mock server

You will frequently want to test the frontend independently of the backend. You'll then need to simulate the backend. To simulate the backend, you can use a mock server.

## Automated vs manual tests

All of the tests mentioned thus far may be categorized as automated tests. They are described in code and may be run automatically by the programmer in their IDE or by the CI tool on the push. Another method of testing is to manually run the program and ensure that everything works properly.

## Online resources

There are many resources that can help you with testing your website.

### Code quality

* https://validator.w3.org/
* https://jigsaw.w3.org/css-validator/

### Links

Check for broken links:

* https://www.drlinkcheck.com/
* https://github.com/PageModifiedOfficial/Check-My-Links

### Performance

* https://www.dareboost.com/en
* https://yellowlab.tools/
* https://pagespeed.web.dev/?utm_source=psi&utm_medium=redirect

### Security

* https://observatory.mozilla.org/
* https://webbkoll.dataskydd.net/en

### SEO

* https://ahrefs.com/free-seo-tools
