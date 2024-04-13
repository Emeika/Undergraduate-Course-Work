import os
import requests
from PIL import Image
import time
from multiprocessing import Pool
from functools import partial


def read_image_urls(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def download_image(index, url, download_folder, max_retries=3, retry_delay=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url.strip())
            response.raise_for_status()  # Raise an exception for HTTP errors
            file_name = f"image_{index}.jpg"
            with open(os.path.join(download_folder, file_name), 'wb') as file:
                file.write(response.content)
            return url, True  # Return the URL and success status
        except (requests.RequestException, IOError) as e:
            print(f"Error downloading {url}: {e}")
            retries += 1
            if retries < max_retries:
                print(f"Retrying ({retries}/{max_retries})...")
                time.sleep(retry_delay)
            else:
                print(f"Max retries ({max_retries}) exceeded. Skipping {url}")
                return url, False  # Return the URL and failure status


def download_images(image_urls, download_folder, num_processes):
    os.makedirs(download_folder, exist_ok=True)
    with Pool(num_processes) as pool:
        download_partial = partial(
            download_image, download_folder=download_folder)
        results = pool.starmap(
            download_partial, enumerate(image_urls, start=1))
    success_urls = [result[0] for result in results if result[1]]
    return success_urls


def resize_image(file_name, image_folder, output_folder, size):
    try:
        with Image.open(os.path.join(image_folder, file_name)) as img:
            img_resized = img.resize(size)
            img_resized.save(os.path.join(output_folder, file_name))
        return True
    except Exception as e:
        print(f"Error resizing {file_name}: {e}")
        return False


def resize_images(image_folder, output_folder, num_processes, size=(256, 256)):
    os.makedirs(output_folder, exist_ok=True)
    with Pool(num_processes) as pool:
        resize_partial = partial(
            resize_image, output_folder=output_folder, size=size)
        results = pool.starmap(
            resize_partial, [(file_name, image_folder) for file_name in os.listdir(image_folder)])  # Pass both file_name and image_folder
    return results


def apply_grayscale_filter(file_name, image_folder):
    try:
        with Image.open(os.path.join(image_folder, file_name)) as img:
            img_grayscale = img.convert('L')
            img_grayscale.save(os.path.join(image_folder, file_name))
        return True
    except Exception as e:
        print(f"Error applying grayscale filter to {file_name}: {e}")
        return False


def apply_grayscale_filters(image_folder, num_processes):
    with Pool(num_processes) as pool:
        results = pool.map(partial(apply_grayscale_filter,
                           image_folder=image_folder), os.listdir(image_folder))
    return results


def generate_report(image_folder, processing_times):
    num_images = len(os.listdir(image_folder))
    avg_time_per_image = processing_times / num_images

    print(f"Number of images processed: {num_images}")
    print(
        f"Average processing time per image: {avg_time_per_image:.2f} seconds")
    print(f"Total execution time: {processing_times:.2f} seconds\n")


if __name__ == "__main__":
    image_urls = read_image_urls("ImageUrls.txt")
    download_folder = "downloaded_images"
    resize_folder = "resized_images"
    num_processes = 12

    start_time = time.time()
    success_urls = download_images(
        image_urls, download_folder, num_processes)

    resize_results = resize_images(
        download_folder, resize_folder, num_processes)

    grayscale_results = apply_grayscale_filters(
        resize_folder, num_processes)
    end_time = time.time()

    processing_times = end_time - start_time

    # Step 5: Generate report
    print("\nParallel Image Processing Report\n")
    print(f"Number of Processes: {num_processes}")
    generate_report(resize_folder, processing_times)
    # Sequential program execution time
    T_seq = 142.44

    # Parallel program execution time
    T_par = processing_times

    P = T_seq / (T_seq + (T_par))

    # Calculate Speedup using Amdahl's Law
    S = 1 / ((1 - P) + (P / (T_seq / T_par)))

    print(f"The speedup factor is {S:.2f}")
