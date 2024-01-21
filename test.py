import pyrebase



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

def signup():
        email=input("Enter Email")
        password=input("Enter pass")

        
        # إنشاء حساب جديد في Firebase Authentication
        user=auth.create_user_with_email_and_password(email,password)
        
        print("sucsess " )

            
signup()
