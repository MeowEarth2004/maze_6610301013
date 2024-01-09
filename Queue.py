##ชุดข้อมูลของ Queue##
#ต้นแบบข้อมูล เพื่อสร้างฟังชั้่นภายในตัว และสร้างออกมาตามสมาชิกของคลาส Queue
class Queue:

    #ฟังชั่น กำหนดค่าไห้กับ self (Key word)
    def __init__(self):
        #กำหนดไห้ self เป็นพาลามิเตอร์ และ _qList เป็น ตัวแปร จาก list() เป็น self._qList
        self._qList = list()

    #ฟังชั่น หาค่าของตัวแปร self
    def isEmpty(self):
        #นับจำนวนตัวเลขหรือตัวอักษรและอื่นๆ ในตัวแปร และ ไห้ค่าทั้งหมดเป็นจริง
        return len(self) == 0
    
    #ฟังชั่น ที่เป็น method พิเศษ เพราะเป็นฟังก์ชั่นของวัตถุตัวใดตัวหนึ่ง ฟังก์ชั่นใดก็ตามที่กลายเป็นฟังก์ชั่นของวัตถุที่อยู่ใน class จะเรียกว่า method
    def __len__(self):
        #นับจำนวนตัวเลขหรือตัวอักษรและอื่นๆ ในตัวแปร self._qList
        return len(self._qList)
    
    #ฟังชั่น การเข้าคิว สิ่งของในรายการ จาก ตัวแปร
    def enqueue(self, item):
        #การเข้าคิว สิ่งของในรายการ ของ self._qList.append
        self._qList.append(item)

    #ฟังชั่น การนำสมาชิกออกจากคิว จาก ตัวแปร
    def dequeue(self):
        #เมื่อไม่ใช่ self.isEmpty จะแสดง Cannot dequeue from an empty queue.
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        #รีเทิร์น เมื่อ self._qList.pop(0)
        return self._qList.pop(0)