#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import numpy as np
def Csv():
    #read data
    Ranked_Data = pd.read_excel(r'C:\Users\King\Desktop\project_\\Dataannotations.xlsx', header=None, sep=" ")
    data = pd.read_excel(r'C:\Users\King\Desktop\project_\Recommender-System-for-Educational-Guidance-1-291-21.xlsx', header=None, sep=" ")
    return data,Ranked_Data


# In[53]:


def Fun_update_data(data):
    #show all columns and rows in a DataFrame
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    #choose the feature we want
    update_data=data[[0,1,2,3,8,9,11,18,15,14,13,16,25,26,27,28,29,30,31,32,33,34,36,38,39,41,40,44,46,47,49,48,52,53,58,54,55,60,61,66,62,63,69,72,68,70,76,79,75,77,154,156,153,155,157,161,163,160,162,164,101,102,103,104,107,110,111,112,113,115]]
    # Convert Yes,No,Male,female to binary data
    update_data = update_data.replace({'نعم': 1, 'لا': 0,'ذكر': 0, 'انثى': 1})
    # Convert NaN data to Zero
    update_data = update_data.fillna(0)
    return update_data


# In[54]:


def divisionList(update_data):
    new_List_of_datas=[]
    #enter to row
    for index_of_datas in range(1,len(update_data)):
        #list of datas
        Division_of_datas=[]
        # each string Until ";"
        datas=""
        #enter to col
        for data in update_data[index_of_datas]:
            #if data contain ; append to list ,then delete datas
            if data==";":
                Division_of_datas.append(datas)
                datas=""
            # if does not contain add char to datas
            else:
                datas=datas+data
        # append list row to list col
        new_List_of_datas.append(Division_of_datas)
    return new_List_of_datas


# In[55]:


def ComparisonList(list_new_data,Selected):
    update_List_of_Lists=[]
    #enter to row 
    for row in range(len(list_new_data)):
        list_data=[]
        #enter to col
        for col in range(len(list_new_data[row])):
            # enter for each row
            for item in range(len(Selected)):
                # if the string is in the list,append it
                if Selected[item] == list_new_data[row][col] :
                    list_data.append(Selected[item])
        # if row is empty,then append char 0 to col list
        if len(list_data)==0:
            update_List_of_Lists.append("0")
        # if row contain data,then append list data to col list
        else:
            update_List_of_Lists.append(list_data)
    return update_List_of_Lists


# In[56]:


# We send List of items and the columns name
def Rows_Columns(List_Data,Names):    
    Row_Col=[]
    #enter to row list ,line by line
    for row in range(len(List_Data)):
        #enter to column of list
        for col in range(len(List_Data[row])): 
            #take name by name
            #then check if this name is found in the list at row,col
            #if yes append it
            for name in Names:  
                if name == List_Data[row][col]:
                    Row_Col.append([row,name])
    return Row_Col


# In[57]:


def Create_DataFrame(List_Row_Col,number,name_col):
    # create dataframe 
    df=pd.DataFrame( columns =name_col)
    if number == 0:
            # enter to row
            for row in range(1,292):
                # make new row of dataframe
                df = df.append({}, ignore_index=True)
            # replace NAN with 0
            df = df.fillna(0)
            # enter to list ,then append data to dataframe
            for i in range(len(List_Row_Col)):
                    x=List_Row_Col[i][0]
                    y=List_Row_Col[i][1]
                    df[y][x]=1
            return df
    if number == 1:
        # enter to row
        for row in range(1,292):
            # make new row of dataframe
            df = df.append({}, ignore_index=True)
        #  replace NAN with 0 in the dataframe
        df = df.fillna(0)
        # enter to list ,then append data to dataframe
        for i in range(len(List_Row_Col)):     
            x=List_Row_Col[i][0]                    
            y=List_Row_Col[i][1]
            x=x-1
            df[y][x]=1
        return df
        


# In[58]:


def repeat_set_axis(df):
    # Repeat each row 4 times
    df=df.iloc[np.repeat(np.arange(len(df)), 4)]
    # Rearrange the number of rows from 0 to 1164
    range_number=range(0,1164)
    df=df.set_axis(range_number, axis='index')
    return df


# In[59]:


def Branch__Name(df_Branch):
    list_Branch=[]
    #enter to col
    for row in range(1,len(df_Branch)):
        #if branch not contain append it
        if df_Branch[row] not in list_Branch:
            list_Branch.append(df_Branch[row])
    return list_Branch    


