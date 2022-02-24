#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago


# ### Task 1 - Define the DAG arguments

# In[2]:


# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Dennis L',
    'start_date': days_ago(0),
    'email': ['dennis@somemail.com'],
    
}


# ### Task 2 - Define the DAG

# In[3]:


dag = DAG(
    dag_id='process_web_log',
    default_args=default_args,
    description='Web Log DAG using Bash',
    schedule_interval=timedelta(days=1),
)


# ### Task 3 - Create a task to extract data

# ### Task 4 - Create a task to transform the data in the txt file

# ### Task 5 - Create a task to load the data

# In[4]:


# define the first task named extract
extract = BashOperator(
    task_id='extract',
    bash_command='cut -d":" -f1 accesslog.txt > extracted-data.txt',
    dag=dag,
)



# define the second task named transform
transform = BashOperator(
    task_id='transform',
    bash_command='tr "198.46.149.143" " " < extracted-data.txt > transformed-data.txt',
    dag=dag,
)

# define the third task named load

load = BashOperator(
    task_id='load',
    bash_command='< transformed-data.txt > weblog.tar',
    dag=dag,
)


# ### Task 6 - Define the task pipeline

# In[5]:


# task pipeline
extract >> transform >> load


# In[ ]:




