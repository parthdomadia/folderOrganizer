import os
import pathlib
import shutil
import logging
from tqdm import tqdm


#extension list
image_extensions = [".jpg",".jpeg",".png",".bmp",".gif",".heif",".heic",".webp"]
video_extensions = [".webm",".mp4",".mov",".flv",".mpv",".mpeg",".mkv"]
audio_extensions = [".m4a",".flac",".mp3",".wav",".aac"]
doc_extensions = [".doc",".docx",".odt",".pdf",".xls",".xlsx",".ppt",".pptx",".txt",".csv"]
extra_extensions = ['.zip','.exe']


def get_files(folder_path):
    try:
        file_list = os.listdir(folder_path)
    except Exception as e :
        print(f" Something went wrong: {e}")
        logging.info(f"Error while tryin to get file list from source directory. Error: {e}")

    return file_list


# def categorize(file_list):
#     move_images = []
#     move_audio = []
#     move_videos = []
#     move_docs = []
#     move_extras = []
#     no_classification = []
#     for name in file_list:
#         extension = name.split('.')[1]
#         if extension in image_extensions:
#             move_images.append(name)
#         elif extension in audio_extensions:
#             move_audio.append(name)
#         elif extension in video_extensions:
#             move_videos.append(name)
#         elif extension in doc_extensions:
#             move_docs.append(name)
#         elif extension in extra_extensions:
#             move_extras.append(name)
#         else:
#             no_classification.append(name)
    

#     print(len(move_images), len(move_videos), len(move_audio), len(move_extras), len(no_classification))


def check_if_image(file, dest, source_dir):
    extension = pathlib.Path(file).suffix
    for image_extension in image_extensions:
        if extension == image_extension:
            move_file(dest, file, source_dir)
            logging.info(f"Moving image file: {file}")
        
def check_if_video(file,dest, source_dir):
    extension = pathlib.Path(file).suffix
    for video_extension in video_extensions:
        if extension == video_extension:
            move_file(dest, file, source_dir)
            logging.info(f"Moving video file: {file}")

def check_if_audio(file,dest, source_dir):
    extension = pathlib.Path(file).suffix
    for audio_extension in audio_extensions:
        if extension == audio_extension:
            move_file(dest, file, source_dir)
            logging.info(f"Moving audio file: {file}")

def check_if_doc(file,dest, source_dir):
    extension = pathlib.Path(file).suffix
    for doc_extension in doc_extensions:
        if extension == doc_extension:
            move_file(dest, file, source_dir)
            logging.info(f"Moving doc file: {file}")

def check_if_extra(file,dest, source_dir):
    extension = pathlib.Path(file).suffix
    for extra_extension in extra_extensions:
        if extension == extra_extension:
            move_file(dest, file, source_dir)
            logging.info(f"Moving extra file: {file}")

def move_file(dest, file, source_dir):
    source = source_dir + '/' + file
    try:
        shutil.move(source, dest)
    except Exception as e:
        print(f"Something went wrong while moving file: {e}")
        logging.info(f"Error while moving file. Error: {e}")
    





if __name__ == "__main__":
    print("Starting engines!")
    logging.info("Starting engines")
    # destination folders
    source_dir = 'C:/Users/parth/Downloads'
    dest_dir_image = 'C:/clutter/downloaded_images'
    dest_dir_audio = 'C:/clutter/downloaded_audio'
    dest_dir_video = 'C:/clutter/downloaded_videos'
    dest_dir_doc = 'C:/clutter/downloaded_docs'
    dest_dir_extra = 'C:/clutter/downloaded_extras'


    file_list = get_files(source_dir)
    for file in tqdm(file_list):
    
        check_if_image(file,dest_dir_image,source_dir)
        check_if_audio(file,dest_dir_audio,source_dir)
        check_if_doc(file,dest_dir_doc,source_dir)
        check_if_video(file,dest_dir_video,source_dir)
        check_if_extra(file,dest_dir_extra,source_dir)