# In[60]:


def RowCol_To_Branch(Branch,Branch_Name):
    list_Index=[]
    #enter to col
    for row in range(1,len(Branch)+1):
        #enter for each branch name 
        for name in Branch_Name:
            #if name contain Branch[row] ,append row and name of branch 
            if name == Branch[row]:
                list_Index.append([row,name])
    return list_Index


# In[61]:


def Rank__Str(Ranked_Data):
    # select col we need
    Str_Rank=Ranked_Data[[3,0]]
    #rename the col name
    Str_Rank=Str_Rank.set_axis(["rank",'str'], axis='columns', inplace=False)
    return Str_Rank
    
    


# In[62]:


def set_axis_columns(df):
    ICol_Name=[]
    #enter to col
    # len(df.columns) -> number of col
    for col in range(1,len(df.columns)+1):
        # append the number to ICol_Name
        ICol_Name.append(col)
    # rename the col of dataframe
    df=df.set_axis(ICol_Name, axis='columns')
    return df


# In[63]:


def Edit_DF(df_3):
    count = 1
    #enter to col
    for c in range(1,len(df_3.columns)):
        count = count + 1
        # if col equal 3
        if df_3.columns[c] == 3:
            count=0
            #enter to row
            for r in range(len(df_3)):
                # update the data
                df_3[c][r]="qid:"+str(df_3[c][r])
        # col not equal 2 and 3 
        if df_3.columns[c] != 2 and df_3.columns[c] != 3:
            # enter to col
            for r in range(len(df_3)):
                # update the data
                df_3[c][r]=str(count)+":"+str(df_3[c][r])
    count=count+1
    #enter to row
    for r in range(len(df_3)):
        #update the data, at col 66
        df_3[66][r]=str(count)+":"+str(df_3[66][r])
    return df_3


# In[64]:


def set_axis_columns_Update(df):
    ICol_Name=[]
    #append rank and str to list
    ICol_Name.append("rank")
    ICol_Name.append("str")
    #enter to col
    for col in range(1,len(df.columns)-1):
        #append number to list(1,len(df.columns)-1)
        ICol_Name.append(col)
    # update the col name  
    df=df.set_axis(ICol_Name, axis='columns')
    return df


# In[65]:


def Personal__details(update_data):
    # select the feature we need :{الجنس ,المعدل الثانوية العامة ,معدل الاول ثاويوي , اجادة فن الحديث ,... }
    Personal_details=update_data[[1,3,8,9,11,15,13,36,38,39,41,40,52,53,58,54,55,69,72,68,70,154,156,153,155,157,101,102,103,104,107]]
    # delete the first row : columns names
    Personal_details=Personal_details.drop(0)
    # call fun repeat_set_axis
    Personal_details=repeat_set_axis(Personal_details)
    return Personal_details


# In[66]:


def Branch__12(update_data):
    #select col [18] from row 1 to 292
    Branch=update_data[18][1:292]
    # call Branch_Name function 
    Branch_Name=Branch__Name(Branch)
    # call fun Fun_RowCol_To_Branch
    Branch_Index=RowCol_To_Branch(Branch,Branch_Name)
    # call fun Create_DataFrame
    df_Branch= Create_DataFrame(Branch_Index,1,Branch_Name)
    # call fun repeat_set_axis
    df_Branch=repeat_set_axis(df_Branch)   
    return df_Branch


# In[67]:


def Branch__11(update_data):
    #select col [14] from row 1 to 292
    Branch=update_data[14][1:292]
    # call fun Fun_Branch_Name
    Branch_Name=Branch__Name(Branch)
    # call fun Fun_RowCol_To_Branch
    Branch_Index=RowCol_To_Branch(Branch,Branch_Name)
    # call fun Create_DataFrame
    df_Branch= Create_DataFrame(Branch_Index,1,Branch_Name)
    # call fun repeat_set_axis
    df_Branch=repeat_set_axis(df_Branch)
    return df_Branch


# In[68]:


def df_object(update_data):
    # select features
    Selected_books=["التربية الإسلامية","مطالعة وقواعد","علوم حياتية","كيمياء","فيزياء","رياضيات","كهرباء","التصميم","الرسم الهندسي","لغة انجليزية","الادارة","جغرافيا والتاريخ"]
    # call fun ComparisonList
    object_Name_WeHave=ComparisonList(divisionList(update_data[16]),Selected_books)
    
    # call fun Rows_Columns
    object_Row_ColName=Rows_Columns(object_Name_WeHave,Selected_books)
     # call fun Create_DataFrame
    object_=Create_DataFrame(object_Row_ColName,0,Selected_books)
     # call fun repeat_set_axis
    object_=repeat_set_axis(object_)
    return object_


