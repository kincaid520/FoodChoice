import random
NUM_RESTAURANT = { 
1:"feng'zheng", 
2:"mei'wei", 
3:"yi'fan", 
4:"wang'pin", 
5:"wang'ji", 
#6:"yi'ji", 
6:"yue'nan", 
7:"tai'ma'ji", 
8:"zheng'guang'xiang", 
9:"ya'xiang'bao", 
10:"liu'mei",
11:"show'it"

}

num = random.randint(1, len(NUM_RESTAURANT))

print NUM_RESTAURANT[num]
