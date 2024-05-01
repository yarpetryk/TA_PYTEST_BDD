Feature: Form example

  Scenario Outline: Apply the form
    Given go to webpage
    When select the gender
    When enter the name
    When enter the address
    When enter the zip_code
    When enter the city
    When enter the phone_number
    When enter the email
    When enter the birth_day
    When submit the form
    Then page should contain <text>

    Examples:
    | text                |
    | Thank you very much |

