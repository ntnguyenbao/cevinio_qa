*** Settings ***
Documentation   Suite description
Library         Selenium2Library
Library         keywords.home.homeKeywords
Library         ../lib/browser_factory.py
Library         lib.dataReader.DataReader
Library         keywords.searchResult.searchResultKeywords
Library         keywords.cityDetail.cityDetailKeywords
Test Setup      Initialize
Test Teardown   Tear Down

*** Variables ***
${expectedFile}     ../Data/search_wearther_in_your_city.xlsx

*** Keywords ***
Initialize
    ${driver}=  Get Browser     ${browser}  ${headless}
    Set Suite Variable  ${driver}

Tear Down
    Run Keyword If Test Failed  capture page screenshot
    close all browsers

*** Test Cases ***
Func-001
    [Documentation]     Validate searching weather by city name via Web UI
    [Tags]  Functional

    Access Home Page    ${driver}
    ${cityData}     Read sheet expected_result from exel file ${expectedFile}
    ${randomCity}   Select random city from ${cityData}
    Search city     ${randomCity}
    ${expectedResult}  find records which have city is ${randomCity} in ${cityData}
    Search Result page is loaded successfully  ${driver}   timeout=10
    Actual result should be same ${expectedResult}
    Click a random result link
    City Detail page is loaded successfully     ${driver}
    Detail of ${randomCity} is displayed

Func-002
    [Documentation]     Validate searching weather by incorrect city name or country code via Web UI home page
    [Tags]  Functional

    Access Home Page    ${driver}
    search random string
    Search Result page is loaded successfully  ${driver}   timeout=10
    Warning message "Not found" is displayed

Usability-001
    [Documentation]     Validate visibility of search field in case browser windows is changed
    [Tags]  Usability

    Access Home Page    ${driver}
    Change browser window size height: 1000 width: 700
    extend home menu
    ${cityData}     Read sheet expected_result from exel file ${expectedFile}
    ${randomCity}   Select random city from ${cityData}
    Search city     ${randomCity}
    ${expectedResult}  find records which have city is ${randomCity} in ${cityData}
    Search Result page is loaded successfully  ${driver}   timeout=10
    Actual result should be same ${expectedResult}
    Click a random result link
    City Detail page is loaded successfully     ${driver}
    Detail of ${randomCity} is displayed
