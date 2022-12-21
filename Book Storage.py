#!/usr/bin/env python
# coding: utf-8

# In[1]:


# GOAL: Get title of every book with 2 star rating  


# In[2]:


import requests 
import bs4


# In[3]:


# we´ll use the page www.toscrape.com to practice 


# In[4]:


# Problem 1 

# the website has 50 pages. How are we going to take the content from all of them? 

'http://books.toscrape.com/catalogue/page-1.html'
'http://books.toscrape.com/catalogue/page-2.html'

# it´s a good idea to loop - /page-[1].html - to 50 to get all the pages


# In[5]:


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'


# In[6]:


# Problem 2

# how to pick 2 star books? check the website with inspect and explore options.

# there is a class called - /star-rating Two / perfect to use to extract those books inside of product_pod 


# In[7]:


res = requests.get(base_url.format(1))


# In[8]:


soup = bs4.BeautifulSoup(res.text,'lxml')


# In[9]:


len(soup.select('.product_pod')) #what does 20 means? check the web and there are 20 items per page!! 


# In[10]:


products = soup.select(".product_pod")


# In[11]:


example = products [0]


# In[12]:


example # this is the information of a book. Is this rated Two starts or not?  


# In[13]:


str(example)


# In[14]:


'star-rating Two' in str(example) #now I can check if there class rating is Two or not 


# In[15]:


# Now I have to identify the title of each book, that can be posted in 


# In[16]:


example.select('a')[1]['title']


# In[17]:


# We can check if something is 2 star rating 
# we can gran the title of the book using example.select('a')[1]['title']


# In[18]:


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

two_star_titles = []

for n in range(1,51):
    
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")
    
    for book in books:
        
        if  'star-rating Two' in str(book):
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)


# In[21]:


two_star_titles


# In[ ]:





# In[ ]:





# In[ ]:




