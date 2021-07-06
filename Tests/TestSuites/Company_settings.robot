*** Settings ***
Documentation    This test suites contains test scenarios for Companny settings feature
Library     Selenium2Library
Resource    ../Keywords/common.robot
Resource    ../Keywords/Managment/CompanySettings/Permissions/ManageUsers.robot

Test Teardown   Teardown

*** Settings ***
Suite Setup

*** Test Cases ***
New User
    [Tags]  Manage Users
    Given user opens ${browser} and accesses T-BLOX by dev/dev
    ${userInfo}    Create Dictionary   Name=test3    Email address=test3@test.com  FTE Percentage=100    Costcenter=General    Username=test3    Password=Test123456
    When user adds a new user   ${userInfo}
    Then a notice message is displayed "The new user was added sucessfully."
    and Role Assignment page is displayed
    When user logout
    and user login by test2/Test123456
    then then cockpit page is displayed
    capture page screenshot



*** Keywords ***
Teardown
    Run keyword if test failed  capture page screenshot
    close all browsers