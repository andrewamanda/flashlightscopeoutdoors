import requests
from sp_api.api import AplusContent, Upload
from sp_api.base import SellingApiException
from ecomstore.settings import AMZN_SP_REFRESH_TOKEN,AMZN_SP_LWA_APP_ID,AMZN_SP_LWA_CLIENT_SECRET
from sp_api.base import Marketplaces, SellingApiException, Credentials
from io import BytesIO
from ecomstore.utils.images import *
from ecomstore.catalog.models import AMAZON_RESTRICTED_KEYWORDS

# Replace these with your actual credentials
credentials = dict(
    refresh_token=AMZN_SP_REFRESH_TOKEN,
    lwa_app_id=AMZN_SP_LWA_APP_ID,
    lwa_client_secret=AMZN_SP_LWA_CLIENT_SECRET,
)
# Step 1: Download image from external URL
def download_image_from_url_inmemory(image_url):
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Error downloading image: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

import requests
import io
from PIL import Image

def download_image_to_memory(image_url, width=970, height=600):
    """
    Downloads an image from the given URL and stores it in memory.
    If the image is not in JPEG format, it converts the image to JPEG format before returning.
    The image is resized to the specified width, and if necessary, cropped to the specified height centered around the middle.
    """
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        # Load image data into memory (BytesIO)
        image_data = io.BytesIO(response.content)
        image_data.seek(0)  # Reset pointer to the beginning of the file-like object

        # Open the image using PIL
        with Image.open(image_data) as img:
            # Convert to RGB if not in JPEG format (JPEG doesn't support alpha channel)
            if img.format != 'JPEG':
                img = img.convert('RGB')

            # Resize the image to fit the target width, maintaining the aspect ratio
            original_width, original_height = img.size
            new_height = int(original_height * (width / original_width))  # Calculate the new height based on the aspect ratio
            img = img.resize((width, new_height), Image.ANTIALIAS)  # Resize image while maintaining aspect ratio

            # If the resized image is taller than the target height, crop it centered
            if new_height > height:
                top = (new_height - height) // 2
                bottom = top + height
                img = img.crop((0, top, width, bottom))  # Crop the height to fit the target

            # Save the resized and cropped image as JPEG into a new BytesIO object
            jpeg_image_data = io.BytesIO()
            img.save(jpeg_image_data, format='JPEG')
            jpeg_image_data.seek(0)  # Reset pointer

            print(f"Downloaded, resized, and cropped image from {image_url} to {width}x{height}")
            return jpeg_image_data
    else:
        raise Exception(f"Failed to download image from {image_url}. Status code: {response.status_code}")



import requests
import os
import tempfile

