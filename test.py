import requests

BASE_URL = 'http://127.0.0.1:8000'

def create_configuration(country_code, data):
    response = requests.post(f'{BASE_URL}/create_configuration', json=data)
    print(f"Create Configuration Response ({country_code}):", response.json())
    return response

def get_configuration(country_code):
    response = requests.get(f'{BASE_URL}/get_configuration/{country_code}')
    print(f"Get Configuration Response ({country_code}):", response.json())
    return response

def update_configuration(country_code, data):
    response = requests.post(f'{BASE_URL}/update_configuration', json=data)
    print(f"Update Configuration Response ({country_code}):", response.json())
    return response

def delete_configuration(country_code):
    response = requests.delete(f'{BASE_URL}/delete_configuration?country_code={country_code}')
    print(f"Delete Configuration Response ({country_code}):", response.json())
    return response

# Example usage:
if __name__ == '__main__':
    # Example: Create configuration
    # create_response = create_configuration("JPN", {
    #     'country_code': 'JPN',
    #     'business_name': 'Example Inc.',
    #     'registration_number': '12345',
    #     'additional_details': 'Additional details about Example Inc.'
    # })

    # Example: Get configuration
    get_response = get_configuration("JPN")

    # Example: Update configuration
    update_response = update_configuration("JPN", {
        'country_code': 'JPN',
        'business_name': 'Updated Updated Business',
        'registration_number': '654321',
        'additional_details': 'Updated additional details'
    })

    # Example: Get configuration after update
    get_response_after_update = get_configuration("JPN")

    # Example: Delete configuration
    delete_response = delete_configuration("JPN")
