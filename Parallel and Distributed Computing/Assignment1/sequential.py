import os
import requests
from PIL import Image
import time
from requests.exceptions import RequestException


def read_image_urls(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def download_image(url, download_folder, index, max_retries=3, retry_delay=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url.strip())
            response.raise_for_status()  # Raise an exception for HTTP errors
            file_name = f"image_{index}.jpg"
            with open(os.path.join(download_folder, file_name), 'wb') as file:
                file.write(response.content)
            return  # Exit the function if download is successful
        except (RequestException, IOError) as e:
            print(f"Error downloading {url}: {e}")
            retries += 1
            if retries < max_retries:
                print(f"Retrying ({retries}/{max_retries})...")
                time.sleep(retry_delay)
            else:
                print(f"Max retries ({max_retries}) exceeded. Skipping {url}")


def download_images(image_urls, download_folder):
    os.makedirs(download_folder, exist_ok=True)
    for index, url in enumerate(image_urls, start=1):
        download_image(url, download_folder, index)


def resize_images(image_folder, output_folder, size=(256, 256)):
    os.makedirs(output_folder, exist_ok=True)
    for file_name in os.listdir(image_folder):
        with Image.open(os.path.join(image_folder, file_name)) as img:
            img_resized = img.resize(size)
            img_resized.save(os.path.join(output_folder, file_name))


def apply_grayscale_filter(image_folder):
    for file_name in os.listdir(image_folder):
        with Image.open(os.path.join(image_folder, file_name)) as img:
            img_grayscale = img.convert('L')
            img_grayscale.save(os.path.join(image_folder, file_name))


def generate_report(image_folder, processing_times):
    num_images = len(os.listdir(image_folder))
    avg_time_per_image = processing_times / num_images

    print("\nSequential Image Processing Report\n")
    print(f"Number of images processed: {num_images}")
    print(
        f"Average processing time per image: {avg_time_per_image:.2f} seconds")
    print(f"Total execution time: {processing_times:.2f} seconds\n")


if __name__ == "__main__":
    image_urls = read_image_urls("ImageUrls.txt")
    download_folder = "downloaded_images"
    resize_folder = "resized_images"

    start_time = time.time()
    download_images(image_urls, download_folder)
    resize_images(download_folder, resize_folder)
    apply_grayscale_filter(resize_folder)
    end_time = time.time()

    processing_times = end_time - start_time

    # Step 5: Generate report
    generate_report(resize_folder, processing_times)
