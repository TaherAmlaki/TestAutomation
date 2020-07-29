*** Settings ***
Library  RequestsLibrary
Library  ./Utils/manageDB.py
Library  ./Queries/TestCaseQueries.py
Library  ./Queries/PeopleQueries.py
Library  Collections
Resource  ./Utils/TestSetupAndTeardown.resource

Suite Setup  manageDB.create_all_tables
Test Setup   TestSetupAndTeardown.Test Setup For DB  
Test Teardown  TestSetupAndTeardown.Test Teardown For DB 


*** Test Cases ***
Get People From SwApi
    [Documentation]  Getting Starwars films people
    create session  get_star_wars  https://swapi.dev/api  verify=True
    ${response} =  get request  get_star_wars  people/3/
    should be equal as strings  ${response.status_code}  200
    ${name} =  get from dictionary  ${response.json()}  name
    PeopleQueries.add_person  test_id=${test_id}  name=${name}
