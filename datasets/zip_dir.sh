#!/bin/sh  

# Choose one path to compress videos
# folder='./datasets/davis/JPEGImages'
folder='./datasets/youtube-vos/JPEGImages'


for file in $folder/*
do
    if test -f $file
    then
        echo $file is file
    else
        echo compressing \"$file\" ...
        zip -q -r -j $file.zip $file/
        rm -rf $file/
    fi
done


echo 'Done!'
