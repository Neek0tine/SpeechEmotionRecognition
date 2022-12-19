#!/usr/bin/env python
# # -*- coding: utf-8 -*- 

__author__ = "Nicholas Juan"
__copyright__ = "Copyright 2022, Group C SER Project"
__credits__ = ["Aretha Levi", "Rofa Arfaqo I.", "Nicholas Juan", "Haffiyah Khayyiroh S."]
__license__ = "GPL"
__version__ = "2.1.0"
__maintainer__ = "Nicholas Juan"
__email__ = "nicholas.juan.kalvin-2020@ftmm.unari.ac.id"
__status__ = "Development"

"""
Modul ini berfungsi untuk mengunduh video dari YouTube dan mengubahnya menjadi 
potongan-potongan audio berdurasi 3 detik yang terkumpul dalam folder khusus.

Contoh:
    Modul ini dapat dijalankan melalui shell secara langsung dengan memanggilnya
    secara langsung menggunakan Python. Direkomdendasikan untuk menggunakan Python versi 3.10.x

        $ python Kelompok_C_Audio_Scrapper.py

    Modul ini juga dapat dijalankan melalui program python lain, dengan cara mengimport modul ini,
    lalu mendeklarasikan kelas dan menjalankan metode `run`

        from AudioScrapperKelompokC import Scrapper
        s = Scrapper(format, codec, quality, dir)
        s.run(title, duration, search_limit)
    
    Arguments:
        format      :str     Format YTDL
        codec       :str     Ekstensi file yang diunduh (mp3, wav)
        quality     :int     Kualitas (bitrate) video/audio
        dir         :str     Direktori spesifik

        title       :str    judul video yang akan didownload
        duration    :int    lama waktu dari setiap segment audio
        search_limit:int    sebarapa banyak video yang akan diquery

Packages:
    youtube_dl
    os
    youtubesearchpython
    tqdm
    re
"""


from yt_dlp import YoutubeDL
from os import system, chdir, path
from youtubesearchpython import VideosSearch
import itertools
import re
import unicodedata
import json 


