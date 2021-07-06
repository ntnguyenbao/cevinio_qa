*** Settings ***
Library     ../Resource/commonActions.py
Library     ../Resource/login/loginActions.py
Library     ../Resource/cockpit/cockpitActions.py
Library     ../Resource/ExtendedMenu/ExtendedMenuActions.py

*** Keywords ***
user opens ${browser} and accesses T-BLOX by ${user}/${pass}
    When user accesses https://local.tblox.com by ${browser}
    then login page is displayed
    When user login by ${user}/${pass}
    then cockpit page is displayed

user logout
    When user selects Back to Cockpit from menu
    then cockpit page is displayed
    When user clicks logout icon
    then login page is displayed


