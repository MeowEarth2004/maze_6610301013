#ใช้คำสั่ง import os เพื่อนำเข้า module OS เข้ามาในโค้ด
import os
#เป็นไลเบอรี่ที่ใช้ควบคุมคีย์บอร์ด
import keyboard
#เป็นไลเบอรี่ที่ใช้ควบคุมเวลา หรือ รีเรย์
import time

##ชุดข้อมูลของ maze##
#ต้นแบบข้อมูล เพื่อสร้างฟังชั้่นภายในตัว และสร้างออกมาตามสมาชิกของคลาส maze
class maze:

    #ฟังชั่น กำหนดค่าไห้กับ self (Key word) ไห้เป็น None(ไม่มี)
    def __init__(self) -> None:
        
        #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร method
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        
        #กำหนดไห้ self เป็นพาลามิเตอร์ และ ply[P] เป็น ตัวแปร และ ตั้งไห้ pos P ไปยังตำแหน่งที่ Y:5,X:1
        self.ply = pos(5, 1)

        #กำหนดไห้ self เป็นพาลามิเตอร์ และ end[E] เป็น ตัวแปร และ ตั้งไห้ pos E ไปยังตำแหน่งที่ Y:2,X:6
        self.end = pos(2, 6)

        #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze วาง P ไปยังตำแหน่งที่ Y:5,X:1
        self.maze[self.ply.y][self.ply.x] = "P"

        #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze วาง E ไปยังตำแหน่งที่ Y:2,X:6
        self.maze[self.end.y][self.end.x] = "E"
    
    # ฟังชั่น ใช้ติดตั้งขอบเขต โดยกำหนดตัวแปรเป็น (self, y, x)
    def isInBound(self, y, x):
        #เมื่อคำสั่งเป็นจริง โดยไห้เงื่อนไขว่า y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0])
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            #รีเทิร์น เมื่อ ถูก
            return True
        #เมื่อคำสั่งไม่เป็นจริง
        else:
            #รีเทิร์น เมื่อ ผิด
            return False
    
    #ฟังชั่นสั่งแสดงผล ข้อมูล ภายใน self เมื่อเริ่มเควส
    def print(self):
        #โมดูล OS ใช้งานระบบ cls
        os.system("cls")
        #แสดงผล ข้อมูลเว้นบรรทัด 3 ครั้ง
        print("\n\n\n")
        #ลูป ภายในแถว ของ self.maze
        for row in self.maze:
            #ลูป โดยรวม ภายในแถว
            for col in row:
                #แสดงผล พากก์รวม และ การสิ้นสุดการทำงาน
                print(col," ", end="")
            #แสดงผล พื้นที่ว่าง
            print("")
        #แสดงผล ข้อมูลเว้นบรรทัด 3 ครั้ง
        print("\n\n\n")

    #ฟังชั่นสั่งแสดงผล ข้อมูล ภายใน self เมื่อสำเร็จเควส
    def printEND(self):
        #ใช้ข้อมูลจาก โมดูล os (class)
        os.system("cls")
        #แสดงผล ข้อมูลเว้นบรรทัด 3 ครั้ง
        print("\n\n\n")
        #แสดงผลข้อความ แสดงความยินดี
        print(">>>>> Congraturation!!! <<<<<")
        #แสดงผล ข้อมูลเว้นบรรทัด 3 ครั้ง
        print("\n\n\n")
        #จะไม่ส่งคืนข้อมูล
        keyboard.wait("")

    #ฟังชันการเคลื่อนที่ขึ้น
    def move_up(self):
        #การเคลื่อนที่ครั้งถัดไป Y-1 เพื่อขึ่นข้างบน
        next_move = pos(self.ply.y-1, self.ply.x)
        #ขอบเขตปัจจุบัน
        if self.isInBound(next_move.y,next_move.x):
            #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป [next_move.y][next_move.x]
            if self.maze[next_move.y][next_move.x] == " ":
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze วาง P ไปยังตำแหน่ง ล่าสุด ของ [self.ply.y][self.ply.x]
                self.maze[self.ply.y][self.ply.x] = " "
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป แล้ว วาง P [next_move.y][next_move.x] = "P"
                self.maze[next_move.y][next_move.x] = "P"
                #เปลี่ยน pos(ที่อดีต)ไห้ขยับไปยัง pos(ปัจจุบัน) [pos(self.ply.y-1, self.ply.x)]
                self.ply = next_move
                #ดีเรย์เมื่อกดจะหยุด 0.1 วิ
                time.sleep(0.1)
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป แล้ว วาง E [next_move.y][next_move.x] == "E"
            if self.maze[next_move.y][next_move.x] == "E":
                #กำหนดไห้ self เป็นพาลามิเตอร์ ของ printEND
                self.printEND()
                #รีเทิร์น เมื่อ ผิด
                return False
        #รีเทิร์น เมื่อ ถูก
        return True
    
    #ฟังชันการเคลื่อนที่ลง
    def move_down(self):
        #การเคลื่อนที่ครั้งถัดไป Y+1 เพื่อลงข้างล่าง
        next_move = pos(self.ply.y+1, self.ply.x)
        #ขอบเขตปัจจุบัน
        if self.isInBound(next_move.y,next_move.x):
            #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป [next_move.y][next_move.x]
            if self.maze[next_move.y][next_move.x] == " ":
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze วาง P ไปยังตำแหน่ง ล่าสุด ของ [self.ply.y][self.ply.x]
                self.maze[self.ply.y][self.ply.x] = " "
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป แล้ว วาง P [next_move.y][next_move.x] = "P"
                self.maze[next_move.y][next_move.x] = "P"
                #เปลี่ยน pos(ที่อดีต)ไห้ขยับไปยัง pos(ปัจจุบัน) [pos(self.ply.y+1, self.ply.x)]
                self.ply = next_move
                #ดีเรย์เมื่อกดจะหยุด 0.1 วิ
                time.sleep(0.1)
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป แล้ว วาง E [next_move.y][next_move.x] == "E"
            if self.maze[next_move.y][next_move.x] == "E":
                #กำหนดไห้ self เป็นพาลามิเตอร์ ของ printEND
                self.printEND()
                #รีเทิร์น เมื่อ ผิด
                return False
        #รีเทิร์น เมื่อ ถูก
        return True

    #ฟังชันการเคลื่อนที่ไปทางซ้าย
    def move_left(self):
        #การเคลื่อนที่ครั้งถัดไป X-1 เพื่อไปทางซ้าย
        next_move = pos(self.ply.y, self.ply.x-1)
        #ขอบเขตปัจจุบัน
        if self.isInBound(next_move.y,next_move.x):
            #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป [next_move.y][next_move.x]
            if self.maze[next_move.y][next_move.x] == " ":
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze วาง P ไปยังตำแหน่ง ล่าสุด ของ [self.ply.y][self.ply.x]
                self.maze[self.ply.y][self.ply.x] = " "
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป แล้ว วาง P [next_move.y][next_move.x] = "P"
                self.maze[next_move.y][next_move.x] = "P"
                #เปลี่ยน pos(ที่อดีต)ไห้ขยับไปยัง pos(ปัจจุบัน) [pos(self.ply.y, self.ply.x-1)]
                self.ply = next_move
                #ดีเรย์เมื่อกดจะหยุด 0.1 วิ
                time.sleep(0.1)
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป แล้ว วาง E [next_move.y][next_move.x] == "E"
            if self.maze[next_move.y][next_move.x] == "E":
                #กำหนดไห้ self เป็นพาลามิเตอร์ ของ printEND
                self.printEND()
                #รีเทิร์น เมื่อ ผิด
                return False
        #รีเทิร์น เมื่อ ถูก
        return True

    #ฟังชันการเคลื่อนที่ไปทางขวา
    def move_right(self):
        #การเคลื่อนที่ครั้งถัดไป x+1 เพื่อไปทางขวา
        next_move = pos(self.ply.y, self.ply.x+1)
        #ขอบเขตปัจจุบัน
        if self.isInBound(next_move.y,next_move.x):
            #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป [next_move.y][next_move.x]
            if self.maze[next_move.y][next_move.x] == " ":
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze วาง P ไปยังตำแหน่ง ล่าสุด ของ [self.ply.y][self.ply.x]
                self.maze[self.ply.y][self.ply.x] = " "
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป แล้ว วาง P [next_move.y][next_move.x] = "P"
                self.maze[next_move.y][next_move.x] = "P"
                #เปลี่ยน pos(ที่อดีต)ไห้ขยับไปยัง pos(ปัจจุบัน) [pos(self.ply.y, self.ply.x+1)]
                self.ply = next_move
                #ดีเรย์เมื่อกดจะหยุด 0.1 วิ
                time.sleep(0.1)
                #กำหนดไห้ self เป็นพาลามิเตอร์ และ maze เป็น ตัวแปร และ ตั้งไห้ maze ไปยังพื้นที่ถัดไป แล้ว วาง E [next_move.y][next_move.x] == "E"
            if self.maze[next_move.y][next_move.x] == "E":
                #กำหนดไห้ self เป็นพาลามิเตอร์ ของ printEND
                self.printEND()
                #รีเทิร์น เมื่อ ผิด
                return False
        #รีเทิร์น เมื่อ ถูก
        return True


