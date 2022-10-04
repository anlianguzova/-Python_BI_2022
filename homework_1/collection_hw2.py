#!/usr/bin/env python
# coding: utf-8

# In[8]:





# In[9]:


def transcribe(seq):
    """Print the transcribed sequence and create the txt-file with it"""
    trans_seq = ""
    trans_dic = {"A" : "U", "T" : "A", "G" : "C", "C" : "G", 
                "a" : "u", "t" : "a", "g" : "c", "c" : "g"}
    for nucl in seq:
        if nucl not in trans_dic.keys():
            print("Invalid alphabet")
            break
        else:
            trans_seq += trans_dic[nucl]
    with open('transcription_nucl.txt', 'w') as f:
                f.write(trans_seq)
    print(trans_seq)
    return trans_seq 
 


# In[10]:


def reverse(seq):
    """Print the reverse sequence and create the txt file with it"""
    rev_seq = ""
    dna_dic = ["A", "T", "G", "C", 
               "a", "t", "g", "c"]
    for nucl in seq:
        if nucl not in dna_dic:
            print("Invalid alphabet")
            break
        else: 
            rev_seq = seq[::-1]
    with open('reverse_seq.txt', 'w') as f:
                f.write(rev_seq)
    print(rev_seq)
    return rev_seq 


# In[12]:


def complement(seq):
    """Print the complement sequence and create the txt file with it"""
    compl_seq = ""
    compl_dic = {"A" : "T", "T" : "A", "G" : "C", "C" : "G", 
                "a" : "t", "t" : "a", "g" : "c", "c" : "g"}
    for nucl in seq:
        if nucl not in compl_dic.keys():
            print("Invalid alphabet")
            break
        else:
            compl_seq += compl_dic[nucl]
    with open('comlement_seq.txt', 'w') as f:
                f.write(compl_seq)
    print(compl_seq)
    return compl_seq


# In[13]:


def reverse_complement(seq):
    """Print the reverse complement sequence and create the txt file with it"""
    compl = ""
    rev_compl = ""
    compl_dic = {"A" : "T", "T" : "A", "G" : "C", "C" : "G", 
                "a" : "t", "t" : "a", "g" : "c", "c" : "g"}
    for nucl in seq:
        if nucl not in compl_dic.keys():
            print("Invalid alphabet")
            break
        else:
            compl += compl_dic[nucl]
            rev_compl = compl[::-1]
    with open('reverse_complemeny.txt', 'w') as f:
                f.write(rev_compl)
    print(rev_compl)
    return rev_compl


# In[3]:


if __name__ == "__main__":
    while True:
        print("Enter the command")
        command = str(input())
        com_dic = {"transcribe" : transcribe, "exit" : "Good luck!", "reverse" : reverse,
                  "complement" : complement, "reverse complement" : reverse_complement}
        if command not in com_dic:
            print("The command does not exist")
        elif command == "exit":
            print(com_dic.get(command))
            break
        else:
            print("Enter the sequence")
            seq = str(input())
            command_fun = com_dic.get(command)
            command_fun(seq)
           
            
                    
                    
                
        
    
        


# In[ ]:



        


# In[ ]:





# In[ ]:





# In[ ]:




