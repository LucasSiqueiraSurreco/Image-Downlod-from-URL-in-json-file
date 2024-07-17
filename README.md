# Image Download Script

---

## Image Download Script

This Python script downloads images from URLs specified in a JSON file. It uses the `requests` library to make HTTP requests and save the images locally.

### How to Use

1. **Setup Environment**
   - Make sure you have Python installed on your system.
   - Install dependencies using `pip install -r requirements.txt`.

2. **Configure JSON File**
   - Edit the `imagens.json` file to include the URLs of the images you want to download. The format should be as shown in the example below:

   ```json
   {
     "products": [
       {
         "imgUrl": "https://example.com/image1.jpg"
       },
       {
         "imgUrl": "https://example.com/image2.jpg"
       }
     ]
   }

3.Run the Script

Execute the script using python download_images.py.
The script will download each image listed in the JSON to the imagens_downloads folder.


4.Notes

The script checks if the image already exists before attempting to download it again, preventing accidental overwrite.
Detailed status messages are displayed during the download process.
Requirements
Python 3.x
requests library (pip install requests)
