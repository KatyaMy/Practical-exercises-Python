from faker import Faker

faker = Faker()
create_case = {
    "id": faker.random_number(2),
    "name": faker.text(8),
    "description": faker.sentence(6),
    "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
    "expected_result": "Ожидаемый результат",
    "priority": faker.random_element(elements=["низкий", "средний", "высокий"]),
}

case1 = {
    "id": 2,
    "name": "TC_001",
    "description": "Not open",
    "steps": [
        "Open page",
        "Click left button"
    ],
    "expected_result": "open block with information",
    "priority": "высокий"

}
case2 = {
    "id": 3,
    "name": "TC_002",
    "description": "Image not visible",
    "steps": [
        "Open page",
        "Check image"
    ],
    "expected_result": "Image damage",
    "priority": "средний"
}
