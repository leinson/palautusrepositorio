*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  hannah
    Set Password  hannah123
    Set Password Confirmation  hannah123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ha
    Set Password  hannah123
    Set Password Confirmation  hannah123
    Submit Credentials
    Register Should Fail With Message  Invalid username or password

Register With Valid Username And Too Short Password
    Set Username  hanna
    Set Password  hanna12
    Set Password Confirmation  hanna12
    Submit Credentials
    Register Should Fail With Message  Invalid username or password

Register With Nonmatching Password And Password Confirmation
    Set Username  anna
    Set Password  anna5678
    Set Password Confirmation  hannah123
    Submit Credentials
    Register Should Fail With Message  Invalid username or password


*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]   ${password_confirmation}
    Input Password  password_confirmation   ${password_confirmation}


