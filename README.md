# Backend_Integration_HubSpot_Automation_Assignment


This project implements a backend integration system that automates contact management workflows in HubSpot. 
It used the HubSpot API using Python.
It covers creating custom properties, adding new contacts, and updating existing contacts.

---

## 1. Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install hubspot-api-client
   pip install os
   pip install python-dotenv
   ```
3. Set your HubSpot API key as an environment variable:
   ```bash
   export HUBSPOT_API_KEY="your_api_key_here"
   ```

## 2. Methods
   ```createCustomProperties() ```  Method to create each custom property.<br>
   ```createContact() ``` Method to add a new contact with properties.<br>
   ```updateContactProperties()``` Method to update an existing contact’s properties.<br>

## 3. Running the Code
   Each action is defined as a separate method.
   In main(), uncomment the desired action and run the file.
   You can also run them together if needed.

## 4. References
[HubSpot API Docs](https://developers.hubspot.com/docs/reference/api/overview).<br>
[HubSpot Python SDK](https://github.com/HubSpot/hubspot-api-python).<br>
