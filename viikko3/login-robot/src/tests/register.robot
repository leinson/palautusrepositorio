*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  hannah  hannah123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already excists

Register With Too Short Username And Valid Password
    Input Credentials  ma  max123456
    Output Should Contain  Too short username

Register With Valid Username And Too Short Password
    Input Credentials  hannah  ha34567
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  hannah  hannahhh
    Output Should Contain  Password must also contain numbers

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123