*** Settings ***
Documentation   Suite description
Library         Selenium2Library
Library         keywords.home.homeKeywords
Library         ../lib/browser_factory.py
Library         lib.dataReader.DataReader
Library         keywords.searchResult.searchResultKeywords
Test Setup      Initialize
Test Teardown   Tear Down

*** Variables ***
${Browser}  Chrome
${expectedFile}     ../Data/search_wearther_in_your_city.xlsx

*** Keywords ***
Initialize
    ${driver}=  Get Browser     ${Browser}
    Set Suite Variable  ${driver}

Tear Down
    Run Keyword If Test Failed  keywords.home.homeKeywords.take screenshot
    close all browsers

*** Test Cases ***
Func-001
    Access Home Page    ${driver}
    ${cityData}     Read sheet expected_result from exel file ${expectedFile}
#    ${randomCity}   Select random city from ${cityData}
    ${randomCity}=  set variable    ho chi minh
    Search city     ${randomCity}
    ${expectedResult}  find records which have city is ${randomCity} in ${cityData}
    Search Result page is loaded successfully  ${driver}   timeout=10
    Actual result should be same ${expectedResult}