class Scrapper:
    """
    Kelas Scrapper berfungsi sebagai kelas yang menyimpan metode untuk mengunduh dan memproses file

    Arguments:
        format:str      Format YTDL
        codec:str       Ekstensi file yang diunduh (mp3, wav)
        quality:int     Kualitas (bitrate) video/audio
        outtmpl:str     Format penamaan file/direktori file
    """

    def __init__(self, format='bestaudio/best', codec='mp3', quality=192, dir='./'):
        chdir(dir)
        # Specify path
        self.result = ''
        self.dataFolder = r'./dataset/'
        self.angryFolder = r'./dataset/angry'
        self.sadFolder = r'./dataset/sad'
        self.neutralFolder = r'./dataset/neutral'
        self.happyFolder = r'./dataset/happy'
        self.undefinedFolder = r'./dataset/undefined'
        self.downloadFolder = r'./dataset/downloaded'
        self.label = 'undefined'
        self.codec = codec

        if path.exists(str(self.dataFolder))  :
            pass
        else:
            system(f'mkdir "{self.dataFolder}"')

        if path.exists(str(self.undefinedFolder)) :
            pass
        else:
            system(f'mkdir "{self.undefinedFolder}"')

        if path.exists(str(self.sadFolder)) :
            pass
        else:
            system(f'mkdir "{self.sadFolder}"')

        if path.exists(str(self.angryFolder)) :
            pass
        else:
            system(f'mkdir "{self.angryFolder}"')

        if path.exists(str(self.neutralFolder)) :
            pass
        else:
            system(f'mkdir "{self.neutralFolder}"')

        if path.exists(str(self.happyFolder)):
            pass
        else:
            system(f'mkdir "{self.happyFolder}"')
            
        if path.exists(self.downloadFolder):
            pass
        else:
            system(f'mkdir "{self.downloadFolder}"') 
            
        self.ydl_opts = {}

        # self.ydl_opts['format'] = format
        self.ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 
                                            'preferredcodec': codec, 
                                            'preferredquality': str(quality)}]
        self.ydl_opts['outtmpl'] = f'{self.downloadFolder}\\%(title)s.%(ext)s'
        self.ydl_opts['restrictfilenames'] = True
        self.ydl_opts['ignoreerrors'] = True
    

    def search(self, query, limit):
        """
        Mencari video dari YouTube

        Args:
            limit (int): jumlah yang ingin dicari
        
        Returns:
            hasil (dicts) dict_keys(['type', 'id', 'title', 'publishedTime', 'duration', 'viewCount', 
            'thumbnails', 'richThumbnail', 'descriptionSnippet', 'channel', 'accessibility', 'link', 'shelfTitle'])

        """


        try:
            _result = VideosSearch(query, limit = limit)
            if len(_result.result()["result"]) != 0: 
                _titles = [ v['title'] + ' ' + '[' + v['duration'] + ']' for i, v in enumerate(_result.result()['result'])]
                _found_queries = len(_result.result()["result"])
                print(f'[+] Ditemukan {_found_queries} hasil. Video mana yang ingin diunduh?\n')
                for i, t in enumerate(_titles):
                    print(str(i+1) +'. ' + t)
                _answer = input(f'Pilihan (1-{_found_queries}): ')
                _chosen = _result.result()['result'][int(_answer)-1]
                print(f"\n[+] Terpilih: '{_chosen['title']}' berdurasi [{_chosen['duration']}]")
                print(f"[+] Label apa yang cocok untuk video diatas?\n")
                labels = ['angry', 'happy', 'neutral', 'sad']
                for li, l in enumerate(labels):
                    print(f"{li+1}. {l.title()}")
                
                self.label = labels[int(input(f'Pilihan (1-{len(labels)}): ')) - 1]
                
                print(f'[+] Label adalah: {(self.label).title()}')
                print(f'[+] Mengunduh: {_chosen["link"]}')
                self.result = _chosen['link']



            elif len(_result.result()["result"]) == 0:  
                print(f'[!] Tidak ditemukan video apapun. Mohon coba lagi.')
                self.run(title=input("[+] YouTube video title: "))

        except Exception as e:
            print(f'[!] {e}')
            exit()



    def download(self, url, duration=3, download=True, label='undefined', segment=True):
        """Mengunduh video dari YouTube dan bertanggung jawab untuk memotong file audio yang sudah di download menjadi beberapa bagian 
        berdurasi 3 detik setiap bagian.

        Args:
            url (str): link dari video
            download (bool, optional): True jika ingin mengunduh, False jika hanya ingin mendapatkan metadata. Defaults to False.

        Returns:
            info_dict (dict):  dict_keys(['id', 'title', 'formats', 'thumbnails', 'description', 'upload_date', 'uploader', 'uploader_id', 
            'uploader_url', 'channel_id', 'channel_url', 'duration', 'view_count', 'average_rating', 'age_limit', 'webpage_url', 
            'categories', 'tags', 'is_live', 'channel', 'extractor', 'webpage_url_basename', 'extractor_key', 'playlist', 'playlist_index', 
            'thumbnail', 'display_id', 'requested_subtitles', 'asr', 'filesize', 'format_id', 'format_note', 'fps', 'height', 'quality', 
            'tbr', 'url', 'width', 'ext', 'vcodec', 'acodec', 'abr', 'downloader_options', 'container', 'format', 'protocol', 'http_headers'])
        """
        self.label = label

        if url == '':
            print('[!] Gagal memuat link, URL salah atau sintaks salah.')
            self.run()
        
        def sanitize_filename(s, restricted=True, is_id=False):
            """Sanitizes a string so it could be used as part of a filename.
            If restricted is set, use a stricter subset of allowed characters.
            Set is_id if this is not an arbitrary string, but an ID that should be kept
            if possible.
            """
            ACCENT_CHARS = dict(zip('ÂÃÄÀÁÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖŐØŒÙÚÛÜŰÝÞßàáâãäåæçèéêëìíîïðñòóôõöőøœùúûüűýþÿ',
                                itertools.chain('AAAAAA', ['AE'], 'CEEEEIIIIDNOOOOOOO', ['OE'], 'UUUUUY', ['TH', 'ss'],
                                                'aaaaaa', ['ae'], 'ceeeeiiiionooooooo', ['oe'], 'uuuuuy', ['th'], 'y')))

            def replace_insane(char):
                if restricted and char in ACCENT_CHARS:
                    return ACCENT_CHARS[char]
                if char == '?' or ord(char) < 32 or ord(char) == 127:
                    return ''
                elif char == '"':
                    return '' if restricted else '\''
                elif char == ':':
                    return '_-' if restricted else ' -'
                elif char in '\\/|*<>':
                    return '_'
                if restricted and (char in '!&\'()[]{}$;`^,#' or char.isspace()):
                    return '_'
                if restricted and ord(char) > 127:
                    return '_'
                return char

            if restricted and not is_id:
                s = unicodedata.normalize('NFKC', s)
            s = re.sub(r'[0-9]+(?::[0-9]+)+', lambda m: m.group(0).replace(':', '_'), s)
            result = ''.join(map(replace_insane, s))
            if not is_id:
                while '__' in result:
                    result = result.replace('__', '_')
                result = result.strip('_')
                if restricted and result.startswith('-_'):
                    result = result[2:]
                if result.startswith('-'):
                    result = '_' + result[len('-'):]
                result = result.lstrip('.')
                if not result:
                    result = '_'
            return result + f'.{self.codec}'

        with YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(url , download=download)
            dirtytitle = info.get('title')
            cleantitle = sanitize_filename(s=dirtytitle, restricted=True)
            target = str(self.downloadFolder + "/" + cleantitle)

            if segment and path.exists(target) and self.label == 'undefined' :
                print(f'[+] Melanjutkan ke proses segmentasi')
                output_file = f"{self.undefinedFolder}/{cleantitle}"
                print(f'[+] Tujuan segmentasi {self.undefinedFolder}/{cleantitle}')
                system(f'ffmpeg -i "{target}" -f segment -segment_time {duration} -c copy {output_file}%d.{self.codec}')
            
            elif segment and path.exists(target) and self.label != 'undefined' :
                print(f'[+] Melanjutkan ke proses segmentasi')
                output_file = f"{self.dataFolder}/{self.label}/{cleantitle}"
                print(f'[+] Tujuan segmentasi {self.dataFolder}/{self.label}/{cleantitle}')
                system(f'ffmpeg -i "{target}" -f segment -segment_time {duration} -c copy {output_file}%d.{self.codec}')

            elif not download:
                print(f'[+] Metadata selesai diunduh.')

                with open(f"{str(self.downloadFolder + '/' + cleantitle)}.json", "w") as outfile:
                    json.dump(info, outfile)
            elif not segment:
                print(f'[+] Audio terunduh dan terdapat di {self.downloadFolder}')

            else:
                print(f'[!] Ada yang salah dengan file yang baru di download. Mohon periksa folder (./dataset/downloaded) atau kontak Juan jika bingung ')
        
           
    def run(self, url=None, duration=3, search_limit = 5):
        print('='*80)
        print('© 2022 Kelompok C SER Project FTMM Airlangga University')
        print('YouTube Audio Scrapper version', __version__)
        print('='*80)
        if url is not None:
            self.download(url, duration)
        else:
            self.search(input("[+] YouTube video title: "), limit=search_limit)
            self.download(self.result, duration=duration)
