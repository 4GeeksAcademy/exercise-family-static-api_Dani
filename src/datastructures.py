
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

    
class FamilyStructure:
    def __init__(self, last_name):

        self.last_name = last_name
        self._next_id = 1
        self._members = []

   
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        
        if 'id' not in member:
            member['id'] = self._generate_id()
            member['last_name'] = self.last_name

            self._members.append(member)

            return self._members

    def delete_member(self, id):
       
        del self._members[id]
        return self.members

    def get_member(self, id):
        # fill this method and update the return
        member = self.members[id]
        return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
