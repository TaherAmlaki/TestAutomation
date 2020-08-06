*** Settings ***
Library  Models.TestCaseModel.TestCase  WITH NAME  TestCase
Library  db.sessionHelper  WITH NAME  sess_helper


*** Keywords ***
Test Setup For DB
    ${session}  ${engine} =  sess_helper.create_new_session
    set test variable  ${db_session}  ${session}

    ${test} =  get library instance  TestCase
    ${test.test_name} =  set variable  ${TEST NAME}
    ${test.suite_name} =  set variable  ${SUITE NAME}
    ${test.status} =  set variable  started 
    TestCase.save  ${db_session}
    set test variable  ${test_id}  ${test.test_id}


Test Teardown For DB 
    ${test} =  TestCase.find_by_test_id  test_id=${test_id}  session=${db_session}
    ${test.status} =  set variable  ${TEST STATUS}
    log to console  ${test}
    TestCase.update  ${db_session}
    sess_helper.close_session  ${db_session}
