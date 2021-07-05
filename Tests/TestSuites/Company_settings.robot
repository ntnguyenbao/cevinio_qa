*** Settings ***
Documentation    This test suites contains test scenarios for Companny settings feature
Library     Selenium2Library
Resource    Tests/Keywords/common.robot
Resource    Tests/Keywords/Managment/CompanySettings/Permissions/ManageUsers.robot
#Library     Resource/cockpit/cockpitActions.py
#Library     Resource/Managment/CompanySettings/CompanySettingsActions.py
#Library     Resource/Managment/CompanySettings/Permissions/ManageUsers/ManageUsersActions.py
#Library     Resource/Managment/CompanySettings/Permissions/ManageUsers/CreateUserActions.py
#Library     Resource/Managment/CompanySettings/Permissions/ManageUsers/EditUserRolesAndRightsActions.py

Test Teardown   Teardown

*** Test Cases ***
New User
    [Tags]  Manage Users
    Given user access T-BLOX by dev/dev
    ${userInfo}    Create Dictionary   Name=test2    Email address=test2@test.com  FTE Percentage=100    Costcenter=General    Username=test2    Password=Test123456
    When user adds a new user   ${userInfo}
#    Then a notice message is displayed "The new user was added sucessfully."
#    and Role Assignment page is displayed
    When user logout
    and user login by test2/Test123456
    then then cockpit page is displayed
    capture page screenshot



*** Keywords ***
Teardown
    Run keyword if test failed  capture page screenshot
    close all browsers