# In[69]:


def df_Hobbies(update_data):
    # select feature
    Selected_hobbies=["الرسم"," تصميم مواقع إلكترونية","تعلم البرمجة ","التصوير","الاهتمام في الحدائق "," زيارة الأماكن الأثرية والتاريخية","التصميم الجرافيكي","قراءة اخر الاخبار ","رياضة (مثل :كرة السلة , كرة القدم ...الخ)","الفن","كتابة الشعر","الحساب","الاهتمام بالاحياء","الاهتمام بالكيمياء","إصلاح الهواتف","البحث والمطالعة"]
     # call fun ComparisonList
    Hobbies_Name_Have=ComparisonList(divisionList(update_data[2]),Selected_hobbies)
     # call fun Rows_Columns
    Hobbies_Row_ColName=Rows_Columns(Hobbies_Name_Have,Selected_hobbies)
     # call fun Create_DataFrame
    Hobbies=Create_DataFrame(Hobbies_Row_ColName,0,Selected_hobbies)
     # call fun repeat_set_axis
    Hobbies=repeat_set_axis(Hobbies)
    return Hobbies


# In[70]:


def Create_Feature(Feature,Hobbies,objects,Branch_12,Branch_11,Personal_details):
    
    for i in range(len(Hobbies.columns)):
        # create new col in dataframe
        Feature[Hobbies.columns[i]] = Hobbies[Hobbies.columns[i]]

    for i in range(len(objects.columns)):
        # create new col in dataframe
        Feature[objects.columns[i]] = objects[objects.columns[i]]

    for i in range(len(Branch_12.columns)):
        # create new col in dataframe
        Feature[Branch_12.columns[i]] = Branch_12[Branch_12.columns[i]]

    for i in range(len(Branch_11.columns)):
        # create new col in dataframe
        Feature[Branch_11.columns[i]] = Branch_11[Branch_11.columns[i]]

    for i in range(len(Personal_details.columns)):
        # create new col in dataframe
        Feature[Personal_details.columns[i]] = Personal_details[Personal_details.columns[i]]
    return Feature


# In[71]:


def Data(update_data,Ranked_Data):
    #call fun df_Hobbies
    Hobbies= df_Hobbies(update_data)
    #call fun df_majors
    object_=df_object(update_data)
    #call fun Fun_Branch_12
    Branch_12=Branch__12(update_data)
    #call fun Fun_Branch_11
    Branch_11=Branch__11(update_data)
    #call fun Personal_details
    Personal_details=Personal__details(update_data)
    #call fun Rank__Str
    Rank_Str=Rank__Str(Ranked_Data)
    return Hobbies,object_,Branch_12,Branch_11,Personal_details,Rank_Str


# In[80]:


def df_Feature(update_data,Ranked_Data):
    # #call fun Data
    Hobbies,object_,Branch_12,Branch_11,Personal_details,Rank_Str=Data(update_data,Ranked_Data)
    # create dataframe from anther dataframe
    Feature=Rank_Str
     #call fun Create_Feature
    Feature=Create_Feature(Feature,Hobbies,object_,Branch_12,Branch_11,Personal_details)
     #call fun set_axis_columns
    Feature= set_axis_columns(Feature)
     #call fun Edit_DF
    Feature0=Feature.copy()
    Feature=Edit_DF(Feature)
     #call fun set_axis_columns_Update
    Feature= set_axis_columns_Update(Feature)
    Feature0= set_axis_columns_Update(Feature0)
    return Feature,Feature0


# In[81]:


def Save_ToText_Csv(Feature,Feature0):
    #save to text file
    Feature0.to_csv("train.csv", index=False)
    np.savetxt(r'train.txt', Feature.values, fmt='%s')


# In[82]:


def main():
    # call fun Csv
    data,Ranked_Data=Csv()
    # call fun Fun_update_data
    data=Fun_update_data(data)
    # call fun df_Feature
    Feature,Feature0=df_Feature(data,Ranked_Data)
    # call fun Save_ToText_Csv
    #Save_ToText_Csv(Feature,Feature0)
    return Feature,Feature0


# In[83]:


if __name__ == "__main__":
    Feature,Feature0=main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




