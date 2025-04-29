import json

class Members:
    def __init__(self):
        pass
    
    def searhMember(self,membersList,ID):
      left, right = 0 , len(membersList)-1
      while left <= right:
          midIndex = (left+right) // 2
          midValue = int(membersList[midIndex]['MemberID'][1:])
          if midValue == int(ID[1:]):
              return midIndex
          elif midValue < int(ID[1:]):
              left = midIndex+1
          else:
              right = midIndex-1
      return None
    
    def generate_member_id(self,memberList):
        try:
          maxID = int(memberList[-1]['MemberID'][1:])
          return f"M{maxID+1:03d}"
        except:
            return f"M{1:03d}"
        
    def checking_if_member_exists(self,memberList:list,name:str,age:int,contact:str):
        for i, member in enumerate(memberList):
            if member["name"].lower() == name.lower() and member["age"] == age and member["contact"].lower() == contact.lower():
                return i
        return None
            
    def add_members(self,memberList:list,name:str,age:int,contact:str,address:str):
        index_if_already_exists = self.checking_if_member_exists(memberList=memberList,name=name,age=age, contact=contact)

        if index_if_already_exists is not None:
            return f"Member Already Exists with ID:{memberList[index_if_already_exists]['MemberID']}"
        
        auto_generated_id = self.generate_member_id(memberList=memberList)
        try:
          memberList.append({
            "name": name,
            "MemberID": auto_generated_id,
            "age": age,
            "contact": contact,
            "Address": address,
            "Books Borrowed": []
          })
          with open('members/members.json','w') as file:
              json.dump(memberList,file, indent=4)
          return "Member Added Sucessfully"
        except:
            print('error while appending new member to database')

    # Update members
    def update_member(self,memberList:list,MemberID:str,name,age,contact,Address,books_borrowed=None):

        memberIndex = self.searhMember(membersList=memberList,ID=MemberID)

        if memberIndex is not None:

            try:

                updated_name = name if name else memberList[memberIndex]["name"]
                updated_age = age if age else memberList[memberIndex]["age"]
                updated_contact = contact if contact else memberList[memberIndex]["contact"]
                updated_Address = Address if Address else memberList[memberIndex]["Address"]
                updated_books_borrowed = books_borrowed if books_borrowed else memberList[memberIndex]["Books Borrowed"]
          
            except:
                print('errrrrror')

            memberList[memberIndex] = {
                "MemberID": MemberID,
                "name": updated_name,
                "age": int(updated_age),
                "contact": updated_contact,
                "Address": updated_Address,
                "Books Borrowed":updated_books_borrowed

            }
            
            # Now write the updated list to json file
            with open('members/members.json','w') as booksFile:
                json.dump(memberList,booksFile,indent=4)
                return 'Member Updated Sucessfully'
        else:
            return "Can't find Member with given (Member ID)"
        
    def delete_member(self,memberList:list,MemberID:str):
        bookIndex = self.searhMember(membersList=memberList,ID=MemberID)

        if bookIndex:
            borrowed_books = memberList[bookIndex]["Books Borrowed"]
            if len(borrowed_books) > 0:
                return "Member has Some Books borrowed First Return it!"
            
            try:
                del memberList[bookIndex]
                with open('members/members.json','w') as booksFile:
                    json.dump(memberList,booksFile,indent=4)
                    return 'Member Delted Sucessfully'
            except Exception:
                return "Error While Deleting Book Try Again"
        else:
            return "No Member Found with given Member ID"