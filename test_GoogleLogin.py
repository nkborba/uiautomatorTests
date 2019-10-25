from uiautomator import device as d

def test_wrongPwd():
    emailacc = "tester123"
    wrongPwd = "wrong:D"
    errorMsg = "Wrong passwaord. Try again or click Forgot password to reset it."

    #Scroll until Add account if needed if not just click
    d(scrollable=True).scroll.to(text='Add account')
    d(text="Add account").click()

    #Scroll until Google account and click
    d(scrollable=True).scroll.to(text='Google')
    d(text="Google").click()

    #Fullfill the account field with an email
    d(resourceId="identifierId").set_text(emailacc)

    #Proceed to login
    d(resourceId="identifierNext").click()

    #Type a wrong password
    d(resourceId="password").set_text(wrongPwd)

    #Verify is error message was displayed
    assert d(text=errorMsg).exists == True