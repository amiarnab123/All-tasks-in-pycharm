import logging
logging.basicConfig(filename='TASK_ANS.log',level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

class lists:
    def __init__(self,l1,l2):
        self.l1 = l1
        self.l2 = l2

    def reversion(self):
        try:
            logging.info("******Try to reverse the data******")
            if type(self.l1) == list:
                return self.l1[::-1]
            else:
                logging.info("Data is not a list. Not possible to reverse now")
        except Exception as e:
            logging.exception(e)

    def access_int(self,a): #a should be a int
        try:
            logging.info('******try to access 234 and 456 from the list******')
            l = []
            for i in self.l1:
                if type(i) == tuple or type(i) == dict or type(i) == list:
                    for j in i:
                        if j == a:
                            l.append(j)
            return l
        except Exception as e:
            logging.exception(e)

    def extract_list(self):
        try:
            logging.info('******try to extract list element from the collection******')
            l = []
            for i in (self.l1 + self.l2) :
                if type(i) == list:
                    l.append(i)
            return l
        except Exception as e:
            logging.exception(e)

    def filter_specific_string(self,s): #s should be a string
        try:
            logging.info('******try to filter out specific string******')
            l = []
            for i in (self.l1 + self.l2) :
                if type(i) == tuple or type(i) == list:
                    for j in i:
                        if j == s:
                            l.append(j)
                if type(i) == dict:
                    for j in i:
                        if i[j] == s:
                            l.append(i[j])
            return l
        except Exception as e:
            logging.exception(e)

    def filter_all_string(self):
        logging.info('******filter out all the string data******')
        try:
            l = []
            for i in self.l2:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            l.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == str:
                                l.append(g)
            return l
        except Exception as e:
            logging.info(e)

    def extract_tuple(self):
        logging.info('******try to extract the tuple entities******')
        try:
            l=[]
            for i in self.l2:
                if type(i) == tuple:
                    l.append(i)
            return l
        except Exception as e:
            logging.info(e)

    def extract_dict(self):
        logging.info('******try to extract dict entities******')
        l = []
        try:
            for i in self.l2:
                if type(i) == dict:
                    l.append(i)
            return l
        except Exception as e:
            logging.info(e)

    def filter_key_dict(self):
        try:
            logging.info('******try to list out key elements from the dictionary under the list******')
            l = []
            for i in self.l1:
                if type(i) == dict:
                    for j in i:
                        l.append(j)
            return l
        except Exception as e:
            logging.exception(e)

    def filter_values_dict(self):
        try:
            logging.info('******try to list out values of dictionary under the list******')
            l = []
            for i in self.l1:
                if type(i) == dict:
                    for j in i:
                        l.append(i[j])
            return l
        except Exception as e:
            logging.info(e)

    def filter_numeric(self):
        logging.info('******try to extract numerical entities******')
        try:
            l = []
            for i in self.l2:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l.append(g)
            return l
        except Exception as e:
            logging.info(e)

    def sum_numeric(self):
        logging.info('******try to sum up the numerical entities******')
        try:
            l = []
            for i in self.l2:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l.append(g)
            return sum(l)
        except Exception as e:
            logging.info(e)

    def filter_odd(self):
        logging.info('******filter out odd values from numeric values******')
        try:
            l = []
            for i in self.l2:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l.append(g)
            l3 = []
            for m in l:
                if m % 2 == 0:
                    pass
                else:
                    l3.append(m)
            return l3
        except Exception as e:
            logging.info(e)

    def multiplication(self):
        logging.info('******try to find multiplication of numerical data******')
        try:
            l = []
            for i in self.l2:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l.append(g)
            m = 1
            for i in l:
                    m = m * i
            return m

        except Exception as e:
            logging.info(e)

    def occcurence(self):
        logging.info('*******try to print occurences of all the data******* ')
        try:
            l = []
            for i in self.l2:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            l.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int or type(g) == str:
                                l.append(g)
            dict1 = {}
            for m in set(l):
                c = l.count(m)
                dict1[m] = c
            logging.info("{dict}")
            return dict1
        except Exception as e:
            logging.info(e)

    def key_num(self):
        logging.info('******find out number of keys in dict******')
        try:
            for i in self.l2:
                if type(i) == dict:
                    return len(i)
        except Exception as e:
            logging.info(e)

    def filter_alphanum(self):
        logging.info('*******filter out alphanum data******')
        try:
            l = []
            for i in self.l2:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            l.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int or type(g) == str:
                                l.append(g)
            l3 = []
            for m in l:
                if type(m) == str:
                    if m.isalnum():
                        l3.append(m)
            return l3
        except Exception as e:
            logging.info(e)



class pattern():

    def __init__(self,s):
        self.s = s

    def ineuron_pattern1(self,n):

        try:
            logging.info('*******try to print 1st pattern of 3rd task*******')
            for i in range(n):
                logging.info((self.s)  * (i + 1))
        except Exception as e:
            logging.info(e)

    def ineuron_pattern2(self,m):

        try:
            logging.info('*******try to print 2nd pattern of 3rd task*******')
            for i in range(m):
                if i <= 3:
                    n = i
                else:
                    n = m - i
                logging.info(((self.s) * n).center(30, ' '))
        except Exception as e:
            logging.info(e)

    def star_pattern(self,i): # please enter the number of rows you want as i

        try:
            logging.info('******try to print star pattern using while loop from task 4******')
            n = 1
            while n <= i:
                logging.info('* ' * n)
                n = n + 1
        except Exception as e:
            logging.exception(e)

    def word_pattren(self):

        try:
            logging.info('******try to print word pattern using while lopp from task 4******')
            x = 0
            while x < 8:
                content = ""
                y = 0
                while y < x:
                    z = 0
                    sum = 0
                    while z < y:
                        sum += 6 - z
                        z += 1
                    if (x + 64 + sum) <= (64 + 26):
                        content += " " + chr(x + 64 + sum)
                    y += 1
                logging.info(content)
                x += 1
        except Exception as e:
            logging.info(e)


class while_task4:

    def __init__(self,text):
        self.text = text

    def divisible_by_3(self,start,end):

        try:
            logging.info('******Try to print all the number divisible by 3 in between a range of 40 - 400******')
            l = []
            while start <= end:
                if start % 3 == 0:
                    l.append(start)
                start = start + 1
            return l
        except Exception as e:
            logging.info(e)

    def vowel(self):

        try:
            logging.info('******Try to filter out all the vowels form the text by using while loop******')
            l=[]
            i = 0
            v = 'aeiou'
            self.text = self.text.lower()
            while i < len(self.text):
                if self.text[i] in v:
                    l.append(self.text[i])
                i = i + 1
            return l
        except Exception as e:
            logging.info(e)

    def even_num(self,start,end):
        try:
            logging.info('******Try to generate all the even number between 1- 1000******')
            l = []
            start = 1
            while start <= end:
                if start % 2 == 0:
                    l.append(start)
                start = start + 1
            return l
        except Exception as e:
            logging.info(e)




#CREATING OBJECTS OF EACH CLASS

obj = lists([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}],
            [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
             {'k1': "sudh", "k2": "ineuron", "k3":
                 "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])

obj1 = pattern('ineuron')
obj2 = while_task4("""Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]

Python consistently ranks as one of the most popular programming languagesc""")


#LOGGING

logging.info(obj.reversion())
logging.info(obj.access_int(234))
logging.info(obj.access_int(456))
logging.info(obj.extract_list())
logging.info(obj.filter_specific_string('sudh'))
logging.info(obj.filter_specific_string('ineuron'))
logging.info(obj.filter_all_string())
logging.info(obj.extract_tuple())
logging.info(obj.extract_dict())
logging.info(obj.filter_key_dict())
logging.info(obj.filter_values_dict())
logging.info(obj.filter_numeric())
logging.info(obj.sum_numeric())
logging.info(obj.filter_odd())
logging.info(obj.multiplication())
logging.info(obj.occcurence())
logging.info(obj.key_num())
logging.info(obj.filter_alphanum())
logging.info(obj1.ineuron_pattern1(4))
logging.info(obj1.ineuron_pattern2(6))
logging.info(obj1.star_pattern(9))
logging.info(obj1.word_pattren())
logging.info(obj2.divisible_by_3(40,400))
logging.info(obj2.vowel())
logging.info(obj2.even_num(1,1000))


