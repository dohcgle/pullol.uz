from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import os

WEBAPP_URL = os.environ.get('WEBAPP_URL', 'https://example.com/webapp-form/')
from apps.landing.models import Application

def get_phone_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📱 Raqamni yuborish", request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard

def get_regions_keyboard():
    # Split regions into 2 columns
    regions = Application.REGION_CHOICES
    keyboard_buttons = []
    row = []
    
    for region_code, region_name in regions:
        # Simplify names for buttons if needed, or use full names
        row.append(KeyboardButton(text=region_name))
        
        if len(row) == 2:
            keyboard_buttons.append(row)
            row = []
            
    if row:
        keyboard_buttons.append(row)
        
    return ReplyKeyboardMarkup(
        keyboard=keyboard_buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )

def get_collateral_keyboard():
    collaterals = Application.COLLATERAL_CHOICES
    keyboard_buttons = [[KeyboardButton(text=name)] for code, name in collaterals]
    return ReplyKeyboardMarkup(
        keyboard=keyboard_buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    
def get_confirmation_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ Tasdiqlash"), KeyboardButton(text="❌ Bekor qilish")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

def get_amount_keyboard():
    amounts = [
        "5 000 000", "10 000 000", "15 000 000",
        "20 000 000", "30 000 000", "50 000 000",
        "100 000 000", "Boshqa summa"
    ]
    keyboard_buttons = []
    row = []
    for amount in amounts:
        row.append(KeyboardButton(text=amount))
        if len(row) == 2:
            keyboard_buttons.append(row)
            row = []
    if row:
        keyboard_buttons.append(row)
        
    return ReplyKeyboardMarkup(
        keyboard=keyboard_buttons,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Summani tanlang yoki yozing..."
    )

def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📝 Ariza topshirish")],
            [KeyboardButton(text="📞 Bog'lanish")]
        ],
        resize_keyboard=True
    )

