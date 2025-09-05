
class Solution:
    def segregate(self, head):
        initAns=[]
        new=head
        while new:
            initAns.append(new.data)
            new=new.next
        initAns.sort()
        current=head
        cou=0
        while current:
            current.data=initAns[cou]
            cou+=1
            current=current.next
        return head
       
    