import os
import requests
from PIL import Image
import time
import multiprocessing


def read_image_urls(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def download_image(url, download_folder, index, max_retries=4, retry_delay=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url.strip())
            response.raise_for_status()  # Raise an exception for HTTP errors
            file_name = f"image_{index}.jpg"
            with open(os.path.join(download_folder, file_name), 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {url}")
            return  # Exit the function if download is successful
        except (requests.RequestException, IOError) as e:
            print(f"Error downloading {url}: {e}")
            retries += 1
            if retries < max_retries:
                print(f"Retrying ({retries}/{max_retries})...")
                time.sleep(retry_delay)
            else:
                print(f"Max retries ({max_retries}) exceeded. Skipping {url}")


def download_images(image_urls, download_folder):
    os.makedirs(download_folder, exist_ok=True)
    with multiprocessing.Pool() as pool:
        pool.starmap(download_image, [
                     (url, download_folder, index + 1) for index, url in enumerate(image_urls)])


def resize_image(image_path, output_folder, size=(256, 256)):
    img = Image.open(image_path)
    img_resized = img.resize(size)
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    img_resized.save(output_path)
    return output_path


def resize_images(image_folder, output_folder, size=(256, 256)):
    os.makedirs(output_folder, exist_ok=True)
    image_paths = [os.path.join(image_folder, file_name)
                   for file_name in os.listdir(image_folder)]
    with multiprocessing.Pool() as pool:
        resized_image_paths = pool.starmap(
            resize_image, [(path, output_folder, size) for path in image_paths])
    return resized_image_paths


def apply_grayscale_filter(image_path):
    img = Image.open(image_path)
    img_grayscale = img.convert('L')
    img_grayscale.save(image_path)


def apply_grayscale_filters(image_paths):
    with multiprocessing.Pool() as pool:
        pool.map(apply_grayscale_filter, image_paths)


def generate_report(image_folder, processing_times):
    num_images = len(os.listdir(image_folder))
    avg_time_per_image = sum(processing_times) / len(processing_times)
    print(f"Number of images processed: {num_images}")
    print(
        f"Average processing time per image: {avg_time_per_image:.2f} seconds")


if __name__ == "__main__":
    start_time = time.time()

    image_urls = read_image_urls("ImageUrls.txt")
    print(image_urls)
    download_folder = "downloaded_images"
    resize_folder = "resized_images"

    # Step 1: Download images
    start_download_time = time.time()
    download_images(image_urls, download_folder)
    end_download_time = time.time()

    # Step 2: Resize images
    start_resize_time = time.time()
    resized_image_paths = resize_images(download_folder, resize_folder)
    end_resize_time = time.time()

    # Step 3: Apply grayscale filter
    start_grayscale_time = time.time()
    apply_grayscale_filters(resized_image_paths)
    end_grayscale_time = time.time()

    end_time = time.time()
    download_time = end_download_time - start_download_time
    resize_time = end_resize_time - start_resize_time
    grayscale_time = end_grayscale_time - start_grayscale_time

    processing_times = [download_time, resize_time, grayscale_time]

    # Generate report
    generate_report(resize_folder, processing_times)
