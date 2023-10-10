import requests
import io


def upload_to_S3(s3, media_urls, s3_bucket):
    try:
        for url in media_urls:
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url

            filename = url.split("/")[-1].split("?")[0]

            response = requests.get(url)
            if response.status_code == 200:
                s3.upload_fileobj(
                    io.BytesIO(response.content),
                    s3_bucket,
                    filename  # Use the filename as the key
                )
                print(f"Uploaded to S3: {filename}")

    except Exception as e:
        print(f"Error uploading to S3: {e}")
