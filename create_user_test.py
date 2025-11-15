import sender_stand_request
import data

# this function changes the values in the "firstName" parameter
def get_user_body(first_name):
    # the dictionary that contains the request body is copied from the file "data" to preserve the original dictionary data
    current_body = data.user_body.copy()
    # change the value of the firstName parameter
    current_body["firstName"] = first_name
    # return a new dictionary with the required firstName value
    return current_body

# Positive test function
def positive_assert(first_name):
    # the updated request body is saved in the variable user_body
    user_body = get_user_body(first_name)
    # the result of the request to create a new user is saved in the variable user_response
    user_response = sender_stand_request.post_new_user(user_body)
    # check if the status code is 201
    assert user_response.status_code == 201
    # check that the authToken field is in the response and contains a value
    assert user_response.json()["authToken"] != ""
    # the result of the request to get data from the "user_model" table is saved in the variable users_table_response
    users_table_response = sender_stand_request.get_users_table()
    # string that must be present in the response body
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    # check if the user exists and is unique
    assert users_table_response.text.count(str_user) == 1

# Negative test function
def negative_assert_symbol(first_name):
    # the updated request body is saved in the variable user_body
    user_body = get_user_body(first_name)
    # check if the variable "response" stores the result of the request
    response = sender_stand_request.post_new_user(user_body)
    # check if the response contains status code 400
    assert response.status_code == 400
    # check if the "code" attribute in the response body is 400
    assert response.json()["code"] == 400
    # DO NOT TRANSLATE THE STRING BELOW — IT MUST MATCH THE API RESPONSE EXACTLY
    assert response.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."

# Negative test function
# The response contains the following error message: "Not all required parameters have been sent"
def negative_assert_no_firstname(user_body):
    # save the result of calling the function in the variable "response"
    response = sender_stand_request.post_new_user(user_body)
    # check if the response contains status code 400
    assert response.status_code == 400
    # check if the "code" attribute in the response body is 400
    assert response.json()["code"] == 400
    # DO NOT TRANSLATE THIS STRING EITHER — MUST MATCH API RESPONSE
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

# Test 1 — Creating a new user
# The parameter "firstName" contains two characters
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

# Test 2 — Creating a new user
# The parameter "firstName" contains 15 characters
def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

# Test 3 — Error
# The parameter "firstName" contains one character
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

# Test 4 — Error
# The parameter "firstName" contains 16 characters
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

# Test 5 — Error
# The parameter "firstName" contains words with spaces
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

# Test 6 — Error
# The parameter "firstName" contains special characters
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

# Test 7 — Error
# The parameter "firstName" contains numbers
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")

# Test 8 — Error
# The request does not contain the "firstName" parameter
def test_create_user_no_first_name_get_error_response():
    # the dictionary with the request body is copied from the "data" file into user_body
    # otherwise the original data could be lost
    user_body = data.user_body.copy()
    # remove the "firstName" parameter from the request
    user_body.pop("firstName")
    # check the response
    negative_assert_no_firstname(user_body)

# Test 9 — Error
# The parameter "firstName" contains an empty string
def test_create_user_empty_first_name_get_error_response():
    # the updated request body is saved in user_body
    user_body = get_user_body("")
    # check the response
    negative_assert_no_firstname(user_body)

# Test 10 — Error
# The type of "firstName" is a number
def test_create_user_number_type_first_name_get_error_response():
    # the updated request body is saved in user_body
    user_body = get_user_body(12)
    # the request result is saved in response
    response = sender_stand_request.post_new_user(user_body)
    # check the response status code
    assert response.status_code == 400
