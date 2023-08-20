## Frontend Testing

Testing ensures the stability, security, and performance of your application. Let's delve deeper into the world of frontend testing.

### What is Testing?

Testing involves assessing software for errors, performance issues, or any unwanted behavior. It ensures software meets the requirements and provides a good user experience.

## Levels of Testing

1. **System Tests**: 
    - Check the system as a whole, ensuring that all integrated components work smoothly together. 
    - Often requires the complete application and environment setup.

2. **Integration Tests**: 
    - Verify that different parts of the application work together seamlessly. 
    - Can be between different software components or between software and hardware components.

3. **Unit Tests**: 
    - Examine individual units or components of a software to ascertain if they function correctly. 
    - Typically, a unit is the smallest part of the software that can be tested in isolation.

### Unit Testing in Depth

Unit tests aim to verify each part of the software by isolating it and proving that it functions correctly on its own.

**Benefits**:

- Quickly locate and fix bugs during development.
- Facilitate code refactoring, ensuring new changes don't introduce bugs.
- Improve code design by making developers write testable code.

**Frameworks**:

1. **MochaJS**: A flexible test framework that supports multiple assertion libraries.
2. **Jest**: Developed by Facebook, it comes with built-in assertions, spies, and mocks.
3. **Jasmine**: A behavior-driven testing framework with no external dependencies.
4. **Karma**: A test runner that can execute tests in various real browsers.
5. **Puppeteer**: Provides methods to launch Chrome and interact with it using the Chrome DevTools Protocol.
6. **NightwatchJS**: An E2E testing framework written in Node.js, using the WebDriver API.
7. **Cypress**: Modern web automation test framework that can test anything running in a browser.

**Example**: Testing roman numbers with Jest

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

## Automated vs Manual Testing

Testing in software development is paramount to ensure the functionality, performance, and security of your application. Broadly speaking, these tests can be divided into two categories: automated and manual testing.

### Automated Testing

Automated tests are scripted and can be executed automatically without any human intervention. These scripts can be integrated into the development process and are often run during development, build, or deployment.

**Advantages**:
- **Speed**: Can be run quickly and frequently.
- **Reusability**: Test cases can be reused across different phases of development.
- **Consistency**: The same test is executed the same way every time, reducing the risk of human error.
- **Efficiency**: Great for regression testing where the same tests need to be executed multiple times.

### Manual Testing

Manual testing involves human testers executing test cases manually without using automation tools. They follow a test plan to ensure the application behaves as expected.

**Advantages**:
- **Flexibility**: Testers can adapt and modify tests on-the-fly based on observations.
- **Usability Feedback**: Testers can provide real user feedback on the usability and experience of the application.
- **Discovery of Real-world Issues**: Real users might use applications in ways not anticipated during automated testing.

## Online Resources for Website Testing

When it comes to ensuring that your website meets industry standards and provides an optimal user experience, various online tools can assist you.

### Code Quality

Ensure your HTML and CSS adhere to standards:

* [W3C HTML Validator](https://validator.w3.org/)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

### Links

Ensure all links on your site are functional:

* [Dr. Link Check](https://www.drlinkcheck.com/)
* [Check My Links on GitHub](https://github.com/PageModifiedOfficial/Check-My-Links)

### Performance

Analyze the speed and performance optimizations of your website:

* [Dareboost](https://www.dareboost.com/en)
* [Yellow Lab Tools](https://yellowlab.tools/)
* [PageSpeed Insights by Google](https://pagespeed.web.dev/?utm_source=psi&utm_medium=redirect)

### Security

Assess the security measures of your website:

* [Mozilla Observatory](https://observatory.mozilla.org/)
* [Webbkoll by Dataskydd](https://webbkoll.dataskydd.net/en)

### SEO

Evaluate and improve the SEO of your site:

* [Ahrefs' Free SEO Tools](https://ahrefs.com/free-seo-tools)
