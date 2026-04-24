from sp_api.base import Client, sp_endpoint
from sp_api.base.helpers import create_md5
import urllib.parse
import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def remove_conflicting_param(url, param_to_remove):
        """
        Remove the specified query parameter from the URL to attempt to resolve the conflict.
        """
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        if param_to_remove in query_params:
            query_params.pop(param_to_remove)

        # Rebuild the URL without the conflicting parameter
        new_query = urlencode(query_params, doseq=True)
        return urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query, parsed_url.fragment))


class Upload(Client):

    @sp_endpoint('/uploads/2020-11-01/uploadDestinations/{}', method='POST')
    def upload_document(self, resource, file, content_type='application/pdf', **kwargs):
        """
        Upload a document (e.g., PDF).
        """
        md5 = urllib.parse.quote(create_md5(file))
        kwargs.update({
            'contentMD5': md5,
            'contentType': kwargs.pop('contentType', content_type),
            'marketplaceIds': self.marketplace_id
        })
        return self._request(kwargs.pop('path').format(resource), params=kwargs)



    @sp_endpoint('/uploads/2020-11-01/uploadDestinations/{}', method='POST')
    def upload_image(self, resource, image_file, content_type='image/jpeg', **kwargs):
        """
        Upload an image (e.g., JPEG).
        """
        try:
            # Generate MD5 hash for the image file
            md5 = urllib.parse.quote(create_md5(image_file))
            kwargs.update({
                'contentMD5': md5,
                'contentType': kwargs.pop('contentType', content_type),
                'marketplaceIds': self.marketplace_id
            })

            # Step 1: Get the upload destination (presigned URL)
            upload_response = self._request(kwargs.pop('path').format(resource), params=kwargs)

            # Use the payload method to access the actual data
            #upload_destination = upload_response.payload['uploadDestinationId']
            #upload_url = upload_destination['url']
            upload_url = upload_response.payload['url']
            upload_destination_id = upload_response.payload['uploadDestinationId']

            print(f"Upload_url = {upload_url}")

            #upload_url = remove_conflicting_param(upload_url, 'policy')
            # Step 2: Upload the image to the presigned URL using a PUT request
            headers = {
                'Content-Type': content_type
            }

            # Make sure the URL is not modified; upload it as it is.
            #image_file="/Users/wangmingye/Downloads/test2.jpeg"
            with open(image_file, 'rb') as img:
                response = requests.put(upload_url, data=img, headers=headers)

                # Check if the upload was successful
                if response.status_code == 200:
                    print("Image uploaded successfully.")
                    return True
                else:
                    print(f"Error uploading image: {response.status_code}, {response.text}")
                    return False
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

