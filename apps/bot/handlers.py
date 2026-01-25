from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from asgiref.sync import sync_to_async

from .states import ApplicationStates
from .keyboards import get_main_menu, get_phone_keyboard, get_regions_keyboard, get_collateral_keyboard, get_confirmation_keyboard, get_amount_keyboard
from apps.landing.models import Application
from apps.utils import format_application_message

router = Router()

@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext):
    await state.clear()
    
    welcome_text = (
        "👋 <b>Assalomu alaykum!</b>\n\n"
        "🚀 <b>Moliaviy muammolarni 15 daqiqada hal qiling!</b>\n\n"
        "✅ <b>Juda tez</b> — 15 daqiqa\n"
        "✅ <b>Oson</b> — ortiqcha hujjatlarsiz\n"
        "✅ <b>Ishonchli</b> — faqat pasport kifoya!\n\n"
        "<i>Quyidagi menyudan kerakli bo'limni tanlang:</i>"
    )
    
    await message.answer(
        welcome_text,
        parse_mode="HTML",
        reply_markup=get_main_menu()
    )

@router.message(F.text == "📝 Ariza topshirish")
async def start_application(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "👋 <b>Ariza topshirish uchun birinchi qadam!</b>\n\n"
        "✍️ Iltimos, o'zingizning <b>To'liq Ism-Sharifingizni (F.I.SH)</b> yozib yuboring.\n\n"
        "<i>Namuna:</i> <b>Axmedov Bobur</b>",
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(ApplicationStates.full_name)

@router.message(ApplicationStates.full_name)
async def process_full_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer(
        "Ajoyib! Endi navbatdagi qadam. 🚀\n\n"
        "📱 <b>Siz bilan bog'lanishimiz uchun telefon raqamingizni yuboring.</b>\n\n"
        "<i>Pastdagi maxsus tugmani bosing</i> 👇",
        parse_mode="HTML",
        reply_markup=get_phone_keyboard()
    )
    await state.set_state(ApplicationStates.phone_number)

@router.message(ApplicationStates.phone_number)
async def process_phone_number(message: Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text
        
    await state.update_data(phone_number=phone)
    await message.answer(
        "Rahmat! 📍 <b>Hozirda qaysi hududda istiqomat qilasiz?</b>\n\n"
        "<i>Quyidagi ro'yxatdan o'z hududingizni tanlang</i> 👇",
        parse_mode="HTML",
        reply_markup=get_regions_keyboard()
    )
    await state.set_state(ApplicationStates.region)

@router.message(ApplicationStates.region)
async def process_region(message: Message, state: FSMContext):
    selected_region = message.text
    region_code = None
    
    # Try to find code from name
    for code, name in Application.REGION_CHOICES:
        if name == selected_region:
            region_code = code
            break
            
    if not region_code:
        # Fallback
        region_code = selected_region

    await state.update_data(region=region_code)
    await message.answer(
        "Tushunarli. 💰 <b>Qancha miqdorda mablag' olmoqchisiz?</b>\n\n"
        "<i>Kerakli summani tanlang yoki o'zingiz yozib yuboring</i> 👇",
        parse_mode="HTML",
        reply_markup=get_amount_keyboard()
    )
    await state.set_state(ApplicationStates.credit_amount)

@router.message(ApplicationStates.credit_amount)
async def process_credit_amount(message: Message, state: FSMContext):
    amount_text = message.text
    
    if amount_text == "Boshqa summa":
        await message.answer("✍️ <b>Marxamat, kerakli summani yozib yuboring:</b>", parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
        return

    clean_amount = amount_text.replace(" ", "").replace(",", "").replace(".", "").lower().replace("mln", "000000").replace("so'm", "")
    
    if not clean_amount.isdigit():
        await message.answer("⚠️ <b>Iltimos, faqat raqamlardan foydalaning yoki tugmani tanlang.</b>", parse_mode="HTML")
        return

    await state.update_data(credit_amount=clean_amount)
    await message.answer(
        "Oxirgi qadam! 🏠 <b>Garov sifatida nima taklif qila olasiz?</b>\n\n"
        "<i>O'zingizga ma'qul variantni tanlang</i> 👇",
        parse_mode="HTML",
        reply_markup=get_collateral_keyboard()
    )
    await state.set_state(ApplicationStates.collateral)

@router.message(ApplicationStates.collateral)
async def process_collateral(message: Message, state: FSMContext):
    selected_collateral = message.text
    collateral_code = None
    
    for code, name in Application.COLLATERAL_CHOICES:
        if name == selected_collateral:
            collateral_code = code
            break
    
    if not collateral_code:
        collateral_code = selected_collateral

    await state.update_data(collateral=collateral_code)
    
    data = await state.get_data()
    
    # Save Application
    application = await sync_to_async(Application.objects.create)(
        full_name=data.get('full_name'),
        phone_number=data.get('phone_number'),
        region=data.get('region'),
        credit_amount=data.get('credit_amount'),
        collateral=data.get('collateral'),
        source='telegram'
    )
    
    # Notify Channel
    from django.conf import settings
    
    target_chat_id = settings.TELEGRAM_CHANNEL_ID or settings.ADMIN_CHAT_ID

    if target_chat_id:
        try:
            message_text = await sync_to_async(format_application_message)(application)
            await message.bot.send_message(chat_id=target_chat_id, text=message_text, parse_mode="HTML")
        except Exception as e:
            print(f"Notification failed: {e}")

    # Success Message to User
    success_text = (
        "✅ <b>Arizangiz qabul qilindi!</b>\n\n"
        "Hurmatli mijoz, siz kiritgan ma'lumotlar muvaffaqiyatli saqlandi va menejerlarimizga yuborildi.\n\n"
        "👩‍💻 <b>Tez orada mutaxassislarimiz siz bilan bog'lanishadi.</b>\n\n"
        "<i>Bizni tanlaganingiz uchun rahmat!</i> 😊"
    )
    
    await message.answer(
        success_text,
        parse_mode="HTML",
        reply_markup=get_main_menu()
    )
    await state.clear()

@router.message(F.text == "📞 Bog'lanish")
async def contact_handler(message: Message):
    contact_text = (
        "📞 <b>Biz bilan aloqa:</b>\n\n"
        "🏢 <b>«PULLOL BUSINESS MIKROMOLIYA TASHKILOTI» MChJ</b>\n\n"
        "📍 <b>Manzil:</b> Toshkent shahri, Yakkasaroy tumani, Rakat ko'chasi, 10-uy, 18 xonadon\n"
        "☎️ <b>Tel:</b> (55) 510 02 16\n"
        "📧 <b>Email:</b> info@pullol.uz\n"
        "🔢 <b>STIR (INN):</b> 310430149\n\n"
        "⏰ <b>Ish vaqti:</b> 09:00 - 18:00\n"
        "🛡 <i>Sizning ishonchingiz — biz uchun muhim!</i>"
    )
    await message.answer(contact_text, parse_mode="HTML", reply_markup=get_main_menu())

