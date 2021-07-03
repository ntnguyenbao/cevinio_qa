*** Settings ***
Documentation    Suite description
Library         Selenium2Library    run_on_failure=Capture Page Screenshot
Library     ../Resource/commonKeywords.py
Library     ../Resource/login/loginKeywords.py
Library     ../Resource/cockpit/cockpitKeywords.py
Library     ../Resource/Managment/CompanySettings/CompanySettingsKeywords.py
Library     ../Resource/Managment/CompanySettings/Permissions/ManageUsers/ManageUsersKeywords.py
Library     ../Resource/Managment/CompanySettings/Permissions/ManageUsers/CreateUserKeywords.py
Library     ../Resource/Managment/CompanySettings/Permissions/ManageUsers/EditUserRolesAndRightsKeywords.py

Test Teardown   Teardown

*** Test Cases ***

New User
    [Tags]  DEBUG
    Given user accesses https://local.tblox.com by Chrome
    and login page is displayed
    and user login by dev/dev
    and cockpit page is displayed
    When user selects module Management/Company Settings from Cockpit page
    Then Company Settings page is displayed
    When user selects Permissions/Manage users from menu
    Then Manage Users page is displayed
    When user clicks Add User link
    Then Create User form is displayed
    ${userInfo}    Create Dictionary   Name=test7    Email address=test7@test.com  FTE Percentage=100    Costcenter=General    Username=test7    Password=Test123456
    When user inputs ${userInfo} into form
    and click Submit button
    Then a notice message is displayed "The new user was added sucessfully."
    and Role Assignment page is displayed


*** Keywords ***
Teardown
    Run keyword if test failed  capture page screenshot
    close all browsers