from lesson1.api_tests.case.pom.case import create_case
from lesson1.api_tests.case.models.case import Case
from lesson1.api_tests.case.data.case import create_case_dict


def test_create_case():
    # response = create_case_dict(Case(**create_case_dict).model_dump())
    response = create_case(json=create_case_dict)
    response.status_code_should_be_eq(200)
    response.json_should_be_eq(create_case_dict)