##ชุดข้อมูลของ pos##
#ต้นแบบข้อมูล เพื่อสร้างฟังชั้่นภายในตัว และสร้างออกมาตามสมาชิกของคลาส pos(แมพ)
class pos:
    #ฟังชั่น กำหนดค่าไห้กับ self (Key word) ไห้เป็น None(ไม่มี)
    def __init__(self) -> None:
        #y จาก self = ไม่มีข้อมูล
        self.y = None
        #x จาก self = ไม่มีข้อมูล
        self.x = None

    #ฟังชั่น กำหนดค่าไห้กับ self,y,x (Key word) ไห้เป็น None(ไม่มี)
    def __init__(self, y, x) -> None:
        #y จาก self = y
        self.y = y
        #x จาก self = x
        self.x = x

##ชุดการทำงานของ keyboard##
#__name__ ใช้บอกชื่อโมดูล '__main__' main ไฟล์ หรือไฟล์, สคริปต์ ที่กำลังรันโค้ดในขณะนั้น----ช่วยให้สามารถที่จะเลือกรันหรือไม่รันสคริปต์หรือไฟล์ที่ต้องการได้ 
if __name__ == '__main__':
    #m ย่อมาจาก maze เพราะ m <= maze
    m = maze()
    #maze แสดงผล
    m.print()

    #while loop ถ้า ถูก
    while True:

        #keyboard.is_pressed("hotkey") ถ้ากดคีถูกต้องจะทำการแสดงผลข้อมูล ภายใน if
        if keyboard.is_pressed("q"):
            #แสดงผล ข้อมูล Quit Program
            print("Quit Program")
            #หยุดลูปที่กำลัง ทำงาน(วนซ้ำ) อยู่ในขณะท่โปรแกรมกำลังทำงาน
            break
        #keyboard.is_pressed("hotkey") ถ้ากดคีถูกต้องจะทำการแสดงผลข้อมูล ภายใน if
        if keyboard.is_pressed("w"):
            #maze แสดงผล เมื่อเคลื่อนที่ไปด้านบน
            if m.move_up():
                #maze แสดงผล
                m.print()
            #เมื่อคำสั่งไม่เป็นจริง
            else:
                #หยุดลูปที่กำลัง ทำงาน(วนซ้ำ) อยู่ในขณะท่โปรแกรมกำลังทำงาน
                break
            #keyboard.is_pressed("hotkey") ถ้ากดคีถูกต้องจะทำการแสดงผลข้อมูล ภายใน if
        if keyboard.is_pressed("s"):
            #maze แสดงผล เมื่อเคลื่อนที่ไปด้านล่าง
            if m.move_down():
                #maze แสดงผล
                m.print()
            #เมื่อคำสั่งไม่เป็นจริง
            else:
                #หยุดลูปที่กำลัง ทำงาน(วนซ้ำ) อยู่ในขณะท่โปรแกรมกำลังทำงาน
                break
            #keyboard.is_pressed("hotkey") ถ้ากดคีถูกต้องจะทำการแสดงผลข้อมูล ภายใน if
        if keyboard.is_pressed("a"):
            #maze แสดงผล เมื่อเคลื่อนที่ไปด้านซ้าย
            if m.move_left():
                #maze แสดงผล
                m.print()
            #เมื่อคำสั่งไม่เป็นจริง
            else:
                #หยุดลูปที่กำลัง ทำงาน(วนซ้ำ) อยู่ในขณะท่โปรแกรมกำลังทำงาน
                break
            #keyboard.is_pressed("hotkey") ถ้ากดคีถูกต้องจะทำการแสดงผลข้อมูล ภายใน if
        if keyboard.is_pressed("d"):
            #maze แสดงผล เมื่อเคลื่อนที่ไปด้านขวา
            if m.move_right():
                #maze แสดงผล
                m.print()
            #เมื่อคำสั่งไม่เป็นจริง
            else:
                #หยุดลูปที่กำลัง ทำงาน(วนซ้ำ) อยู่ในขณะท่โปรแกรมกำลังทำงาน
                break