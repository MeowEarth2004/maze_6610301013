##ชุดข้อมูลของ Stack##
#ต้นแบบข้อมูล เพื่อสร้างฟังชั้่นภายในตัว และสร้างออกมาตามสมาชิกของคลาส Stack
class Stack:

    #ฟังชั่น กำหนดค่าไห้กับ self (Key word)
    def __init__(self):
        #กำหนดไห้ self เป็นพาลามิเตอร์ และ _top เป็นตัวแปร และ ไห้เป็น None(ไม่มี)
        self._top = None
        #กำหนดไห้ self เป็นพาลามิเตอร์ และ _size เป็นตัวแปร และ ไห้เป็น 0
        self._size = 0

    #ฟังชั่น หาค่าของตัวแปร self
    def isEmpty(self):
        #รีเทิร์น เมื่อ self._top เป็น None
        return self._top is None
    
    #ฟังชั่น ที่เป็น method พิเศษ เพราะเป็นฟังก์ชั่นของวัตถุตัวใดตัวหนึ่ง ฟังก์ชั่นใดก็ตามที่กลายเป็นฟังก์ชั่นของวัตถุที่อยู่ใน class จะเรียกว่า method
    def __len__(self):
        #รีเทิร์น self._size
        return self._size
    
    #ฟังชั่น สำหรับดูข้อมูล
    def peek(self):
         #เมื่อไม่ใช่ self.isEmpty จะแสดง Cannot peek at an empty stack
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        #รีเทิร์น self._top.item
        return self._top.item
    #ฟังชั่น เป็นการนำค่าใน index สุดท้ายออกมา และ return ค่านั้นออกมา ซึ่ง จะทำการ mutate array เหมือนกับ push
    def pop(self):
         #เมื่อไม่ใช่ self.isEmpty จะแสดง Cannot pop from an empty stack
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        #node <= self._top
        node = self._top
        #self._top <= self._top.next
        self._top = self._top.next
        #self._size <= self._size - 1
        self._size = self._size - 1
        #รีเทิร์น node.item
        return node.item
    
    #ฟังชั่น เป็น function ที่เพิ่มค่าเข้าไปที่ค่าสุดท้ายของ array
    def push(self, item):
        #self._top <= _StackNode(item, self._top)
        self._top = _StackNode(item, self._top)
        #self._size <= self._size + 1
        self._size = self._size + 1
##ชุดข้อมูลของ _StackNode##
class _StackNode:
    #ฟังชั่น กำหนดค่าไห้กับ self,item,link (Key word)
    def __init__(self, item, link):
        #self.item <= item
        self.item = item
        #self.next = link
        self.next <= link