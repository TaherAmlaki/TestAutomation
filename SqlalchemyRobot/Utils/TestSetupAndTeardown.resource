*** Settings ***
Library  ../Queries/TestCaseQueries.py


*** Keywords ***
Test Setup For DB
    ${test_id} =  TestCaseQueries.add_test  suite_name=${SUITE NAME}  test_name=${TEST NAME}  status=started
    set suite variable  ${test_id}  ${test_id}

Test Teardown For DB 
    TestCaseQueries.update_test  test_id=${test_id}  status=${TEST STATUS}
