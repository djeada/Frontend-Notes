## Testing Frontend

We'll explore various aspects of frontend testing, including the different levels of testing, popular testing frameworks, and various types of tests, such as unit, end-to-end (E2E), and UI tests. We'll also discuss the benefits of using mock servers, the differences between automated and manual tests, and provide a list of online resources for testing code quality, links, performance, security, and SEO. Additionally, we'll include examples to help illustrate these concepts.

## What is testing?


Testing is the process of executing a program with the intention of finding errors. It helps to ensure the quality and reliability of software applications.

There are three main levels of tests:
* System tests
* Integration tests
* Unit tests

System testing is the most complex and also the most vulnerable since it relies on all of the system's components. Unit tests are the smallest and fastest tests.

### Unit tests

Unit tests are used to test a single component of an application. This component is generally associated with a single function. Test-Driven Development (TDD) is a programming approach in which unit tests are written before the actual code.

Some popular JavaScript testing frameworks include:

1. MochaJS
2. Jest
3. Jasmine
4. Karma
5. Puppeteer
6. NightwatchJS
7. Cypress

**Example: Testing roman numbers with Jest**

```javascript
const romanNumberConverter = require('./romanNumberConverter');

test('Converts I to 1', () => {
  expect(romanNumberConverter('I')).toBe(1);
});

test('Converts IV to 4', () => {
  expect(romanNumberConverter('IV')).toBe(4);
});

test('Converts XL to 40', () => {
  expect(romanNumberConverter('XL')).toBe(40);
});

test('Converts MCMXCIV to 1994', () => {
  expect(romanNumberConverter('MCMXCIV')).toBe(1994);
});
```

## E2E

End-to-end tests (also known as system tests) are used to ensure that the entire application functions properly. On a website, we may simulate situations of normal user behavior, such as creating an account, logging in, performing activities enabled for logged-in users, and deleting the account.

**Example: E2E test with Cypress**

```javascript
describe('User account creation, login, and deletion', () => {
  it('Creates, logs in, and deletes a user account', () => {
    // Visit the website
    cy.visit('https://example.com');

    // Click on the "Sign Up" button
    cy.contains('Sign Up').click();

    // Fill out the registration form
    cy.get('#username').type('testuser');
    cy.get('#email').type('testuser@example.com');
    cy.get('#password').type('securepassword');
    cy.get('#confirmPassword').type('securepassword');

    // Submit the form
    cy.get('#registerBtn').click();

    // Log out after successful registration
    cy.contains('Log Out').click();

    // Log in with the created account
    cy.contains('Log In').click();
    cy.get('#email').type('testuser@example.com');
    cy.get('#password').type('securepassword');
    cy.get('#loginBtn').click();
    // Verify successful login
    cy.contains('Welcome, testuser!');

    // Perform activities enabled for logged-in users
    // ... (insert additional test steps here)

    // Delete the account
    cy.contains('Account Settings').click();
    cy.contains('Delete Account').click();
    cy.get('#confirmDeletion').click();

    // Verify successful account deletion
    cy.contains('Your account has been deleted.');
    });
});
```

## Ui tests

UI tests allow us to use code to replicate real-world scenarios. Frameworks exist that allow us to use code to perform certain tasks and then compare the results to our expectations. For example, suppose we wish to do a right-click on a button with a specific id, and we expect a popup window to open. Selenium is an example of a framework that would allow us to perform such tests.

**Example: UI test with Selenium**

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://example.com')

button = driver.find_element_by_id('rightClickButton')

# Perform a right-click on the button
action = ActionChains(driver)
action.context_click(button).perform()

# Verify the popup window is opened
popup = driver.find_element_by_id('popupWindow')
assert popup.is_displayed()

driver.quit()
```

Another technique for conducting UI tests is to record the tests themselves rather than coding the desired behavior. We then compare a set of screenshots taken at the time of recording to new screenshots taken whenever the tests are run. Recorded tests typically break for any minor change you make to your code.

## Mock server

When testing the frontend independently of the backend, you'll need to simulate the backend. To do this, you can use a mock server.

**Example: Mock server with Nock**

```javascript
const nock = require('nock');
const api = require('./api');

test('Fetches data from the mock server', async () => {
  // Set up a mock server response
  nock('https://api.example.com')
    .get('/data')
    .reply(200, { message: 'Success', data: { value: 42 } });

  // Call the API function
  const response = await api.fetchData();

  // Verify the response from the mock server
  expect(response.message).toEqual('Success');
  expect(response.data.value).toEqual(42);
});
```

## Automated vs manual tests

All of the tests mentioned thus far can be categorized as automated tests. They are described in code and may be run automatically by the programmer in their IDE or by the Continuous Integration (CI) tool on the push. Manual tests, on the other hand, involve manually running the program and ensuring that everything works properly.

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
