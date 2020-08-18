*** Settings ***
Library  RequestsLibrary
Library  Collections


*** Test Cases ***
Get Person 3 From SwApi
    [Documentation]  Getting People in Star Wars
    create session  get_star_wars  https://swapi.dev/api  verify=True
    ${response} =  get request  get_star_wars  people/3/
    should be equal as strings  ${response.status_code}  200


Get Person 5 From SwApi
    [Documentation]  Getting People in Star Wars
    create session  get_star_wars  https://swapi.dev/api  verify=True
    ${response} =  get request  get_star_wars  people/5/
    should be equal as strings  ${response.status_code}  200
 