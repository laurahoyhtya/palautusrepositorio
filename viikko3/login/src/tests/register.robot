*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register User  matti  salasana123
    Registration Should Succeed

Register With Password That Contains Digits
    Register User  matti2  kalle123
    Registration Should Succeed

Register With Password That Contains Special Character
    Register User  matti3  kalle#abc
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Register User  u1  salasana123
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Register User  matti  short7
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Password That Contains Only Letters
    Register User  matti4  kallekalle
    Registration Should Fail With Message  Password must contain at least one number or special character

Register With Password That Contains Only Uppercase Letters
    Register User  matti5  KalleKalle
    Registration Should Fail With Message  Password must contain at least one number or special character

Register With Username That Is Already In Use
    Register User  kalle  kalle123
    Registration Should Fail With Message  Username is already in use

*** Keywords ***
Registration Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Register User
    [Arguments]  ${username}  ${password}
    Fill Text  id=username  ${username}
    Fill Secret  id=password  $password
    Fill Secret  id=password_confirmation  $password
    Click  button >> text=Register

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To  ${REGISTER_URL}
