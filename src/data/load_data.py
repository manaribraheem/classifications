
import wget
import zipfile
import glob2
import os

def get_data(src, dst):
    """
    Downloads a file from a remote source src to a local destination dst.
    """
    remote_url = src
    local_dir = dst
    wget.download(remote_url, local_dir)


def unzip_data(my_dir, dst_1):
    """Unpacks the first zip file in a directory"""
    local_dir = my_dir
    file = glob2.glob(f'{local_dir}/*.zip')[0]
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(dst_1)

if __name__ == '__main__':
  print ('starting download')
  get_data('https://dsticlasskeras.s3.eu-west-3.amazonaws.com/kagglecatsanddogs_3367a.zip',
          '/content/gdrive/MyDrive/aws_classifier/data/raw')
     
  unzip_data('/content/gdrive/MyDrive/aws_classifier/data/raw', '/content/gdrive/MyDrive/aws_classifier/data/processed')

  # Make http request for remote file data

  