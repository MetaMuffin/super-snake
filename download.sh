#!/bin/sh

youtube-dl -o 'temp.opus' -x https://www.youtube.com/watch?v=MFtr4rw-dwI
ffmpeg -y -i 'temp.opus' -ss 00:00:00 -t 00:00:20 -async 1 'audio/star1.wav'
ffmpeg -y -i 'temp.opus' -ss 00:00:20 -t 00:00:36 -async 1 'audio/star2.wav'
ffmpeg -y -i 'temp.opus' -ss 00:00:36 -t 00:01:00 -async 1 'audio/star3.wav'
ffmpeg -y -i 'temp.opus' -ss 00:01:00 -t 00:01:25 -async 1 'audio/star4.wav'
rm temp.opus