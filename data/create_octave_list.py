alphabet = '0:1:2:3:4:5:6:7:8:9:!:@:#:~:%:^:&:*:(:):+:=:{:}:<:>:a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:z:A:B:C:D:E:F:G:H:I:J:K:L:M:N:O:P:Q:R:S:T:U:V:W:X:Y:Z:[:]:,:.:?:;:|:$'
alphabet = alphabet.split(':')

train_fp = open('data/train_list.txt', 'w')
test_fp = open('data/test_list.txt', 'w')

for i in range(10000):
    imgpath = 'data/images/%08d.png' % i
    labpath = imgpath.replace('images', 'labels').replace('.png', '.txt')
    with open(labpath) as lfp:
        label = lfp.read().strip()
    label = label.split(',')
    label = [int(item) for item in label]
    label = label[0:len(label)-1]
    label = [alphabet[item] for item in label]
    label.append('$')
    label = ':'.join(label)
    output = ' '.join([imgpath, label])
    if i < 9000:
        print >> train_fp, output
    else:
        print >> test_fp, output

train_fp.close()
test_fp.close()
