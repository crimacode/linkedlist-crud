#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Creating a Node Class for each item in a list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# In[2]:


#CRUD LinkedList - CRUD : CREATE, READ, UPDATE, DELETE
class LinkedList:
    def __init__(self):
        #starting point of linkedlist
        self.start_node = None
    def append(self, data):
        node = Node(data)
        #check if their is not node yet in our linkedlist
        if(self.start_node == None):
            self.start_node = node
        else:
            #check if the next node exist or not after the first before appending it
            if(self.start_node.next == None):
                self.start_node.next = node
            else:
                #start searching to find the last node and append to it next node
                start_n = self.start_node
                while(start_n != None):
                    if(start_n.next == None):
                        start_n.next = node
                        break
                    start_n = start_n.next
    def display_all(self):
        #search through the entire list and display the data it contains at each step
        start_n = self.start_node
        while(start_n != None):
            print(start_n.data)
            start_n = start_n.next
    def delete(self, data):
        #check if the deleted data is the first node
        if(self.start_node.data == data):
            self.start_node = self.start_node.next
            print("deleted", data)
        else:
            # start searching through the connected nodes to find the data we want to delete
            start_n = self.start_node
            while(start_n != None):
                if(start_n.next != None):
                    #if the data is found, link the current next node to the next node of the data node
                    if(start_n.next.data == data):
                        start_n.next = start_n.next.next
                        print("deleted", data)
                        return
                    else:
                        start_n = start_n.next
                else:
                    print("Data not found")
                    return
    def update(self, original_data, update_data):
        # start searching through the connected nodes to find the data we want to update
        start_n = self.start_node
        while(start_n != None):
            if(start_n.data == original_data):
                #if the data is found, update the node data with the updated data
                start_n.data = update_data
                print(original_data, "is updated to", update_data)
                return
            else:
                start_n = start_n.next
        print("Data not found")


# In[3]:


l_list = LinkedList()


# In[4]:


l_list.append(2)


# In[5]:


l_list.append(4)


# In[6]:


l_list.append(7)


# In[7]:


l_list.display_all()


# In[8]:


l_list.append(12)


# In[9]:


l_list.append(19)


# In[10]:


l_list.append(67)


# In[11]:


l_list.display_all()


# In[12]:


l_list.display_all()


# In[13]:


l_list.delete(2)


# In[14]:


l_list.display_all()


# In[15]:


l_list.delete(19)


# In[16]:


l_list.display_all()


# In[17]:


l_list.delete(7)


# In[18]:


l_list.display_all()


# In[19]:


l_list.delete(200)


# In[20]:


l_list.display_all()


# In[21]:


l_list.update(8, 30)


# In[22]:


l_list.update(4, 30)


# In[23]:


l_list.display_all()


# In[24]:


l_list.update(67, 5)


# In[25]:


l_list.display_all()


# In[26]:


l_list.update(67, 5)


# In[27]:


l_list.update(5, 9)


# In[28]:


l_list.display_all()


# In[29]:


l_list.update(12, 25)


# In[30]:


l_list.display_all()


# In[ ]:




