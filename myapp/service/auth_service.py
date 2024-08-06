#from ..repositoy.user_repository import select_userb_by_email
#import bcrypt as bc
import reflex as rx

import xmlrpc.client
from typing import List
from ..pages.profile import ProfileState

def auth_user(username: str, password: str):
    #buscar usuario
    #user = select_userb_by_email(email)
    #if(user == None):
    #    raise BaseException('El usuario no existe')
    #if(not validate_password(password, user.password)):
    #    raise BaseException('Credenciales incorrectas')
    # Guardar un valor en LocalStorage
    #rx.LocalStorage("dos", name="user", sync=True)
    
    #rx.Cookie(name="pruebatoken", max_age=3600)
    url = 'https://comeritk.odoo.com'
    db = 'comeritk'
    
    #username = 'eduardo.macias@iteknia.com'
    
    #password = 'iteknia2023'

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    #x = common.version()
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    #socios = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
    #socios = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [[['write_uid', '=', 23]]], {'fields': ['name', 'id'], 'limit': 1})
    #socios = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [[['write_uid', '=', 23]]], {'attributes': ['string', 'help', 'type']})
    ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['write_uid', '=', 23]]], { 'limit': 1})
    socios = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'id']})
    print(socios[0]["name"])
  
    return True
    #return False


 