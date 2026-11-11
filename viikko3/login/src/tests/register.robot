*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register User  matti  salasana123
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Register User  u1  salasana123
    Registration Should Fail

Register With Valid Username And Too Short Password
    Register User  matti  short7
    Registration Should Fail

Register With Username That Is Already In Use
    Register User  kalle  kalle123
    Registration Should Fail

*** Keywords ***
Registration Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Registration Should Fail
    Register Page Should Be Open

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
