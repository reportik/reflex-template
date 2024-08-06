# Welcome to Reflex! This file outlines the steps to create a basic app
import asyncio
import json
import os
import requests

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth, exceptions
from . import styles
from .key import API # API key

import reflex as rx

for root, dirs, files in os.walk("./myapp"):
    for file in files:
        if file.endswith(".json"):
            path = os.path.join(root, file)
            
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)

class MainState(rx.State):
    pass

class SignUpState(MainState):
    email : str = ""
    password: str = ""
    handle: str =""
    
    placeEmail: str=""
    placePassword: str=""
    placeHandle: str =""
    
    borderEmail: str=""
    borderPassword: str=""
    borderHandle: str=""
    btnName: str="Registrar"
    
    isLoading: bool = False
    isDisabled: bool=False
    loadingText: str = "Espera..."
    @vars
    def get_signup_email(self, email):
        self.email = email
    
    def get_signup_password(self, password):
        self.password = password    
    
    def get_signup_handle(self, handle):
        self.handle = handle    
    
    def auth_user_email(self):
        try:
            if auth.get_user_by_email(self.email):
                return True
        except Exception:
            return False
            
    def auth_user_handle(self):
        pass
    def authenticate_user(self):
        temp_email = self.email
        temp_password = self.password
        temp_handle = self.handle
        
        if len(self.password) >= 6:
            self.borderPassword = "teal"
        else:
            self.password = ""
            self.borderPassword = "red"
            self.placePassword = "El password debe tener una longitud minima de 6"
            
        if len(self.email) != 0:
            if self.auth_user_email():
                self.email = ""
                self.placeEmail = "El email ya existe"
                self.borderEmail = "red"
            else:
                self.email = temp_email
                self.placeEmail = ""
                self.borderEmail = "teal"
                    
    def validate_user(self):
        pass
    
    def run_button_loader(self):
        pass
    
    def stop_button_loader(self):
        pass
    
    def restart_page(self):
        self.email = ""
        self.handle = ""
        self.password = ""
                
        self.borderEmail = ""
        self.borderPassword = ""
        self.borderHandle = ""        
        
        self.placeEmail = "Email"
        self.placePassword = "Password"
        self.placeHandle = "Hnadle"

class LoginState(MainState):
    email: str = "Emaill"
    password: str = ""
    placeEmail: str = "Email"
    placePassword: str = "Password"
    borderEmail: str = ""
    borderPassword: str = ""
    btnName: str = "Log In"
    
    
    def get_login_email(self, email:str):
        self.email = email
        yield
        
    def get_login_password(self, password:str):
        self.email = password
        
    def auth_user_data(self):
        pass    
        
    def restart_page(self):
        self.email = ""
        self.password = ""
        self.btnName = ""
        self.borderEmail = ""
        self.borderPassword = ""
        self.placeEmail = "Email"
        self.placePassword = "Password"
    

class CustomInputs(rx.chakra.Input):
    def __init__(
            self, 
            placeholder : str,
            type_: str,
            value: rx.State,
            on_change: callable,
            border_color: rx.State,
    ):
        super().__init__(
            placeholder = placeholder,
            type_ = type_,
            value = value,
            on_change = on_change,
            border_color = border_color
        )
        
class CustomButton(rx.chakra.Button):
    def __init__(
            self, 
            children : list,
            is_loading: bool,
            is_disabled: bool,
            on_click: callable,
            loading_text: SignUpState.loadingText,
            
    ):
        super().__init__(
            children = children,
            is_loading = is_loading,
            is_disabled = is_disabled,
            on_click = on_click,
            loading_text = loading_text
        )

@rx.page(route='/')
def index():
    return rx.text("Dashboard")

class PageView:
    def __init__(self, components: list): 
        self.components = components
      
        self.stack = rx.stack(
            
            width = "100%",
            height = "100vh",
            padding = "2rem",
            display = "flex",
            align_items = "center",
            spacing= "1rem",
            justify_content = "center",
            
        )
        #super().__init__()
        
    def build(self):
        for component in self.components:
            self.stack.children.append(component)
            
        return self.stack

@rx.page(route='/login')
def login():
    return rx.vstack(
            rx.heading("Login"),
            rx.text("Inicia Sesion"),
            rx.text(""+ LoginState.email),
            rx.spacer(),
            rx.input(
                placeholder=LoginState.placeEmail,
                type="text",
                value=LoginState.email,
                on_change=LoginState.get_login_email,
            ),
            width = "100%",
            height = "15rem",
            justify_content= "center",
            spacing = "1.5rem",
        )

@rx.page(route='/registro', on_load=SignUpState.restart_page)
def signup():
    components: list =[
        rx.vstack(
            rx.heading("Registro"),
           rx.text(""+ LoginState.email),
            rx.spacer(),
          
            width = "100%",
            height = "22rem",
            justify_content= "center",
            spacing = "1.5rem",
        )
    ]
    signup = PageView(components)
    
    return signup.build()

app = rx.App(
    #state = MainState, 
    theme=rx.theme(color_mode="dark", accent_color="blue"), 
    style=styles.base_style,
    stylesheets=styles.base_stylesheets
    )

app._compile()