def download_image_from_url(image_url):
    try:
        # Get the image data from the URL
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            print("Image downloaded successfully")

            # Create a temporary file in the current working directory
            temp_dir = os.getcwd()  # Get the current working directory
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg", dir=temp_dir)

            # Write the image content to the temporary file
            with open(temp_file.name, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            # Return the full path of the temporary file
            return convert_to_jpeg(temp_file.name)
        else:
            print(f"Error downloading image: {response.status_code}")
            return None
    except Exception as e:
        raise Exception(f"Failed to download image from {image_url}. {str(e)}")

import requests
from urllib.parse import urlparse, parse_qs

def extract_data_from_url(dynamic_url):
    """
    Parses the dynamic URL returned by Amazon and constructs the multipart form data
    for the file upload.

    Args:
    - dynamic_url (str): The URL returned from Amazon containing query parameters.

    Returns:
    - base_url (str): The base URL to make the POST request.
    - data (dict): A dictionary containing the form data for the POST request.
    """
    # Parse the URL to get the base URL and the query parameters
    parsed_url = urlparse(dynamic_url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"  # Base URL without query params
    query_params = parse_qs(parsed_url.query)  # Dictionary of query parameters

    # Convert lists to single values (because parse_qs returns lists)
    for key in query_params:
        query_params[key] = query_params[key][0]

    # Construct the multipart form data from query parameters
    data = {
        'key': query_params['key'],
        'acl': query_params['acl'],
        'policy': query_params['policy'],
        'x-amz-credential': query_params['x-amz-credential'],
        'x-amz-algorithm': query_params['x-amz-algorithm'],
        'x-amz-date': query_params['x-amz-date'],
        'x-amz-signature': query_params['x-amz-signature'],
        'x-amz-meta-owner': query_params['x-amz-meta-owner']
    }

    return base_url, data


import requests
from sp_api.api import Upload
from sp_api.base.marketplaces import Marketplaces

def upload_image_to_amazon(image_data, marketplace_id):
    try:
        # Initialize the Upload API with credentials
        uploads_api = Upload(credentials=credentials, marketplace=Marketplaces.US)

        # Step 1: Request the upload destination from Amazon
        response = uploads_api.upload_document(
            resource="aplus/2020-11-01/contentDocuments",
            file=image_data,
            content_type="image/jpeg"
        )

        # Get the upload URL and destination ID from Amazon's response
        upload_url = response.payload['url']
        upload_destination_id = response.payload['uploadDestinationId']
        print(f"Upload URL: {upload_url}, Upload Destination ID: {upload_destination_id}")

        # Step 2: Prepare the headers for uploading the image to Amazon's server
        headers = {
            'Content-Type': 'image/jpeg',  # Use JPEG format as image is converted already
            'enctype': 'multipart/form-data'
        }

        # Step 3: Extract the base URL and any form fields required by Amazon (if necessary)
        # In some cases, Amazon's API may return form fields that need to be sent along with the file.
        base_url, data = extract_data_from_url(upload_url)

        # Step 4: Use the in-memory image file (BytesIO object) to send the image data
        files = {
            'file': ('image.jpg', image_data, 'image/jpeg')  # Provide filename, data, and content type
        }

        # Step 5: Perform the POST request to upload the image to Amazon's server
        response = requests.post(base_url, files=files, data=data)

        # Step 6: Check the response from the server
        if response.status_code == 204:
            print("File uploaded successfully!")
            return upload_destination_id
        else:
            raise Exception(f"Failed to upload file. Status code: {response.status_code}, Response: {response.text}")

        # Close the in-memory file
        image_data.close()

    except SellingApiException as e:
        print(f"Error: {str(e)}")
        raise Exception(f"Failed to upload image to {str(e)}")


import re

def strip_html_tags(text):
    """
    Strips HTML tags from the provided text.

    :param text: String that may contain HTML.
    :return: Clean text without HTML tags.
    """
    # Use a regular expression to remove HTML tags
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text

import html

def escape_html_tags(text):
    """
    Escapes HTML tags from the provided text so that they are treated as literal text.

    :param text: String that may contain HTML.
    :return: Text with HTML tags escaped.
    """
    # Escape HTML special characters
    return html.escape(text)

from bs4 import BeautifulSoup

def clean_html_for_amazon(html_content):
    """
    Cleans the provided HTML content, replacing <strong> with <b> and <p> with <br>,
    and keeping only allowed tags for Amazon product descriptions.
    """
    # Define the allowed tags, where <b> and <br> are preferred
    allowed_tags = ['b', 'br', 'i', 'ul', 'li']

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Replace <strong> with <b>
    for strong_tag in soup.find_all('strong'):
        strong_tag.name = 'b'

    # Replace <p> with <br>
    for p_tag in soup.find_all('p'):
        # Replace <p> with <br> and also append a <br> at the end of the text to preserve line breaks
        p_tag.insert_after(soup.new_tag('br'))
        p_tag.unwrap()  # Unwrap to remove the <p> but keep the content

    # Remove all other tags not in the allowed list
    for tag in soup.find_all(True):  # True finds all tags
        if tag.name not in allowed_tags:
            tag.unwrap()  # Removes the tag but keeps its content

    # Return the cleaned HTML
    return str(soup)

from bs4 import BeautifulSoup

# Define the character limit
CHARACTER_LIMIT = 6000

def parse_html_to_json(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    text_list = []
    total_char_count = 0  # To track the total character count

    # Function to add text to textList
    def add_to_text_list(text, decorator_set):
        nonlocal total_char_count
        if text:
            if total_char_count + len(text) > CHARACTER_LIMIT:
                # Calculate how much of the text can be added before reaching the limit
                remaining_chars = CHARACTER_LIMIT - total_char_count
                if remaining_chars > 0:
                    truncated_text = text[:remaining_chars]  # Truncate the text
                    entry = {
                        "value": truncated_text,
                        "decoratorSet": decorator_set
                    }
                    text_list.append(entry)
                    total_char_count += len(truncated_text)  # Update character count with truncated length
                return False  # Stop further processing as the limit has been reached
            else:
                entry = {
                    "value": text,
                    "decoratorSet": decorator_set
                }
                text_list.append(entry)
                total_char_count += len(text)  # Update the total character count
        else:
            text_list.append({
                "value": "",
                "decoratorSet": []
            })
        return True

    # Function to process paragraphs and bold text
    def process_paragraph(tag, is_bold=False):
        text = tag.get_text(strip=True)
        if is_bold:
            decorator_set = [{
                "type": "STYLE_BOLD",
                "offset": 0,
                "length": len(text),
                "depth": 0
            }]
        else:
            decorator_set = []

        # Try adding the paragraph and check if we exceed the character limit
        return add_to_text_list(text, decorator_set)

    # Function to process unordered list and calculate offsets relative to the start of the list
    def process_list(ul_tag):
        list_items = ul_tag.find_all('li')
        combined_text = ''
        decorators = []
        local_offset = 0  # Reset the local offset for each list

        for li in list_items:
            li_text = li.get_text(strip=True)

            if combined_text:
                combined_text += li_text
            else:
                combined_text = li_text

            # Add a LIST_ITEM decorator for each list item
            decorators.append({
                "type": "LIST_ITEM",
                "offset": local_offset,
                "length": len(li_text),
                "depth": 0
            })

            # Update the local offset for the next list item
            local_offset += len(li_text)

        # Add a LIST_UNORDERED decorator for the whole list
        decorators.append({
            "type": "LIST_UNORDERED",
            "offset": 0,
            "length": local_offset,
            "depth": 0
        })

        # Add the entire list as one entry in the text list
        add_to_text_list(combined_text, decorators)  # List items are not truncated but count towards the 6000 character limit

    # Iterate over all tags in the HTML
    for tag in soup.find_all(['p', 'ul', 'li']):
        if total_char_count >= CHARACTER_LIMIT:
            break  # Stop processing further content if the limit is reached

        if tag.name == 'p':
            # Check if the paragraph has bold text
            if tag.find('strong'):
                if not process_paragraph(tag, is_bold=True):
                    break  # Stop processing further paragraphs if the limit is exceeded
            else:
                if not process_paragraph(tag):
                    break  # Stop processing further paragraphs if the limit is exceeded
        elif tag.name == 'ul':
            process_list(tag)  # Lists are processed, but their character count still contributes to the total

    return {
        "textList": text_list
    }




import re
def remove_restricted_keywords(text, restricted_keywords):
    """
    Remove all occurrences of restricted keywords from the text.

    :param text: The input text to check and clean.
    :param restricted_keywords: A list of restricted keywords to remove from the text.
    :return: The cleaned text with restricted keywords removed.
    """
    # Create a regular expression pattern that matches any of the restricted keywords
    #pattern = r'\b(?:' + '|'.join(map(re.escape, restricted_keywords)) + r')\b'
    pattern = r'(?:' + '|'.join(map(re.escape, restricted_keywords)) + r')'  #partial match
    # Substitute restricted keywords with an empty string
    cleaned_text = re.sub(pattern, '', text, flags=re.IGNORECASE)

    # Remove extra spaces after cleaning
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text

def replace_all_empty_value(content_document):
    """
    Replace all instances of empty 'value' fields with '-----'.
    """
    # Navigate through the content document's structure
    for module in content_document.get("contentModuleList", []):
        # Ensure you're modifying the standard product description's body
        if "standardProductDescription" in module:
            text_list = module["standardProductDescription"]["body"].get("textList", [])

            # Iterate over the textList and replace empty values
            for text_item in text_list:
                if text_item.get("value") == "":
                    text_item["value"] = "      "  # Replace empty value with 5 hyphens

    return content_document




def create_content_document(name, highlights, descriptions, alts, body_text, image_upload_destinations):
    # Ensure we have exactly 4 image destinations
    if len(image_upload_destinations) < 4:
        raise ValueError("At least 4 image upload destinations are required.")

    # Strip HTML tags from the body_text
    #clean_body_text = strip_html_tags(body_text)

    # Strip HTML tags from the body_text
    #print(f"original HTML_CONTENT = {body_text}")
    #clean_body_text = clean_html_for_amazon(body_text)
    #print(f"cleaned HTML_CONTENT = {clean_body_text}")
    clean_body_text = remove_restricted_keywords(body_text, AMAZON_RESTRICTED_KEYWORDS)
    # Call the function
    json_output = parse_html_to_json(clean_body_text)
    file_path = f"FullDescription.json"

    # Write the payload to the file
    import json
    with open(file_path, 'w') as file:
        # If payload is a dictionary, write it as JSON
        json.dump(json_output, file, indent=4)

    print(f"Text Json has been written to {file_path}")


    # Define the base structure for the content document
    content_document = {
        "name": name,
        "contentType": "EBC",  # Example content type, this might vary depending on your needs
        "locale": "en-US",
        "contentModuleList": []
    }

    # Step 1: Add StandardProductDescriptionModule with the passed body text
    product_description_module = {
        "contentModuleType": "STANDARD_PRODUCT_DESCRIPTION",
        "standardProductDescription": {
            "body": {
                    "textList": []
                }
        }
    }
    product_description_module['standardProductDescription']['body'] = json_output
    content_document["contentModuleList"].append(product_description_module)
    content_document = replace_all_empty_value(content_document)

    #print(json.dumps(content_document, indent=4))

    # Step 2: Add 4 StandardImageTextOverlayModules with images and descriptions
    for i in range(4):
        standard_header_image_module = {
            "contentModuleType": "STANDARD_HEADER_IMAGE_TEXT",
            "standardHeaderImageText": {
                "block": {
                    "headline": {
                        "value": f"{highlights[i]}"  # Dynamically set the headline
                    },
                    "body": {
                        "textList": [{"value": f"{descriptions[i]}."}]
                    },
                    "image": {
                        "uploadDestinationId": image_upload_destinations[i],  # Assign image destination dynamically
                        "imageCropSpecification": {
                            "size": {
                                "width": {"value": 970, "units": "pixels"},
                                "height": {"value": 600, "units": "pixels"}
                            },
                            "offset": {
                                "x": {"value": 0, "units": "pixels"},
                                "y": {"value": 0, "units": "pixels"},
                            }
                        },
                        "altText": f"{alts[i]}"  # Dynamic alt text
                    }
                }
            }
        }
        content_document["contentModuleList"].append(standard_header_image_module)

        """
        # Assuming content_document is your data structure that contains contentModuleList and textList

        # Access textList[1]
        try:
            text_value = content_document['contentModuleList'][0]['standardProductDescription']['body']['textList'][1]['value']

            # Print the content of textList[1]
            print(f"textList[1] value: {text_value}")

            # Calculate the size (length) of the content
            text_length = len(text_value)

            # Print the length
            print(f"Size of textList[1] value: {text_length}")

        except IndexError:
            print("textList[1] does not exist or is out of range")
        """


    return content_document



# Step 3: Create A+ Content Document with multiple StandardImageTextOverlayModules
def create_aplus_content_with_images(name, highlights, descriptions, alts, prod_desc, asins, marketplace_id, image_urls):
    try:
        aplus_content = AplusContent(credentials=credentials, marketplace=Marketplaces.US)

        # Step 1: Download and upload each image to Amazon
        image_upload_destinations = []
        for image_url in image_urls:
            #print(f"*****image_url = {image_url}")
            image_data = download_image_to_memory(image_url)
            if image_data:
                upload_destination_id = upload_image_to_amazon(image_data, Marketplaces.US.marketplace_id)
                if upload_destination_id:
                    image_upload_destinations.append(upload_destination_id)
            else:
                print(f"Skipping image from URL: {image_url}")

        if len(image_upload_destinations) != len(image_urls):
            return "Not all images were uploaded successfully. Aborting."

        # Step 2: Create A+ content document with the uploaded images

        content_document = create_content_document(name, highlights, descriptions, alts, prod_desc, image_upload_destinations)

        response = aplus_content.validate_content_document_asin_relations(
            marketplaceId=Marketplaces.US.marketplace_id,
            asinSet=asins,
            body= {"contentDocument": content_document}
        )
        print(f"Validation Content Document Response: {response}")

        # Step 3: Create the content document using the SP-API
        response = aplus_content.create_content_document(
            marketplaceId=Marketplaces.US.marketplace_id,
            body= {"contentDocument": content_document}
        )
        print(f"Create Content Document Response: {response}")
        # Get the contentReferenceKey from the response
        content_reference_key = response.payload['contentReferenceKey']

        # Step 4: Associate the ASIN with the created content document
        response = aplus_content.post_content_document_asin_relations(
            contentReferenceKey=content_reference_key,
            marketplaceId=Marketplaces.US.marketplace_id,
            body={
                "asinSet": asins
            }
        )
        print(f"Post Content Asin Relationship Response: {response}")
        response = aplus_content.post_content_document_approval_submission(
            contentReferenceKey=content_reference_key,
            marketplaceId=Marketplaces.US.marketplace_id,
        )
        return (f"Post_content_document_approval_submission: {response}")

    except SellingApiException as e:
        return (f"Error for {', '.join(asins)}: {str(e)}")
