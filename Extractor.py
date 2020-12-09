import pysrt
import re 
import string 
from collections import OrderedDict 
  

# F:\ffmpeg-N-100125-gba6e2a2d05-win32-static\bin\ffmpeg.exe -i F:\ffmpeg-N-100125-gba6e2a2d05-win32-static\music.mp4 -ss 00:02:50 -to 00:02:55 -c copy F:\ffmpeg-N-100125-gba6e2a2d05-win32-static\music_new1.mp4

sub_file_path=list()
vid_file_path=list()
words_target=list()
target_words_no_duplicate=list()
target_words_not_found=list()
target_words_found=list()

found_file_path=list()
found_file_path.append([])
found_word_strttime=list()
found_word_strttime.append([])
found_word_endtime=list()
found_word_endtime.append([])

i=int()
j=int()
# target_sub=(input("Enter path to target subtitle : "))
# val = int(input("Enter no of subtitles to analyse : "))
# print(val)

# for i in range(val):
    # subname=input("Enter path to subtitle - %d: " % i)
    # sub_file_path.append(str(subname))
    # vid_file_path.append(sub_file_path[i].replace(".srt", ".mp4"))
    # print(sub_file_path[i])
    # print(vid_file_path[i])

val=1
sub_file_path.append("F:/YoutubeVideos/2.srt")
target_sub=("F:/Python_AudioExtract/video/TheWeekend_Blind.srt")
vid_file_path.append("F:/YoutubeVideos/2.mp4")

subs_target = pysrt.open(target_sub)
subs_target_length = len(subs_target)


for j in range(subs_target_length):
    words_target.append(re.sub('['+string.punctuation+']', '', subs_target[j].text).split())
    for k in range(len(words_target[j])):
        target_words_no_duplicate.append(words_target[j][k].lower())
        
target_words_no_duplicate = list(OrderedDict.fromkeys(target_words_no_duplicate)) 
target_words_no_duplicate_length=len(target_words_no_duplicate)
# print(target_words_no_duplicate)
# print(target_words_no_duplicate_length)

word_found_cnt=-1
for j in range(target_words_no_duplicate_length):
    word_found_flg=0
    for i in range(val):
        subs_analyse = pysrt.open(sub_file_path[i])
        sub_length=len(subs_analyse)
        for x in range(sub_length):
            words_analyse = re.sub('['+string.punctuation+']', '', subs_analyse[x].text).split() 
            words_analyse_len=len(words_analyse)
            for u in range(words_analyse_len):
                if (words_analyse[u].lower()==target_words_no_duplicate[j].lower()):
                    found_file_path[word_found_cnt+1].append(sub_file_path[i])
                    found_word_strttime[word_found_cnt+1].append('{}:{}'.format(subs_analyse[x].start.minutes,subs_analyse[x].start.seconds))
                    found_word_endtime[word_found_cnt+1].append('{}:{}'.format(subs_analyse[x].end.minutes,subs_analyse[x].end.seconds))
                    # found_file_path[1].append(sub_file_path[i])
                    # found_file_path[word_found_cnt+1].append(sub_file_path[i])
                    # found_word_strttime=list()
                    # found_word_endtime=list()
                    # print("Found a match")
                    # print(words_analyse[u].lower())
                    # print(target_words_no_duplicate[j].lower())
                    # print(subs_analyse[x].start.minutes)
                    # print(subs_analyse[x].start.seconds)
                    # print(subs_analyse[x].end.minutes)
                    # print(subs_analyse[x].end.seconds)
                    word_found_flg=1
    if(word_found_flg==1):
        word_found_cnt=word_found_cnt+1
        found_file_path.append([])
        found_word_strttime.append([])
        found_word_endtime.append([])
        target_words_found.append(target_words_no_duplicate[j].lower())
    
    if(word_found_flg==0):
        target_words_not_found.append(target_words_no_duplicate[j].lower())

# print('No of found words :',target_words_no_duplicate_length-len(target_words_not_found))
# print('Words Subtitle path info :',found_file_path)
# print('No of not found words :',len(target_words_not_found))
# print('list of not found words :',target_words_not_found)
print('Found word - ',target_words_found[12])
print('File path - ',found_file_path[12])
print('Word start Time - ',found_word_strttime[12])
print('Word End Time - ',found_word_endtime[12])
        # for i in range(val):
            # subs_analyse = pysrt.open(sub_file_path[i])
            # sub_length=len(subs_analyse)
            # for x in range(sub_length):
                # words_analyse = re.sub('['+string.punctuation+']', '', subs_analyse[x].text).split() 
                # words_analyse_len=len(words_analyse)
                # for u in range(words_analyse_len):
                    # if (words_analyse[u].lower()==words_target[y].lower()):
                        # print("Found a match")
                        # print(words_analyse[u].lower())
                        # print(subs_analyse[x].start.minutes)
                        # print(subs_analyse[x].start.seconds)
                        # print(subs_analyse[x].end.minutes)
                        # print(subs_analyse[x].end.seconds)

    
        
# for j in range(subs_target_length):
    # words_target = re.sub('['+string.punctuation+']', '', subs_target[j].text).split()
    # words_target_length = len(words_target)
    # for y in range(words_target_length):
        # for i in range(val):
            # subs_analyse = pysrt.open(sub_file_path[i])
            # sub_length=len(subs_analyse)
            # for x in range(sub_length):
                # words_analyse = re.sub('['+string.punctuation+']', '', subs_analyse[x].text).split() 
                # words_analyse_len=len(words_analyse)
                # for u in range(words_analyse_len):
                    # if (words_analyse[u].lower()==words_target[y].lower()):
                        # print("Found a match")
                        # print(words_analyse[u].lower())
                        # print(subs_analyse[x].start.minutes)
                        # print(subs_analyse[x].start.seconds)
                        # print(subs_analyse[x].end.minutes)
                        # print(subs_analyse[x].end.seconds)



# # initializing string   
# words_sub = "Geeksforgeeks,    is best @# Computer Science Portal.!!!"  
# # printing original string 
# print ("The original string is : " +  words_sub)   
# # using regex() + string.punctuation 
# # to extract words from string 
# res = re.sub('['+string.punctuation+']', '', words_sub).split()   
# # printing result 
# print ("The list of words is : " +  str(res)) 



# words=subs[5].text.split()
# j=len(words)
# print("No of words", j)
# print(str(words))
# # for x in range(i):
    # # sub_line = subs[x]
    # # print(sub_line.text)
    # # print(sub_line.start.minutes)
    # # print(sub_line.start.seconds)
    # # print(sub_line.end.minutes)
    # # print(sub_line.end.seconds)






