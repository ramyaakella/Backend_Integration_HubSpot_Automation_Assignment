from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInputForCreate
from hubspot.crm.contacts.exceptions import ApiException
from hubspot.crm.contacts import SimplePublicObjectInput
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("HUBSPOT_API_KEY")
# Use .env file to add the API Key

# New Properties
newPropertyCandidateExperience = {
                        "groupName": "contactinformation",
                        "name": "candidate_experience",
                        "label": "Candidate Experience",
                        "type": "number",
                        "fieldType": "number"
                }
    
newPropertyCandidateDoj = {
                        "groupName": "contactinformation",
                        "name": "candidate_date_of_joining",
                        "label": "Candidate Date of Joining",
                        "type": "date",
                        "fieldType": "date"
                }
    
newPropertyCandidateName = {
                        "groupName": "contactinformation",
                        "name": "candidate_name",
                        "label": "Candidate Name",
                        "type": "string",
                        "fieldType": "text"
                }
    
newPropertyCandidatePastCompany = {
                        "groupName": "contactinformation",
                        "name": "candidate_past_company",
                        "label": "Candidate Past Company",
                        "type": "string",
                        "fieldType": "text"
                }

# New contact properties
contactProperties = {
                    "email": "AbhisekK@hubspot.com",
                    "firstname": "Abhisek",
                    "lastname": "K",
                    "phone": "+91700999999",
                    "company": "HubSpot",
                    "website": "hubspot.com",
                    "lifecyclestage": "marketingqualifiedlead",
                    "favorite_food": "Oranges",
                    "candidate_experience": "5",
                    "candidate_date_of_joining": "1654473600000",
                    "candidate_name": "Abhisek",
                    "candidate_past_company": "Omega"
                }

# properties to updates 
updated_properties = {
                    "candidate_experience": "2",
                    "candidate_date_of_joining": "1654473600000",
                    "candidate_name": "Beta",
                    "candidate_past_company": "Gamma"
                }



# Method to create a new contact
def createContact(api_client, contactProperties):
    try:
        simple_public_object_input_for_create = SimplePublicObjectInputForCreate(
            properties=contactProperties
        )
        api_response = api_client.crm.contacts.basic_api.create(
            simple_public_object_input_for_create=simple_public_object_input_for_create
        )
    except ApiException as e:
        print("Exception when creating contact: %s\n" % e)


# Method to add a custom property to contacts
def createCustomProperties(api_client, newProperty):
    try:
        response = api_client.api_request(
            {
                "path": "/crm/v3/properties/contacts",
                "method": "POST",
                "body": newProperty
            }

        )
        pprint(response.json())
    except ApiException as e:
        print("Exception when adding custom contact properties: %s\n" % e)


# Method to update a contact's properties
def updateContactProperties(api_client, updated_properties, contact_id):
    try:
        simple_public_object_input = SimplePublicObjectInput(properties=updated_properties)

        updated_contact = api_client.crm.contacts.basic_api.update(
            contact_id=contact_id,
            simple_public_object_input=simple_public_object_input
        )
        print(f"Contact updated successfully")
    except Exception as e:
        print(f"Error updating contact: {e}")


# Main 
if __name__ == '__main__':

    # create API client
    api_client = HubSpot()
    api_client.access_token = api_key
    
    # Uncomment as necesary
    
    # createCustomProperties(api_client,newPropertyCandidateExperience)

    # createCustomProperties(api_client,newPropertyCandidateDoj)

    # createCustomProperties(api_client,newPropertyCandidateName)

    # createCustomProperties(api_client,newPropertyCandidatePastCompany)


    # createContact(api_client, contactProperties)
    # id = "your_contact_id" # Need to give an actual contact ID here
    # updateContactProperties(api_client, updated_properties, id)

