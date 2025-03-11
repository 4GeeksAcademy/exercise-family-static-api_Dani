
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
        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['id'] = self._generateId()
        member['last_name'] = self.last_name
        self._members.append(member)
        return member

    
    def delete_member(self, id):
        for idx, member in enumerate(self._members):
            if member['id'] == id:
                del self._members[idx]
                return True
        return False 

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
