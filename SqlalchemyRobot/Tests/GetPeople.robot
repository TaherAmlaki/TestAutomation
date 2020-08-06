*** Settings ***
Library  RequestsLibrary
Library  Collections
Library  ./db/create_all_tables.py
Resource  ./Utils/TestSetupAndTeardown.resource
Resource  ./Utils/PeopleHelper.resource 

Suite Setup  create_all_tables
Test Setup   TestSetupAndTeardown.Test Setup For DB  
Test Teardown  TestSetupAndTeardown.Test Teardown For DB 


*** Test Cases ***
Get Person 3 From SwApi
    [Documentation]  Getting Starwars films people
    create session  get_star_wars  https://swapi.dev/api  verify=True
    ${response} =  get request  get_star_wars  people/3/
    should be equal as strings  ${response.status_code}  200
    log to console  test_id is ${test_id}
    ${name} =  get from dictionary  ${response.json()}  name
    Save New Person To DB  ${name}  ${test_id}


Get Person 5 From SwApi
    [Documentation]  Getting Starwars films people
    create session  get_star_wars  https://swapi.dev/api  verify=True
    ${response} =  get request  get_star_wars  people/5/
    should be equal as strings  ${response.status_code}  200
    log to console  test_id is ${test_id}
    ${name} =  get from dictionary  ${response.json()}  name
    Save New Person To DB  ${name}  ${test_id}
    
