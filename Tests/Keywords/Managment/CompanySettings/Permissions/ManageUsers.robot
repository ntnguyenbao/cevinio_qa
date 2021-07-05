*** Settings ***
Library     Resource/Managment/CompanySettings/CompanySettingsActions.py
Library     Resource/Managment/CompanySettings/Permissions/ManageUsers/ManageUsersActions.py
Library     Resource/Managment/CompanySettings/Permissions/ManageUsers/CreateUserActions.py
Library     Resource/Managment/CompanySettings/Permissions/ManageUsers/EditUserRolesAndRightsActions.py

*** Keywords ***
User adds a new user
    [Arguments]     ${userInfo}
    When user selects module Management/Company Settings from Cockpit page
    Then Company Settings page is displayed
    When user selects Permissions/Manage users from menu
    Then Manage Users page is displayed
    When user clicks Add User link
    Then Create User form is displayed
    When user inputs ${userInfo} into form
    and click Submit button
#    Then a notice message is displayed "The new user was added sucessfully."
#    and Role Assignment page is displayed


