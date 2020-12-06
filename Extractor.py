import pysrt
import re 
import string 

sub_file_path=list()
vid_file_path=list()
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
sub_file_path.append("F:/YoutubeVideos/NDTV_Kamal.srt")
target_sub=("F:/Python_AudioExtract/video/TheWeekend_Blind.srt")
vid_file_path.append("F:/YoutubeVideos/memoriesbringback.mp4")

subs_target = pysrt.open(sub_file_path[i])
subs_target_length = len(subs_target)
for j in range(subs_target_length):
    words_target = re.sub('['+string.punctuation+']', '', subs_target[j].text).split()
    words_target_length = len(words_target)
    for y in range(words_target_length):
        for i in range(val):
            subs_analyse = pysrt.open(sub_file_path[i])
            sub_length=len(subs_analyse)
            for x in range(sub_length):
                words_analyse = re.sub('['+string.punctuation+']', '', subs_analyse[x].text).split() 
                words_analyse_len=len(words_analyse)
                for u in range(words_analyse_len):
                    if (words_analyse[u].lower()==words_target[y].lower()):
                        print("Found a match")
                        print(words_analyse[u].lower())
                        print(subs_analyse[x].start.minutes)
                        print(subs_analyse[x].start.seconds)
                        print(subs_analyse[x].end.minutes)
                        print(subs_analyse[x].end.seconds)
                # print(subs_analyse[x].text)
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






