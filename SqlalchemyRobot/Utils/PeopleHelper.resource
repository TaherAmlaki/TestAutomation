*** Settings ***
Library  Models.PeopleModel.People  WITH NAME  People


*** Keywords ***
Save New Person To DB
    [Arguments]  ${name}  ${test_id}
    ${person} =  get library instance  People
    ${person.name} =  set variable  ${name}
    ${person.test_id} =  set variable  ${test_id}
    People.save  ${db_session}
