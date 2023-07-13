# Goal
Unit test the printCurrentDate function.

1. Test coupled code
2. Test the code with doubles from a library.
3Test the code with doubles created by you.
# Code to test
    class PrintDate:
        def print_current_date(self):
            print(datetime.today())
# Learnings
How to build a Mock and Stub manually.

How to use Unittest Mock to generate the doubles.

## Tools
[Unittest documentation](https://cpython-test-docs.readthedocs.io/en/latest/library/unittest.mock.html)
### Example of spy

    def test_should_send_an_email(self):
        emailSender = Mock(EmailSender)
        user_registration = UserRegistration(email_sender)
    
        user_registration.register()
    
        email_sender.send.assert_called()

	
### Example of stub

    def test_should_success_when_password_is_valid(self):
        password_validator = Mock(PasswordValidator)
        password_validator.is_valid = Mock(return_value=true)
        user_registration = UserRegistration(password_validator)

        success = user_registration.register()

        assertTrue(success)
