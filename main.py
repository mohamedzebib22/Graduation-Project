from kivy.core.text import LabelBase
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import requests
import firebase_admin
from firebase_admin import credentials, auth ,db
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
import firebase_admin
import pyrebase

Window.size=(330,590)

config = {
    "apiKey": "AIzaSyDyuEohOlFGGJDDsSAlh9rvjZSZ8shXEig",
    "authDomain": "medicalapp-73d41.firebaseapp.com",
    "databaseURL": "https://medicalapp-73d41-default-rtdb.firebaseio.com/",
    "projectId": "medicalapp-73d41",
    "storageBucket": "medicalapp-73d41.appspot.com",
    "messagingSenderId": "565079436237",
    "appId": "1:565079436237:web:5ac629e5d123113ed3f284",
    "measurementId": "G-1F5LN1DJHW"
}

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()

class Slope(MDApp): 
  
    
    
    def build(self):
        self.title="Laboratory"
        screen_manager =MDScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file('choose_entry.kv'))
        screen_manager.add_widget(Builder.load_file('login_admin.kv'))
        screen_manager.add_widget(Builder.load_file("signupadmin.kv"))
        screen_manager.add_widget(Builder.load_file("choose_signup.kv"))
        return screen_manager
    
    
    def login(self, email, password):
        try:
            # تسجيل الدخول باستخدام Firebase Authentication
            auth.sign_in_with_email_and_password(email, password)
            
            # يمكنك إضافة مزيد من الكود هنا، مثل تحويل المستخدم إلى الشاشة المطلوبة
            self.root.current="choose"
            

        except requests.exceptions.HTTPError as e:
            # إذا كان هناك خطأ أثناء تسجيل الدخول، يمكنك عرض رسالة الخطأ
           
            self.show_error_dialog("password or email is error")


    def show_error_dialog(self, error_message):
        dialog = MDDialog(
            title="ُERROR",
            text=error_message,
            size_hint=(0.7, 0.3)
        )
        dialog.open()
        
    
    
    def signup(self,email,password,user_name,date,phone):
       
       

        try:
            from firebase import firebase
            # إنشاء حساب جديد في Firebase Authentication
            firebase=firebase.FirebaseApplication('https://medicalapp-73d41-default-rtdb.firebaseio.com/',None)
            user=auth.create_user_with_email_and_password(email,password)
            data1={
                'email':email,
                'password':password,
                'date':date,
                'phone':phone,
                'user_name':user_name,
            }
            
            firebase.post('https://medicalapp-73d41-default-rtdb.firebaseio.com/Users',data1)
            result=firebase.get('medicalapp-73d41-default-rtdb/Users','')
        except Exception as Er:
            self.show_error_dialog("The Email is invalid")
            print(Er)   
            
    def show_error_dialog(self, error_message):
        dialog = MDDialog(
            title="An Error",
            text=error_message,
            size_hint=(0.7, 0.3)
        )
        dialog.open()
        
    def signup_admin(self,name,email,password,address,phone):
        from firebase import firebase
        try:
            firebase=firebase.FirebaseApplication('https://medicalapp-73d41-default-rtdb.firebaseio.com/',None)
            user=auth.create_user_with_email_and_password(email,password)
            data={
                'email':email,
                'password':password,
                'address':address,
                'phone':phone,
                'name':name,
            }
            
            firebase.post('https://medicalapp-73d41-default-rtdb.firebaseio.com/Admin',data)
            result=firebase.get('medicalapp-73d41-default-rtdb/Users','')
        except Exception as Er:
            self.show_error_dialog("The Email is invalid")
            print(Er)   
        
if __name__ == "__main__":
    LabelBase.register(name="MPoppins" , fn_regular="Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins" , fn_regular="Poppins-SemiBold.ttf")

    Slope().run()