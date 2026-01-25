import requests
from django.conf import settings
from apps.landing.models import Application

def format_application_message(application: Application) -> str:
    """
    Format application data into a readable message for Telegram.
    """
    # Get readable names for choices
    region_display = application.get_region_display()
    collateral_display = application.get_collateral_display()
    source_display = application.get_source_display()
    
    # Format amount with spaces
    try:
        formatted_amount = f"{int(application.credit_amount):,}".replace(",", " ")
    except:
        formatted_amount = str(application.credit_amount)

    message = (
        f"🔔 <b>Yangi Ariza!</b>\n"
        f"🆔 <b>Ariza №:</b> {application.id}\n\n"
        f"👤 <b>Mijoz:</b> {application.full_name}\n"
        f"📞 <b>Tel:</b> {application.phone_number}\n"
        f"📍 <b>Hudud:</b> {region_display}\n"
        f"💰 <b>Summa:</b> {formatted_amount} so'm\n"
        f"🏠 <b>Garov:</b> {collateral_display}\n"
        f"📱 <b>Manba:</b> {source_display}"
    )
    return message

def send_to_telegram_channel(message_text: str):
    """
    Send a message to the configured Telegram channel.
    """
    if not settings.TELEGRAM_CHANNEL_ID or not settings.BOT_TOKEN:
        print("Telegram settings missing: TELEGRAM_CHANNEL_ID or BOT_TOKEN not set.")
        return

    url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': settings.TELEGRAM_CHANNEL_ID,
        'text': message_text,
        'parse_mode': 'HTML'
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to send message to Telegram channel: {e}")
