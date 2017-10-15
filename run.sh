# the format or list file
# imagepath label
# /ab/cd/image.jpg a:b:c:d 

#nohup python main.py --trainlist data/train_list.txt --vallist data/test_list.txt --cuda --adam --lr=0.001 > log.txt &



#python data/create_octave_list.py
CUDA_VISIBLE_DEVICES=3 nohup python main.py --trainlist=data/train_list.txt --vallist=data/test_list.txt --cuda --adam --lr=0.001 --niter=100 --saveInterval=100 --alphabet '0:1:2:3:4:5:6:7:8:9:!:@:#:~:%:^:&:*:(:):+:=:{:}:<:>:a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:z:A:B:C:D:E:F:G:H:I:J:K:L:M:N:O:P:Q:R:S:T:U:V:W:X:Y:Z:[:]:,:.:?:;:|:$' --imgW=512 --imgH=128 --displayInterval=5 --n_test_disp=10 --valInterval=5 --saveInterval=50 --task='octave' > log.txt &
