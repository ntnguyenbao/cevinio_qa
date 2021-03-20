*** Settings ***
Documentation    Suite description
Library           Selenium2Library

*** Variables ***
${URL}  https://openweathermap.org/
${Browser}  Edge
${xpath}    //*[@id="q"]
*** Test Cases ***
Open browser
    [Tags]    DEBUG
    Open Browser    ${URL}  ${Browser}
    maximize browser window
    wait until element is visible   ${xpath}    30
    close all browsers

*** Test Cases ***
Open browser2
    [Tags]    DEBUG
    Open Browser    ${URL}  ${Browser}
    maximize browser window
    wait until element is visible   ${xpath}    30
    close all browsers
